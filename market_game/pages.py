from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Roles(Page):
    pass

class Choose(Page):
    def is_displayed(self):
        return self.player.id_in_group != 3

    form_model = 'player'
    form_fields = ['offer']

    def offer_error_message(self, value):
        if not(value in Constants.offer_choices):
            return 'Must be be in increments of E$0.01'
    pass

class Accept(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3
    form_model = 'group'
    form_fields = ['accepted']
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
    Roles,
    Choose,
    MyWaitPage,
    Accept,
    ResultsWaitPage,
    Results
]
