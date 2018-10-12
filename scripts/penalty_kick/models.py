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
    num_rounds = 3
    roles = ['Keeper', 'Striker']
    choices = ['Right', 'Left']
    payoff_matrix = {'Keeper': [10,0], 'Striker': [0,10]}



class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for p in self.get_players():
            p.set_role()
            p.set_pref()
    pass


class Group(BaseGroup):
    def set_payoff(self):
        for p in self.get_players():
            p.set_payoff()

    pass


class Player(BasePlayer):
    role = models.StringField(choices=Constants.roles)
    choice = models.StringField(choices=Constants.choices)
    pref = models.StringField(choices=Constants.choices)
    def set_pref(self):
        if self.id_in_group == 1:
            self.pref = 'Left'
        else:
            self.pref = 'Right'

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
            if self.choice == self.pref and self.role == 'Keeper':
                self.payoff += 10
        else:
            self.payoff = Constants.payoff_matrix[self.role][1]
            if self.choice == self.pref & self.role == 'Striker':
                self.payoff += 10
    pass
