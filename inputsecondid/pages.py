from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class IDPage(Page):
    form_model = 'player'
    form_fields = ['player2id']

    def vars_for_template(self):
        return {
            'participant_label': self.participant.label,
        }

page_sequence = [
    IDPage
]
