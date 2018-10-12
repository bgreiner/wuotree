from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants

class Role(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
    pass

class Offer(Page):
    form_model = 'group'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1

class WaitForProposer(WaitPage):
    pass

class Accept(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2
    form_model = 'group'
    form_fields = ['offer_accepted']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [Role,
                 Offer,
                 WaitForProposer,
                 Accept,
                 ResultsWaitPage,
                 Results]
