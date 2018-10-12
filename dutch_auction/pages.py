from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    pass
class Auction(Page):
    form_model = 'player'
    form_fields = ['drop_out']
    def is_displayed(self):
        return not self.player.drop_out and not self.group.auction_ended
    pass

class AuctionWaitPage(WaitPage):
    def is_displayed(self):
        return not self.group.auction_ended
    def after_all_players_arrive(self):
        self.group.increase_price()
    pass

class Wait(WaitPage):
    wait_for_all_groups = True
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass

class Results(Page):
    pass


page_sequence = [Intro, Wait]
for x in range(0,50):
    page_sequence.append(Auction)
    page_sequence.append(AuctionWaitPage)
page_sequence.append(ResultsWaitPage)
page_sequence.append(Results)