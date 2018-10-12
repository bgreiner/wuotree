from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Introduction)
        if self.player.id_in_group == 1:
            yield (Player1ChoosePage, {'price': 0.30})
        yield (pages.IntWaitPage)
        if self.player.id_in_group == 2:
            yield (Player2ChoosePage, {'price': 0.30})
        yield (pages.IntWaitPage)
        if self.player.id_in_group == 3:
            yield (Player3ChoosePage, {'price': 0.30})
        yield (pages.IntWaitPage)
        if self.player.id_in_group == 4:
            yield (Player4ChoosePage, {'price': 0.30})
        yield (pages.IntWaitPage)
        if self.player.id_in_group == 5:
            yield (Player5ChoosePage, {'price': 0.30})
        yield (pages.ResWaitPage)
        yield (pages.Results)
