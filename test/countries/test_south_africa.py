# -*- coding: utf-8 -*-

#  python-marketholidayss
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of marketholidayss on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-marketholidayss
#  License: MIT (see LICENSE file)

import unittest

from datetime import date

import sys
sys.path.insert(0, 'C:/Users/momojola/projects/marketanalysis/marketanalysis/')

from marketanalysis import marketholidays
from marketanalysis import markettradingdays

class TestSouthAfrica(unittest.TestCase):
    def setUp(self):
        self.marketholidayss = marketholidays.ZA()
        self.markettradingdayss = markettradingdays.ZA()
        
    def test_new_years(self):
        self.assertIn("1910-01-01", self.marketholidayss)
        self.assertIn("2017-01-01", self.marketholidayss)
        self.assertIn("2999-01-01", self.marketholidayss)
        self.assertIn("2017-01-02", self.marketholidayss)  # sunday

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.marketholidayss)
        self.assertIn(date(2017, 4, 17), self.marketholidayss)
        self.assertIn(date(1994, 4, 1), self.marketholidayss)
        
    def test_family_day(self):
        vi_marketholidayss = marketholidays.ZA()
        for dt in [
            date(2018, 4, 2),
            date(2017, 4, 17),
            date(2016, 3, 28),
            date(2014, 4, 21),
            date(2013, 4, 1),
            date(2012, 4, 9),
            date(2011, 4, 25),
            date(2010, 4, 5),
            date(2009, 4, 13),
            date(2008, 3, 24),
            date(2007, 4, 9),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, vi_marketholidayss)

    def test_freedom_day(self):
        vi_marketholidayss = marketholidays.ZA()
        for dt in [
            date(2009, 4, 27),
            date(2008, 4, 28),
            date(2007, 4, 27),
            date(2006, 4, 27),
            date(2005, 4, 27),
            date(2004, 4, 27),
            date(2003, 4, 28),
            date(2002, 4, 27),
            date(2001, 4, 27),
            date(2000, 4, 27),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, vi_marketholidayss)
 
    def test_future_list(self):
        current_date = '2021-04-13'
        lookup_step = 10
        self.assertIn(date(2021, 4, 16), self.markettradingdayss.future_list(current_date, lookup_step))
        self.assertNotIn(date(2021, 4, 18), self.markettradingdayss.future_list(current_date, lookup_step))
        
    def test_prevDays(self):
        current_date = '2021-04-13'
        lookback_step = 4
        self.assertIn(date(2021, 4, 9), self.markettradingdayss.prevDays(current_date, lookback_step))
        self.assertNotIn(date(2021, 4, 11), self.markettradingdayss.prevDays(current_date, lookback_step))

    def test_BtwDates(self):
        current_date = '2021-04-13'
        future_date = '2021-04-20'
        self.assertIn(date(2021, 4, 15), self.markettradingdayss.BtwDates(current_date, future_date))
        self.assertNotIn(date(2021, 4, 18), self.markettradingdayss.BtwDates(current_date, future_date))
        

# if __name__ == "__main__":
#     unittest.main()