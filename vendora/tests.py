from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        if self.subsession.round_number == 1:
            yield (pages.Instructions)
            if self.group.id_in_subsession == 3 or self.group.id_in_subsession == 4:
                if self.player.cost == 3:
                    yield (pages.Optimal_1, {'optimal_1': random.randrange(185, 206, 5)})
                else:
                    yield (pages.Optimal_1, {'optimal_1': random.randrange(100, 120, 5)})
        if self.player.cost == 3:
            yield (pages.Decide, {'order': random.randrange(175,196,5)})
        else:
            yield (pages.Decide, {'order': random.randrange(120, 146, 5)})
        yield (pages.Results)
