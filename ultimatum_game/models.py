from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = "Jon Wood"

doc = """
Ultimatum game. One player offers to split an endowment between both participants.
This can either be rejected or accepted.
"""

class Constants(BaseConstants):
    name_in_url = 'Ultimatum'
    players_per_group = 2
    num_rounds = 1
    endowment = c(100)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    amount_offered = models.CurrencyField(min=0.1,max=Constants.endowment,
                                          doc="Amount offered")
    offer_accepted = models.BooleanField(doc="if offered amount is accepted")

    def set_payoffs(self):
        p1, p2 = self.get_players()
        p1.payoff = (Constants.endowment - self.amount_offered)*self.offer_accepted
        p2.payoff = self.amount_offered*self.offer_accepted


class Player(BasePlayer):
    pass
