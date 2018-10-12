from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jon Wood'

doc = """
1 wine producer and 5 buyers from small liquor stores compete by
setting the price of wine and deciding how much wine to buy
"""


class Constants(BaseConstants):
    name_in_url = 'Monopoly'
    players_per_group = 6
    num_rounds = 3
    prices = [c(4), c(14), c(34), c(54), c(74)]
    max_bottles = 200
    max_price = 100


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for p in self.get_players():
            p.get_role()


class Group(BaseGroup):

    tot_bottles_sold = models.PositiveIntegerField(
        initial=0,
        doc="""Total Number of bottles sold this round"""
    )

    sell_price = models.PositiveIntegerField(initial=0, doc="""Wine producer sale-price""")

    def set_payoff(self):
        players = self.get_players()
        for p in players:
            if p.role != 'Seller':
                self.tot_bottles_sold += p.number_of_bottles
            else:
                self.sell_price = p.wine_sell_price
        for p in players:
            if p.role == 'Seller':
                p.payoff =  c((p.wine_sell_price) * sum(p.number_of_bottles for p in players if p.role != 'Seller'))
            else:
                p.payoff = c((p.wine_buy_price - sum(p.wine_sell_price for p in players if p.role == 'Seller')) * p.number_of_bottles)
    pass

class Player(BasePlayer):

    role = models.StringField(doc="""Role in group""")

    wine_sell_price = models.PositiveIntegerField(min=0, max=Constants.max_price,doc="""Price seller chooses to sell wine at""")

    wine_buy_price = models.PositiveIntegerField(
        choices=Constants.prices,
        doc="""Price buyer will buy the wine at""")

    number_of_bottles = models.PositiveIntegerField(
        min=0, max=Constants.max_bottles,
        doc="""Number of bottles""")

    def get_role(self):
        if self.id_in_group == 1:
            self.role = 'Seller'
        elif self.id_in_group == 2:
            self.role = 'Buyer 1'
            self.wine_buy_price = Constants.prices[0]
        elif self.id_in_group == 3:
            self.role = 'Buyer 2'
            self.wine_buy_price = Constants.prices[1]
        elif self.id_in_group == 4:
            self.role = 'Buyer 3'
            self.wine_buy_price = Constants.prices[2]
        elif self.id_in_group == 5:
            self.role = 'Buyer 4'
            self.wine_buy_price = Constants.prices[3]
        elif self.id_in_group == 6:
            self.role = 'Buyer 5'
            self.wine_buy_price = Constants.prices[4]