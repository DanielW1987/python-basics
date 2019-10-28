import datetime as dt

# current date
today: dt.datetime = dt.datetime.today()
print(today)
print("Current date: {}.{}.{}".format(today.day, today.month, today.year))
print("Current time: {}:{}:{}".format(today.hour, today.minute, today.second))

# specified date
christmas = dt.date(2019, 12, 24)
sleep_time = dt.time(10, 30)

print(christmas)
print(sleep_time)
print(dt.datetime.combine(christmas, sleep_time))
