from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def is_displayed(self):
        return self.player.role == 'Firm'
    form_model = 'player'
    form_fields = ['wage_offered']
    pass

class Master(Page):
    def is_displayed(self):
        return self.player.role == 'Employee'
    form_model = 'player'
    form_fields = ['master']
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.check_zero()
        self.group.set_payoff()
        pass

class MyWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
    Master,
    MyWaitPage,
    MyPage,
    ResultsWaitPage,
    Results
]