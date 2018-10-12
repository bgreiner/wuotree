from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Jon Wood'

doc = """
Two randomly matched pairs compete as buyers or sellers. The buyer decides whether
to buy the commodity and then in turn the seller decides whether to produce and
ship the commodity.
"""


class Constants(BaseConstants):
    name_in_url = 'RepTrust'
    players_per_group = 2
    num_rounds = 10


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
            if self.round_number%2:
                l1 = l1[1:] + l1[:1]
            else:
                l2 = l2[1:] + l2[:1]
            self.set_group_matrix([[l2[i], l1[i]] for i in range(len(l1))])

            for p in self.get_players():
                p.retrieve_role()


    pass


class Group(BaseGroup):
    buy = models.BooleanField(initial=True)
    produce = models.BooleanField(initial=True)

    def set_payoff(self):
        for p in self.get_players():
            if self.buy and self.produce:
                p.payoff = c(7)
            elif self.buy and not self.produce:
                if p.role == 'Buyer':
                    p.payoff = c(0)
                else:
                    p.payoff = c(10)
            elif not self.buy:
                p.payoff = c(5)

    pass


class Player(BasePlayer):
    current_balance = models.CurrencyField(initial=0)
    role = models.StringField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def get_role(self):
        if self.id_in_group == 1:
            self.role = 'Buyer'
        elif self.id_in_group == 2:
            self.role = 'Seller'

    def retrieve_role(self):
        if self.in_round(self.round_number - 1).role == 'Buyer':
            self.role = 'Seller'
        else:
            self.role = 'Buyer'

    pass
