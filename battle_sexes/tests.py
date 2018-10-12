from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.role == 'Rugby':
            yield (pages.MyPage, {'choice': 'Opera'})
        else:
            yield (pages.MyPage, {'choice': 'Rugby'})
        yield (pages.Results)
        print(self.player.role,self.player.choice,self.player.payoff)
