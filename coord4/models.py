from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)



author = 'Jon Wood'

doc = """
Second of the 6 little coordination games. Two participants choose a direction and are rewarded
when the choices match you receive nothing but if they don't match you will lose the money
 defined in the session configs as payoff - default is 10.
"""


class Constants(BaseConstants):
    name_in_url = 'coord4'
    players_per_group = 2
    num_rounds = 1
    directions = ['Left','Right']


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
    turn = models.StringField(choices=Constants.directions, widget=widgets.RadioSelect())

    def set_payoff(self):
        if self.turn == self.other_player().turn:
            self.payoff = 0
        else:
            self.payoff = -self.session.config['poss_payoff']

    def other_player(self):
        return self.get_others_in_group()[0]
    pass
