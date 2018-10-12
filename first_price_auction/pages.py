from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Bid(Page):
    form_model = 'player'
    form_fields = ['bid']
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass


class Results(Page):
    pass


page_sequence = [
    Bid,
    ResultsWaitPage,
    Results
]
