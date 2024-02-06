"""______________________WORKING WITH DATE AND DATE USING PANDAS______________________
The data class in the DateTime Module of python deals with date
 in the gregorian calendar, it accepts three 3 integer argument,
 year, month and day"""
# import datetime
from datetime import date

import pandas as pd
from pandas import Timestamp
"""my_date = date(1970,6,19)
print(my_date)
print(my_date.year)
print(my_date.month)
print(my_date.day)
print(type(my_date))
df = pd.Timestamp('2021-05-22 06:23:15')
print(df)
print(type(df))
print(df.year)
# Timestamp can be used to access weekdays, weekend, periods etc
ex = pd.Timestamp.weekday(df)
print(ex)
dx = pd.Timestamp('2024-01-30')
print(dx.weekday()) # Note: Monday == 0...... Sunday == 6
# the day_of_year is used to return the day of the year
ts = pd.Timestamp(2024,2,15)
print(ts.day_of_year)
tr = Timestamp.now()
# To check if the year is a leap year
ta = pd.Timestamp(2024,2,15)
print(ta.is_leap_year)
# USING THE FORMAT METHOD
Time_stamp = pd.Timestamp('2024-01-30')
print('{},{} {},{}'.format(Time_stamp.day_name(), Time_stamp.month_name(), Time_stamp.day, Time_stamp.year))
# Print between start time and end time """
""""______________________WORKING WITH TIME PERIOD________________________
Why an instance of the timestamp class represent a single point of time,
 an instance of the period object represents a period such as a year, a month e.t.c"""
"""__________________________year = pd.Period('2021', freq='M')
print(year)
event_year = pd.date_range('2021-2-7', '2021-6-19', periods=7)
print(event_year)
ert = pd.date_range('2021-2-7', '2021-6-19', freq='D')
print(ert)
for day in event_year:
    print('{}-{}\t{}'.format(day.day_of_week, day.day_name(), day.date()))
event_year1 = pd.date_range('2021-2-7', '2023-3-7', periods=30)
for month in event_year1:
    print('{}'.format(month.month_name()))"""
"""____________________ASSIGNMENT_________________
1. Generate a data value 1000 range and set it as a new column to the csv file using pandas
"""
# READ CSV FILE
nba = pd.read_csv("C:/Users/NEW USER/OneDrive/Documents/nba.csv")
# import numpy as np
import numpy as np
# Generate a random date between today and 10 years ago

# Generate random date data in the range of 1000
random = pd.date_range('2014-1-31', '2024-1-31', periods=458)
#print(random_date)

# Add the random date data as a new column to the dataframe
#dy = nba.assign(random_date=random_date)
nba['Date'] = random

# Write the updated dataframe back to the CSV file
nba.to_csv("C:/Users/NEW USER/OneDrive/Documents/nba.csv", index=False)
print(nba)

# Note: Remember to replace "data.csv" and "data_with_random_date.csv" with
# the actual file names and paths in your code.




