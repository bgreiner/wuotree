from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class PersonA(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1 and self.group.cont == 'Right'
    form_model = 'group'
    form_fields = ['cont']
    def before_next_page(self):
        if self.group.cont == 'Right':
            self.group.count_pages()

class PersonB(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.cont == 'Right'
    form_model = 'group'
    form_fields = ['cont']
    def before_next_page(self):
        if self.group.cont == 'Right':
            self.group.count_pages()

class IntWaitPage(WaitPage):
    def is_displayed(self):
        return self.group.cont == 'Right'

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass


class Results(Page):
    def before_next_page(self):
        if self.subsession.round_number == 3:
            self.group.set_rand_payoff()
    pass


page_sequence = [
    Introduction,
    PersonA,
    IntWaitPage,
    PersonB,
    IntWaitPage,
    PersonA,
    IntWaitPage,
    PersonB,
    IntWaitPage,
    PersonA,
    IntWaitPage,
    PersonB,
    IntWaitPage,
    PersonA,
    IntWaitPage,
    PersonB,
    IntWaitPage,
    PersonA,
    IntWaitPage,
    PersonB,
    ResultsWaitPage,
    Results
]
