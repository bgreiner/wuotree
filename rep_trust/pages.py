from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class MyWaitPage(WaitPage):
    pass

class BuyPage(Page):
    def is_displayed(self):
        return self.player.role == 'Buyer'
    form_model = 'group'
    form_fields = ['buy']
    pass

class SellPage(Page):
    def is_displayed(self):
        return self.player.role == 'Seller' and self.group.buy
    form_model = 'group'
    form_fields = ['produce']
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass


class Results(Page):
    pass


page_sequence = [
    BuyPage,
    MyWaitPage,
    SellPage,
    ResultsWaitPage,
    Results
]
