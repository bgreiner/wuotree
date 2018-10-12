from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)


author = 'Owen Powell'

doc = """
If the device is shared, allows the ID of the second player to be inputted.
"""


class Constants(BaseConstants):
    name_in_url = 'inputsecondid'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    player2id = models.StringField(doc="Player 2 ID", blank=True)
    pass
