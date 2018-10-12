from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Choose(Page):
    form_model = 'player'
    form_fields = ['bolt_price']
    def before_next_page(self):
        for p in self.group.get_players():
            p.not_zero()
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()
        pass

class Results(Page):
    def vars_for_template(self):
        return {'min_price': min(self.player.bolt_price,self.player.other_player().bolt_price),}
    pass



page_sequence = [
    Choose,
    ResultsWaitPage,
    Results
]
