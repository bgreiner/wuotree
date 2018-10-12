from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Jon Wood'


class Constants(BaseConstants):
    name_in_url = 'InfoCasc'
    players_per_group = None
    num_rounds = 3
    urn_colour = ['Yellow', 'Blue']



class Subsession(BaseSubsession):
    def creating_session(self):

        matrix = self.get_group_matrix()
        flat_matrix = [item for sublist in matrix for item in sublist]
        random.shuffle(flat_matrix)
        size_of_groups = len(flat_matrix)//self.session.config['no_of_groups'] + \
                         (len(flat_matrix)% self.session.config['no_of_groups'] > 0)
        new_matrix = [flat_matrix[i:i+size_of_groups]
                      for i in range(0,len(flat_matrix),size_of_groups)]
        for x in new_matrix:
            if len(x)==1:
                temp=x
                new_matrix.remove(x)
                new[-1].append(temp[0])
        self.set_group_matrix(new_matrix)
        for p in self.get_groups():
            p.set_urn_colour()
        for p in self.get_players():
            p.set_hint()
    pass


class Group(BaseGroup):
    urn_colour = models.StringField(choices=Constants.urn_colour)
    current_turn = models.PositiveIntegerField(initial=1)

    def next_turn(self):
        self.current_turn += 1
    pass

    def set_urn_colour(self):
        self.urn_colour = Constants.urn_colour[random.randrange(100) < 50]

    def final_count(self):
        final_count = {}
        for p in self.get_players():
            final_count[p.id_in_group] = p.guess
        return final_count

    def set_payoff(self):
        for p in self.get_players():
            p.set_payoff()

    pass


class Player(BasePlayer):
    hint = models.StringField(choices=Constants.urn_colour)
    guess = models.StringField(choices=Constants.urn_colour)
    chosen = models.BooleanField(initial=False)

    def set_chosen(self):
        self.chosen = True

    def set_payoff(self):
        if self.guess == self.group.urn_colour:
            self.payoff = 50
        else:
            self.payoff = 0

    def get_others(self):
        chosen_list = {}
        for other in self.get_others_in_group():
            if other.chosen:
                chosen_list[other.id_in_group] = other.guess
        return chosen_list

    def set_hint(self):
        if self.group.urn_colour == 'Blue':
            self.hint = Constants.urn_colour[random.randrange(100) < 60]
        else:
            self.hint = Constants.urn_colour[random.randrange(100) < 40]
    pass
