import logging

import otree.channels.utils as channel_utils
from channels.generic.websocket import (
    JsonWebsocketConsumer)
from channels.layers import get_channel_layer
from django.conf import settings

logger = logging.getLogger(__name__)
from asgiref.sync import async_to_sync
from .models import Group
from django.db import connection
from threading import Thread, Event
from time import sleep
import json

ALWAYS_UNRESTRICTED = 'ALWAYS_UNRESTRICTED'
UNRESTRICTED_IN_DEMO_MODE = 'UNRESTRICTED_IN_DEMO_MODE'


def group_model_exists():
    return 'dutch_group' in connection.introspection.table_names()


def subsession_model_exists():
    return 'dutch_subsession' in connection.introspection.table_names()


#  Copied from otree.channels.consumers.py - where Chris asks not to directly subclass but rather copy this over
#  It provides a basic implementation of a consumer with several functions to be defined by the implementing class
class _OTreeJsonWebsocketConsumer(JsonWebsocketConsumer):
    '''
    THIS IS NOT PUBLIC API.
    Third party apps should not subclass this.
    Either copy this class into your code,
    or subclass directly from JsonWebsocketConsumer,
    '''

    def group_send_channel(self, type: str, groups=None, **event):
        print('in group_send_channel')
        for group in (groups or self.groups):
            channel_utils.sync_group_send(group, {'type': type, **event})
            # print('call_args', channel_utils.sync_group_send.call_args)
            # assert channel_utils.sync_group_send.call_args

    def clean_kwargs(self, **kwargs):
        '''
        subclasses should override if the route receives a comma-separated params arg.
        otherwise, this just passes the route kwargs as is (usually there is just one).
        The output of this method is passed to self.group_name(), self.post_connect,
        and self.pre_disconnect, so within each class, all 3 of those methods must
        accept the same args (or at least take a **kwargs wildcard, if the args aren't used)
        '''
        return kwargs

    def group_name(self, **kwargs):
        raise NotImplementedError()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cleaned_kwargs = self.clean_kwargs(**self.scope['url_route']['kwargs'])
        self.groups = self.connection_groups()

    def connection_groups(self, **kwargs):
        group_name = self.group_name(**self.cleaned_kwargs)
        return [group_name]

    unrestricted_when = ''

    # there is no login_required for channels
    # so we need to make our own
    # https://github.com/django/channels/issues/1241
    def connect(self):
        # need to accept no matter what, so we can at least send
        # an error message
        self.accept()

        AUTH_LEVEL = settings.AUTH_LEVEL

        auth_required = (
                (not self.unrestricted_when) and AUTH_LEVEL
                or
                self.unrestricted_when == UNRESTRICTED_IN_DEMO_MODE and AUTH_LEVEL == 'STUDY'
        )

        if auth_required and not self.scope['user'].is_staff:
            msg = 'rejected un-authenticated access to websocket'
            logger.warning(msg)
            # it's good to send an explanation so we understand e.g.
            # test failures
            self.send_json({'unauthenticated_websocket': msg})
            return
        else:
            self.post_connect(**self.cleaned_kwargs)

    def post_connect(self, **kwargs):
        pass

    def disconnect(self, message, **kwargs):
        self.pre_disconnect(**self.cleaned_kwargs)

    def pre_disconnect(self, **kwargs):
        pass

    def receive_json(self, content, **etc):
        self.post_receive_json(content, **self.cleaned_kwargs)

    def post_receive_json(self, content, **kwargs):
        pass


# Consumer is one per Group, multiple players are connected to one
class AuctionRoom(_OTreeJsonWebsocketConsumer):
    def clean_kwargs(self, params):
        group_id, session_code = params.split(',')
        return {
            'group_id': int(group_id),
            'session_code': session_code,
        }

    # return a unique group_name for the channel_layer so that each oTree group gets its own channel_layer
    def group_name(self, group_id, session_code):
        return "dutch_session-" + str(session_code) + "_group-" + str(group_id)

    def translate_message(self, event):
        self.send(text_data=json.dumps(event))

    def post_connect(self, group_id, session_code):
        # add them to the channel_layer
        room_group_name = self.group_name(group_id, session_code)
        async_to_sync(self.channel_layer.group_add)(
            room_group_name,
            self.channel_name
        )

    def pre_disconnect(self, group_id, session_code):
        # remove the player from their channel_layer
        room_group_name = self.group_name(group_id, session_code)
        async_to_sync(self.channel_layer.group_discard)(
            room_group_name,
            self.channel_name
        )

    # we dont expect any posting by the consumers in this experiment
    def post_receive_json(self, content, group_id, session_code):
        pass


# Make process for periodic increase of the price using Twisted, added to already present reactor
class PriceUpdater(Thread):
    def __init__(self, stop_event=None):
        super(PriceUpdater, self).__init__()
        if not stop_event:
            stop_event = Event()
        self.stop_event = stop_event

    def run(self):
        while True:
            if group_model_exists():
                activated_groups = Group.objects.filter(activated=True)
                channel_layer = get_channel_layer()
                for g in activated_groups:
                    channel_name = g.get_channel_group_name()
                    if g.price > 1:
                        g.price -= 1
                        g.save()
                        async_to_sync(channel_layer.group_send)(
                            channel_name,
                            {
                                'type': 'translate_message',
                                'message': g.price,
                                'advance': False,
                            }
                        )
                    else:
                        g.save()
                        g.timeout = True
                        async_to_sync(channel_layer.group_send)(
                            channel_name,
                            {
                                'type': 'translate_message',
                                'advance': True,
                            }
                        )
            sleep(2)


print("Dutch auction, active groups checking process started.....")
t = PriceUpdater()
t.daemon = True
t.start()
