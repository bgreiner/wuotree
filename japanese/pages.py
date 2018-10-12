from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json
import channels
from .finish_auction import advance_participants



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
                advance_participants([p.participant for p in self.player.get_others_in_group()])
        else:
            self.group.activated = False
            self.player.auction_winner = True


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
