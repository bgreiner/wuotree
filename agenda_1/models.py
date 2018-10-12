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
    name_in_url = 'agenda_1'
    players_per_group = None
    num_rounds = 3
    roles = ["A","B","C"]
    strategies = ["X","Y","Z"]
    pref = {"A": ["X","Y","Z"], "B": ["Y","Z","X"], "C": ["Z","X","Y"]}
    a_pay = {"X":10, "Y":8, "Z":3}
    b_pay = {"X":3, "Y":7, "Z":5}
    c_pay = {"X":7, "Y":2, "Z":9}


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.set_role()
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    role = models.StringField(choices=Constants.roles)
    choice_1 = models.StringField(choices=Constants.strategies)
    choice_2 = models.StringField(choices=Constants.strategies)
    vote_1 = models.StringField(choices=Constants.strategies)
    vote_2 = models.StringField(choices=Constants.strategies)
    round_1_winner = models.StringField(choices=Constants.strategies)
    winner = models.StringField()
    dir_a_choice = models.StringField()
    dir_b_choice = models.StringField()
    dir_c_choice = models.StringField()
    dir_a_choice_2 = models.StringField()
    dir_b_choice_2 = models.StringField()
    dir_c_choice_2 = models.StringField()

    def reset_vote_arrays(self):
        self.participant.vars['vote_choices'] = ["X", "Y", "Z"]
        self.participant.vars['vote_order'] = []

    def set_role(self):
        self.role = random.choice(Constants.roles)
        self.participant.vars['vote_choices'] = ["X","Y","Z"]
        self.participant.vars['vote_order'] = []
    def pop_vote_1(self):
        self.participant.vars['vote_choices'].remove(self.choice_1)
        self.participant.vars['vote_order'].append(self.choice_1)
    def pop_vote_2(self):
        self.participant.vars['vote_choices'].remove(self.choice_2)
        self.participant.vars['vote_order'].append(self.choice_2)
    def pop_vote_3(self):
        self.participant.vars['vote_choices'].append(self.round_1_winner)
        self.participant.vars['vote_choices'] = self.participant.vars['vote_choices'][::-1]

    def round_1_vote(self):
        tally = []
        if self.role == "A":
            if Constants.pref["B"][0] in self.participant.vars['vote_order']:
                self.dir_b_choice = Constants.pref["B"][0]
            else:
                self.dir_b_choice = Constants.pref["B"][1]
            if Constants.pref["C"][0] in self.participant.vars['vote_order']:
                self.dir_c_choice = Constants.pref["C"][0]
            else:
                self.dir_c_choice = Constants.pref["C"][1]
            tally.append(self.vote_1)
            tally.append(self.dir_b_choice)
            tally.append(self.dir_c_choice)
            self.round_1_winner = statistics.mode(tally)

        elif self.role == "B":
            if Constants.pref["A"][0] in self.participant.vars['vote_order']:
                self.dir_a_choice = Constants.pref["A"][0]
            else:
                self.dir_a_choice = Constants.pref["A"][1]
            if Constants.pref["C"][0] in self.participant.vars['vote_order']:
                self.dir_c_choice = Constants.pref["C"][0]
            else:
                self.dir_c_choice = Constants.pref["C"][1]
            tally.append(self.vote_1)
            tally.append(self.dir_a_choice)
            tally.append(self.dir_c_choice)
            self.round_1_winner = statistics.mode(tally)

        else:
            if Constants.pref["B"][0] in self.participant.vars['vote_order']:
                self.dir_b_choice = Constants.pref["B"][0]
            else:
                self.dir_b_choice = Constants.pref["B"][1]
            if Constants.pref["A"][0] in self.participant.vars['vote_order']:
                self.dir_a_choice = Constants.pref["A"][0]
            else:
                self.dir_c_choice = Constants.pref["C"][1]
            tally.append(self.vote_1)
            tally.append(self.dir_b_choice)
            tally.append(self.dir_a_choice)
            self.round_1_winner = statistics.mode(tally)




    def final_vote(self):
        tally = []
        if self.role == "A":
            if Constants.pref["B"][0] in self.participant.vars['vote_choices']:
                self.dir_b_choice_2 = Constants.pref["B"][0]
            else:
                self.dir_b_choice_2 = Constants.pref["B"][1]
            if Constants.pref["C"][0] in self.participant.vars['vote_choices']:
                self.dir_c_choice_2 = Constants.pref["C"][0]
            else:
                self.dir_c_choice_2 = Constants.pref["C"][1]
            tally.append(self.vote_2)
            tally.append(self.dir_b_choice_2)
            tally.append(self.dir_c_choice_2)
            self.winner = statistics.mode(tally)

        elif self.role == "B":
            if Constants.pref["A"][0] in self.participant.vars['vote_choices']:
                self.dir_a_choice_2 = Constants.pref["A"][0]
            else:
                self.dir_a_choice_2 = Constants.pref["A"][1]
            if Constants.pref["C"][0] in self.participant.vars['vote_choices']:
                self.dir_c_choice_2 = Constants.pref["C"][0]
            else:
                self.dir_c_choice_2 = Constants.pref["C"][1]
            tally.append(self.vote_2)
            tally.append(self.dir_a_choice_2)
            tally.append(self.dir_c_choice_2)
            self.winner = statistics.mode(tally)

        else:
            if Constants.pref["B"][0] in self.participant.vars['vote_choices']:
                self.dir_b_choice_2 = Constants.pref["B"][0]
            else:
                self.dir_b_choice_2 = Constants.pref["B"][1]
            if Constants.pref["A"][0] in self.participant.vars['vote_choices']:
                self.dir_a_choice_2 = Constants.pref["A"][0]
            else:
                self.dir_a_choice_2 = Constants.pref["A"][1]
            tally.append(self.vote_2)
            tally.append(self.dir_b_choice_2)
            tally.append(self.dir_a_choice_2)
            self.winner = statistics.mode(tally)

    def set_payoff(self):
        if self.role == "A":
            self.payoff = Constants.a_pay[self.winner]
        elif self.role == "B":
            self.payoff = Constants.b_pay[self.winner]
        else:
            self.payoff = Constants.c_pay[self.winner]