from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Note(Page):
    def is_displayed(self):
        return self.player.role == 'Hermit'
    form_model = 'player'
    form_fields = ['stated_choice']
    pass

class Receive_Note(Page):
    def is_displayed(self):
        return self.player.role == 'Socialiser'
    pass

class MyPage(Page):
    form_model = 'player'
    form_fields = ['choice']
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass

class MyWaitPage(WaitPage):
    pass


class Results(Page):
    pass

page_sequence = [
    Note,
    Receive_Note,
    MyWaitPage,
    MyPage,
    ResultsWaitPage,
    Results
]

