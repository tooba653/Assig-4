import time
import datetime
import calendar
import math

# The date and time (current datetime)
now = datetime.datetime.now()
print("Now:", now)

# Epoch used in Python 
epoch_time = time.time()
print("Epoch time:", epoch_time)

# Getting the correct time using localtime
local_time = time.localtime()
print("Local Time:", local_time)

# Getting the formatted time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted Time:", formatted_time)

# The calendar - Get calendar for a month
print(calendar.month(2025, 4))

# The datetime - using date, timedelta
today = datetime.date.today()
print("Today's Date:", today)
future_date = today + datetime.timedelta(days=10)
print("Date after 10 days:", future_date)

# The strftime() method
formatted_date = today.strftime("%A, %d %B %Y")
print("Formatted Date:", formatted_date)

# Python Math Module
print("Square Root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Pi:", math.pi)
print("Power 2^3:", math.pow(2, 3))
print("Floor of 2.9:", math.floor(2.9))
print("Ceil of 2.1:", math.ceil(2.1))

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught Error:", e)

# NaN 
nan_value = float('nan')
print("Value:", nan_value)
print("Is NaN:", math.isnan(nan_value))

# Working with NaN
a = float('nan')
b = 10
print("NaN + 10 =", a + b)  # Still NaN
print("NaN == NaN?", a == a)  # False

# Infinity
pos_inf = float('inf')
neg_inf = float('-inf')
print("Positive Infinity:", pos_inf)
print("Negative Infinity:", neg_inf)
print("Is Positive Infinity infinite?", math.isinf(pos_inf))
print("Infinity + 1000 =", pos_inf + 1000)