from datetime import timedelta, date

# import sys
# sys.path.insert(0, 'C:/Users/momojola/projects/marketanalysis/')

import marketholidays
from marketholidays.constants import WEEKEND
from markettradingdays.markettradingdays_base import MarketTradingDaysBase
        
class UnitedStates(MarketTradingDaysBase):
    
    def __init__(self, **kwargs):
        pass
    
    def future_list(self, current_date, lookup_step):  
        self.current_date = self.__keytransform__(current_date) 
        # Preallocate for, say, thirty years from the current date.
        future_date = self.current_date + timedelta(days=365*30)
        
        # date you want to pull
        prediction_date = self.current_date + timedelta(days = lookup_step)
        
        def diff_dates(current_date, future_date):
            difference_in_days = abs((current_date - future_date).days)
            return difference_in_days
        
        def allDays(current_date, future_date):
            nextDay = []
            marketholidays_US = marketholidays.US()
            diff = diff_dates(current_date, future_date)
            for i in range(1,diff+1): 
                    next = current_date + timedelta(days=i)
                    nextDay.append(next)
                    if next.weekday() in WEEKEND or next in marketholidays_US:
                        nextDay.remove(next)
            return nextDay

        datelist = allDays(self.current_date, future_date) # for all preallocated days 
        requiredlistdates = datelist[:diff_dates(self.current_date, prediction_date)] # pull out the required date list
        return requiredlistdates
    
    def prevDays(self, current_date, lookback_step):  
        self.current_date = self.__keytransform__(current_date) 
        # Preallocate for, say, thirty years previously from the current date.
        backup_date = self.current_date - timedelta(days=365*30)
        
        # date you want to pull backwards
        prevDate = self.current_date - timedelta(days = lookback_step)
        
        def diff_dates(current_date, future_date):
            difference_in_days = abs((current_date - future_date).days)
            return difference_in_days
        
        def allDays(current_date, future_date):
            nextDay = []
            marketholidays_US = marketholidays.US()
            diff = diff_dates(current_date, future_date)
            for i in range(1,diff+1): 
                    next = current_date + timedelta(days=i)
                    nextDay.append(next)
                    if next.weekday() in WEEKEND or next in marketholidays_US:
                        nextDay.remove(next)
            return nextDay

        datelist = allDays(backup_date, self.current_date) # for all preallocated days 
        requiredlistdates = datelist[-diff_dates(prevDate, self.current_date):] # pull out the required date list
        return requiredlistdates
    
    def BtwDates(self, current_date, future_date):  
        self.current_date = self.__keytransform__(current_date) 
        self.future_date = self.__keytransform__(future_date)
        
        def diff_dates(current_date, future_date):
            difference_in_days = abs((current_date - future_date).days)
            return difference_in_days
        
        def allDays(current_date, future_date):
            nextDay = []
            marketholidays_US = marketholidays.US()
            diff = diff_dates(current_date, future_date)
            for i in range(1,diff+1): 
                    next = current_date + timedelta(days=i)
                    nextDay.append(next)
                    if next.weekday() in WEEKEND or next in marketholidays_US:
                        nextDay.remove(next)
            return nextDay
        
        if self.current_date < self.future_date:    
            datelist = allDays(self.current_date, self.future_date) # for all preallocated days 
        else:
            datelist = allDays(self.future_date, self.current_date) # for all preallocated days 
        # requiredlistdates = datelist[:diff_dates(prevDate, self.current_date)] # pull out the required date list
        return datelist
    
class US(UnitedStates):
    pass

class USA(UnitedStates):
    pass


# PROVINCES = []
# years = 2021; expand=True; observed=True; prov=None; state=None
# # key = '2020/02/01'
# # key = datetime(2021,3,6)
# # key = key.date()

# key = 20120213
# # key = datetime.utcfromtimestamp(key).date()
# key = datetime.strptime(str(key), '%Y%m%d').date()
# # isinstance(key, date)
# if isinstance(years, int):
#     years = [
#         years,
#     ]
# years = set(years)

# print(key)









####################################################
# current_date = date.today()
# future_date = '2021-03-18'
# lookup_step = 14
# lookback_step = 4
# a = UnitedStates()
# # a.future_list(current_date, lookup_step)
# # a.prevDays(current_date, lookback_step)
# # a.BtwDates(current_date, future_date)
# print(a.BtwDates(current_date, future_date))
####################################################