from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['wage_offered']
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.check_zero()
        self.group.set_payoff()
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
