# -*- coding: utf-8 -*-

#  marketanalysis
#  ----------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of marketmarketholidayss on the fly. It aims to make determining whether a
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


class TestUS(unittest.TestCase):
    def setUp(self):
        self.marketholidayss = marketholidays.USA(observed=False)
        self.markettradingdayss = markettradingdays.USA()

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
    

    def test_washingtons_birthday(self):
        de_marketholidayss = marketholidays.US()
        for dt in [
            date(1969, 2, 22),
            date(1970, 2, 22),
            date(1971, 2, 15),
            date(1997, 2, 17),
            date(1999, 2, 15),
            date(2000, 2, 21),
            date(2012, 2, 20),
            date(2013, 2, 18),
            date(2014, 2, 17),
            date(2015, 2, 16),
            date(2016, 2, 15),
            date(2020, 2, 17),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)
            self.assertIn(dt, de_marketholidayss)    
        self.assertEqual(marketholidays.US().get("2015-02-16"), "Presidents' Day")
       

    def test_good_friday(self):
        marketholidayss_US = marketholidays.US()
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
            self.assertIn(dt, marketholidayss_US)


    def test_memorial_day(self):
        for dt in [
            date(1969, 5, 30),
            date(1970, 5, 30),
            date(1971, 5, 31),
            date(1997, 5, 26),
            date(1999, 5, 31),
            date(2000, 5, 29),
            date(2012, 5, 28),
            date(2013, 5, 27),
            date(2014, 5, 26),
            date(2015, 5, 25),
            date(2016, 5, 30),
            date(2020, 5, 25),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)

  

    def test_independence_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 4)
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)
        self.assertNotIn(date(2010, 7, 5), self.marketholidayss)
        self.assertNotIn(date(2020, 7, 3), self.marketholidayss)
        self.marketholidayss.observed = True
        self.assertIn(date(2010, 7, 5), self.marketholidayss)
        self.assertIn(date(2020, 7, 3), self.marketholidayss)

    def test_labor_day(self):
        for dt in [
            date(1997, 9, 1),
            date(1999, 9, 6),
            date(2000, 9, 4),
            date(2012, 9, 3),
            date(2013, 9, 2),
            date(2014, 9, 1),
            date(2015, 9, 7),
            date(2016, 9, 5),
            date(2020, 9, 7),
        ]:
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)

    def test_thanksgiving_day(self):
        for dt in [
            date(1997, 11, 27),
            date(1999, 11, 25),
            date(2000, 11, 23),
            date(2012, 11, 22),
            date(2013, 11, 28),
            date(2014, 11, 27),
            date(2015, 11, 26),
            date(2016, 11, 24),
            date(2020, 11, 26),
        ]:
            self.assertNotIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)


    def test_christmas_eve(self):
        as_marketholidayss = marketholidays.US()
        self.marketholidayss.observed = False
        for year in range(1900, 2050):
            self.assertNotIn(date(year, 12, 24), self.marketholidayss)
            # self.assertIn(date(year, 12, 24), as_marketholidayss)
        self.assertNotIn(date(2016, 12, 23), as_marketholidayss)
        self.assertNotIn(
            "Christmas Eve (Observed)",
            as_marketholidayss.get_list(date(2017, 12, 22)),
        )
        
    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=-1), self.marketholidayss)
            self.assertNotIn(dt + relativedelta(days=+1), self.marketholidayss)
        self.assertNotIn(date(2010, 12, 24), self.marketholidayss)
        self.assertNotIn(date(2016, 12, 26), self.marketholidayss)
        self.marketholidayss.observed = True
        self.assertIn(date(2010, 12, 24), self.marketholidayss)
        self.assertIn(date(2016, 12, 26), self.marketholidayss)

    def test_day_after_christmas(self):
        nc_marketholidayss = marketholidays.US(observed=False)
        self.assertNotIn(date(2015, 12, 28), nc_marketholidayss)
        self.assertNotIn(date(2016, 12, 27), nc_marketholidayss)
        nc_marketholidayss.observed = True
        
        

    def test_new_years_eve(self):
        ky_marketholidayss = marketholidays.US()
        self.assertNotIn(date(2012, 12, 31), ky_marketholidayss)
        for dt in [date(2013, 12, 31), date(2016, 12, 30)]:
            self.assertNotIn(dt, self.marketholidayss)
            self.assertNotIn(dt, ky_marketholidayss)
            
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