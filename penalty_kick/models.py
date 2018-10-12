from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Jon Wood'

doc = """

"""


class Constants(BaseConstants):
    name_in_url = 'PenaltyKick'
    players_per_group = 2
    num_rounds = 5
    roles = ['Keeper', 'Striker']
    choices = ['Right', 'Left']
    payoff_matrix = {'Keeper': [20,-20], 'Striker': [-20,20]}



class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for p in self.get_players():
            p.set_role()
    pass


class Group(BaseGroup):
    def set_payoff(self):
        for p in self.get_players():
            p.set_payoff()

    pass


class Player(BasePlayer):
    role = models.StringField(choices=Constants.roles)
    choice = models.StringField(choices=Constants.choices)
    stated_choice = models.StringField(
        choices=[
            ['Left', 'I am going to shoot Left'],
            ['Right', 'I am going to shoot Right'],
        ])

    def set_role(self):
        if self.id_in_group == 1:
            self.role = 'Keeper'
        else:
            self.role = 'Striker'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.choice == self.other_player().choice:
            self.payoff = Constants.payoff_matrix[self.role][0]
        else:
            self.payoff = Constants.payoff_matrix[self.role][1]
    pass
