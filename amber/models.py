from otree.api import (
    BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)


author = 'Owen Powell'

doc = """
A simple page that does not let users pass without *advance slowest users* command. Useful for pausing play.
"""


class Constants(BaseConstants):
    name_in_url = 'ready'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
