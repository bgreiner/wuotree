from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class EnterMarket(Page):
    form_model = 'player'
    form_fields = ['enter']
    def vars_for_template(self):
        ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
        return {'num_rounds': int((len(self.subsession.get_players()) / 2)),
                'ordinal': ordinal(self.subsession.round_number)}

    def is_displayed(self):
        return self.player.role == 'Entrant'
    pass

class Intro(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
    def vars_for_template(self):

        return {'num_rounds': int((len(self.subsession.get_players()) / 2)),
                'num_players': int((len(self.subsession.get_players())))
                }
    pass

class PriceWar(Page):
    form_model = 'player'
    form_fields = ['price_war']
    def vars_for_template(self):
        return {'num_rounds': int((len(self.subsession.get_players())/2)),
                'for_ordinal': self.subsession.round_number}
    def is_displayed(self):
        return self.player.role == 'Incumbent' and self.player.other_player().enter == 'Enter the market'
    pass

class NoPriceWar(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {'num_rounds': int((len(self.subsession.get_players())/2)),
                'for_ordinal': self.subsession.round_number}
    def is_displayed(self):
        return self.player.role == 'Incumbent' and self.player.other_player().enter != 'Enter the market'
    pass

class MyWaitPage(WaitPage):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()
        pass

class Results(Page):
    def vars_for_template(self):
        return {'num_rounds': int((len(self.subsession.get_players())/2)),
                'for_ordinal': self.subsession.round_number}
    pass
class EveryoneMatched(Page):
    def is_displayed(self):
        return self.subsession.round_number == (len(self.subsession.get_players())/2)
    pass


    

page_sequence = [
    Intro,
    EnterMarket,
    MyWaitPage,
    PriceWar,
    NoPriceWar,
    ResultsWaitPage,
    Results,
    EveryoneMatched
]
