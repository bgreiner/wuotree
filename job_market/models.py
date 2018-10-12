from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'JobMark'
    players_per_group = 2
    num_rounds = 3
    roles = ['Employee', 'Firm']
    skill_level = {'High': 2, 'Low': 0}
    wages = [20,40]

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for p in self.get_players():
            p.set_role()
    pass


class Group(BaseGroup):
    def check_zero(self):
        for p in self.get_players():
            p.check_zero()

    def set_payoff(self):
        for p in self.get_players():
            p.set_payoff()
    pass


class Player(BasePlayer):
    role = models.StringField(choices=Constants.roles)
    skill_level = models.StringField()
    wage_offered = models.PositiveIntegerField(choices=Constants.wages, blank=True)

    def other_player(self):
        return self.get_others_in_group()[0]

    def check_zero(self):
        if self.wage_offered == None: self.wage_offered = 0

    def set_payoff(self):
        if self.role == 'Employee':
            self.payoff = self.other_player().wage_offered
        else:
            self.payoff = (40 - self.wage_offered) + (self.wage_offered*Constants.skill_level[self.other_player().skill_level])


    def set_role(self):
        if self.id_in_group == 1:
            self.role = 'Employee'
            self.skill_level = list(Constants.skill_level)[random.randrange(100) < 60]
        else:
            self.role = 'Firm'
    pass
