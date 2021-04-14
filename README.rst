===============
marketanalysis
===============

A fast, efficient Python library for generating market holidays and trading days based on countries'
security exchanges. It aims to make determining whether a specific date is a market 
holiday as fast and flexible as possible.


Example Usage
-------------

.. code-block:: python

    from datetime import date
    from marketanalysis import marketholidays
    from marketanalysis import markettradingdays

    us_marketholidays = marketholidays.UnitedStates()
    # or:
    # us_marketholidays = marketholidays.US()
    # or:
    # us_marketholidays = marketholidays.CountryHoliday('US')
    # or, for specific prov / states:
    # us_marketholidays = marketholidays.CountryHoliday('US', prov=None, state='CA')

    date(2015, 1, 1) in us_marketholidays  # True
    date(2015, 1, 2) in us_marketholidays  # False

    # The Holiday class will also recognize strings of any format
    # and int/float representing a Unix timestamp
    '2014-01-01' in us_marketholidays  # True
    '1/1/2014' in us_marketholidays    # True
    1388597445 in us_marketholidays    # True

    us_marketholidays.get('2014-01-01')  # "New Year's Day"

    us_marketholidays['2014-01-01': '2014-01-03']  # [date(2014, 1, 1)]

    us_pr_marketholidays = marketholidays.UnitedStates()  # or marketholidays.US(...), or marketholidays.CountryHoliday('US', state='PR')

    # some marketholidays are only present in parts of a country
    '2018-01-06' in us_marketholidays     # False
    '2018-01-06' in us_pr_marketholidays  # True

    # Easily create custom Holiday objects with your own dates instead
    # of using the pre-defined countries/states/provinces available
    custom_marketholidays = marketholidays.MarketHolidayBase()
    # Append custom holiday dates by passing:
    # 1) a dict with date/name key/value pairs,
    custom_marketholidays.append({"2015-01-01": "New Year's Day"})
    # 2) a list of dates (in any format: date, datetime, string, integer),
    custom_marketholidays.append(['2015-07-01', '07/04/2015'])
    # 3) a single date item
    custom_marketholidays.append(date(2015, 12, 25))

    date(2015, 1, 1) in custom_marketholidays  # True
    date(2015, 1, 2) in custom_marketholidays  # False
    '12/25/2015' in custom_marketholidays      # True

    # For more complex logic like 4th Monday of January, you can inherit the
    # HolidayBase class and define your own _populate(year) method. See below
    # documentation for examples.


Install
-------

The latest stable version can always be installed or updated via pip:

.. code-block:: bash

    $ pip install marketholidays==0.11
    
Clone repo with git bash:

 .. code-block:: bash 
 
   $ git clone https://github.com/OmoMicheal/marketanalysis.git


Available Countries
-------------------

=================== =========== =============================================================
Country             ISO code    Securities/Exchanges Available
=================== =========== =============================================================
Canada              CA/CAN      Canadian Securities Exchange
Nigeria             NG/NGA      Nigerian Stock Exchange, NSE
SouthAfrica         ZA/ZAF      Johannesburg Stock Exchange
UnitedStates        US/USA      New York Stock Exchange (NYSE);
                                National Association of Securities 
                                Dealers Automated Quotations (NASDAQ)
=================== =========== =============================================================


API
---

class marketholidays.MarketHolidayBase(years=[], expand=True, observed=True, prov=None, state=None)
    The base class used to create holiday country classes.

Parameters:

years
    An iterable list of integers specifying the years that the Holiday object
    should pre-generate. This would generally only be used if setting *expand*
    to False. (Default: [])

expand
    A boolean value which specifies whether or not to append marketholidays in new
    years to the marketholidays object. (Default: True)

observed
    A boolean value which when set to True will include the observed day of a
    holiday that falls on a weekend, when appropriate. (Default: True)

prov
    A string specifying a province that has unique statutory marketholidays.
    (Default: Canada='ON')

state
    A string specifying a state that has unique statutory marketholidays.
    (Default: UnitedStates=None)

Methods:

get(key, default=None)
    Returns a string containing the name of the holiday(s) in date ``key``, which
    can be of date, datetime, string, unicode, bytes, integer or float type. If
    multiple marketholidays fall on the same date the names will be separated by
    commas

get(key, default=None)
    Returns a string containing the name of the holiday(s) in date ``key``, which
    can be of date, datetime, string, unicode, bytes, integer or float type. If
    multiple marketholidays fall on the same date the names will be separated by
    commas

get_list(key)
    Same as ``get`` except returns a ``list`` of holiday names instead of a comma
    separated string

get_named(name)
    Returns a ``list`` of marketholidays matching (even partially) the provided name
    (case insensitive check)

pop(key, default=None)
    Same as ``get`` except the key is removed from the holiday object

pop_named(name)
    Same as ``pop`` but takes the name of the holiday (or part of it) rather than
    the date

update/append
    Accepts dictionary of {date: name} pairs, a list of dates, or even singular
    date/string/timestamp objects and adds them to the list of marketholidays


-------------

.. code-block:: python

    # Simplest example possible

    >>> from datetime import date
    >>> from marketanalysis import marketholidays
    >>> date(2021, 4, 2) in marketholidays.US()
    True
    >> date(2021, 1, 2) in marketholidays.US()
    False

    # However, this is not efficient because it is initializing a new market holiday 
    # object and generating a list of all the holidays in 2021 during each comparison.

    # It is more efficient to create the object only once

    >>> us_marketholidays = marketholidays.US()
    >>> date(2021, 4, 2) in us_marketholidays
    True
    >> date(2021, 1, 2) in us_marketholidays
    False

    # You can pick whichever you prefer of the following two.

    >>> marketholidays.UnitedStates() == marketholidays.US()
    True


    # Let's print out the market holidays in 2021 specific to NYSE and NASDAQ

    >>> for date, name in sorted(marketholidays.US(state='CA', years=2021).items()):
    >>>     print(date, name)
    2021-01-01 New Year's Day
    2021-01-18 Martin Luther King, Jr. Day
    2021-02-15 Presidents' Day
    2021-04-02 Good Friday
    2021-05-31 Memorial Day
    2021-07-04 Independence Day
    2021-07-05 Independence Day (Observed)
    2021-09-06 Labour Day
    2021-10-11 Thanksgiving
    2021-12-24 Christmas Day (Observed)
    2021-12-25 Christmas Day
    2021-12-31 New Year's Day (Observed)
    
    
    from marketholidays import NG
    >>> for date, name in sorted(NG(years=2021).items()):
    >>>    print(date, name)
    
    2021-01-01 New Year's Day
    2021-04-02 Good Friday
    2021-04-05 Easter Monday
    2021-05-01 Workers’ Day
    2021-05-03 Workers’ Day (Observed)
    2021-06-12 Democracy Day
    2021-06-14 Democracy Day (Observed)
    2021-10-01 Independence Day
    2021-12-25 Christmas Day
    2021-12-26 Boxing Day
    2021-12-27 Christmas Day (Observed)
    2021-12-31 New Year's Day (Observed)



    from marketholidays import CA
    >>> for date, name in sorted(CA(years=2022).items()):
    >>>    print(date, name)
    
    2021-12-31 New Year's Day (Observed)
    2022-01-01 New Year's Day
    2022-02-21 Family Day
    2022-04-15 Good Friday
    2022-05-23 Victoria Day
    2022-07-01 Canada Day
    2022-08-01 Civic Holiday
    2022-09-05 Labour Day
    2022-10-10 Thanksgiving
    2022-12-25 Christmas Day
    2022-12-26 Boxing Day
    2022-12-27 Christmas Day (Observed)

