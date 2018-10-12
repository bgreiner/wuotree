from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = "Jon Wood"

doc = """
"""


class Constants(BaseConstants):
    players_per_group = None
    name_in_url = 'VendorB'
    num_rounds = 5
    price = 12
    cost = {3:9,9:3}


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.rand_demand()
            p.new_cost()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    order = models.PositiveIntegerField(min = 0, max = 300)
    demand = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()

    def rand_demand(self):
        self.demand = random.randrange(0,301)

    def new_cost(self):
        self.cost = Constants.cost[self.participant.vars['previous_cost']]

    def set_payoff(self):
        self.payoff = c((min(self.demand, self.order) * Constants.price) - (self.order * self.cost))