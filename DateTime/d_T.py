import datetime
import pytz

"""
 naive dates and times
 datetime.date
 datetime.date.today()
 weekday, isoweekday
 timedeltas
 datetime.time
 datetime.datetime
 .now(), .today(), .utcnow()
 pytz
 timezone aware utcnow()
 timezone conversions
 timezone aware naive datetime
 isoformat() 
 strftime()
 strptime()
"""

tday = datetime.date.today()

# dt = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone("Asia/Dhaka"))
# print(dt)

dt = datetime.datetime.now()
print(type(dt))
tzzz = pytz.timezone("US/Mountain").localize(dt)

print(tzzz)

