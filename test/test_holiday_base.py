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



from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, MO

import marketholidays

import pickle
import unittest


# class TestBasics(unittest.TestCase):
#     def setUp(self):
#         self.marketholidays = marketholidays.US()

#     def test_contains(self):
#         self.assertIn(date(2014, 1, 1), self.marketholidays)
#         self.assertNotIn(date(2014, 1, 2), self.marketholidays)

#     def test_getitem(self):
#         self.assertEqual(self.marketholidays[date(2014, 1, 1)], "New Year's Day")
#         self.assertEqual(self.marketholidays.get(date(2014, 1, 1)), "New Year's Day")
#         self.assertRaises(KeyError, lambda: self.marketholidays[date(2014, 1, 2)])
#         self.assertIsNone(self.marketholidays.get(date(2014, 1, 2)))

#         self.assertListEqual(
#             self.marketholidays[date(2013, 12, 31) : date(2014, 1, 2)],
#             [date(2014, 1, 1)],
#         )
#         self.assertListEqual(
#             self.marketholidays[date(2013, 12, 24) : date(2014, 1, 2)],
#             [date(2013, 12, 25), date(2014, 1, 1)],
#         )
#         self.assertListEqual(
#             self.marketholidays[date(2013, 12, 25) : date(2014, 1, 2) : 3],
#             [date(2013, 12, 25)],
#         )
#         self.assertListEqual(
#             self.marketholidays[date(2013, 12, 25) : date(2014, 1, 2) : 7],
#             [date(2013, 12, 25), date(2014, 1, 1)],
#         )
#         self.assertListEqual(
#             self.marketholidays[date(2014, 1, 2) : date(2013, 12, 30)],
#             [date(2014, 1, 1)],
#         )
#         self.assertListEqual(
#             self.marketholidays[date(2014, 1, 2) : date(2013, 12, 25)],
#             [date(2014, 1, 1)],
#         )
#         self.assertListEqual(
#             self.marketholidays[date(2014, 1, 2) : date(2013, 12, 24)],
#             [date(2014, 1, 1), date(2013, 12, 25)],
#         )
#         self.assertListEqual(
#             self.marketholidays[date(2014, 1, 1) : date(2013, 12, 24) : 3],
#             [date(2014, 1, 1)],
#         )
#         self.assertListEqual(
#             self.marketholidays[date(2014, 1, 1) : date(2013, 12, 24) : 7],
#             [date(2014, 1, 1), date(2013, 12, 25)],
#         )
#         self.assertListEqual(
#             self.marketholidays[date(2013, 12, 31) : date(2014, 1, 2) : -3], []
#         )
#         self.assertListEqual(
#             self.marketholidays[
#                 date(2014, 1, 1) : date(2013, 12, 24) : timedelta(days=3)
#             ],
#             [date(2014, 1, 1)],
#         )
#         self.assertListEqual(
#             self.marketholidays[
#                 date(2014, 1, 1) : date(2013, 12, 24) : timedelta(days=7)
#             ],
#             [date(2014, 1, 1), date(2013, 12, 25)],
#         )
#         self.assertListEqual(
#             self.marketholidays[
#                 date(2013, 12, 31) : date(2014, 1, 2) : timedelta(days=3)
#             ],
#             [],
#         )
#         self.assertRaises(
#             ValueError, lambda: self.marketholidays[date(2014, 1, 1) :]
#         )
#         self.assertRaises(
#             ValueError, lambda: self.marketholidays[: date(2014, 1, 1)]
#         )
#         self.assertRaises(
#             TypeError,
#             lambda: self.marketholidays[date(2014, 1, 1) : date(2014, 1, 2) : ""],
#         )
#         self.assertRaises(
#             ValueError,
#             lambda: self.marketholidays[date(2014, 1, 1) : date(2014, 1, 2) : 0],
#         )

#     def test_get(self):
#         self.assertEqual(self.marketholidays.get("2014-01-01"), "New Year's Day")
#         self.assertIsNone(self.marketholidays.get("2014-01-02"))
#         self.assertFalse(self.marketholidays.get("2014-01-02", False))
#         self.assertTrue(self.marketholidays.get("2014-01-02", True))

