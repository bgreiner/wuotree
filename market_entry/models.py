from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Jon Wood'

doc = """

"""


class Constants(BaseConstants):
    name_in_url = 'MarketEntry'
    players_per_group = 2
    num_rounds = 5
    roles = ['A', 'B']
    choices = ['Enter The Market', 'Do Not Enter The Market']



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


    def set_role(self):
        if self.id_in_group == 1:
            self.role = 'A'
        else:
            self.role = 'B'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.choice == self.other_player().choice:
            if self.choice == 'Enter The Market':
                self.payoff = -20
                if self.role == 'B':
                    self.payoff -= 30
            else:
                self.payoff = 0
        else:
            if self.choice == 'Enter The Market':
                self.payoff = 40
                if self.role == 'B':
                    self.payoff -= 30
            else:
                self.payoff = 0
    pass
