from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class FirstPage(Page):
    form_model = 'player'
    form_fields = ['num_chosen']
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.get_lowest()
        for p in self.group.get_players():
            p.set_payoff()
        pass


class Results(Page):
    pass


page_sequence = [
    FirstPage,
    ResultsWaitPage,
    Results
]
