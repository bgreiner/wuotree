from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range)
import random

author = 'Jon Wood'

doc = """
At each decision node in this experiment a participant has the choice of moving right or down. Right
continues the experiment and down finishes it immediately. At each stage of the centipede there is a 
different distribution of E$ - always favouring the decision maker. After 10 decisions the experiment 
ends.
"""


class Constants(BaseConstants):
    name_in_url = 'cent'
    players_per_group = 2
    num_rounds = 3
    payoff_choices=[(3,1),
                    (1.5,4),
                    (6,2),
                    (3,8.5),
                    (12,4),
                    (5.5,17),
                    (24,8),
                    (11.5,34),
                    (48,16),
                    (22.5,68),
                    (96,32)]
    dir_choices = ['Right','Down']


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
    pass


class Group(BaseGroup):

    page_num = models.PositiveIntegerField(initial=0)
    cont = models.StringField(choices=Constants.dir_choices, initial='Right', widget=widgets.RadioSelect(),
                            doc = "Direction Choice")
    def count_pages(self):
        self.page_num += 1

    def set_payoff(self):
        for p in self.get_players():
            p.payoff=c(Constants.payoff_choices[self.page_num][(p.id_in_group-1)])

    def set_rand_payoff(self):
        for player in self.get_players():
            player.rand_payoff = c(random.choice([p.payoff for p in player.in_all_rounds()]))
    pass


class Player(BasePlayer):
    rand_payoff = models.CurrencyField(doc = "Random Payoff")
    pass
