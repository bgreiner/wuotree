from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
# from background_task import background
# from background_task.models import Task
import atexit
import subprocess
from django.db import transaction, models as dmodels
import channels
import json
from django.db import connection
import random

from twisted.internet import task

author = 'Filipp Chapkovski, chapkovski@gmail.com'

doc = """
Your app description
"""

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


def group_model_exists():
    return 'japanese_group' in connection.introspection.table_names()


    # for p in players:
    #     print(p.participant.code)


class Constants(BaseConstants):
    name_in_url = 'japanese'
    players_per_group = 4
    num_rounds = 1
    endowment = 50


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.set_cert()
pass

class Player(BasePlayer):
    drop_out = models.BooleanField(initial=False)
    cert_price = models.CurrencyField()
    def set_cert(self):
        self.cert_price = random.randrange(10, 50, 1)
    def set_payoff(self):
        self.payoff = ((self.cert_price - self.group.price) * (self.drop_out)) * (not self.group.timeout)


class Group(BaseGroup):
    price = models.IntegerField(initial=5)
    activated = models.BooleanField(initial=False)
    timeout = models.BooleanField(initial=False)
    def get_channel_group_name(self):
        return 'auction_group_{}'.format(self.pk)

    def advance_participants(self):
        channels.Group(self.get_channel_group_name()).send(
            {'text': json.dumps({'accept': True, 'session': self.session.code})})

def runEverySecond():
    print('checking if there are active groups...')
    if group_model_exists():
        activated_groups = Group.objects.filter(activated=True)
        for g in activated_groups:
            if g.price < 52:
                g.price += 1
                g.save()
                channels.Group(
                    g.get_channel_group_name()
                ).send(
                    {'text': json.dumps(
                        {'price': g.price,
                         'session': g.session.code})}
                )
            else:
                g.timeout = True
                g.save()
                l.stop()
                g.advance_participants()


l = task.LoopingCall(runEverySecond)
if not l.running:
    l.start(2.0)

