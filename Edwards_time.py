"""from datetime import datetime

# Store the current time in a variable
current_time = datetime.now()

# Print out the current year
current_year = current_time.year
print("Current Year:", current_year)

# Print the weekday of the week
weekday = current_time.strftime("%A")
print("Weekday:", weekday)

# Determine if a provided year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

year_to_check = 2024
if is_leap_year(year_to_check):
    print(year_to_check, "is a leap year")
else:
    print(year_to_check, "is not a leap year")

# Convert a string into a datetime object
date_str = "2023-04-26"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj)"""


"""# Task 1
from datetime import datetime

# Create a datetime object for the desired year (2014 in this case)
current_datetime = datetime(year=2014, month=1, day=1)

# Extract the year component and print it
current_year = current_datetime.year
print(current_year)"""


"""# Task 2

from datetime import datetime

# Define the some_date variable
some_date = datetime(2021, 7, 14)

# Extract the weekday component and print it as a number (0-6, where Monday is 0 and Sunday is 6)
weekday_num = some_date.weekday()
print(weekday_num)"""


"""
# Task 3
def is_leap_year(year):
    #Return True if the year is a leap year, False otherwise.
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Check if 2021 is a leap year and print the result
if is_leap_year(2021):
    print("2021 is a leap year")
else:
    print("2021 is not a leap year")
"""

"""# Task 4

from datetime import datetime

date_as_string = "Feb 14 2021 8:30AM"

# Use strptime() to parse the string and create a datetime object
datetime_object = datetime.strptime(date_as_string, '%b %d %Y %I:%M%p')

# Print the datetime object
print(datetime_object)"""


