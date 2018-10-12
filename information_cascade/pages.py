from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def is_displayed(self):
        return self.player.id_in_group == self.group.current_turn
    form_model = 'player'
    form_fields = ['guess']

    def vars_for_template(self):
        return {
            'other_players': self.player.get_others(),
        }
    def before_next_page(self):
        self.group.next_turn()
        self.player.set_chosen()
    pass


class BWaitPage(WaitPage):
    template_name = 'information_cascade/BWaitPage.html'

    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass

class AWaitPage(WaitPage):
    template_name = 'information_cascade/BWaitPage.html'
    def is_displayed(self):
        return not self.player.chosen
    pass


class Results(Page):
    def vars_for_template(self):
        return {
            'yellow_count': list(self.group.final_count().values()).count('Yellow'),
            'blue_count': list(self.group.final_count().values()).count('Blue'),
        }
    pass


page_sequence = []

for x in range(0,50):
    page_sequence.append(MyPage)
    page_sequence.append(AWaitPage)
page_sequence.append(BWaitPage)
page_sequence.append(Results)