#     def test_pop(self):
#         self.assertRaises(KeyError, lambda: self.marketholidays.pop("2014-01-02"))
#         self.assertFalse(self.marketholidays.pop("2014-01-02", False))
#         self.assertTrue(self.marketholidays.pop("2014-01-02", True))
#         self.assertIn(date(2014, 1, 1), self.marketholidays)
#         self.assertEqual(self.marketholidays.pop("2014-01-01"), "New Year's Day")
#         self.assertNotIn(date(2014, 1, 1), self.marketholidays)
#         self.assertIn(date(2014, 7, 4), self.marketholidays)

#     def test_pop_named(self):
#         self.assertIn(date(2014, 1, 1), self.marketholidays)
#         self.marketholidays.pop_named("New Year's Day")
#         self.assertNotIn(date(2014, 1, 1), self.marketholidays)
#         self.assertRaises(
#             KeyError, lambda: self.marketholidays.pop_named("New Year's Dayz")
#         )

#     def test_setitem(self):
#         self.marketholidays = marketholidays.US(years=[2014])
#         self.assertEqual(len(self.marketholidays), 10)
#         self.marketholidays[date(2014, 1, 3)] = "Fake Holiday"
#         self.assertEqual(len(self.marketholidays), 11)
#         self.assertIn(date(2014, 1, 3), self.marketholidays)
#         self.assertEqual(self.marketholidays.get(date(2014, 1, 3)), "Fake Holiday")

#     def test_update(self):
#         h = marketholidays.HolidayBase()
#         h.update(
#             {
#                 date(2015, 1, 1): "New Year's Day",
#                 "2015-12-25": "Christmas Day",
#             }
#         )
#         self.assertIn("2015-01-01", h)
#         self.assertIn(date(2015, 12, 25), h)

#     def test_append(self):
#         h = marketholidays.HolidayBase()
#         h.update(
#             {
#                 date(2015, 1, 1): "New Year's Day",
#                 "2015-12-25": "Christmas Day",
#             }
#         )
#         h.append([date(2015, 4, 1), "2015-04-03"])
#         h.append(date(2015, 4, 6))
#         h.append("2015-04-07")
#         self.assertIn("2015-01-01", h)
#         self.assertIn(date(2015, 12, 25), h)
#         self.assertIn("2015-04-01", h)
#         self.assertNotIn("2015-04-02", h)
#         self.assertIn("2015-04-03", h)
#         self.assertNotIn("2015-04-04", h)
#         self.assertNotIn("2015-04-05", h)
#         self.assertIn("2015-04-06", h)
#         self.assertIn("2015-04-07", h)

#     def test_eq_ne(self):
#         us1 = marketholidays.UnitedStates()
#         us2 = marketholidays.US()
#         us3 = marketholidays.UnitedStates(years=[2014])
#         us4 = marketholidays.US(years=[2014])
#         ca1 = marketholidays.Canada()
#         ca2 = marketholidays.CA()
#         ca3 = marketholidays.Canada(years=[2014])
#         ca4 = marketholidays.CA(years=[2014])
#         self.assertEqual(us1, us2)
#         self.assertEqual(us3, us4)
#         self.assertEqual(ca1, ca2)
#         self.assertEqual(ca3, ca4)
#         self.assertNotEqual(us1, us3)
#         self.assertNotEqual(us1, ca1)
#         self.assertNotEqual(us3, ca3)
#         self.assertNotEqual(us1, us3)

