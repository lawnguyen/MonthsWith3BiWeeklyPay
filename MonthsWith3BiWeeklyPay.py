#!/usr/bin/python
import calendar

# Region Functions

def month_num_to_string(month):
    month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return month_names[month]

# Check whether or not there are 3 pay periods in this month
# starting from the start_week
def is_there_3_pay_periods(start_week, num_weeks, month, year):
    pay_count = 0
    week = start_week
    final_week = week
    while week < num_weeks:
        pay_count += 1
        final_week = week
        if pay_count == 3:
            display_result(month, year)
        week += 2
    return final_week

def display_result(month, year):
    print "\n", calendar.month(year, month), "\n", month_num_to_string(month), year, "has three pay periods"

def find_first_week_of_pay(month, day):
    for week in month:
        if day in week:
            return month.index(week)

def find_first_day_of_pay(num_weeks, month, final_week):
    # If we got paid in the last week of the month
    if final_week == num_weeks-1:
        if month[0][0] == 0:
            return month[2][0]
        else:
            return month[1][0]
    # We got paid in the second last week of the month
    else:
        if month[0][0] == 0:
            return month[1][0]
        else:
            return month[0][0]

def print_results_banner():
    print '\n'
    for i in range(15):
        print '*',
    print '\n        R E S U L T S'
    for i in range(15):
        print '*',
    print '\n'


# Region User Logic
print("\nEnter a starting pay date")
month = input("Month (MM): ")
day = input("Day (DD): ")
year = input("Year (YYYY): ")

pay_day = calendar.weekday(year, month, day)
calendar.setfirstweekday(pay_day)

month_array = calendar.monthcalendar(year, month)
num_weeks = len(month_array)

start_week = find_first_week_of_pay(month_array, day)
n = input("\nHow many months do you want to check? ")

print_results_banner()

# Check the next n months
for i in range(n):
    final_week = is_there_3_pay_periods(start_week, num_weeks, month, year)

    # Update current month and/or year
    year = (year + 1) if month == 12 else year
    month = 1 if month == 12 else (month + 1)
    month_array = calendar.monthcalendar(year, month)

    # Update current day and week
    day = find_first_day_of_pay(num_weeks, month_array, final_week)
    start_week = find_first_week_of_pay(month_array, day)
    num_weeks = len(month_array)