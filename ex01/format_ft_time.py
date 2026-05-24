from datetime import datetime as dt

#print(dt.timezone)#atributos utc
#print(dt.date)#atributos year, month, day
#print(dt.time)#atributos hour, minute, second, microsecond, tzinfo
#print(dt.datetime)#atributos year, month, day, hour, minute, second, microsecond, tzinfo
now = dt.now()
seconds = now.timestamp()
print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(f"{now.strftime('%b %d %Y')}")
