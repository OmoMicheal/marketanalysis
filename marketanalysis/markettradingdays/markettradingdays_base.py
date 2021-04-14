# -*- coding: utf-8 -*-

#  marketholidays.py
#  -----------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of marketholidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  MichealOmojola <momojola@aust.edu.ng>
#  Website: https://github.com/OmoMicheal/trading_days
#  License: MIT (see LICENSE file)
#  Version: 0.1 (April 7, 2021)

from datetime import datetime, date

import six
from dateutil.parser import parse

class MarketTradingDaysBase(dict):

    def __init__(
        self, current_date = '2021-01-01', future_date = '2030-01-01', 
        lookup_step = 10, lookback_step = 10
    ):
        self.current_date = current_date     
        self.future_date = future_date
        self.lookup_step = lookup_step
        self.lookback_step = lookback_step
        
    
    def __keytransform__(self, key):
        if isinstance(key, datetime):
            key = key.date()
        elif isinstance(key, date):
            key = key
        elif isinstance(key, int) or isinstance(key, float):
                key = datetime.strptime(str(key), '%Y%m%d') # to be used
        elif isinstance(key, six.string_types):
            try:
                key = parse(key).date()
            except (ValueError, OverflowError):
                raise ValueError("Cannot parse date from string '%s'" % key)
        else:
            raise TypeError("Cannot convert type '%s' to date." % type(key))

        return key
        
        
        # self.current_date = self.__keytransform__(current_date)        
        # self.future_date = self.__keytransform__(future_date)