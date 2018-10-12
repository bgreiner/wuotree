from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class IntWaitPage(WaitPage):
    body_text = "You are waiting for other participants to make their choice."

class PlayerChoosePage(Page):
    form_model = 'player'
    form_fields = ['price']
    def before_next_page(self):
        self.player.set_has_chosen()

class Player1ChoosePage(PlayerChoosePage):
    def is_displayed(self):
        return self.player.id_in_group == 1

class Player2ChoosePage(PlayerChoosePage):
    def is_displayed(self):
        return self.player.id_in_group == 2

class Player3ChoosePage(PlayerChoosePage):
    def is_displayed(self):
        return self.player.id_in_group == 3

class Player4ChoosePage(PlayerChoosePage):
    def is_displayed(self):
        return self.player.id_in_group == 4

class Player5ChoosePage(PlayerChoosePage):
    def is_displayed(self):
        return self.player.id_in_group == 5

class ResWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.checkzero()
        self.group.set_payoffs()

class Results(Page):
    timeout_seconds = 30
    def vars_for_template(self):
        return {
            'my_price': self.player.price,
            'price_choice_1': self.group.price1,
            'price_choice_2': self.group.price2,
            'price_choice_3': self.group.price3,
            'price_choice_4': self.group.price4,
            'price_choice_5': self.group.price5,
            'price_1': Constants.prices[0],
            'price_2': Constants.prices[1],
            'price_3': Constants.prices[2],
            'price_4': Constants.prices[3],
            'price_5': Constants.prices[4],
            'winning_price': self.group.winning_price,
            'winning_demand': self.group.winning_demand,
            'my_demand': self.player.demand,
            'my_cost': Constants.cost,
            'my_profit': self.player.payoff,
        }

page_sequence = [Player1ChoosePage,
                 IntWaitPage,
                 Player2ChoosePage,
                 IntWaitPage,
                 Player3ChoosePage,
                 IntWaitPage,
                 Player4ChoosePage,
                 IntWaitPage,
                 Player5ChoosePage,
                 ResWaitPage,
                 Results]