#     def test_add(self):
#         ca = marketholidays.CA()
#         us = marketholidays.US()
#         mx = marketholidays.MX()
#         na = ca + (us + mx)
#         self.assertNotIn("2014-07-01", us)
#         self.assertIn("2014-07-01", ca)
#         self.assertNotIn("2014-07-04", ca)
#         self.assertIn("2014-07-04", us)
#         self.assertIn("2014-07-04", ca + us)
#         self.assertIn("2014-07-04", us + ca)
#         self.assertIn("2015-07-04", ca + us)
#         self.assertIn("2015-07-04", us + ca)
#         self.assertIn("2015-07-01", ca + us)
#         self.assertIn("2015-07-01", us + ca)
#         self.assertIn("2014-07-04", na)
#         self.assertIn("2015-07-04", na)
#         self.assertIn("2015-07-01", na)
#         self.assertIn("2000-02-05", na)
#         self.assertEqual((ca + us).prov, "ON")
#         self.assertEqual((us + ca).prov, "ON")
#         ca = marketholidays.CA(years=[2014], expand=False)
#         us = marketholidays.US(years=[2014, 2015], expand=True)
#         self.assertTrue((ca + us).expand)
#         self.assertEqual((ca + us).years, {2014, 2015})
#         self.assertEqual((us + ca).years, {2014, 2015})
#         na = marketholidays.CA()
#         na += marketholidays.US()
#         na += marketholidays.MX()
#         self.assertEqual(na.country, ["CA", "US", "MX"])
#         self.assertIn("2014-07-04", na)
#         self.assertIn("2014-07-04", na)
#         self.assertIn("2015-07-04", na)
#         self.assertIn("2015-07-04", na)
#         self.assertIn("2015-07-01", na)
#         self.assertIn("2015-07-01", na)
#         self.assertIn("2000-02-05", na)
#         self.assertEqual(na.prov, "ON")
#         na = marketholidays.CA() + marketholidays.US()
#         na += marketholidays.MX()
#         self.assertIn("2014-07-04", na)
#         self.assertIn("2014-07-04", na)
#         self.assertIn("2015-07-04", na)
#         self.assertIn("2015-07-04", na)
#         self.assertIn("2015-07-01", na)
#         self.assertIn("2015-07-01", na)
#         self.assertIn("2000-02-05", na)
#         self.assertEqual(na.prov, "ON")
#         self.assertRaises(TypeError, lambda: marketholidays.US() + {})
#         na = ca + (us + mx) + ca + (mx + us + marketholidays.CA(prov="BC"))
#         self.assertIn("2000-02-05", na)
#         self.assertIn("2014-02-10", na)
#         self.assertIn("2014-02-17", na)
#         self.assertIn("2014-07-04", na)
#         provs = marketholidays.CA(prov="ON", years=[2014]) + marketholidays.CA(
#             prov="BC", years=[2015]
#         )
#         self.assertIn("2015-02-09", provs)
#         self.assertIn("2015-02-16", provs)
#         self.assertEqual(provs.prov, ["ON", "BC"])
#         a = sum(marketholidays.CA(prov=x) for x in marketholidays.CA.PROVINCES)
#         self.assertEqual(a.country, "CA")
#         self.assertEqual(a.prov, marketholidays.CA.PROVINCES)
#         self.assertIn("2015-02-09", a)
#         self.assertIn("2015-02-16", a)
#         na = marketholidays.CA() + marketholidays.US() + marketholidays.MX()
#         self.assertIn(date(1969, 12, 25), na)
#         self.assertEqual(na.get(date(1969, 7, 1)), "Dominion Day")
#         self.assertEqual(na.get(date(1983, 7, 1)), "Canada Day")
#         self.assertEqual(
#             na.get(date(1969, 12, 25)), "Christmas Day, Navidad [Christmas]"
#         )
#         na = marketholidays.MX() + marketholidays.CA() + marketholidays.US()
#         self.assertEqual(
#             na.get(date(1969, 12, 25)), "Navidad [Christmas], Christmas Day"
#         )

    # def test_get_list(self):
    #     westland = marketholidays.NZ(prov="WTL")
    #     chathams = marketholidays.NZ(prov="CIT")
    #     wild = westland + chathams
    #     self.assertEqual(
    #         wild[date(1969, 12, 1)],
    #         ("Westland Anniversary Day, " + "Chatham Islands Anniversary Day"),
    #     )

    #     self.assertEqual(
    #         wild.get_list(date(1969, 12, 1)),
    #         ["Westland Anniversary Day", "Chatham Islands Anniversary Day"],
    #     )
    #     self.assertEqual(wild.get_list(date(1969, 1, 1)), ["New Year's Day"])
    #     self.assertEqual(
    #         westland.get_list(date(1969, 12, 1)), ["Westland Anniversary Day"]
    #     )
    #     self.assertEqual(
    #         westland.get_list(date(1969, 1, 1)), ["New Year's Day"]
    #     )
    #     self.assertEqual(
    #         chathams.get_list(date(1969, 12, 1)),
    #         ["Chatham Islands Anniversary Day"],
    #     )
    #     self.assertEqual(
    #         chathams.get_list(date(1969, 1, 1)), ["New Year's Day"]
    #     )
    #     ca = marketholidays.CA()
    #     us = marketholidays.US()
    #     mx = marketholidays.MX()
    #     na = ca + us + mx
    #     self.assertIn(date(1969, 12, 25), na)
    #     self.assertEqual(
    #         na.get_list(date(1969, 12, 25)),
    #         ["Christmas Day", "Navidad [Christmas]"],
    #     )
    #     self.assertEqual(na.get_list(date(1969, 7, 1)), ["Dominion Day"])
    #     self.assertEqual(na.get_list(date(1969, 1, 3)), [])

