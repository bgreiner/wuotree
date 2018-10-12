from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.role == 'Employee':
            yield (pages.Master, {'master': 'Yes'})
        else:
            yield (pages.MyPage, {'wage_offered': 20})
        yield (pages.Results)
        if self.player.role == 'Employee':
            print(self.player.role,self.player.skill_level,self.player.master,self.player.payoff)
        else:
            print(self.player.role, self.player.wage_offered, self.player.payoff)