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

import inspect
import markettradingdays

def list_supported_countries():
    """List all supported countries incl. their abbreviation."""
    return [
        name
        for name, obj in inspect.getmembers(
            markettradingdays.countries, inspect.isclass
        )
    ]