#     def test_list_supported_countries(self):
#         self.assertIn("NG", marketholidays.list_supported_countries())
#         self.assertIn("ZA", marketholidays.list_supported_countries())

#     def test_radd(self):
#         self.assertRaises(TypeError, lambda: 1 + marketholidays.US())

#     def test_inheritance(self):
#         class NoColumbusmarketholidays(marketholidays.US):
#             def _populate(self, year):
#                 marketholidays.US._populate(self, year)
#                 self.pop(date(year, 10, 1) + relativedelta(weekday=MO(+2)))

#         hdays = NoColumbusmarketholidays()
#         self.assertIn(date(2014, 10, 13), self.marketholidays)
#         self.assertNotIn(date(2014, 10, 13), hdays)
#         self.assertIn(date(2014, 1, 1), hdays)
#         self.assertIn(date(2020, 10, 12), self.marketholidays)
#         self.assertNotIn(date(2020, 10, 12), hdays)
#         self.assertIn(date(2020, 1, 1), hdays)

#         class NinjaTurtlesmarketholidays(marketholidays.US):
#             def _populate(self, year):
#                 marketholidays.US._populate(self, year)
#                 self[date(year, 7, 13)] = "Ninja Turtle's Day"

#         hdays = NinjaTurtlesmarketholidays()
#         self.assertNotIn(date(2014, 7, 13), self.marketholidays)
#         self.assertIn(date(2014, 7, 13), hdays)
#         self.assertIn(date(2014, 1, 1), hdays)
#         self.assertNotIn(date(2020, 7, 13), self.marketholidays)
#         self.assertIn(date(2020, 7, 13), hdays)
#         self.assertIn(date(2020, 1, 1), hdays)

#         class NewCountry(marketholidays.HolidayBase):
#             def _populate(self, year):
#                 self[date(year, 1, 2)] = "New New Year's"

#         hdays = NewCountry()
#         self.assertNotIn(date(2014, 1, 1), hdays)
#         self.assertIn(date(2014, 1, 2), hdays)

#         class Dec31Holiday(marketholidays.HolidayBase):
#             def _populate(self, year):
#                 self[date(year, 12, 31)] = "New Year's Eve"

#         self.assertIn(date(2014, 12, 31), Dec31Holiday())

#     def test_get_named(self):
#         us = marketholidays.UnitedStates(years=[2020])
#         # check for "New Year's Day" presence in get_named("new")
#         self.assertIn(date(2020, 1, 1), us.get_named("new"))

#         # check for searching holiday in US when the observed holiday is on
#         # a different year than input one
#         us = marketholidays.US(years=[2022])
#         us.get_named("Thanksgiving")
#         self.assertEqual([2022], list(us.years))


# class TestArgs(unittest.TestCase):
#     def setUp(self):
#         self.marketholidays = marketholidays.US()

#     def test_country(self):
#         self.assertEqual(self.marketholidays.country, "US")
#         self.assertIn(date(2014, 7, 4), self.marketholidays)
#         self.assertNotIn(date(2014, 7, 1), self.marketholidays)
#         self.marketholidays = marketholidays.UnitedStates()
#         self.assertEqual(self.marketholidays.country, "US")
#         self.assertIn(date(2014, 7, 4), self.marketholidays)
#         self.assertNotIn(date(2014, 7, 1), self.marketholidays)
#         self.assertEqual(self.marketholidays.country, "US")
#         self.marketholidays = marketholidays.CA()
#         self.assertEqual(self.marketholidays.country, "CA")
#         self.assertEqual(self.marketholidays.prov, "ON")
#         self.assertIn(date(2014, 7, 1), self.marketholidays)
#         self.assertNotIn(date(2014, 7, 4), self.marketholidays)
#         self.marketholidays = marketholidays.CA(prov="BC")
#         self.assertEqual(self.marketholidays.country, "CA")
#         self.assertEqual(self.marketholidays.prov, "BC")
#         self.assertIn(date(2014, 7, 1), self.marketholidays)
#         self.assertNotIn(date(2014, 7, 4), self.marketholidays)

