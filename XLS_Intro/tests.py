from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Welcome)
        yield (pages.Introduction10)
        yield (pages.Introduction20)
        yield (pages.Introduction30)
        yield (pages.Introduction40)
        if self.participant.vars['treatment'] != 'C':
            yield (pages.Introduction50)
        else:
            pass
        if self.participant.vars['treatment'] == 'C':
            yield (pages.Introduction60, {'a1': 50, 'a2': 1})
        else:
            if self.participant.vars['treatment'] == 'O':
                yield (pages.Introduction60, {'a1': 50, 'a2': 1, 'a3': 'profit'})
            else:
                yield (pages.Introduction60, {'a1': 50, 'a2': 1, 'a3': 'strategy'})
