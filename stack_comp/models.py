from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Jon Wood'

doc = """
Pairs of spring water producers and buyers compete in a market.
"""


class Constants(BaseConstants):
    name_in_url = 'Stackcomp'
    players_per_group = 2
    num_rounds = 3
    max_bottles = 600


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
            for p in self.get_players():
                p.get_role()
                p.retrieve_role()
        else:
            for p in self.get_players():
                p.retrieve_role()
            players = self.get_players()
            prod_1_players = [p for p in players if p.participant.vars['role'] == 'Producer 1']
            prod_2_players = [p for p in players if p.participant.vars['role'] == 'Producer 2']
            random.shuffle(prod_1_players,random.random)
            group_matrix = []
            num_groups = int(len(players)/2)
            for i in range(num_groups):
                new_group = [
                    prod_1_players.pop(),
                    prod_2_players.pop()]
                group_matrix.append(new_group)
            self.set_group_matrix(group_matrix)
    pass


class Group(BaseGroup):
    bottle_price = models.CurrencyField(
        doc="""Price the bottles sell at"""
    )
    def set_payoffs(self):
        players = self.get_players()
        self.bottle_price = (1 - (sum(p.number_of_bottles for p in players) / 1000))
        if self.bottle_price < 0:
            self.bottle_price = 0
        for p in players:
            p.payoff = self.bottle_price * p.number_of_bottles
    pass


class Player(BasePlayer):
    number_of_bottles = models.PositiveIntegerField(
        min=0, max=Constants.max_bottles,
        doc="""Number of bottles"""
    )

    role = models.StringField(doc="""Role: Producer 1 or Producer 2""")

    def get_role(self):
        if self.id_in_group == 1:
            self.participant.vars['role'] = 'Producer 1'
        elif self.id_in_group == 2:
            self.participant.vars['role'] = 'Producer 2'

    def retrieve_role(self):
        if self.participant.vars['role'] == 'Producer 1':
            self.role = 'Producer 1'
        if self.participant.vars['role'] == 'Producer 2':
            self.role = 'Producer 2'
    pass
