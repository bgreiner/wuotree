from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group == 1:
            yield (pages.MyPage, {'turn': 'Left'})
            print(self.player.payoff)
        else:
            yield (pages.MyPage, {'turn': 'Right'})
            print(self.player.payoff)