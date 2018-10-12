from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
Battle of the sexes.
"""


class Constants(BaseConstants):
    name_in_url = 'battlesex'
    players_per_group = 2
    num_rounds = 3
    roles = ['Football', 'Opera']


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
    choice = models.StringField(choices=Constants.roles,
                              doc="""Which event player decides to attend""")
    role = models.StringField(choices=Constants.roles,
                            doc="""The player's preferred event""")

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.choice == self.other_player().choice:
            if self.choice == self.role:
                self.payoff = 30
            else:
                self.payoff = 20
        else:
            if self.choice == self.role:
                self.payoff = 10
            else:
                self.payoff = 0

    def set_role(self):
        if self.id_in_group == 1:
            self.role = self.session.config['male_role']
        else:
            self.role = self.session.config['fem_role']


    pass
