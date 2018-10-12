from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
Over 10 rounds two participants (A and B) offer to split 10 E$ between themselves and a third player (C).
C then decides to accept one of either offer or reject both.
"""


class Constants(BaseConstants):
    name_in_url = 'MarkGame'
    players_per_group = 3
    num_rounds = 5
    endowment = c(10)
    offer_increment = c(0.01)
    offer_choices = currency_range(0,endowment-2,offer_increment)
    accept_choices = ['A','B','Reject Both']
    roles = {1:'A',2:'B',3:'C'}

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for p in self.get_players():
            p.get_role()
    pass


class Group(BaseGroup):

    accepted = models.StringField(choices=Constants.accept_choices, widget=widgets.RadioSelect())
    accepted_offer = models.CurrencyField()

    def set_payoff(self):

        for p in self.get_players():
            if self.accepted == 'A':
                if p.role == 'A':
                    self.accepted_offer = p.offer
                    p.payoff = Constants.endowment - self.accepted_offer
                elif p.role == 'B':
                    p.payoff = c(0)
                else:
                    p.payoff = self.accepted_offer
            elif self.accepted == 'B':
                if p.role == 'A':
                    p.payoff = c(0)
                elif p.role == 'B':
                    self.accepted_offer = p.offer
                    p.payoff = Constants.endowment - self.accepted_offer
                else:
                    p.payoff = self.accepted_offer
            else:
                p.payoff = c(0)
    pass


class Player(BasePlayer):
    offer = models.CurrencyField(min=0.01, max=Constants.endowment-2)
    role = models.StringField()
    offer_accepted = models.BooleanField()

    def get_role(self):
        self.role = Constants.roles[self.id_in_group]

    pass
