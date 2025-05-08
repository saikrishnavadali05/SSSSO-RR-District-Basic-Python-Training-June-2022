# Given time in seconds, display the equivalent in hours, minutes and seconds. For example, 5000 seconds should print output as follows: 5000 seconds is 1 hours, 23 minutes and 20 seconds

Seconds = int(input("Enter the seconds which needs to be converter into x hours x minutes and x seconds "))
Hours = Seconds // 3600
Minutes = (Seconds % 3600)//60
seconds = (Seconds % 3600)%60
print(Hours,"Hours",Minutes,"Minutes",seconds,"seconds")