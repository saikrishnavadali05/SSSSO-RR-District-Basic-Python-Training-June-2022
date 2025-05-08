from datetime import datetime
try:
    Todays_Date = '2022/07/24'
    Birthday = '2022/11/22'
    d1 = datetime.strptime(Todays_Date, "%Y/%m/%d")
    d2 = datetime.strptime(Birthday, "%Y/%m/%d")
    Difference = d2 - d1
    print("Current timestamp is ",Todays_Date)
    print("Countdown for the birthday is", Difference, "days" )
    print(f'Difference is {Difference.days} days')

    file = open("Assignment2_24_07_2022.txt","r")
    line = file.read()
    print("Line is", line)
    D3 = datetime.strptime(line, "%Y/%m/%d")
    print("D3 is", D3)
    D4 = datetime.strptime(Birthday, "%Y/%m/%d")
    print(D4)
    Difference = D4 - D3
    if Difference > 0:
        print("The difference is",Difference)
    else:
        Difference2 = D3 - D4
    print("The difference is",Difference2)
except:
    print("Enter proper details")