from django.test import TestCase
# ###   Python Get Business Days ######

from datetime import date, timedelta
# Create your tests here.
import datetime
import numpy as np

# method1
start = datetime.date(2023, 6, 1)
end = datetime.date(2023, 6, 30)

days = np.busday_count(start, end)
print('Number of business days is:', days)

# include holidays in a list
days = np.busday_count(start, end, holidays=['2023-06-20'])
print('Number of business days is:', days)

# method2
start2 = '2023-06'
end2 = '2023-07'

days2 = np.busday_count(start2, end2)
print('Number of business days is:', days2)

# method3
start3 = date(2023, 6, 1)
end3 = date(2023, 6, 30)

# get list of all days
all_days = (start3 + timedelta(x + 1) for x in range((end3 - start3).days))

# filter business days
# weekday from 0 to 4. 0 is monday adn 4 is friday
# increase counter in each iteration if it is a weekday
count = sum(1 for day in all_days if day.weekday() < 5)
print('Number of business days is:', count)