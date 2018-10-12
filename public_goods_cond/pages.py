from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['contribution']
    pass

class MyPage2(Page):
    form_model = 'player'
    form_fields = ['cond_cont{}'.format(i) for i in range(1, 11)]
    def before_next_page(self):
        self.group.mayor_lotto()
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    MyPage2,
    ResultsWaitPage,
    Results
]

