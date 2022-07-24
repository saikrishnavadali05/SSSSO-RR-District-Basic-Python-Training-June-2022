time_in_secs = int(input("Enter your time in seconds: "))
hrs = time_in_secs//3600
mints = (time_in_secs%3600)//60
sec = (time_in_secs%3600)%60
print("The entered time is",hrs, ":", mints, ":", sec)