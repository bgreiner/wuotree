from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Jon Wood'

doc = """
Bidders are assigned a random certificate price and then compete in a bid
where participants bid simultaneously. The payment the winning participant
pays however, is decided by the second highest bid.
"""


class Constants(BaseConstants):
    name_in_url = 'SecPrice'
    players_per_group = 4
    num_rounds = 1
    start_price = 5


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
        for p in self.get_players():
            p.set_cert()
    pass


class Group(BaseGroup):
    winner = models.PositiveIntegerField()
    winning_bid = models.PositiveIntegerField()
    mult_win = models.BooleanField()
    second_highest = models.PositiveIntegerField()

    def set_payoff(self):
        highest = 0
        second_highest = 0
        winner_collection = []
        for p in self.get_players():
            if p.bid > highest:
                second_highest = highest
                highest = p.bid
            if highest > p.bid > second_highest:
                second_highest = p.bid
        for p in self.get_players():
            if p.bid == highest:
                p.winner = True
                winner_collection.append(p.id_in_group)
        if len(winner_collection) > 1:
            self.mult_win = True
            second_highest = highest
        random_win = random.choice(winner_collection)
        for p in self.get_players():
            if p.winner and p.id_in_group == random_win:
                p.payoff = p.cert_price - second_highest
                self.second_highest = second_highest
                self.winner = p.id_in_group
                self.winning_bid = p.bid
            else:
                p.payoff = c(0)


    pass


class Player(BasePlayer):
    bid = models.CurrencyField(min=0,max=100)
    cert_price = models.CurrencyField()
    winner = models.BooleanField(initial=False)

    def set_cert(self):
        self.cert_price = random.randrange(10,50,1)
    pass
    pass
