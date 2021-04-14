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
from dateutil.relativedelta import MO, FR
from dateutil.easter import easter

from marketholidays.marketholiday_base import MarketHolidayBase


class UnitedStates(MarketHolidayBase):
    # https://www.nyse.com/markets/hours-calendars (NYSE)
    # http://www.nasdaqtrader.com/trader.aspx?id=calendar (NASDAQ)

    def __init__(self, **kwargs):
        self.country = 'US'
        MarketHolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if year > 1870:
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
                
              
        # Martin Luther King, Jr. Day
        if year >= 1986:
            name = "Martin Luther King, Jr. Day"
            self[date(year, 1, 1) + rd(weekday=MO(+3))] = name
            
            
        # Presidents' Day (Washington's Birthday)
        name = "Presidents' Day"
        
        if year > 1970:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = name
        elif year >= 1879:
            self[date(year, 2, 22)] = name
            
        # Easter
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"
        
        # Memorial Day
        if year > 1970:
            self[date(year, 5, 31) + rd(weekday=MO(-1))] = "Memorial Day"
        elif year >= 1888:
            self[date(year, 5, 30)] = "Memorial Day"
            
        
        # Independence Day
        if year > 1870:
            name = "Independence Day"
            self[date(year, 7, 4)] = name
            if self.observed and date(year, 7, 4).weekday() == 5:
                self[date(year, 7, 4) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 7, 4).weekday() == 6:
                self[date(year, 7, 4) + rd(days=+1)] = name + " (Observed)"
            
                
        # Labour Day
        if year >= 1894:
            self[date(year, 9, 1) + rd(weekday=MO)] = "Labour Day"

        # Thanksgiving
        if year >= 1931:
            self[date(year, 10, 1) + rd(weekday=MO(+2))] = "Thanksgiving"
        
        # Christmas Day
        if year >= 1867:
            self[date(year, 12, 25)] = "Christmas Day"
            if self.observed and date(year, 12, 25).weekday() == 5:
                self[date(year, 12, 24)] = "Christmas Day (Observed)"
            elif self.observed and date(year, 12, 25).weekday() == 6:
                self[date(year, 12, 26)] = "Christmas Day (Observed)"


class US(UnitedStates):
    pass


class USA(UnitedStates):
    pass
