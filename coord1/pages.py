from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Choice(Page):
    form_model = 'player'
    form_fields = ['coin']
    def vars_for_template(self):
        return {'poss_payoff': self.session.config['poss_payoff']}
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):

        self.group.set_payoff()
        for p in self.group.get_players():
            p.participant.vars['total_payoff'] = 0
            p.participant.vars['round_1_payoff'] = p.payoff
            p.participant.vars['total_payoff'] += p.payoff
        pass



page_sequence = [
    Choice,
    ResultsWaitPage
]
