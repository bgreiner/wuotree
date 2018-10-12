from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Choice(Page):
    form_model = 'player'
    form_fields = ['split']
    def vars_for_template(self):
        return {'pot': self.session.config['pot']}

    def split_max(self):
        return self.session.config['pot']
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff()
        for p in self.group.get_players():
            p.participant.vars['round_3_payoff'] = p.payoff
            p.participant.vars['total_payoff'] += p.payoff
        pass



page_sequence = [
    Choice,
    ResultsWaitPage
]