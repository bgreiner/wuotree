from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
Final little coordination game. Two participants choose a coin and are rewarded when the choices
match you receive the payoff defined in the session configs - default is 10. Tails is the first choice.
"""


class Constants(BaseConstants):
    name_in_url = 'coord6'
    players_per_group = 2
    num_rounds = 1
    coin = ['Tails','Heads']


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
    coin = models.StringField(choices=Constants.coin, widget=widgets.RadioSelect(),
                            doc = """Coin Choice""")

    def set_payoff(self):
        if self.coin == self.other_player().coin:
            self.payoff = self.session.config['poss_payoff']
        else:
            self.payoff = 0

    def other_player(self):
        return self.get_others_in_group()[0]

    pass
