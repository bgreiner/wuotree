from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json
import channels



class Intro(Page):
    ...

class StartWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.activated = True


class Decision(Page):
    form_model = 'player'
    form_fields = ['drop_out']


    def before_next_page(self):
        if self.player.drop_out:
            finished = 0
            for p in self.group.get_players():
                finished += p.drop_out
            if finished == 3:
                self.group.advance_participants()
                self.group.activated = False



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    pass


page_sequence = [
    Intro,
    StartWaitPage,
    Decision,
    ResultsWaitPage,
    Results
]
