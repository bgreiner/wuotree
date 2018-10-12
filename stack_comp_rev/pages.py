from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass

class MyWaitPage(WaitPage):
    pass

class Prod1(Page):
    def is_displayed(self):
        return self.player.role == 'Producer 1'
    form_model = 'player'
    form_fields = ['number_of_bottles_redecide']

class Prod2(Page):
    form_model = 'player'
    form_fields = ['number_of_bottles']

class Prod1Redecide(Page):
    def is_displayed(self):
        return self.player.role == 'Producer 1'
    form_model = 'player'
    form_fields = ['number_of_bottles']

class WaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()
        pass


class Results(Page):
    timeout_seconds = 30
    pass


page_sequence = [
    MyPage,
    Prod1,
    MyWaitPage,
    Prod2,
    MyWaitPage,
    ResultsWaitPage,
    Results
]
