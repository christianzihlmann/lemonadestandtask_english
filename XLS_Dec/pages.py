from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_tools.utils import get_focused_time, get_time_per_page, get_unfocused_time, num_focusoff_events
import statistics

class Decision(Page):
    form_model = 'player'
    form_fields = ['location', 'sugar', 'lemon', 'color', 'price']

    def is_displayed(self):
        if self.round_number == 1:
            setattr(self.player, 'location', 1)
            setattr(self.player, 'sugar', 5.2)
            setattr(self.player, 'lemon', 7.0)
            setattr(self.player, 'color', 1)
            setattr(self.player, 'price', 8.2)
            return True
        else:
            if self.round_number > 1:
                fields = ['location', 'sugar', 'lemon', 'color', 'price']
                for f in fields:
                    oldvalue = getattr(self.player.in_round(self.round_number - 1), f)
                    setattr(self.player, f, oldvalue)
                return True
            else:
                pass


    def before_next_page(self):
        self.player.treatment = self.participant.vars['treatment']
        self.player.set_profit()
        self.player.set_payoff()
        self.player.feedback()
        self.player.set_expphase()


class Results(Page):
    def before_next_page(self):
        self.player.Dtime = get_time_per_page(self.player, 'Decision')
        self.player.Dfocustime = get_focused_time(self.player, 'Decision')
        self.player.Dunfocustime = get_unfocused_time(self.player, 'Decision')
        self.player.Dfocusevent = num_focusoff_events(self.player, 'Decision')
        self.player.Rtime = get_time_per_page(self.player, 'Results')
        self.player.Rfocustime = get_focused_time(self.player, 'Results')
        self.player.Runfocustime = get_unfocused_time(self.player, 'Results')
        self.player.Rfocusevent = num_focusoff_events(self.player, 'Results')

        if self.round_number == Constants.num_rounds:
            self.participant.vars['Dtotaltime'] = sum([get_time_per_page(p, 'Decision') for p in self.player.in_all_rounds()])
            self.participant.vars['Dtotalfocustime'] = sum([get_focused_time(p, 'Decision') for p in self.player.in_all_rounds()])
            self.participant.vars['Dtotalunfocustime'] = sum([get_unfocused_time(p, 'Decision') for p in self.player.in_all_rounds()])
            self.participant.vars['Dtotalfocusevents'] = sum([num_focusoff_events(p, 'Decision') for p in self.player.in_all_rounds()])
            self.participant.vars['Rtotaltime'] = sum([get_time_per_page(p, 'Results') for p in self.player.in_all_rounds()])
            self.participant.vars['Rtotalfocustime'] = sum([get_focused_time(p, 'Results') for p in self.player.in_all_rounds()])
            self.participant.vars['Rtotalunfocustime'] = sum([get_unfocused_time(p, 'Results') for p in self.player.in_all_rounds()])
            self.participant.vars['Rtotalfocusevents'] = sum([num_focusoff_events(p, 'Results') for p in self.player.in_all_rounds()])
            self.participant.vars['YEtotaltime'] = sum([get_time_per_page(p, 'Report') for p in self.player.in_all_rounds()])
            self.participant.vars['YEtotalfocustime'] = sum([get_focused_time(p, 'Report') for p in self.player.in_all_rounds()])
            self.participant.vars['YEtotalunfocustime'] = sum([get_unfocused_time(p, 'Report') for p in self.player.in_all_rounds()])
            self.participant.vars['YEtotalfocusevents'] = sum([num_focusoff_events(p, 'Report') for p in self.player.in_all_rounds()])
            self.participant.vars['overallprofit'] = sum([p.profit for p in self.player.in_all_rounds()])
            self.participant.vars['overallpayoffrealworld'] = c(self.participant.payoff_plus_participation_fee())
            self.participant.vars['finallocation'] = self.player.in_round(20).location
            self.participant.vars['finalprofit'] = self.player.in_round(20).profit
            self.participant.vars['maxprofit'] = max([p.profit for p in self.player.in_all_rounds()])
            self.participant.vars['locdefault'] = ([p.location for p in self.player.in_all_rounds()]).count(1) #self.player.locnotdefault.in_all_rounds().count(True)
            self.participant.vars['locdefaulth1'] = ([p.location for p in self.player.in_rounds(1, 10)]).count(1)
            self.participant.vars['locdefaulth2'] = ([p.location for p in self.player.in_rounds(11, 20)]).count(1)
            self.participant.vars['locdefaulth2'] = ([p.location for p in self.player.in_rounds(11, 20)]).count(1)
            self.participant.vars['stdvsugar'] = statistics.stdev(([p.sugar for p in self.player.in_all_rounds()]),
                                                                  xbar=(statistics.mean(
                                                                      [p.sugar for p in self.player.in_all_rounds()])))
            self.participant.vars['stdvlemon'] = statistics.stdev(([p.lemon for p in self.player.in_all_rounds()]),
                                                                  xbar=(statistics.mean(
                                                                      [p.lemon for p in self.player.in_all_rounds()])))
            self.participant.vars['stdvprice'] = statistics.stdev(([p.price for p in self.player.in_all_rounds()]),
                                                                  xbar=(statistics.mean(
                                                                      [p.price for p in self.player.in_all_rounds()])))
            self.participant.vars['stdvsugarh1'] = statistics.stdev(([p.sugar for p in self.player.in_rounds(1,10)]),
                                                                    xbar=(statistics.mean(
                                                                        [p.sugar for p in self.player.in_rounds(1,10)])))
            self.participant.vars['stdvlemonh1'] = statistics.stdev(([p.lemon for p in self.player.in_rounds(1,10)]),
                                                                  xbar=(statistics.mean(
                                                                      [p.lemon for p in self.player.in_rounds(1,10)])))
            self.participant.vars['stdvpriceh1'] = statistics.stdev(([p.price for p in self.player.in_rounds(1,10)]),
                                                                  xbar=(statistics.mean(
                                                                      [p.price for p in self.player.in_rounds(1,10)])))
            self.participant.vars['stdvsugarh2'] = statistics.stdev(([p.sugar for p in self.player.in_rounds(11,20)]),
                                                                    xbar=(statistics.mean(
                                                                        [p.sugar for p in self.player.in_rounds(11,20)])))
            self.participant.vars['stdvlemonh2'] = statistics.stdev(([p.lemon for p in self.player.in_rounds(11,20)]),
                                                                  xbar=(statistics.mean(
                                                                      [p.lemon for p in self.player.in_rounds(11,20)])))
            self.participant.vars['stdvpriceh2'] = statistics.stdev(([p.price for p in self.player.in_rounds(11,20)]),
                                                                  xbar=(statistics.mean(
                                                                      [p.price for p in self.player.in_rounds(11,20)])))
            self.participant.vars['stdvprofit'] = statistics.stdev(
                ([p.profit for p in self.player.in_all_rounds()]),
                xbar=(statistics.mean(
                    [p.profit for p in self.player.in_all_rounds()])))
            self.participant.vars['stdvprofith1'] = statistics.stdev(
                ([p.profit for p in self.player.in_rounds(1, 10)]),
                xbar=(statistics.mean(
                    [p.profit for p in self.player.in_rounds(1, 10)])))
            self.participant.vars['stdvprofith2'] = statistics.stdev(
                ([p.profit for p in self.player.in_rounds(11,20)]),
                xbar=(statistics.mean(
                    [p.profit for p in self.player.in_rounds(11,20)])))
            self.participant.vars['maxexpphase']= max([p.maxexpphase for p in self.player.in_all_rounds()])
            self.participant.vars['durexpphase']= sum([p.durexpphase for p in self.player.in_all_rounds()])
            if self.player.treatment == 'P':
                self.participant.vars['report']= "Period3" + self.player.in_round(3).report + "Period6" + \
                                                 self.player.in_round(6).report + "Period9" + self.player.in_round(
                    9).report + "Period12"+ self.player.in_round(
                    12).report
                self.participant.vars['reportlength']= self.player.in_round(3).reportlength + self.player.in_round(
                    6).reportlength + \
                                             self.player.in_round(9).reportlength + self.player.in_round(
                    12).reportlength
            else:
                pass

        else:
            pass


