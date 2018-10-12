from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):

    pass

class Strategies(Page):
    form_model = 'group'
    form_fields = ['choice_1', 'choice_2']

    def is_displayed(self):
        return self.player.committee

    def error_message(self, values):
        if values["choice_2"] == values["choice_1"]:
            return 'You must select two different strategies.'

    def before_next_page(self):
        self.group.set_final_choice()

class Vote_1(Page):
    form_model = 'player'
    form_fields = ['vote_1']

    def vote_1_choices(self):
        choices = [self.group.choice_1,self.group.choice_2]
        return choices

    def vars_for_template(self):
        return {'vote_choice_1': self.group.choice_1,
                'vote_choice_2': self.group.choice_2,
                'vote_choice_3': self.group.choice_3
                }


class ChairWaitPage(WaitPage):
    title_text = "Waiting for chairperson to decide"
    body_text = "The chairperson will now choose the two strategies that will compete in the first round of voting..."

class InterimWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.round_1_vote()
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.final_vote()
    pass

class Interim(Page):
    def vars_for_template(self):
        return {'a_choice': self.group.get_player_by_id(1).vote_1,
                'b_choice': self.group.get_player_by_id(2).vote_1,
                'c_choice':self.group.get_player_by_id(3).vote_1,
                'vote_choice_1': self.group.choice_1,
                'vote_choice_2': self.group.choice_3
                }
    pass


class Vote_2(Page):
    form_model = 'player'
    form_fields = ['vote_2']

    def vote_2_choices(self):
        choices = [self.group.round_1_winner,self.group.choice_3]
        return choices

    def vars_for_template(self):
        return {'vote_choice_1': self.group.round_1_winner,
                'vote_choice_2': self.group.choice_3
                }
    pass

class Results(Page):
    def vars_for_template(self):
        return {'a_choice_2': self.group.get_player_by_id(1).vote_2,
                'b_choice_2': self.group.get_player_by_id(2).vote_2,
                'c_choice_2': self.group.get_player_by_id(3).vote_2}


    pass



page_sequence = [
    Intro,
    Strategies,
    ChairWaitPage,
    Vote_1,
    InterimWaitPage,
    Interim,
    Vote_2,
    ResultsWaitPage,
    Results
]
