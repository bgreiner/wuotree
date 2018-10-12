from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = "Jon Wood"

doc = """
"""


class Constants(BaseConstants):
    players_per_group = None
    name_in_url = 'VendorC2'
    num_rounds = 1      
    sexes = ['Male','Female']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    sex = models.StringField(choices=Constants.sexes)
    age = models.PositiveIntegerField(min=1, max=120)
    siblings = models.PositiveIntegerField(min=0, max=15)
    born_vienna = models.BooleanField()

