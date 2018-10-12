from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Jon Wood'

doc = """
Bidders are assigned a random certificate price and then compete in a bid
where participants bid sequentially.
"""

class Constants(BaseConstants):
    name_in_url = 'englishauction'
    players_per_group = 4
    num_rounds = 50
    start_price = 0

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
            for p in self.get_players():
                p.set_cert()
        else:
            for p in self.get_players():
                p.get_cert()
    pass


class Group(BaseGroup):
    highest_bid = models.IntegerField(initial=Constants.start_price)
    winner_decided = models.BooleanField(initial=False)

    def get_last_round(self):
        self.highest_bid = self.in_round(self.round_number - 1).highest_bid
        for p in self.get_players():
            p.get_lastround_bid()
            p.get_lastround_drop()

    def check_winner_decided(self):
        wincheck=0
        for p in self.get_players():
            wincheck += p.drop_out
        if wincheck == 3:
            self.winner_decided = True

    def set_payoff(self):
        if self.winner_decided:
            for p in self.get_players():
                if not p.drop_out:
                    p.winner = True
                    p.payoff = c(p.cert_price - self.highest_bid)
                else:
                    p.payoff = c(0)

    pass


class Player(BasePlayer):
    bid = models.PositiveIntegerField(max=70)
    drop_out = models.BooleanField(initial=False)
    winner = models.BooleanField(initial=False)
    cert_price = models.CurrencyField()

    def set_highest_bid(self):
        if self.bid > self.group.highest_bid:
            self.group.highest_bid = self.bid
        else:
            self.drop_out = True

    def set_cert(self):
        self.cert_price = random.randrange(10,50,1)
    pass

    def get_cert(self):
        self.cert_price = self.in_round(self.round_number - 1).cert_price
    pass

    def get_lastround_bid(self):
        if self.subsession.round_number != 1:
            self.bid = self.in_round(self.round_number - 1).bid

    def get_lastround_drop(self):
        if self.subsession.round_number != 1:
            self.drop_out = self.in_round(self.round_number - 1).drop_out