from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        sex = ['Male','Female']
        yield (pages.question, {'sex': sex[random.randrange(0,2)],'age': random.randrange(19,32),'siblings': random.randrange(0,16),'born_vienna': True})
