from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
Third of the 6 little coordination games. Two participants choose to distribute a shared
 pot defined in session configs - default is 100. If the total exceeds the pot then both
 get nothing.
"""


class Constants(BaseConstants):
    name_in_url = 'coord3'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
    pass


class Group(BaseGroup):
    def set_payoff(self):
        for p in self.get_players():
            p.set_payoff()
    pass


class Player(BasePlayer):

    split = models.PositiveIntegerField(min=0,
                                        doc = """The chosen split by each participant up to the maximum""")

    def set_payoff(self):
        if self.split + self.other_player().split <= self.session.config['pot']:
            self.payoff = self.split
        else:
            self.payoff = 0

    def other_player(self):
        return self.get_others_in_group()[0]
    pass
