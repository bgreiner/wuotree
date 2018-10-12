from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Jon Wood'

doc = """
Two players are matched with the roles Socialiser and Hermit. They have a choice to visit
either the lake or the forest. The Hermit prefers to be alone and the socialiser prefers
if both players end up at the same location.
"""


class Constants(BaseConstants):
    name_in_url = 'PenaltyKickBri'
    players_per_group = 2
    num_rounds = 3
    roles = ['Keeper', 'Striker']
    choices = ['Right', 'Left']
    payoff_bribed_matrix_same = {'Keeper': {'Left': 20, 'Right': 10}, 'Striker': {'Left': 10, 'Right': 20}}
    payoff_bribed_matrix_diff = {'Keeper': {'Left': 0, 'Right': 0}, 'Striker': {'Left': 0, 'Right': 0}}
    payoff_matrix_same = {'Keeper': {'Left': 20, 'Right': 10}, 'Striker': {'Left': 0, 'Right': 0}}
    payoff_matrix_diff = {'Keeper': {'Left': 0, 'Right': 0}, 'Striker': {'Left': 10, 'Right': 20}}



class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for p in self.get_groups():
            p.set_bribe()
        for p in self.get_players():
            p.set_role()

    pass


class Group(BaseGroup):
    def set_payoff(self):
        for p in self.get_players():
            p.set_payoff()

    bribed = models.BooleanField()

    def set_bribe(self):
        self.bribed = random.choice([True,False])

    def check_zero(self):
        for p in self.get_players():
            p.check_zero()

    pass


class Player(BasePlayer):
    role = models.StringField(choices=Constants.roles)
    choice = models.StringField(choices=Constants.choices)

    def set_role(self):
        if self.id_in_group == 1:
            self.role = 'Keeper'
        else:
            self.role = 'Striker'

    def check_zero(self):
        if self.choice == "": self.choice = Constants.choices[0]

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.group.bribed:
            if self.choice == self.other_player().choice:
                self.payoff = Constants.payoff_bribed_matrix_same[self.role][self.choice]
            else:
                self.payoff = Constants.payoff_bribed_matrix_diff[self.role][self.choice]
        else:
            if self.choice == self.other_player().choice:
                self.payoff = Constants.payoff_matrix_same[self.role][self.choice]
            else:
                self.payoff = Constants.payoff_matrix_diff[self.role][self.choice]
    pass
