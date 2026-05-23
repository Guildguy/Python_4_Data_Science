import time as t
import datetime as dt

print(dt.timezone)#atributos utc

print(dt.date)#atributos year, month, day
print(dt.time)#atributos hour, minute, second, microsecond, tzinfo
print(dt.datetime)#atributos year, month, day, hour, minute, second, microsecond, tzinfo
first_time = dt.timestamp(dt.date(1, 1, 1970))
print(f"Seconds since {first_time}")
#print(time)
