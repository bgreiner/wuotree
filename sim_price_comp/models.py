from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = "Owen Powell"

doc = """
5 firms complete in a market by setting prices for homogenous goods.
"""



class Constants(BaseConstants):
    players_per_group = 5
    name_in_url = 'Simultaneouspricecompetition'
    num_rounds = 10
    pricesC = [c(0.3), c(0.4), c(0.6), c(0.8), c(1)]
    demands = [600, 480, 360, 240, 120]
    cost = c(0.26)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    winning_price = models.CurrencyField(
        choices=Constants.pricesC,
        doc="""Cheapest price"""
    )
    winning_demand = models.PositiveIntegerField(
        choices=Constants.demands,
        doc="""Demand at cheapest price"""
    )

    price1 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 0,30 E$."""
    )

    price2 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 0,40 E$."""
    )

    price3 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 0,60 E$."""
    )

    price4 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 0,80 E$."""
    )

    price5 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 1,00 E$."""
    )

    def checkzero(self):
        player = self.get_players()
        for p in player:
            if p.price == 0:
                p.price = c(0.3)

    def set_payoffs(self):
        players = self.get_players()
        winning_price = min([p.price for p in players])
        self.winning_demand = Constants.demands[Constants.pricesC.index(winning_price)]
        self.winning_price = c(winning_price)
        winners = [p for p in players if p.price == self.winning_price]

        self.price1 = len([p for p in players if p.price == Constants.pricesC[0]])
        self.price2 = len([p for p in players if p.price == Constants.pricesC[1]])
        self.price3 = len([p for p in players if p.price == Constants.pricesC[2]])
        self.price4 = len([p for p in players if p.price == Constants.pricesC[3]])
        self.price5 = len([p for p in players if p.price == Constants.pricesC[4]])

        for p in players:
            p.payoff = c(0) # store as currency
            if p in winners:
                p.is_a_winner = True
                p.demand = int(self.winning_demand/len(winners))
                p.payoff = c((p.price - Constants.cost) * p.demand)


class Player(BasePlayer):
    price = models.CurrencyField(
        choices=Constants.pricesC,
        doc="""Price player chooses to sell product for""",
        widget=widgets.RadioSelect()
    )

    is_a_winner = models.BooleanField(
        initial=False,
        doc="""Whether this player offered lowest price"""
    )

    demand = models.IntegerField(
        initial=0,
        doc="""Share of total demand served by this player"""
    )