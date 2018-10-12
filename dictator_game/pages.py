from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'group'
    form_fields = ['given']

    def is_displayed(self):
        return self.player.id_in_group == 1


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):
        if self.player.id_in_group == 2:
            body_text = "You were randomly assigned the role of person B. You were randomly matched with a participant in the role of person A." \
                        " Person A now decides how much of the E$ 100 she/he gives to you, and how much she/he takes for herself/himself."
        else:
            body_text = 'Please wait'
        return {'body_text': body_text}


class Results(Page):
    def vars_for_template(self):
        return {
            'offer': Constants.endowment - self.group.kept,
        }


page_sequence = [
    Offer,
    ResultsWaitPage,
    Results
]
