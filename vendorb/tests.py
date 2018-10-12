from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        # compete price
        if self.subsession.round_number == 1:
            yield (pages.Instructions)
        if self.player.cost == 3:
            yield (pages.Decide, {'order': random.randrange(175,196,5)})
        else:
            yield (pages.Decide, {'order': random.randrange(120, 146, 5)})
        yield (pages.Results)
