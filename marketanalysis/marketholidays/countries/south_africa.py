# -*- coding: utf-8 -*-

#  marketanalysis
#  ----------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of marketholidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  MichealOmojola <momojola@aust.edu.ng>
#  Website: https://github.com/OmoMicheal/trading_days
#  License: MIT (see LICENSE file)
#  Version: 0.1 (April 7, 2021)


from datetime import date
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, FR
from dateutil.easter import easter


from marketholidays.marketholiday_base import MarketHolidayBase

# from datetime import date, datetime

# from dateutil.easter import easter
# from dateutil.relativedelta import relativedelta as rd

# from holidays.constants import FRI, SUN
# from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, DEC
# from holidays.holiday_base import HolidayBase


class SouthAfrica(MarketHolidayBase):
    def __init__(self, **kwargs):
        # https://www.tradinghours.com/markets/jse/holidays (Johannesburg Stock Exchange)
        self.country = "ZA"
        MarketHolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if year > 1909:
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
        
        if year > 1994:
            name = "Human Rights Day"
            self[date(year, 3, 21)] = name
            if self.observed and date(year, 3, 21).weekday() == 5:
                self[date(year, 3, 21) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, 3, 21).weekday() == 6:
                self[date(year, 3, 21) + rd(weekday = MO(+1))] = name + " (Observed)"
        
        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"
        
        # Family Day
        if year >= 1995:
            self[easter(year) + rd(weekday=MO(+1))] = "Family Day"
        
        if year > 1994:
            name = "Freedom Day"
            self[date(year, 4, 27)] = name
            if self.observed and date(year, 4, 27).weekday() == 5:
                self[date(year, 4, 27) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, 4, 27).weekday() == 6:
                self[date(year, 4, 27) + rd(weekday = MO(+1))] = name + " (Observed)"

        if year > 1994:
            name = "Youth Day"
            self[date(year, 6, 16)] = name
            if self.observed and date(year,  6, 16).weekday() == 5:
                self[date(year,  6, 16) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year,  6, 16).weekday() == 6:
                self[date(year,  6, 16) + rd(weekday = MO(+1))] = name + " (Observed)"

        if year > 1994:
            name = "National Women's Day"
            mm = 8; dd = 9
            self[date(year, mm, dd)] = name
            if self.observed and date(year, mm, dd).weekday() == 5:
                self[date(year, mm, dd) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, mm, dd).weekday() == 6:
                self[date(year, mm, dd) + rd(weekday = MO(+1))] = name + " (Observed)"

        if year > 1994:
            name = "Heritage Day"
            mm = 9; dd = 24
            self[date(year, mm, dd)] = name
            if self.observed and date(year, mm, dd).weekday() == 5:
                self[date(year, mm, dd) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, mm, dd).weekday() == 6:
                self[date(year, mm, dd) + rd(weekday = MO(+1))] = name + " (Observed)"

        if year > 1994:
            name = "Day of Reconciliation"
            mm = 12; dd = 16
            self[date(year, mm, dd)] = name
            if self.observed and date(year, mm, dd).weekday() == 5:
                self[date(year, mm, dd) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, mm, dd).weekday() == 6:
                self[date(year, mm, dd) + rd(weekday = MO(+1))] = name + " (Observed)"

        # Christmas Day
        if year >= 1910:
            name = "Christmas Day"
            mm = 12; dd = 25
            self[date(year, mm, dd)] = name
            if self.observed and date(year, mm, dd).weekday() == 5:
                self[date(year, mm, dd) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, mm, dd).weekday() == 6:
                self[date(year, mm, dd) + rd(weekday = TU(+1))] = name + " (Observed)"

        # Boxing Day
        if year >= 1910:
            name = "Boxing Day"
            mm = 12; dd = 26
            self[date(year, mm, dd)] = name
            if self.observed and date(year, mm, dd).weekday() == 5:
                self[date(year, mm, dd) + rd(weekday = MO(+1))] = name + " (Observed)"
            elif self.observed and date(year, mm, dd).weekday() == 6:
                self[date(year, mm, dd) + rd(weekday = TU(+1))] = name + " (Observed)"


class ZA(SouthAfrica):
    pass


class ZAF(SouthAfrica):
    pass
