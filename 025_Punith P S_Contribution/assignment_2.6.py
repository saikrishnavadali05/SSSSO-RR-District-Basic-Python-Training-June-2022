#Find out what is a timestamp? Print date and time in a timestamp. Print the seconds, hours, 
# minutes as sepearate integer numbers from that timestamp. (hint : use datetime module. 
# Search on google when stuck).

#Timestamp is the date and time of occurrence of an event. In Python we can get the timestamp of an event to an accuracy of milliseconds
import datetime;

time_stamp = datetime.datetime.now()
  
# print the current timestamp
print("seconds:" ,time_stamp.second,"\n")
print("Minutes:",time_stamp.minute,"\n")
print("Hour",time_stamp.hour,"\n")