class Report(Page):
    form_model = 'player'
    form_fields = ['report', 'reportp1', 'reportp2', 'reportp3']
    def is_displayed(self):
        if self.participant.vars['treatment'] != 'C':
            if (self.round_number == 3) or (self.round_number == 6 ) or (self.round_number == 9) or (
                    self.round_number == 12):
                return True
            else:
                return False
        else:
            return False



    def vars_for_template(self):
        basevars = self.player.vars_for_template()
        if self.participant.vars['treatment'] == 'PC':
            basevars.update({'treatmentvariable': 'does not exist any more'})
            return basevars
        if self.participant.vars['treatment'] == 'P':
            basevars.update({'treatmentvariable': 'Please describe your strategy in the last three periods. Why did '
                                                  'you choose this strategy?'})
            return basevars
        if self.participant.vars['treatment'] == 'O':
            basevars.update({'treatmentvariable': 'Please report your profits of the last three periods.'})
            return basevars


    def before_next_page(self):
        self.player.YEtime = get_time_per_page(self.player, 'Report')
        self.player.YEfocustime = get_focused_time(self.player, 'Report')
        self.player.YEunfocustime = get_unfocused_time(self.player, 'Report')
        self.player.YEfocusevent = num_focusoff_events(self.player, 'Report')
        self.player.reportlength = len(self.player.report)







page_sequence = [Decision,Results,Report
]
