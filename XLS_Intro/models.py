from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools

author = 'Christian Zihlmann, University of Fribourg, Switzerland'
doc = """
This application contains: 
1) The instructions for the lemonade stand task, a game developed by Ederer & Manso (2013). We adapted the 
experimental instructions to the needs of our experiment, a modified version of the original game. 
All rights for the game belong to Ederer & Manso (2013). Reference: Ederer, F., & Manso, G. (2013). Is pay for performance detrimental to innovation?. Management Science, 59(7), 1496-1513.
ISO 690.
Code for this experiment: Copyright &#169 2019 Christian Zihlmann.
"""


class Constants(BaseConstants):
    name_in_url = 'XLS_Intro'
    players_per_group = None
    num_rounds = 1
    instructions_template10 = 'XLS_Intro/Instructions10.html'
    instructions_template20 = 'XLS_Intro/Instructions20.html'
    instructions_template30 = 'XLS_Intro/Instructions30.html'
    instructions_template40 = 'XLS_Intro/Instructions40.html'
    instructions_template50 = 'XLS_Intro/Instructions50.html'

class Subsession(BaseSubsession):
    def creating_session(self):
        #treatments = itertools.cycle(['O', 'P'])
        treatments = itertools.cycle(['C', 'O', 'P'])
        if self.round_number == 1:
            if 'treatment' in self.session.config:
                for p in self.get_players():
                    p.participant.vars['treatment'] = self.session.config['treatment']
            else:
                for p in self.get_players():
                    p.participant.vars['treatment'] = next(treatments)
        else:
            pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    a1=models.IntegerField(
    verbose_name='What percentage of the total lemonade stand profit will you earn?',)
    a2=models.IntegerField(choices=[
        [1, '1'],
        [2, '10'],
        [3, '100'],
    ],
        verbose_name = '100 thaler are worth €:',
    widget=widgets.RadioSelect)

    a3=models.StringField(verbose_name='In period 3,6,9 and 12, what will you need to report? I will need to report my '
                                       '______ '
                                       '.',
                          blank=True)
    a4=models.IntegerField(
    verbose_name='What percentage of the total lemonade stand profit will you earn?',)
    a5=models.IntegerField(choices=[
        [1, '1'],
        [2, '10'],
        [3, '100'],
    ],
        verbose_name = '100 thaler are worth €:',
    widget=widgets.RadioSelect)

    a6=models.StringField(verbose_name='In period 3,6,9 and 12, what will you need to report? I will need to report my '
                                       '______ '
                                       '.',
                          blank=True)

    def a4_error_message(self, value):
        print('value is', value)
        if value is not 50:
            return 'Your answer is wrong. Please enter the correct percentage. If you have questions, raise your ' \
                   'hand and wait until the instructor will come to your cubicle.'
    def a5_error_message(self, value):
        print('value is', value)
        if value is not 1:
            return 'Your answer is wrong. Please enter the correct amount in Euro. If you have questions, raise your ' \
                   'hand and wait until the instructor will come to your cubicle.'

    def a6_error_message(self, value):
        print('value is', value)
        message = 'Your answer is wrong. Please enter the correct answer. If you have questions, raise your ' \
                  'hand and wait until the instructor will come to your cubicle.'
        if self.participant.vars['treatment'] == 'O':
            if value not in {'profit','bénéfice','Profit','Bénéfice','Bénéfices','Profits','profits','bénéfices'}:
                return message
            else:
                pass
        if self.participant.vars['treatment'] == 'P':
            if value not in {'strategy','strategies','stratégie','stratégies','Stratégie','Strategy','Stratégies',
                             'Strategies'}:
                return message


    def role(self):
        if self.participant.vars['treatment'] == 'C':
            return 'Control'
        if self.participant.vars['treatment'] == 'PC':
            return 'Placebo Control'
        if self.participant.vars['treatment'] == 'P':
            return 'Process'
        if self.participant.vars['treatment'] == 'O':
            return 'Outcome'
