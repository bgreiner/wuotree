from ._builtin import Page


class Wait(Page):
    def vars_for_template(self):
        return {
            'participant_label': self.participant.label,
        }


page_sequence = [
    Wait
]
