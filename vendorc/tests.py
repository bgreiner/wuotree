from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        if self.player.cost_1 == 3:
            yield (pages.Optimal_1, {'optimal_1': random.randrange(185,206,5)})
        else:
            yield (pages.Optimal_1, {'optimal_1': random.randrange(100,120,5)})
        if self.player.cost_2 == 3:
            yield (pages.Optimal_2, {'optimal_2': random.randrange(185,206,5)})
        else:
            yield (pages.Optimal_2, {'optimal_2': random.randrange(100,120,5)})