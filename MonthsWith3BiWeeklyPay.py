#!/usr/bin/python
import calendar

# Functions
def month_num_to_string(month):
    month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return month_names[month]

# User Logic
print("Enter starting pay date (MM/DD/YYYY)")
month = input("Month (MM): ")
day = input("Day (DD): ")
year = input("Year (YYYY): ")

pay_day = calendar.weekday(year, month, day)
calendar.setfirstweekday(pay_day)

month_array = calendar.monthcalendar(year, month)
num_weeks = len(month_array)

# Find the first week of pay
for week in month_array:
    if day in week:
        start_week = month_array.index(week)
        break

# Check whether or not there are 3 pay periods in this month
# starting from the start_week
pay_count = 0
for week in range(start_week, num_weeks, 2):
    pay_count += 1
    if pay_count == 3:
        print "\n", calendar.month(year, month), "\n", month_num_to_string(month), year, "has three pay periods"
        pay_count == 0
