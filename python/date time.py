# date time in python

import datetime as dt

current_date=dt.date.today()
print("current date:",current_date)

new=dt.date(2024, 10, 16)
print(new)
print("year:",new.year)
print("month:",new.month)
print("date:",new.day)
print("-------------------------------------")

a=dt.time(4, 43, 5, 555505)
print(a)
print("hour:",a.hour)
print("minute:",a.minute)
print("second:",a.second)
print("microsecond:",a.microsecond)

print("-------------------------------")

current_time=dt.datetime.now()
print(current_time)
print("-------------------------------")
new=dt.datetime(2024,10,16,5,53,50)
print(new.date())
print(new.time())

# we can also difference the date and time...if you want to know how many days are there for next year new year.

current=dt.datetime.now()
new_year=dt.datetime(2025,1,1)
difference=new_year-current
print(difference)

print("-------------------------------")
current=dt.datetime.now()
print(current)
s=current.strftime("%A %B %d %Y")
print(s)