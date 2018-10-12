from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
Weakest link experiment.
"""


class Constants(BaseConstants):
    name_in_url = 'MinGame'
    players_per_group = 6
    num_rounds = 5
    numbers = [1,2,3,4,5,6,7]
    payoff_matrix = [[8.00],
                     [4.00,14.40],
                     [2.00,7.20,17.60],
                     [1.00,3.60,8.80,19.20],
                     [0.50,1.80,4.40,9.60,20.00],
                     [0.25,0.90,2.20,4.80,10.00,20.40],
                     [0.13,0.45,1.10,2.40,5.00,10.20,20.60]
                     ]



class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
    pass


class Group(BaseGroup):
    lowest_num = models.PositiveIntegerField(initial=0,
                                             doc="""Lowest number selected in group""")

    def get_lowest(self):
        self.lowest_num = min(p.num_chosen for p in self.get_players())

    pass


class Player(BasePlayer):
    num_chosen = models.PositiveIntegerField(choices=Constants.numbers,
                                             doc="""Number chosen by player""")

    def set_payoff(self):
        self.payoff = Constants.payoff_matrix[(self.num_chosen - 1)][(self.group.lowest_num - 1)]
    pass
