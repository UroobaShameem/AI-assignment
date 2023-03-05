import datetime
date_time= datetime.datetime.now()
print(date_time)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print('Year:',year(date_time))
print('Month:',month(date_time))
print('Day:',day(date_time))
print('Time:',t(date_time))