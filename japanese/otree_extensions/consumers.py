from channels.generic.websockets import JsonWebsocketConsumer
import random
from japanese.models import Constants, Player, Group, Subsession
import json


class PriceTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/price_increase_japan/(?P<player_pk>[0-9]+)/(?P<group_pk>[0-9]+)/(?P<subsession_pk>[0-9]+)$')

    def clean_kwargs(self):
        self.player_pk = self.kwargs['player_pk']
        self.group_pk = self.kwargs['group_pk']
        self.subsession_pk = self.kwargs['subsession_pk']

    def connection_groups(self, **kwargs):
        group_name = self.get_group().get_channel_group_name()
        return [group_name]

    def connect(self, message, **kwargs):
        print('someone connected')

    def disconnect(self, message, **kwargs):
        print('someone disconnected')

    def get_player(self):
        self.clean_kwargs()
        return Player.objects.get(pk=self.player_pk)

    def get_player(self):
        self.clean_kwargs()
        return Subsession.objects.get(pk=self.subsession_pk)

    def get_group(self):
        self.clean_kwargs()
        return Group.objects.get(pk=self.group_pk)


