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
    name_in_url = 'VendorA'
    num_rounds = 20
    price = 12
    cost = [3,9]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            matrix = self.get_group_matrix()
            flat_matrix = [item for sublist in matrix for item in sublist]
            random.shuffle(flat_matrix)
            size_of_groups = len(flat_matrix) // 4 + \
                             (len(flat_matrix) % 4 > 0)
            new_matrix = [flat_matrix[i:i + size_of_groups]
                          for i in range(0, len(flat_matrix), size_of_groups)]

            self.set_group_matrix(new_matrix)
        else:
            self.group_like_round(1)
            print(self.get_group_matrix())
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
    optimal_1 = models.PositiveIntegerField()

    def rand_demand(self):
        self.demand = random.randrange(0,301)

    def cost_from_previous(self):
        self.cost = self.in_round(self.subsession.round_number -1).cost

    def rand_cost(self):
        self.cost = Constants.cost[self.group.id_in_subsession % 2]
        self.participant.vars['previous_cost'] = self.cost

    def set_payoff(self):
        self.payoff = c((min(self.demand, self.order) * Constants.price) - (self.order * self.cost))