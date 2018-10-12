from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class FirstPage(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
    pass

class Continue(WaitPage):
    title_text = "Auction Continuing"
    def after_all_players_arrive(self):
            self.group.get_last_round()

    def is_displayed(self):
        return self.subsession.round_number != 1
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.check_winner_decided()
        self.group.set_payoff()
    pass

class Results(Page):
    def is_displayed(self):
        return self.group.winner_decided
    pass

class ThankYou(Page):
    def is_displayed(self):
        return self.group.winner_decided
    pass

class PlayerChoice(Page):

    form_model = 'player'
    form_fields = ['bid']

    def error_message(self, values):
        if 0 < values["bid"] <= self.group.highest_bid:
            return 'Must be higher than current bid. Or 0 to drop out.'

    def before_next_page(self):
        self.player.set_highest_bid()
        self.group.check_winner_decided()
        pass

class Player1Choice(PlayerChoice):
    def is_displayed(self):
        return self.player.id_in_group == 1 and not self.player.drop_out and not self.group.winner_decided
    pass

class Player2Choice(PlayerChoice):
    def is_displayed(self):
        return self.player.id_in_group == 2 and not self.player.drop_out and not self.group.winner_decided
    pass

class Player3Choice(PlayerChoice):
    def is_displayed(self):
        return self.player.id_in_group == 3 and not self.player.drop_out and not self.group.winner_decided
    pass

class Player4Choice(PlayerChoice):
    def is_displayed(self):
        return self.player.id_in_group == 4 and not self.player.drop_out and not self.group.winner_decided
    pass

class ThankYou(Page):
    def is_displayed(self):
        return self.group.winner_decided
    pass

class MyWaitPage(WaitPage):
    pass

page_sequence = [
    FirstPage,
    Continue,
    Player1Choice,
    MyWaitPage,
    Player2Choice,
    MyWaitPage,
    Player3Choice,
    MyWaitPage,
    Player4Choice,
    ResultsWaitPage,
    Results,
    ThankYou
]
