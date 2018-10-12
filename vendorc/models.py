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
    name_in_url = 'VendorC'
    num_rounds = 1
    cost = [3,9]

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.cost_order()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    optimal_1 = models.PositiveIntegerField()
    optimal_2 = models.PositiveIntegerField()

    cost_1 = models.PositiveIntegerField()
    cost_2 = models.PositiveIntegerField()


    def cost_order(self):
        first_choice = random.randrange(0,2)
        self.cost_1 = Constants.cost[first_choice]
        self.cost_2 = Constants.cost[first_choice - 1]

