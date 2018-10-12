from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'RepPrice'
    players_per_group = 2
    num_rounds = 10
    prices = [0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12]
    bolts_sold = {0.06: 1200,
                  0.07: 1000,
                  0.08: 800,
                  0.09: 700,
                  0.10: 600,
                  0.11: 550,
                  0.12: 500,
                  }

class Subsession(BaseSubsession):
    def before_subsession_starts(self):
        if self.subsession.round_number == 1:
            self.group_randomly()
    pass


class Group(BaseGroup):
    winning_demand = models.IntegerField()
    winning_price = models.FloatField()
    def set_payoff(self):
        for p in self.get_players():
            p.check_zero()
            p.set_payoff()

    pass


class Player(BasePlayer):
    chosen_price = models.FloatField(choices=Constants.prices)
    winner = models.BooleanField()

    def check_zero(self):
        if self.chosen_price not in Constants.prices: self.chosen_price = Constants.prices[0]

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = (self.chosen_price - 0.05) * Constants.bolts_sold[self.chosen_price]
        if self.chosen_price < self.other_player().chosen_price:
           self.payoff = payoff
           self.winner = True
           self.group.winning_demand = Constants.bolts_sold[self.chosen_price]
           self.group.winning_price = self.chosen_price
        elif self.chosen_price == self.other_player().chosen_price:
            self.payoff = payoff/2
            self.winner = True
            self.group.winning_demand = int(Constants.bolts_sold[self.chosen_price]/2)
            self.group.winning_price = self.chosen_price
        else:
            self.payoff = 0
            self.winner = False
    pass
