from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Decide(Page):
    form_model = 'player'
    form_fields = ['order']
    def before_next_page(self):
        self.player.set_payoff()

class Instructions(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class Results(Page):
    timeout_seconds = 20


page_sequence = [Instructions,
                 Decide,
                 Results]
