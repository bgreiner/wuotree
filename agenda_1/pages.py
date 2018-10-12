from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):

    pass

class Strategies(Page):
    form_model = 'player'
    form_fields = ['choice_1', 'choice_2']

    def before_next_page(self):
        self.player.pop_vote_1()
        self.player.pop_vote_2()
    """pop vote_1 from vote_order"""
    pass

    def error_message(self, values):
        if values["choice_2"] == values["choice_1"]:
            return 'You must select two different strategies.'

"""
class Strategies_2(Page):
    form_model = 'player'
    form_fields = ['choice_2']

    def choice_2_choices(self):
        choices = self.participant.vars['vote_choices']
        return choices

    def before_next_page(self):
        self.player.pop_vote_2()
    pass

"""
class Vote_1(Page):
    form_model = 'player'
    form_fields = ['vote_1']

    def vote_1_choices(self):
        choices = self.participant.vars['vote_order']
        return choices

    def before_next_page(self):
        self.player.round_1_vote()
        self.player.pop_vote_3()

    def vars_for_template(self):
        return {'vote_choice_1': self.participant.vars['vote_order'][0],
                'vote_choice_2': self.participant.vars['vote_order'][1],
                'vote_choice_3': self.participant.vars['vote_choices'][0]
                }
    pass


class Interim(Page):
    def vars_for_template(self):
        return {'vote_choice_1': self.participant.vars['vote_choices'][0],
                'vote_choice_2': self.participant.vars['vote_choices'][1]
                }
    pass


class Vote_2(Page):
    form_model = 'player'
    form_fields = ['vote_2']

    def vote_2_choices(self):
        choices = self.participant.vars['vote_choices']
        return choices

    def before_next_page(self):
        self.player.final_vote()
        self.player.set_payoff()

    def vars_for_template(self):
        return {'vote_choice_1': self.participant.vars['vote_choices'][0],
                'vote_choice_2': self.participant.vars['vote_choices'][1]
                }

    pass



class Results(Page):
    def before_next_page(self):
        self.player.reset_vote_arrays()
    pass



page_sequence = [
    Intro,
    Strategies,
    Vote_1,
    Interim,
    Vote_2,
    Results
]
