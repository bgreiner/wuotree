import random

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import connection
from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

author = 'Filipp Chapkovski, chapkovski@gmail.com, upgraded to new Channels API by Jan Vavra, vavra.jn@gmail.com'

doc = """
Dutch Auction with realtime decrease done by Channels
"""


def group_model_exists():
    return 'dutch_group' in connection.introspection.table_names()

    # for p in players:
    #     print(p.participant.code)


class Constants(BaseConstants):
    name_in_url = 'dutch'
    players_per_group = 4
    num_rounds = 1
    endowment = 50


class Subsession(BaseSubsession):

    #
    # def get_subsession_id(self):
    #     return int(self.pk)
    #
    def creating_session(self):
        #     id_for_channel = get_subsession_id()
        for p in self.get_players():
            p.set_cert()


pass


class Player(BasePlayer):
    auction_winner = models.BooleanField(initial=False)
    cert_price = models.CurrencyField()

    def set_cert(self):
        self.cert_price = random.randrange(10, 50, 1)

    def set_payoff(self):
        self.payoff = ((self.cert_price - self.group.price) * self.auction_winner) * (not self.group.timeout)


class Group(BaseGroup):
    price = models.IntegerField(initial=50)
    activated = models.BooleanField(initial=False)
    timeout = models.BooleanField(initial=False)

    def get_channel_group_name(self):
        return "dutch_session-" + str(self.session.code) + "_group-" + str(self.id)

    def advance_participants(self):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            self.get_channel_group_name(),
            {
                'type': 'translate_message',
                'advance': True,
            }
        )
