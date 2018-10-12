from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'PubGoodCon'
    players_per_group = 4
    num_rounds = 5


class Subsession(BaseSubsession):
    def before_subsession_starts(self):
        if self.subsession.round_number == 1:
            self.group_randomly()
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    average_contribution = models.CurrencyField()

    def mayor_lotto(self):
        [p.average_cont() for p in self.get_players() if p.id_in_group == random.randrange(1,5)]

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.average_contribution = self.total_contribution/Constants.players_per_group
        self.individual_share = self.total_contribution * 0.4
        for p in self.get_players():
                p.kept = 10 - p.contribution
                p.payoff = p.kept + self.individual_share
    pass


class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=10)
    kept = models.CurrencyField()

    def average_cont(self):
        self.contribution = (sum(p.contribution for p in self.get_others_in_group())/(Constants.players_per_group-1))
    pass

for i in range(0, 11):
    Player.add_to_class('cond_cont%s' % i, models.CurrencyField(min=0, max=10))