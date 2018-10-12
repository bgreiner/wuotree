from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Info(Page):
    pass

class WinePricePage(Page):
    def is_displayed(self):
        return self.player.role == 'Seller'
    form_model = 'player'
    form_fields = ['wine_sell_price']

class WineBuyPage(Page):
    def is_displayed(self):
        return self.player.role != 'Seller'

    form_model = 'player'
    form_fields = ['number_of_bottles']
    pass

class IntWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):
    timeout_seconds = 30
    pass


page_sequence = [
    Info,
    WinePricePage,
    IntWaitPage,
    WineBuyPage,
    ResultsWaitPage,
    Results
]
