from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Jon Wood'

doc = """
Bidders are assigned a random certificate price and then compete in a bid
where participants bid simultaneously.
"""

class Constants(BaseConstants):
    name_in_url = 'FirstPrice'
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

    def set_payoff(self):
        highest = 0
        winner_collection = []
        for p in self.get_players():
            if p.bid > highest:
                highest = p.bid
        for p in self.get_players():
            if p.bid == highest:
                p.winner = True
                winner_collection.append(p.id_in_group)
        if len(winner_collection) > 1:
            self.mult_win = True
        random_win = random.choice(winner_collection)
        for p in self.get_players():
            if p.winner and p.id_in_group == random_win:
                p.payoff = p.cert_price - highest
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
