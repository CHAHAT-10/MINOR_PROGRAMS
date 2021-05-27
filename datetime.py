#from datetime import datetime
#my_date_string = input("enter date and time:- ")
#datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')
#print(type(datetime_object))
#print(datetime_object)
from dateutil import parser
date_time = parser.parse("mar 11 2011 11:31am")
print(date_time)
print(type(date_time))