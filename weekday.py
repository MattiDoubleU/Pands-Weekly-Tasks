# weekday.py
# Author: Matthias Wiedemann
# stackoverflow.com was great help here: https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python.

import datetime # datetime module is a tool for handling dates, times, and time-related calculations in Python. 
                # In the datetime module in Python, days of the week (e.g., Monday, Tuesday, etc.) are represented as integers, starting with Monday as 0 and ending with Sunday as 6. 

today = datetime.datetime.now().weekday()               # Get the current date.

if today < 5:                                           # Check if today is a weekday.
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yeah!")


