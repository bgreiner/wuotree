from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import statistics
author = 'Jon Wood'

doc = """
You act as director of a company making decisions about the
company's future strategies
"""


class Constants(BaseConstants):
    name_in_url = 'agenda_2'
    players_per_group = 3
    num_rounds = 10
    roles = ["A","B","C"]
    strategies = ["X","Y","Z"]
    pref = {"A": ["X","Y","Z"], "B": ["Y","Z","X"], "C": ["Z","X","Y"]}
    a_pay = {"X":10, "Y":8, "Z":3}
    b_pay = {"X":3, "Y":7, "Z":5}
    c_pay = {"X":7, "Y":2, "Z":9}


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for p in self.get_groups():
            p.set_committee()
        for p in self.get_players():
            p.set_role()
    pass

class Group(BaseGroup):

    choice_1 = models.StringField(choices=Constants.strategies)
    choice_2 = models.StringField(choices=Constants.strategies)
    choice_3 = models.StringField(choices=Constants.strategies)

    round_1_winner = models.StringField(choices=Constants.strategies)
    winner = models.StringField()
    committee = models.IntegerField()

    def set_final_choice(self):
        temp_choices = ["X","Y","Z"]
        temp_choices.remove(self.choice_1)
        temp_choices.remove(self.choice_2)
        temp_choices = [x for x in temp_choices if x]
        self.choice_3 = temp_choices[0]

    def round_1_vote(self):
        tally = []
        for p in self.get_players():
            tally.append(p.vote_1)
        self.round_1_winner = statistics.mode(tally)

    def final_vote(self):
        tally = []
        for p in self.get_players():
            tally.append(p.vote_2)
        self.winner = statistics.mode(tally)
        for p in self.get_players():
            p.set_payoff()

    def set_committee(self):
        self.committee = random.randrange(1,4)



class Player(BasePlayer):
    role = models.StringField(choices=Constants.roles)
    vote_1 = models.StringField(choices=Constants.strategies)
    vote_2 = models.StringField(choices=Constants.strategies)
    committee = models.BooleanField()

    def set_role(self):
        self.role = Constants.roles[self.id_in_group-1]
        if self.id_in_group == self.group.committee:
            self.committee = True

    def set_payoff(self):
        if self.role == "A":
            self.payoff = Constants.a_pay[self.group.winner]
        elif self.role == "B":
            self.payoff = Constants.b_pay[self.group.winner]
        else:
            self.payoff = Constants.c_pay[self.group.winner]