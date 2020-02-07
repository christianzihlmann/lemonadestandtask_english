from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Christian Zihlmann, University of Fribourg, Switzerland'
doc = """
This application contains: 
1) A result stage, which calculates in python various outcomes and variables of interest, obtained from game-play 
data of the lemonade stand task, 
a game developed by Ederer & Manso (2013). 
Code for this experiment: Copyright &#169 2019 Christian Zihlmann.
"""



class Constants(BaseConstants):
    name_in_url = 'XLS_Results'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    LS_treatment = models.StringField(blank=True)
    LS_Dtotaltime = models.FloatField(doc="The total (raw) time elapsed for all Decision-pages.")
    LS_Dtotalfocustime = models.FloatField(doc="The total focus time elapsed for all Decision-pages.")
    LS_Dtotalunfocustime = models.FloatField(doc="The total unfocus time elapsed for all Decision-pages.")
    LS_Dtotalfocusevents = models.FloatField(doc="The total focus off events for all Decision-pages.")
    LS_Rtotaltime = models.FloatField(doc="The total (raw) time elapsed for all Results-pages.")
    LS_Rtotalfocustime = models.FloatField(doc="The total focus time elapsed for all Results-pages.")
    LS_Rtotalunfocustime = models.FloatField(doc="The total unfocus time elapsed for all Results-pages.")
    LS_Rtotalfocusevents = models.FloatField(doc="The total focus off events for all Results-pages.")
    LS_YEtotaltime = models.FloatField(doc="The total (raw) time elapsed for all Year-End-Summary (Report)-pages.")
    LS_YEtotalfocustime = models.FloatField(doc="The total focus time elapsed for all Year-End-Summary (Report)-pages.")
    LS_YEtotalunfocustime = models.FloatField(
        doc="The total unfocus time elapsed for all Year-End-Summary (Report)-pages.")
    LS_YEtotalfocusevents = models.FloatField(doc="The total focus off events for all Year-End-Summary (Report)-pages.")
    LS_overallprofit = models.CurrencyField(doc="Total profit from all periods in points excl. show-up fee")
    LS_overallpayoffrealworld = models.CurrencyField(doc="Total profit incl. show-up fee all periods")
    LS_finloc = models.IntegerField(doc="Location in final period")
    LS_finprofit = models.CurrencyField(doc="Profit in final period")
    LS_maxprofit = models.CurrencyField(doc="Highest profit over all 20 rounds")
    LS_maxexpphase = models.IntegerField(doc="Longest duration of an exploration phase. An exploration phase starts "
                                             "when subjects choose a location other than the default location "
                                             "suggested by the previous manager. An explorative phase is defined as "
                                             "ending when a subject switches back to the default location or when a "
                                             "subject does not change location and lemonade color and also does not "
                                             "change lemon content, sugar content and price by more than 0.25 units. "
                                             "All that is adapted 1:1 from Ederer&Manso.  ")
    LS_durexpphase = models.IntegerField(doc="Total duration of exploration phases, that is the sum of periods a "
                                             "subject explored. See above for defintion of exp phase.")
    LS_locnotdefault =models.IntegerField(doc="Count of chosen non-default (=non-Business) locations.")
    LS_stdvsugar = models.FloatField(doc="The standard deviation for sugar choices.")
    LS_stdvlemon= models.FloatField(doc="The standard deviation for lemon choices.")
    LS_stdvprice = models.FloatField(doc="The standard deviation for price choices.")
    LS_stdvprofit = models.CurrencyField(doc="The standard deviation of subject-specific payoffs.")
    LS_stdv3con = models.FloatField(
        doc="The average subject-specific standard deviation of strategy choices for the three continuous variables.")
    LS_locnotdefaulth1 = models.IntegerField(doc="Count of chosen non-default (=non-Business) locations round 1-10.")
    LS_stdvsugarh1 = models.FloatField(doc="The standard deviation for sugar choices, round 1-10.")
    LS_stdvlemonh1= models.FloatField(doc="The standard deviation for lemon choices, round 1-10.")
    LS_stdvpriceh1 = models.FloatField(doc="The standard deviation for price choices, round 1-10.")
    LS_stdvprofith1 = models.CurrencyField(doc="The standard deviation of subject-specific payoffs, round 1-11.")
    LS_stdv3conh1 = models.FloatField(
        doc="The average subject-specific standard deviation for the three continuous variables, round 1-10.")
    LS_locnotdefaulth2 = models.IntegerField(doc="Count of chosen non-default (=non-Business) locations round 10-20.")
    LS_stdvsugarh2 = models.FloatField(doc="The standard deviation for sugar choices, round 11-20.")
    LS_stdvlemonh2= models.FloatField(doc="The standard deviation for lemon choices, round 11-20.")
    LS_stdvpriceh2 = models.FloatField(doc="The standard deviation for price choices, round 11-20.")
    LS_stdv3conh2 = models.FloatField(
        doc="The average subject-specific standard deviation for the three continuous variables, round 11-20.")
    LS_stdvprofith2 = models.CurrencyField(doc="The standard deviation of subject-specific payoffs, round 11-20.")
    LS_report = models.LongStringField(doc="Text report, summary of all 4 reports (period 4, 8, 12, 16).")
    LS_reportlength = models.IntegerField(doc="total length of text reports of all four reporting periods.")










