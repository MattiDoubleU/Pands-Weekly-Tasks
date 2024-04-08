# weekday.py
# Author: Matthias Wiedemann
# With help from:
# https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/ 
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date.

import datetime # datetime module is a tool for handling dates, times, and time-related calculations in Python. 
                # In the datetime module in Python, days of the week (e.g., Monday, Tuesday, etc.) are represented as integers, starting with Monday as 0 and ending with Sunday as 6. 

today = datetime.datetime.now().weekday()               # Get the current date.
                                                        # Using if/else statement as per course material in week04, what works great here since we know that Saturday and Sunday represent, number 5 and 6 respectively.
if today < 5:                                           # Check if today is a weekday.
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yeah!")


