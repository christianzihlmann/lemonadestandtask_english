from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number > 15:
            yield (pages.Decision, {'location': 3, 'sugar': 8, 'lemon': 1, 'color': 2, 'price': 1.8})
        else:
            if self.round_number > 10:
                yield (pages.Decision, {'location': 2, 'sugar': 1, 'lemon': 8, 'color': 1, 'price': 3.8})
            else:
                if self.round_number > 5:
                    yield (pages.Decision, {'location': 1, 'sugar': 2, 'lemon': 3, 'color': 2, 'price': 9.8})
                else:
                     yield (pages.Decision)
        yield (pages.Results)
        if self.participant.vars['treatment'] == 'P':
            if (self.round_number == 3) or (self.round_number == 6) or (self.round_number == 9) or (
                    self.round_number == 12):
                yield (pages.Report, {'report': 'browser bot result'})
            else:
                pass
        if self.participant.vars['treatment'] == 'O':
            if (self.round_number == 3) or (self.round_number == 6) or (self.round_number == 9) or (
                    self.round_number == 12):
                yield (pages.Report, {'reportp1': 2, 'reportp2':3, 'reportp3':100})
            else:
                pass
        else:
            pass
        #if self.round_number==Constants.num_rounds:
            #yield (pages.ResultsOverall)
        #else:
            #pass
        pass
