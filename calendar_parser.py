import icalendar
import requests
import csv
import datetime

# If iCalendar module is not installed, use the following command to install it
# pip3 install icalendar

def calendar_utility(window_start: datetime.datetime,window_end: datetime.datetime,ical: str,output_to_csv: bool=False):
    """ Find calendar events within a time frame from an iCal Calendar and return their Names and Durations
    :param window_start: datetime, Start date of the requested calendar events
    :param window_end: datetime, End date of the requested calendar events
    :param ical: string, iCal URL
    :param output_to_csv: bool, Enable saving output to CSV Default is False
    """

    # Pull data from ical link, convert to text, and push to library object
    data = requests.get(ical)
    calendar_data = data.text
    calendar = icalendar.Calendar.from_ical(calendar_data)


    # Add headers to CSV file if enabled
    if output_to_csv == True:
        with open("calendar_data.csv", 'a', newline='') as csvfile:
            csv_output = csv.writer(csvfile, delimiter=',')
            csv_output.writerow(['id','summary','start','end','duration'])

    total_time = datetime.timedelta() #create an empty datetime variable to increment total time
    count = 0
    print()
    
    # Step through each event stored in the calendar
    for event in calendar.walk('VEVENT'):
        # Pull data from each event
        summary = event.get("SUMMARY")
        start = event.decoded("DTSTART")
        end = event.decoded("DTEND")

        # Check if event is within window
        if (start < window_end) and (start > window_start):
            duration = end-start
            # If csv ouput is enabled, write out to file
            if output_to_csv == True:
                with open("calendar_data.csv", 'a', newline='') as csvfile:
                    csv_output = csv.writer(csvfile, delimiter=',')
                    csv_output.writerow([count,summary,start,end,duration])
            print(summary, duration)
            # print(start)
            # print(end)

            total_time = total_time + duration
            count += 1
        else:
            # Event isn't within time window given, skip it
            pass
            

    print()
    print("Total Time Spent", total_time)
