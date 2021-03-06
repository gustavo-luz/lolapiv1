#import pytz
#from lolesports_api import Lolesports_API
#import json
#import requests
#from datetime import timedelta
import json, datetime
import requests
from lolesports_api import get_latest_date


now = datetime.datetime.now(datetime.timezone.utc)
print(now)
now = now - datetime.timedelta(seconds=now.second,microseconds=now.microsecond)
print(now)
from datetime import datetime, timedelta
now = datetime.now() + timedelta(seconds=10)
print(now)

now_string = now.isoformat()
print(str(now_string).replace('+00:00', 'Z'))

"""
import datetime
def round_time(dt=None, round_to=60):
   if dt == None: 
       dt = datetime.datetime.now()
   seconds = (dt - dt.min).seconds
   rounding = (seconds+round_to/2) // round_to * round_to
   return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)
"""
#now = datetime.datetime.now()
#print(now)
#print (round_time(datetime.datetime(now),round_to=60))

#print (round_time(datetime.datetime(2012,12,31,23,44,59),round_to=1.5))




#all_timezones = pytz.all_timezones
#print(all_timezones)
#'America/Sao_Paulo'
#api = Lolesports_API()
#api.get_latest_date()


'''
now = datetime.now()

print(now)

import datetime #com timedelta
rounded = now - (now - datetime.second) % timedelta(seconds=10)
#now = now - (now - datetime.timedelta(microseconds=now.microsecond))

#print(now)
#date_arred = now - datetime.timedelta(seconds=10)
#print(date_arred)
'''
"""
def ceil_dt(dt, delta):
    return dt + (dat.second - dt) % delta
now = dat.now()
print(now)    
print(ceil_dt(now, timedelta(seconds=10)))
"""
"""
def roundTime(dt=None, roundTo=60):
   #Round a datetime object to any time lapse in seconds
   #dt : datetime.datetime object, default now.
   #roundTo : Closest number of seconds to round to, default 1 minute.
   
   if dt == None : dt = datetime.datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + dat.timedelta(0,rounding-seconds,-dt.microsecond)

print(roundTime(datetime.datetime.now()),roundTo=30*60)

now = datetime.datetime.now(datetime.timezone.utc)
print( str(now))
now = now - datetime.timedelta(
     
     microseconds=now.microsecond
    )
print(type(now))
print( str(now))
now_string = now.isoformat()
print( str(now_string))
print( str(now_string).replace('+00:00', 'Z'))
"""