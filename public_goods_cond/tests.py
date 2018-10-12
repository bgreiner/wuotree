from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        d={}
        for x in range(1,11):
            d["cond_cont{0}".format(x)]=5
        yield (pages.MyPage, {'contribution': 5})
        yield (pages.MyPage2, d)
        yield (pages.Results)
        print(self.player.payoff)
