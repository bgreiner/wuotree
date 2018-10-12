from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
Two cars are driving heading for a collision. The pairs of players decide whether to swerve
or go straight. A collision loses you money - as does swerving. Going straight and not hitting
anything makes you the winner.
"""


class Constants(BaseConstants):
    name_in_url = 'chicken'
    players_per_group = 2
    num_rounds = 3
    roles = ['Swerve', 'Go Straight']
    payoff_matrix = {'Swerve': {'Swerve': 0, 'Go Straight': -20}, 'Go Straight': {'Swerve': 20, 'Go Straight': -100}}



class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
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
    choice = models.StringField(choices=Constants.roles)

    def check_zero(self):
        if self.choice == "": self.choice = Constants.roles[0]

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        self.payoff = Constants.payoff_matrix[self.choice][self.other_player().choice]

    pass
