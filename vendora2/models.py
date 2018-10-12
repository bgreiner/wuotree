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
    name_in_url = 'VendorA2'
    num_rounds = 5
    price = 12
    cost = [3,9]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.rand_demand()
            if self.round_number == 1:
                p.rand_cost()
            else:
                p.cost_from_previous()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    order = models.PositiveIntegerField(min = 0, max = 300)
    demand = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()

    def rand_demand(self):
        self.demand = random.randrange(0,301)

    def cost_from_previous(self):
        self.cost = self.in_round(self.subsession.round_number -1).cost

    def rand_cost(self):
        self.cost = Constants.cost[random.randrange(0,2)]
        self.participant.vars['previous_cost'] = self.cost

    def set_payoff(self):
        self.payoff = c((min(self.demand, self.order) * Constants.price) - (self.order * self.cost))