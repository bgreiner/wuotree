from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)



author = 'Jon Wood'

doc = """
Fifth of the 6 little coordination games. Two participants choose a number and are rewarded
when the choices match you receive the payoff defined in the session configs - default is 10.
"""


class Constants(BaseConstants):
    name_in_url = 'coord5'
    players_per_group = 2
    num_rounds = 1
    numbers = [14, 15, 16, 17, 18, 100]


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
    number = models.PositiveIntegerField(choices=Constants.numbers, widget=widgets.RadioSelect(),
                                         doc="""Number choices""")

    def set_payoff(self):
        if self.number == self.other_player().number:
            self.payoff = self.session.config['poss_payoff']
        else:
            self.payoff = 0

    def other_player(self):
        return self.get_others_in_group()[0]

    pass
