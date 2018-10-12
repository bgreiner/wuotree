from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Optimal_1(Page):
    form_model = 'player'
    form_fields = ['optimal_1']

class Optimal_2(Page):
    form_model = 'player'
    form_fields = ['optimal_2']


page_sequence = [Optimal_1,
                 Optimal_2]

