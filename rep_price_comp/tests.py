from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group == 1:
            yield (pages.MyPage, {'chosen_price': self.do_something_else()})
        else:
            yield (pages.MyPage, {'chosen_price': self.do_something()})
        yield (pages.Results)
        print(self.player.id_in_group, self.player.payoff)


    def do_something(self):
        thing = 0
        if self.subsession.round_number < 7:
            thing = Constants.prices[self.subsession.round_number]
        else:
            thing = 0.07
        return thing

    def do_something_else(self):
        thing = 0
        if self.subsession.round_number < 7:
            thing = Constants.prices[6-self.subsession.round_number]
        else:
            thing = 0.07
        return thing