from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
    pass

class Introduction10(Page):
    pass

class Introduction20(Page):
    pass

class Introduction30(Page):
    pass

class Introduction40(Page):
    pass

class Introduction50(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] is not 'C'
    pass

class Introduction60(Page):
    form_model = 'player'
    form_fields = ['a1','a2','a3']
    pass


class Introduction70(Page):
    form_model = 'player'
    form_fields = ['a4','a5','a6']
    def is_displayed(self):
        if self.participant.vars['treatment'] is 'C':
            return (self.player.a1 is not 50) or (self.player.a2 is not 1)
        else:
            if self.participant.vars['treatment'] is 'O':
                return (self.player.a1 is not 50) or (self.player.a2 is not 1) or (self.player.a3 not in {
                'profit', 'bénéfice', 'Profit', 'Bénéfice', 'Bénéfices', 'Profits', 'profits',
                                 'bénéfices'})
            else:
                if self.participant.vars['treatment'] == 'P':
                    return (self.player.a1 is not 50) or (self.player.a2 is not 1) or (self.player.a3 not in {
                        'strategy', 'strategies', 'stratégie', 'stratégies', 'Stratégie', 'Strategy',
                                 'Stratégies','Strategies'})
    pass



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
 Welcome, Introduction10, Introduction20, Introduction30, Introduction40, Introduction50, Introduction60, Introduction70
]
