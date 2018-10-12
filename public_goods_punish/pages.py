from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['contribution']
    pass


class FirstWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_initial_payoffs()
        pass

class Punishment(Page):
    form_model = 'player'
    form_fields = ['punishment_1',
                   'punishment_2',
                   'punishment_3',
                   'punishment_4']
    def error_message(self, values):
        if int(values["punishment_1"] or 0) + int(values["punishment_2"] or 0)\
                + int(values["punishment_3"] or 0)  + int(values["punishment_4"] or 0) > self.player.kept:
            return 'Cannot be more than the money you have left - {} E$'.format(int(self.player.kept))

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        pass


class Results(Page):
    pass



page_sequence = [
    MyPage,
    FirstWaitPage,
    Punishment,
    ResultsWaitPage,
    Results
]
