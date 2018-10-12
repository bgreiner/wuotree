from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = "Jon Wood"

doc = """
Players compete to sell homogenous souvenirs with a price matching option.
"""


class Constants(BaseConstants):
    players_per_group = 5
    name_in_url = 'Pricematchbert'
    num_rounds = 3
    prices = [c(0.30), c(0.40), c(0.60), c(0.80), c(1.00)]
    demands = [600, 480, 360, 240, 120]
    cost = c(0.26)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    winning_price = models.CurrencyField(
        choices=Constants.prices,
        doc="""Cheapest price"""
    )
    winning_demand = models.PositiveIntegerField(
        choices=Constants.demands,
        doc="""Demand at cheapest price"""
    )

    price1 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 0,30 EUR."""
    )

    price2 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 0,40 EUR."""
    )

    price3 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 0,60 EUR."""
    )

    price4 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 0,80 EUR."""
    )

    price5 = models.PositiveIntegerField(
        min=0, max=Constants.players_per_group,
        doc="""Number of sellers who chose a price of 1,00 EUR."""
    )

    price_matching_count = models.PositiveIntegerField(initial = 0)
    def store_old_price(self):
        players = self.get_players()
        for p in players:
            p.price_before_match = p.price

    def non_zero(self):
        players = self.get_players()
        for p in players:
            if p.price not in Constants.prices:
                p.price = c(0.30)

    def count_price_matching(self):
        players = self.get_players()
        for p in players:
            self.price_matching_count += p.price_matching

    def set_payoffs(self):
        players = self.get_players()
        winning_price = min([p.price for p in players])
        for p in players:
            if p.price_matching == True and p.price > winning_price:
                p.price = winning_price
        self.winning_demand = Constants.demands[Constants.prices.index(winning_price)]
        self.winning_price = c(winning_price)
        winners = [p for p in players if p.price == self.winning_price]

        self.price1 = len([p for p in players if p.price_before_match == Constants.prices[0]])
        self.price2 = len([p for p in players if p.price_before_match == Constants.prices[1]])
        self.price3 = len([p for p in players if p.price_before_match == Constants.prices[2]])
        self.price4 = len([p for p in players if p.price_before_match == Constants.prices[3]])
        self.price5 = len([p for p in players if p.price_before_match == Constants.prices[4]])

        for p in players:
            p.payoff = c(0) # store as currency
            if p in winners:
                p.is_a_winner = True
                p.demand = int(self.winning_demand/len(winners))
                p.payoff = c((p.price - Constants.cost) * p.demand)


class Player(BasePlayer):
    price_before_match = models.CurrencyField(
        choices=Constants.prices,
        doc="""Price before match""")

    price = models.CurrencyField(
        choices=Constants.prices,
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
    price_matching = models.BooleanField(
        initial=False,
        doc="""Whether they want price matching enabled"""
    )