#     def test_years(self):
#         self.assertEqual(len(self.marketholidays.years), 0)
#         self.assertNotIn(date(2014, 1, 2), self.marketholidays)
#         self.assertEqual(len(self.marketholidays.years), 1)
#         self.assertIn(2014, self.marketholidays.years)
#         self.assertNotIn(date(2013, 1, 2), self.marketholidays)
#         self.assertNotIn(date(2014, 1, 2), self.marketholidays)
#         self.assertNotIn(date(2015, 1, 2), self.marketholidays)
#         self.assertEqual(len(self.marketholidays.years), 3)
#         self.assertIn(2013, self.marketholidays.years)
#         self.assertIn(2015, self.marketholidays.years)
#         self.marketholidays = marketholidays.US(years=range(2010, 2015 + 1))
#         self.assertEqual(len(self.marketholidays.years), 6)
#         self.assertNotIn(2009, self.marketholidays.years)
#         self.assertIn(2010, self.marketholidays.years)
#         self.assertIn(2015, self.marketholidays.years)
#         self.assertNotIn(2016, self.marketholidays.years)
#         self.marketholidays = marketholidays.US(years=(2013, 2015, 2015))
#         self.assertEqual(len(self.marketholidays.years), 2)
#         self.assertIn(2013, self.marketholidays.years)
#         self.assertNotIn(2014, self.marketholidays.years)
#         self.assertIn(2015, self.marketholidays.years)
#         self.assertIn(date(2021, 12, 31), marketholidays.US(years=[2022]).keys())
#         self.marketholidays = marketholidays.US(years=2015)
#         self.assertNotIn(2014, self.marketholidays.years)
#         self.assertIn(2015, self.marketholidays.years)

#     def test_expand(self):
#         self.marketholidays = marketholidays.US(years=(2013, 2015), expand=False)
#         self.assertEqual(len(self.marketholidays.years), 2)
#         self.assertIn(2013, self.marketholidays.years)
#         self.assertNotIn(2014, self.marketholidays.years)
#         self.assertIn(2015, self.marketholidays.years)
#         self.assertNotIn(date(2014, 1, 1), self.marketholidays)
#         self.assertEqual(len(self.marketholidays.years), 2)
#         self.assertNotIn(2014, self.marketholidays.years)

#     def test_observed(self):
#         self.marketholidays = marketholidays.US(observed=False)
#         self.assertIn(date(2000, 1, 1), self.marketholidays)
#         self.assertNotIn(date(1999, 12, 31), self.marketholidays)
#         self.assertIn(date(2012, 1, 1), self.marketholidays)
#         self.assertNotIn(date(2012, 1, 2), self.marketholidays)
#         self.marketholidays.observed = True
#         self.assertIn(date(2000, 1, 1), self.marketholidays)
#         self.assertIn(date(1999, 12, 31), self.marketholidays)
#         self.assertIn(date(2012, 1, 1), self.marketholidays)
#         self.assertIn(date(2012, 1, 2), self.marketholidays)
#         self.marketholidays.observed = False
#         self.assertIn(date(2000, 1, 1), self.marketholidays)
#         self.assertNotIn(date(1999, 12, 31), self.marketholidays)
#         self.assertIn(date(2012, 1, 1), self.marketholidays)
#         self.assertNotIn(date(2012, 1, 2), self.marketholidays)
#         self.marketholidays = marketholidays.US(years=[2022], observed=False)
#         self.assertNotIn(date(2021, 12, 31), self.marketholidays.keys())

#         self.marketholidays = marketholidays.CA(observed=False)
#         self.assertNotIn(date(1878, 7, 3), self.marketholidays)
#         self.marketholidays.observed = True
#         self.assertIn(date(2018, 7, 2), self.marketholidays)

