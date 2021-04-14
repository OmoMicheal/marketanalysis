# -*- coding: utf-8 -*-

#  marketholidays.py
#  ----------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of marketholidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  MichealOmojola <momojola@aust.edu.ng>
#  Website: https://github.com/OmoMicheal/trading_days
#  License: MIT (see LICENSE file)
#  Version: Python 3.9.1 (April 7, 2021)


from datetime import date
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, FR
from dateutil.easter import easter


from marketholidays.marketholiday_base import MarketHolidayBase
from holidays.constants import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.constants import MON, WED, FRI, SAT, SUN, WEEKEND


class Nigeria(MarketHolidayBase):
    # http://www.nse.com.ng/investing/trading-holidays (Nigerian Stock Exchange, NSE)
    def __init__(self, **kwargs):
        self.country = "NG"
        MarketHolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if year > 1960:
            name = "New Year's Day"
            self[date(year, 1, 1)] = name
            if self.observed and date(year, 1, 1).weekday() == 6:
                self[date(year, 1, 1) + rd(days=+1)] = name + " (Observed)"
            elif self.observed and date(year, 1, 1).weekday() == 5:
                # Add Dec 31st from the previous year without triggering
                # the entire year to be added
                expand = self.expand
                self.expand = False
                self[date(year, 1, 1) + rd(days=-1)] = name + " (Observed)"
                self.expand = expand
            # The next year's observed New Year's Day can be in this year
            # when it falls on a Friday (Jan 1st is a Saturday)
            if self.observed and date(year, 12, 31).weekday() == 4:
                self[date(year, 12, 31)] = name + " (Observed)"
                
        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"     
         
        # Easter Monday
        self[easter(year) + rd(weekday=MO(+1))] = "Easter Monday" 
        
        
        # Workers’ Day
        if year > 1960:
            name = "Workers’ Day"
            self[date(year, 5, 1)] = name
            if self.observed and date(year, 5, 1).weekday() == 5:
                self[date(year, 5, 1) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, 5, 1).weekday() == 6:
                self[date(year, 5, 1) + rd(weekday = TU(+1))] = name + " (Observed)"
        
        
        # Democracy Day
        name = "Democracy Day"
        if 2000 <= year <= 2018:            
            self[date(year, MAY, 29)] = name
            if self.observed and date(year, MAY, 29).weekday() == 5:
                self[date(year, MAY, 29) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, MAY, 29).weekday() == 6:
                self[date(year, MAY, 29) + rd(weekday = MO(+1))] = name + " (Observed)"
        elif year >= 2019:
            self[date(year, JUN, 12)] = name
            if self.observed and date(year, JUN, 12).weekday() == 5:
                self[date(year, JUN, 12) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, JUN, 12).weekday() == 6:
                self[date(year, JUN, 12) + rd(weekday = MO(+1))] = name + " (Observed)"
            
        # Independence Day
        if year >= 1960:
            name = "Independence Day"
            self[date(year, 10, 1)] = name
            if self.observed and date(year, 10, 1).weekday() == 5:
                self[date(year, 10, 1) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, 10, 1).weekday() == 6:
                self[date(year, 10, 1) + rd(weekday = TU(+1))] = name + " (Observed)"
        
        # Christmas Day
        if year >= 1960:
            self[date(year, 12, 25)] = "Christmas Day"
            if self.observed and date(year, 12, 25).weekday() == 5:
                self[date(year, 12, 27)] = "Christmas Day (Observed)"
            elif self.observed and date(year, 12, 25).weekday() == 6:
                self[date(year, 12, 26)] = "Christmas Day (Observed)"
     
        
        # Boxing Day
        if year >= 1960:
            name = "Boxing Day"
            name_observed = name + " (Observed)"
            if self.observed and date(year, DEC, 26).weekday() in WEEKEND:
                self[date(year, DEC, 27) + rd(days = +1)] = name_observed
            elif self.observed and date(year, DEC, 26).weekday() == 0:
                self[date(year, DEC, 28)] = name_observed
            else:
                self[date(year, DEC, 26)] = name
                
        
class NG(Nigeria):
    pass


class NGA(Nigeria):
    pass
