from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'PubGoodPun'
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
    punishment_p_1 = models.CurrencyField(initial = 0)
    punishment_p_2 = models.CurrencyField(initial = 0)
    punishment_p_3 = models.CurrencyField(initial = 0)
    punishment_p_4 = models.CurrencyField(initial = 0)

    def set_payoffs(self):
        for p in self.get_players():
            p.tot_punish = (int(p.punishment_1 or 0) + int(p.punishment_2 or 0) +
                         int(p.punishment_3 or 0) + int(p.punishment_4 or 0))
            self.punishment_p_1 += int(p.punishment_1 or 0)
            self.punishment_p_2 += int(p.punishment_2 or 0)
            self.punishment_p_3 += int(p.punishment_3 or 0)
            self.punishment_p_4 += int(p.punishment_4 or 0)
        #old payoff - punishments - 3punishments aimed at them
        for p in self.get_players():
            p.payoff -= p.tot_punish
            if p.id_in_group == 1:
                p.payoff -= (3 * self.punishment_p_1)
            elif p.id_in_group == 2:
                p.payoff -= (3 * self.punishment_p_2)
            elif p.id_in_group == 3:
                p.payoff -= (3 * self.punishment_p_3)
            elif p.id_in_group == 4:
                p.payoff -= (3 * self.punishment_p_4)
    pass

    def set_initial_payoffs(self):
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
    tot_punish = models.CurrencyField(blank=True)
    punishment_1 = models.CurrencyField(blank=True)
    punishment_2 = models.CurrencyField(blank=True)
    punishment_3 = models.CurrencyField(blank=True)
    punishment_4 = models.CurrencyField(blank=True)

    pass
