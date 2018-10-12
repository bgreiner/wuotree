from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
Two players are matched with the roles Socialiser and Hermit. They have a choice to visit
either the lake or the forest. The Hermit prefers to be alone and the socialiser prefers
if both players end up at the same location. The Hermit can first write a note telling the
socialiser where they will go - but is under no obligation to be honest.
"""


class Constants(BaseConstants):
    name_in_url = 'SocialHermit'
    players_per_group = 2
    num_rounds = 5
    roles = ['Socialiser', 'Hermit']
    choices = ['Lake', 'Forest']
    payoff_matrix = {'Socialiser': [20,-20], 'Hermit': [-20,20]}

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
    stated_choice = models.StringField(
        choices=[
            ['Forest', 'I am going to the Forest'],
            ['Lake', 'I am going to the Lake'],
        ])

    def set_role(self):
        if self.id_in_group == 1:
            self.role = 'Socialiser'
        else:
            self.role = 'Hermit'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.choice == self.other_player().choice:
            self.payoff = Constants.payoff_matrix[self.role][0]
        else:
            self.payoff = Constants.payoff_matrix[self.role][1]

    pass
