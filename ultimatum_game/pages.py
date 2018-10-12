from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants


class Offer(Page):
    form_model = 'group'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1

class WaitForProposer(WaitPage):
    def vars_for_template(self):
            body_text = "You were randomly assigned the role of person B. You were randomly matched with a participant in the role of person A.\
                        Person A now decides how much of the E$ 100 she/he gives to you, and how much she/he takes for herself/himself.\
                        Then you will decide whether to accept or reject that offer."
            return {'body_text': body_text}
    def is_displayed(self):
        return self.player.id_in_group == 2

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


page_sequence = [Offer,
                 WaitForProposer,
                 Accept,
                 ResultsWaitPage,
                 Results]
