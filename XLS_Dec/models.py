from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools


author = 'Christian Zihlmann, University of Fribourg, Switzerland'
doc = """
This application contains: 
1) The decision stages for the lemonade stand task, a game developed by Ederer & Manso (2013). We adapted the 
game to the needs of our experiment, a modified version of the original game. Namely, there is a reporting period 
after every four periods. Otherwise, parameters as well as wording is unchanged to the original code.
All rights for the game belong to Ederer & Manso (2013). Reference: Ederer, F., & Manso, G. (2013). Is pay for performance detrimental to innovation?. Management Science, 59(7), 1496-1513.
ISO 690.
Code for this experiment: Copyright &#169 2019 Christian Zihlmann.
"""



class Constants(BaseConstants):
    name_in_url = 'XLS_Dec'
    players_per_group = None
    num_rounds = 20
    BusinessDemand = 100
    SchoolDemand = 200
    StadiumDemand = 60
    #Bliss points for each location
    BusinessSugar = 1.55
    BusinessLemon = 7.55
    BusinessLemonadeColor = 1
    BusinessPrice = 7.55
    SchoolSugar = 9.55
    SchoolLemon = 1.55
    SchoolLemonadeColor = 2
    SchoolPrice = 2.55
    StadiumSugar = 5.55
    StadiumLemon = 5.55
    StadiumLemonadeColor = 1
    StadiumPrice = 7.55
    #Penalties for each location
    BusinessSugarPenalty = 3
    BusinessLemonPenalty = 3
    BusinessLemonadeColorPenalty = 20
    BusinessPricePenalty = 3
    SchoolSugarPenalty = 6
    SchoolLemonPenalty = 6
    SchoolLemonadeColorPenalty = 60
    SchoolPricePenalty = 6
    StadiumSugarPenalty = 0.5
    StadiumLemonPenalty = 0.5
    StadiumLemonadeColorPenalty = 0.5
    StadiumPricePenalty = 0.5
    SugarLow = "Some of your customers told you that the lemonade is not sweet enough."
    SugarHigh = "Some of your customers told you that the lemonade is too sweet."
    LemonLow = "Some of your customers told you that the lemonade is not sour/acidic enough."
    LemonHigh = "Some of your customers told you that the lemonade is too sour/acidic."
    PriceLow = "You have too many customers demanding lemonade. The price may be too low."
    PriceHigh = "You have too few customers demanding lemonade. The price may be too high."


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            if 'treatment' in self.session.config:
                for p in self.get_players():
                    p.participant.vars['treatment'] = self.session.config['treatment']
            else:
                pass
        else:
            pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField(blank=True)
    location = models.IntegerField(
        choices=[
            (1, 'Business District'),
            (2, 'School'),
            (3, 'Stadium'),
        ],
        verbose_name='Location of your stand:',
        widget=widgets.RadioSelectHorizontal)
    color = models.IntegerField(
        choices=[
            (1, 'Green'),
            (2, 'Pink'),
        ],
        verbose_name='Lemonade color:',
        widget=widgets.RadioSelectHorizontal)

    sugar = models.FloatField(
        min=0, max=20,
        verbose_name='Sugar content (in %):',
        widget=widgets.NumberInput(attrs={'step': '0.1'}),
    )

    lemon = models.FloatField(
        min=0, max=20,
        verbose_name='Lemon content (in %):',
        widget=widgets.NumberInput(attrs={'step': '0.1'}),
    )
    price = models.FloatField(
        #min=c(0.0), max=c(10.0),
        verbose_name='Price of one cup (in thaler):',
        min=0.1, max=10,
        #currency_range=(c(0), c(10), c(0.1))
        #currency_range(c(0), c(0.10), c(0.02))
        widget=widgets.NumberInput(attrs={'step': '0.1'}),
    )
    random_customer = models.FloatField(doc="creating a random variable to determine customer feedback")
    profit = models.CurrencyField(doc="profit of the lemonade stand, in thalers")
    maxexpphase = models.IntegerField(doc="maximal duration of a exploratory phase")
    durexpphase = models.IntegerField(doc="total duration of all exploratory phases")
    Dtime=models.FloatField(doc="time elapsed on decision screen")
    Dfocustime=models.FloatField(doc="focus time elapsed on decision screen")
    Dunfocustime=models.FloatField(doc="unfocus time elapsed on decision screen")
    Dfocusevent=models.IntegerField(doc="focus off events on decision screen")
    Rtime=models.FloatField(doc="time elapsed on results screen")
    Rfocustime=models.FloatField(doc="focus time elapsed on results screen")
    Runfocustime=models.FloatField(doc="unfocus time elapsed on results screen")
    Rfocusevent=models.IntegerField(doc="focus off events on results screen")
    YEtime=models.FloatField(doc="time elapsed on reporting screen")
    YEfocustime=models.FloatField(doc="focus time elapsed on reporting screen")
    YEunfocustime=models.FloatField(doc="unfocus time elapsed on reporting screen")
    YEfocusevent=models.IntegerField(doc="focus off events on reporting screen")
    report = models.LongStringField(doc="text of reporting field, free form text subjects reported", verbose_name='',
                                    blank=True)
    reportp1 = models.FloatField(
        min=0,
        widget=widgets.NumberInput(attrs={'step': '0.01'}),
        verbose_name='',
        blank=True
    )
    reportp2 = models.FloatField(
        min=0,
        widget=widgets.NumberInput(attrs={'step': '0.01'}),
        verbose_name='',
        blank=True
    )
    reportp3 = models.FloatField(
        min=0,
        widget=widgets.NumberInput(attrs={'step': '0.01'}),
        verbose_name='',
        blank=True
    )
    reportlength = models.IntegerField(doc="length of reported text")
    # TO INCLUDE STANDARD DEVIATIONS from ROUND TO ROUND.
    

    def set_profit(self):
        self.random_customer = round((random.random()), 3)  # assign random value for feedback
        if self.location == 1:
            SugarPenalty = abs(Constants.BusinessSugar - self.sugar) * Constants.BusinessSugarPenalty
            LemonPenalty = abs(Constants.BusinessLemon - self.lemon) * Constants.BusinessLemonPenalty
            ColorPenalty = abs(
            Constants.BusinessLemonadeColor - self.color) * Constants.BusinessLemonadeColorPenalty
            PricePenalty = abs(Constants.BusinessPrice - self.price) * Constants.BusinessPricePenalty
            TotalPenalty = SugarPenalty + LemonPenalty + ColorPenalty + PricePenalty
            if Constants.BusinessDemand - TotalPenalty > 0:
                self.profit = Constants.BusinessDemand - TotalPenalty
            else:
                self.profit = 0

        if self.location == 2:
            SugarPenalty = abs(Constants.SchoolSugar - self.sugar) * Constants.SchoolSugarPenalty
            LemonPenalty = abs(Constants.SchoolLemon - self.lemon) * Constants.SchoolLemonPenalty
            ColorPenalty = abs(
                        Constants.SchoolLemonadeColor - self.color) * Constants.SchoolLemonadeColorPenalty
            PricePenalty = abs(Constants.SchoolPrice - self.price) * Constants.SchoolPricePenalty
            TotalPenalty = SugarPenalty + LemonPenalty + ColorPenalty + PricePenalty
            if Constants.SchoolDemand - TotalPenalty > 0:
                self.profit = Constants.SchoolDemand - TotalPenalty
            else:
                self.profit = 0

        if self.location == 3:
            SugarPenalty = abs(Constants.StadiumSugar - self.sugar) * Constants.StadiumSugarPenalty
            LemonPenalty = abs(Constants.StadiumLemon - self.lemon) * Constants.StadiumLemonPenalty
            ColorPenalty = abs(
                        Constants.StadiumLemonadeColor - self.color) * Constants.StadiumLemonadeColorPenalty
            PricePenalty = abs(Constants.StadiumPrice - self.price) * Constants.StadiumPricePenalty
            TotalPenalty = SugarPenalty + LemonPenalty + ColorPenalty + PricePenalty
            if Constants.StadiumDemand - TotalPenalty > 0:
                    self.profit = Constants.StadiumDemand - TotalPenalty
            else:
                    self.profit = 0

    def set_payoff(self):
        self.payoff = (self.profit * 0.5)


    def set_expphase(self):
        if self.location == 1:
            self.maxexpphase = 0
            self.durexpphase = 0
        else:
            if self.round_number==1:
                self.maxexpphase = 1
                self.durexpphase = 1
            else:
                if self.location == self.in_round(self.round_number -1).location and self.color == self.in_round(
                self.round_number -1).color and (abs(self.sugar-self.in_round(self.round_number -1).sugar)<0.25) and \
            (abs(self.lemon-self.in_round(self.round_number -1).lemon)<0.25) and (abs(self.price-self.in_round(
                self.round_number -1).price)<0.25):
                    self.maxexpphase = 0
                    self.durexpphase = 0
                else:
                    self.maxexpphase = (1 + self.in_round(self.round_number -1).maxexpphase)
                    self.durexpphase = 1

    def feedback(self):
        if self.location == 1:
            if self.random_customer <= (1 / 3):  # FEEDBACK ON SUGAR
                if (Constants.BusinessSugar - self.sugar) > 0:
                    return Constants.SugarLow
                else:
                    return Constants.SugarHigh
            else:
                pass
            if (1 / 3) < self.random_customer <= (2 / 3):  # FEEDBACK ON LEMON
                if (Constants.BusinessLemon - self.lemon) > 0:
                    return Constants.LemonLow
                else:
                    return Constants.LemonHigh
            else:
                pass

            if self.random_customer > (2 / 3):  # FEEDBACK ON PRICE
                if (Constants.BusinessPrice - self.price) > 0:
                    return Constants.PriceLow
                else:
                    return Constants.PriceHigh
            else:
                pass

        if self.location == 2:
            if self.random_customer <= (1 / 3):  # FEEDBACK ON SUGAR
                if (Constants.SchoolSugar - self.sugar) > 0:
                    return Constants.SugarLow
                else:
                    return Constants.SugarHigh
            else:
                pass
            if (1 / 3) < self.random_customer <= (2 / 3):  # FEEDBACK ON LEMON
                if (Constants.SchoolLemon - self.lemon) > 0:
                    return Constants.LemonLow
                else:
                    return Constants.LemonHigh
            else:
                pass

            if self.random_customer > (2 / 3):  # FEEDBACK ON PRICE
                if (Constants.SchoolPrice - self.price) > 0:
                    return Constants.PriceLow
                else:
                    return Constants.PriceHigh
            else:
                pass

        if self.location == 3:
            if self.random_customer <= (1 / 3):  # FEEDBACK ON SUGAR
                if (Constants.StadiumSugar - self.sugar) > 0:
                    return Constants.SugarLow
                else:
                    return Constants.SugarHigh
            else:
                pass

            if (1 / 3) < self.random_customer <= (2 / 3):  # FEEDBACK ON LEMON
                if (Constants.StadiumLemon - self.lemon) > 0:
                    return Constants.LemonLow
                else:
                    return Constants.LemonHigh
            else:
                pass

            if self.random_customer > (2 / 3):  # FEEDBACK ON PRICE
                if (Constants.StadiumPrice - self.price) > 0:
                    return Constants.PriceLow
                else:
                    return Constants.PriceHigh
            else:
                pass

    def vars_for_template(self):
        return {
            'period1': self.round_number - 2,
            'period2': self.round_number - 1,
            'period3': self.round_number,
        }
