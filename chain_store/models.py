from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
An experiment where a monopoly firm competes with entrants into their market with price wars.
The entrant firm sees a history of the incumbent before making a decision to enter.
"""


class Constants(BaseConstants):
    name_in_url = 'chain'
    players_per_group = 2
    num_rounds = 40
    roles = ['Incumbent','Entrant']
    enter = ['Enter the market', 'Do not enter the market']
    price_war = ['Price war', 'No price war']

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
            for p in self.get_players():
                p.get_role()
        else:
            self.group_like_round(self.round_number - 1)
            matrix = self.get_group_matrix()
            l1 = []
            l2 = []
            for row in matrix:
                l1.append(row[0])
                l2.append(row[1])
            l2 = l2[1:] + l2[:1]
            self.set_group_matrix([[l1[i], l2[i]] for i in range(len(l1))])
            for p in self.get_players():
                p.get_role()
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):

        if self.role == 'Entrant':
            if self.enter == 'Enter the market':
                if self.other_player().price_war == 'Price war':
                    self.payoff = c(0)
                else:
                    self.payoff = c(10)
            else:
                self.payoff = c(5)
        else:
            if self.other_player().enter == 'Enter the market':
                if self.price_war == 'Price war':
                    self.payoff = c(0)
                else:
                    self.payoff = c(10)
            else:
                self.payoff = c(25)


    def other_player(self):
        return self.get_others_in_group()[0]
    role = models.StringField(choices = Constants.roles)
    enter = models.StringField(choices = Constants.enter, initial = 'Not Applicable',
	widget=widgets.RadioSelect())
    price_war = models.StringField(choices=Constants.price_war, initial='Not Applicable', blank=True,
	widget=widgets.RadioSelect())
    def get_role(self):
        if self.id_in_group == 1:
            self.role = 'Incumbent'
        else:
            self.role = 'Entrant'
    pass
