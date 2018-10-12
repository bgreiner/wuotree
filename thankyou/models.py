from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Owen Powell'

doc = """
A screen with a thank you message to indicate the experiment is over.
"""


class Constants(BaseConstants):
    name_in_url = 'thankyou'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
