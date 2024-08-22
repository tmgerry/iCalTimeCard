# iCalTimeCard
iCal parser, used for generating time card style output based on time logged by events in a iCal supported calendar.

Example script calling the function, with automatic time windowing-
```
from calendar_parser  import *

ical = "ical_url_goes_here"

# Define the time window to get events from
window_end = datetime.datetime.now(datetime.timezone.utc) # End the window at present time, timezone-aware (not niave)
window_start = window_end-datetime.timedelta(days=14) # Start the window at [x] number of days before, in this case 14 days

calendar_utility(window_start,window_end,ical)
```

Example console output-
```
Fabrication 0:30:00
Testing 0:15:00
Sponsor Meeting 0:30:00
Software Debugging 1:00:00
Literature Review 1:00:00

Total Time Spent 3:15:00
```

Example CSV Output if `output_to_csv=True`-
```
id,summary,start,end,duration
0,Fabrication,2024-08-19 09:00:00-06:00,2024-08-19 09:30:00-06:00,0:30:00
1,Testing,2024-08-19 13:45:00-06:00,2024-08-19 14:00:00-06:00,0:15:00
2,Sponsor Meeting,2024-08-20 09:00:00-06:00,2024-08-20 09:30:00-06:00,0:30:00
3,Software Debugging,2024-08-21 10:15:00-06:00,2024-08-21 11:15:00-06:00,1:00:00
4,Literature Review,2024-08-21 17:30:00-06:00,2024-08-21 18:30:00-06:00,1:00:00
```
