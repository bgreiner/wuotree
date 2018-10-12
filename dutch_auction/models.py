from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Jon Wood'

doc = """
Bidders are assigned a random certificate price and then compete in a bid
for a certificate whose value decreases periodically.
"""

class Constants(BaseConstants):
    name_in_url = 'dutchauction'
    players_per_group = 4
    num_rounds = 1
    start_price = 55
    increment = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
        for p in self.get_players():
            p.set_cert()
    pass


class Group(BaseGroup):
    winner = models.PositiveIntegerField()
    auction_ended = models.BooleanField(initial=False)
    current_price = models.IntegerField(initial=Constants.start_price)
    mult_win = models.BooleanField(initial=False)

    def increase_price(self):
        game_over = 0
        for p in self.get_players():
            game_over += p.drop_out
        if game_over > 0:
            self.auction_ended = True
        else:
            self.current_price -= Constants.increment
            for p in self.get_players():
                if p.drop_out:
                    p.dropped_out = True

    def set_payoff(self):
        winners = []
        game_over = 0
        for p in self.get_players():
            game_over += p.drop_out
        if game_over > 1:
            self.mult_win = True
        for p in self.get_players():
            if p.drop_out: 
                winners.append(p.id_in_group)
        random_win = random.choice(winners)        
        for p in self.get_players():
            if p.id_in_group == random_win:
                self.winner = p.id_in_group
                p.winner = True
                p.payoff = p.cert_price - self.current_price
            else:
                p.payoff = 0

    pass


class Player(BasePlayer):
    drop_out = models.BooleanField(initial=False)
    dropped_out = models.BooleanField(initial=False)
    winner = models.BooleanField(initial=False)
    cert_price = models.CurrencyField()

    def set_cert(self):
        self.cert_price = random.randrange(10,50,1)
    pass
