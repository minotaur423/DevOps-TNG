import time 
from datetime import datetime, date 

#printing date and time values for the current date/time 
print(time.time()) #timestamp 
print(time.localtime(time.time())) #time struct 
print(date.today()) #current date part of ISO 8601 format 
print(datetime.today()) #ISO 8601 date-time 

#some common date-time conversions 
dt1 = datetime.strptime('12/01/2018', '%m/%d/%Y').isoformat() 
print(dt1) 

dt2 = datetime.strptime('25/12/17', '%d/%m/%y').isoformat() 
print(dt2) 

#timestamp since 8:00PM on December 31st, 1969 
dt3 = datetime.fromtimestamp(0).isoformat() 
print(dt3) 

dt4 = datetime.strptime('Sun 01 Apr 2018 12:00:00','%a %d %b %Y %H:%M:%S').isoformat()
print(dt4)
