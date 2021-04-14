# -*- coding: utf-8 -*-

#  marketanalysis
#  ----------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of marketmarketholidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  MichealOmojola <momojola@aust.edu.ng>
#  Website: https://github.com/OmoMicheal/trading_days
#  License: MIT (see LICENSE file)
#  Version: 0.1 (April 7, 2021)

import unittest

from datetime import date
from dateutil.relativedelta import relativedelta

import sys
sys.path.insert(0, 'C:/Users/momojola/projects/marketanalysis/marketanalysis/')

from marketanalysis import marketholidays
from marketanalysis import markettradingdays

class TestNigeria(unittest.TestCase):
    def setUp(self):
        self.marketholidayss = marketholidays.Nigeria(observed=False)
        self.markettradingdayss = markettradingdays.NG()

    def test_new_years(self):
        self.assertNotIn(date(2010, 12, 31), self.marketholidayss)
        self.assertNotIn(date(2017, 1, 2), self.marketholidayss)
        self.marketholidayss.observed = True
        self.assertIn(date(2010, 12, 31), self.marketholidayss)
        self.assertIn(date(2017, 1, 2), self.marketholidayss)
        self.marketholidayss.observed = False
        for year in range(1961, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)
            
    def test_good_friday(self):
        ng_marketholidayss = marketholidays.NG()
        for dt in [
            date(1900, 4, 13),
            date(1901, 4, 5),
            date(1902, 3, 28),
            date(1999, 4, 2),
            date(2000, 4, 21),
            date(2010, 4, 2),
            date(2018, 3, 30),
            date(2019, 4, 19),
            date(2020, 4, 10),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)
            self.assertIn(dt, ng_marketholidayss)
            
    def test_easter_monday(self):
        vi_marketholidayss = marketholidays.NG()
        for dt in [
            date(1900, 4, 16),
            date(1901, 4, 8),
            date(1902, 3, 31),
            date(1999, 4, 5),
            date(2010, 4, 5),
            date(2018, 4, 2),
            date(2019, 4, 22),
            date(2020, 4, 13),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, vi_marketholidayss)
            
    def test_workers_day(self):
       vi_marketholidayss = marketholidays.NG()
       for dt in [
           date(2017, 5, 1),
           date(2018, 5, 1),
           date(2019, 5, 1),
           date(2020, 5, 1),
           date(2021, 5, 1),
           date(2022, 5, 1),
           date(2023, 5, 1),
           date(2024, 5, 1),
       ]:           
           self.assertIn(dt, self.marketholidayss)
           self.assertIn(dt, vi_marketholidayss)   
           
    def test_democracy_day(self):
        vi_marketholidayss = marketholidays.NG()
        for dt in [
            date(2017, 5, 29),
            date(2018, 5, 29),
            date(2019, 6, 12),
            date(2020, 6, 12),
            date(2021, 6, 12),
            date(2022, 6, 12),
            date(2023, 6, 12),
            date(2024, 6, 12),
        ]:           
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, vi_marketholidayss)    

    def test_independence_day(self):
        vi_marketholidayss = marketholidays.NG()
        for dt in [
            date(2017, 10, 1),
            date(2018, 10, 1),
            date(2019, 10, 1),
            date(2020, 10, 1),
            date(2021, 10, 1),
            date(2022, 10, 1),
            date(2023, 10, 1),
            date(2024, 10, 1),
        ]:           
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, vi_marketholidayss)  
            
    def test_christmas_day(self):
        for year in range(1960, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
        self.assertNotIn(date(2010, 12, 24), self.marketholidayss)
        self.marketholidayss.observed = True
        self.assertEqual(self.marketholidayss[date(2011, 12, 26)], "Christmas Day (Observed)")
        self.assertEqual(
            self.marketholidayss[date(2011, 12, 26)], "Christmas Day (Observed)"
        )

    def test_boxing_day(self):
        for year in range(1960, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)
        self.assertNotIn(date(2009, 12, 28), self.marketholidayss)
        self.assertNotIn(date(2010, 12, 27), self.marketholidayss)
        self.marketholidayss.observed = True
        self.assertIn(date(2009, 12, 28), self.marketholidayss)
        self.assertIn(date(2010, 12, 27), self.marketholidayss)
        
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