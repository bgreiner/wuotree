from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Jon Wood'

doc = """
Two players are matched with the roles Socializer and Hermit. They have a choice to visit
either the lake or the forest. The Hermit prefers to be alone and the socialiser prefers
if both players end up at the same location.
"""


class Constants(BaseConstants):
    name_in_url = 'SocialHermitb'
    players_per_group = 2
    num_rounds = 3
    roles = ['Socializer', 'Hermit']
    choices = ['Lake', 'Forest']
    payoff_matrix = {'Socializer': [10,0], 'Hermit': [0,10]}



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
            self.pref = 'Forest'
        else:
            self.pref = 'Lake'

    def set_role(self):
        if self.id_in_group == 1:
            self.role = 'Socializer'
        else:
            self.role = Constants.roles[random.randrange(0,2)]

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.choice == self.other_player().choice:
            self.payoff = Constants.payoff_matrix[self.role][0]
            if self.choice == self.pref and self.role == 'Socializer':
                self.payoff += 10
        else:
            self.payoff = Constants.payoff_matrix[self.role][1]
            if self.choice == self.pref and self.role == 'Hermit':
                self.payoff += 10
    pass
