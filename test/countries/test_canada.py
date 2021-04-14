# -*- coding: utf-8 -*-

#  marketanalysis
#  ----------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of marketholidayss on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  MichealOmojola <momojola@aust.edu.ng>
#  Website: https://github.com/OmoMicheal/trading_days
#  License: MIT (see LICENSE file)
#  Version: 0.1 (April 7, 2021)

import unittest

from datetime import date
from dateutil.relativedelta import relativedelta

# import sys
# sys.path.insert(0, 'C:/Users/momojola/projects/marketanalysis/marketanalysis/')

from marketanalysis import marketholidays
from marketanalysis import markettradingdays


class TestCA(unittest.TestCase):
    # https://www.thecse.com/en/trading/market-operations
    
    def setUp(self):
        self.marketholidayss = marketholidays.CA(observed=False)
        self.markettradingdayss = markettradingdays.CA()

    def test_new_years(self):
        self.assertNotIn(date(2010, 12, 31), self.marketholidayss)
        self.assertNotIn(date(2017, 1, 2), self.marketholidayss)
        self.marketholidayss.observed = True
        self.assertIn(date(2010, 12, 31), self.marketholidayss)
        self.assertIn(date(2017, 1, 2), self.marketholidayss)
        self.marketholidayss.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)

    def test_martin_luther(self):
        for dt in [
            date(1986, 1, 20),
            date(1999, 1, 18),
            date(2000, 1, 17),
            date(2012, 1, 16),
            date(2013, 1, 21),
            date(2014, 1, 20),
            date(2015, 1, 19),
            date(2016, 1, 18),
            date(2020, 1, 20),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)
    

    def test_family_day(self):
        ab_marketholidayss = marketholidays.CA()
        for dt in [
            date(1990, 2, 19),
            date(1999, 2, 15),
            date(2000, 2, 21),
            date(2006, 2, 20),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, ab_marketholidayss)
        dt = date(2007, 2, 19)
        self.assertIn(dt, self.marketholidayss)
        self.assertIn(dt, ab_marketholidayss)
        for dt in [
            date(2008, 2, 18),
            date(2012, 2, 20),
            date(2014, 2, 17),
            date(2018, 2, 19),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, ab_marketholidayss)
        for dt in [date(2019, 2, 18), date(2020, 2, 17)]:
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, ab_marketholidayss)
        for dt in [date(2013, 2, 11), date(2016, 2, 8)]:
            self.assertNotIn(dt, self.marketholidayss)
            self.assertNotIn(dt, ab_marketholidayss)

    
    def test_good_friday(self):
        qc_marketholidayss = marketholidays.CA()
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
            self.assertIn(dt, qc_marketholidayss)

    def test_victoria_day(self):
        for dt in [
            date(1953, 5, 18),
            date(1999, 5, 24),
            date(2000, 5, 22),
            date(2010, 5, 24),
            date(2015, 5, 18),
            date(2020, 5, 18),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)

    def test_civic_holiday(self):
        bc_marketholidayss = marketholidays.CA()
        for dt in [date(1900, 8, 6), date(1955, 8, 1), date(1973, 8, 6)]:
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, bc_marketholidayss)
        for dt in [
            date(1974, 8, 5),
            date(1999, 8, 2),
            date(2000, 8, 7),
            date(2010, 8, 2),
            date(2015, 8, 3),
            date(2020, 8, 3),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertIn(dt, bc_marketholidayss)

    def test_labour_day(self):
        self.assertNotIn(date(1893, 9, 4), self.marketholidayss)
        for dt in [
            date(1894, 9, 3),
            date(1900, 9, 3),
            date(1999, 9, 6),
            date(2000, 9, 4),
            date(2014, 9, 1),
            date(2015, 9, 7),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)

    def test_thanksgiving(self):
        ns_marketholidayss = marketholidays.CA()
        for dt in [
            date(1931, 10, 12),
            date(1990, 10, 8),
            date(1999, 10, 11),
            date(2000, 10, 9),
            date(2013, 10, 14),
            date(2020, 10, 12),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)
            self.assertIn(dt, ns_marketholidayss)

    def test_remembrance_day(self):
        ab_marketholidayss = marketholidays.CA(observed=False)
        self.assertNotIn(date(1930, 11, 11), ab_marketholidayss)
        for year in range(1931, 2100):
            dt = date(year, 11, 11)
            self.assertNotIn(dt, self.marketholidayss)
            self.assertNotIn(dt, ab_marketholidayss)
        self.assertNotIn(date(2007, 11, 12), ab_marketholidayss)
        ab_marketholidayss.observed = True
        self.assertNotIn(date(2007, 11, 12), ab_marketholidayss)

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
        self.assertNotIn(date(2010, 12, 24), self.marketholidayss)
        self.marketholidayss.observed = True
        self.assertEqual(self.marketholidayss[date(2011, 12, 26)], "Christmas Day (Observed)")
        self.assertIn(date(2010, 12, 24), self.marketholidayss)
        self.assertEqual(
            self.marketholidayss[date(2011, 12, 26)], "Christmas Day (Observed)"
        )

    def test_boxing_day(self):
        for year in range(1900, 2100):
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