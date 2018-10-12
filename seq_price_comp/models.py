from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = """
5 firms complete in a market by setting prices for homogenous goods.

See "Kruse, J. B., Rassenti, S., Reynolds, S. S., & Smith, V. L. (1994).
Bertrand-Edgeworth competition in experimental markets.
Econometrica: Journal of the Econometric Society, 343-371."
"""


class Constants(BaseConstants):
    players_per_group = 5
    name_in_url = 'Seqpricecomp'
    num_rounds = 5
    prices = [c(0.30), c(0.40), c(0.60), c(0.80), c(1.00)]
    demands = [600,480,360,240,120]
    cost = c(0.26)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for p in self.get_players():
            if p.id_in_group == 1:
                p.order = "first"
            elif p.id_in_group == 2:
                p.order = "second"
            elif p.id_in_group == 3:
                p.order = "third"
            elif p.id_in_group == 4:
                p.order = "fourth"
            else:
                p.order = "fifth"

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
        self.winning_demand = Constants.demands[Constants.prices.index(winning_price)]
        self.winning_price = c(winning_price)
        winners = [p for p in players if p.price == self.winning_price]

        self.price1 = len([p for p in players if p.price == Constants.prices[0]])
        self.price2 = len([p for p in players if p.price == Constants.prices[1]])
        self.price3 = len([p for p in players if p.price == Constants.prices[2]])
        self.price4 = len([p for p in players if p.price == Constants.prices[3]])
        self.price5 = len([p for p in players if p.price == Constants.prices[4]])

        for p in players:
            p.payoff = c(0) # store as currency
            if p in winners:
                p.is_a_winner = True
                p.demand = int(self.winning_demand/len(winners))
                p.payoff = c((p.price - Constants.cost) * p.demand)


class Player(BasePlayer):
    price = models.CurrencyField(
        choices=Constants.prices,
        doc="""Price player chooses to sell product for""",
        widget=widgets.RadioSelect()
    )

    is_a_winner = models.BooleanField(
        initial=False,
        doc="""Whether this player offered lowest price"""
    )

    has_chosen = models.BooleanField(
        initial=False,
        doc="""Whether this player has chosen yet"""
    )
    player1id = models.StringField(doc="Player 1 ID")
    player2id = models.StringField(doc="Player 2 ID")
    demand = models.IntegerField(
        initial=0,
        doc="""Share of total demand served by this player"""
    )

    order = models.StringField(doc="Order in group")

    def set_has_chosen(self):
         self.has_chosen = True




