from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.role == 'Firm':
            yield (pages.MyPage, {'wage_offered': 20})
        else:
            yield (pages.MyPage)
        yield (pages.Results)
        print(self.player.role,self.player.skill_level,self.player.payoff)
