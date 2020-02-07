from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import statistics



class BeforeResultsOverall(Page):
    def before_next_page(self):
        self.player.LS_treatment = self.participant.vars['treatment']
        self.player.LS_Dtotaltime = self.participant.vars['Dtotaltime']
        self.player.LS_Dtotalfocustime= self.participant.vars['Dtotalfocustime']
        self.player.LS_Dtotalunfocustime = self.participant.vars['Dtotalunfocustime']
        self.player.LS_Dtotalfocusevents= self.participant.vars['Dtotalfocusevents']
        self.player.LS_Rtotaltime = self.participant.vars['Rtotaltime']
        self.player.LS_Rtotalfocustime = self.participant.vars['Rtotalfocustime']
        self.player.LS_Rtotalunfocustime = self.participant.vars['Rtotalunfocustime']
        self.player.LS_Rtotalfocusevents = self.participant.vars['Rtotalfocusevents']
        self.player.LS_YEtotaltime = self.participant.vars['YEtotaltime']
        self.player.LS_YEtotalfocustime = self.participant.vars['YEtotalfocustime']
        self.player.LS_YEtotalunfocustime = self.participant.vars['YEtotalunfocustime']
        self.player.LS_YEtotalfocusevents = self.participant.vars['YEtotalfocusevents']
        self.player.LS_overallprofit = self.participant.vars['overallprofit']
        self.player.LS_overallpayoffrealworld = self.participant.vars['overallpayoffrealworld']
        self.player.LS_finloc = self.participant.vars['finallocation']
        self.player.LS_finprofit = self.participant.vars['finalprofit']
        self.player.LS_maxprofit = self.participant.vars['maxprofit']
        self.player.LS_locnotdefault = 20 - self.participant.vars['locdefault']
        self.player.LS_locnotdefaulth1 = 10 - self.participant.vars['locdefaulth1']
        self.player.LS_locnotdefaulth2 = 10 - self.participant.vars['locdefaulth2']
        self.player.LS_stdvsugar = self.participant.vars['stdvsugar']
        self.player.LS_stdvlemon = self.participant.vars['stdvlemon']
        self.player.LS_stdvprice = self.participant.vars['stdvprice']
        self.player.LS_stdv3con = (self.player.LS_stdvsugar+self.player.LS_stdvlemon+self.player.LS_stdvprice)/3
        self.player.LS_stdvsugarh1 = self.participant.vars['stdvsugarh1']
        self.player.LS_stdvlemonh1 = self.participant.vars['stdvlemonh1']
        self.player.LS_stdvpriceh1 = self.participant.vars['stdvpriceh1']
        self.player.LS_stdv3conh1 = (self.player.LS_stdvsugarh1+self.player.LS_stdvlemonh1+self.player.LS_stdvpriceh1)/3
        self.player.LS_stdvsugarh2 = self.participant.vars['stdvsugarh2']
        self.player.LS_stdvlemonh2 = self.participant.vars['stdvlemonh2']
        self.player.LS_stdvpriceh2 = self.participant.vars['stdvpriceh2']
        self.player.LS_stdv3conh2 = (self.player.LS_stdvsugarh2+self.player.LS_stdvlemonh2+self.player.LS_stdvpriceh2)/3
        self.player.LS_stdvprofit = self.participant.vars['stdvprofit']
        self.player.LS_stdvprofith1 = self.participant.vars['stdvprofith1']
        self.player.LS_stdvprofith2 = self.participant.vars['stdvprofith2']
        self.player.LS_maxexpphase = self.participant.vars['maxexpphase']
        self.player.LS_durexpphase = self.participant.vars['durexpphase']
        if self.player.LS_treatment != 'C':
            self.player.LS_report = self.participant.vars['report']
            self.player.LS_reportlength = self.participant.vars['reportlength']
        else:
            pass


class ResultsOverall(Page):
    pass




page_sequence = [BeforeResultsOverall,ResultsOverall
]
