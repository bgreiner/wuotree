from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['chosen_price']
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass


class Results(Page):
    def vars_for_template(self):
        return {
            'my_demand': Constants.bolts_sold[self.player.chosen_price],
            'other_player_demand': Constants.bolts_sold[self.player.other_player().chosen_price],
        }
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