#     def test_serialization(self):
#         loaded_marketholidays = pickle.loads(pickle.dumps(self.marketholidays))
#         assert loaded_marketholidays == self.marketholidays

#         dt = datetime(2020, 1, 1)
#         res = dt in self.marketholidays
#         loaded_marketholidays = pickle.loads(pickle.dumps(self.marketholidays))
#         assert loaded_marketholidays == self.marketholidays
#         assert (dt in loaded_marketholidays) == res


class TestKeyTransforms(unittest.TestCase):
    def setUp(self):
        self.marketholidays = marketholidays.US()

    def test_dates(self):
        self.assertIn(date(2014, 1, 1), self.marketholidays)
        self.assertEqual(self.marketholidays[date(2014, 1, 1)], "New Year's Day")
        self.marketholidays[date(2014, 1, 3)] = "Fake Holiday"
        self.assertIn(date(2014, 1, 3), self.marketholidays)
        self.assertEqual(self.marketholidays.pop(date(2014, 1, 3)), "Fake Holiday")
        self.assertNotIn(date(2014, 1, 3), self.marketholidays)

    def test_datetimes(self):
        self.assertIn(datetime(2014, 1, 1, 13, 45), self.marketholidays)
        self.assertEqual(
            self.marketholidays[datetime(2014, 1, 1, 13, 45)], "New Year's Day"
        )
        self.marketholidays[datetime(2014, 1, 3, 1, 1)] = "Fake Holiday"
        self.assertIn(datetime(2014, 1, 3, 2, 2), self.marketholidays)
        self.assertEqual(
            self.marketholidays.pop(datetime(2014, 1, 3, 4, 4)), "Fake Holiday"
        )
        self.assertNotIn(datetime(2014, 1, 3, 2, 2), self.marketholidays)

    def test_timestamp(self):
        self.assertIn(1388552400, self.marketholidays)
        self.assertEqual(self.marketholidays[1388552400], "New Year's Day")
        self.assertIn(1388552400.01, self.marketholidays)
        self.assertEqual(self.marketholidays[1388552400.01], "New Year's Day")
        self.marketholidays[1388725200] = "Fake Holiday"
        self.assertIn(1388725201, self.marketholidays)
        self.assertEqual(self.marketholidays.pop(1388725202), "Fake Holiday")
        self.assertNotIn(1388725201, self.holidays)

    def test_strings(self):
        self.assertIn("2014-01-01", self.holidays)
        self.assertEqual(self.holidays["2014-01-01"], "New Year's Day")
        self.assertIn("01/01/2014", self.holidays)
        self.assertEqual(self.holidays["01/01/2014"], "New Year's Day")
        self.holidays["01/03/2014"] = "Fake Holiday"
        self.assertIn("01/03/2014", self.holidays)
        self.assertEqual(self.holidays.pop("01/03/2014"), "Fake Holiday")
        self.assertNotIn("01/03/2014", self.holidays)

    def test_exceptions(self):
        self.assertRaises(
            (TypeError, ValueError), lambda: "abc" in self.holidays
        )
        self.assertRaises(
            (TypeError, ValueError), lambda: self.holidays.get("abc123")
        )
        self.assertRaises(
            (TypeError, ValueError), self.holidays.__setitem__, "abc", "Test"
        )
        self.assertRaises((TypeError, ValueError), lambda: {} in self.holidays)


# class TestCountryHoliday(unittest.TestCase):
#     def setUp(self):
#         self.marketholidays = marketholidays.CountryHoliday("US")

#     def test_country(self):
#         self.assertEqual(self.marketholidays.country, "US")

#     def test_country_years(self):
#         h = marketholidays.CountryHoliday("US", years=[2015, 2016])
#         self.assertEqual(h.years, {2015, 2016})

#     def test_country_state(self):
#         h = marketholidays.CountryHoliday("US", state="NY")
#         self.assertEqual(h.state, "NY")

#     def test_country_province(self):
#         h = marketholidays.CountryHoliday("AU", prov="NT")
#         self.assertEqual(h.prov, "NT")

#     def test_exceptions(self):
#         self.assertRaises((KeyError), lambda: marketholidays.CountryHoliday("XXXX"))


