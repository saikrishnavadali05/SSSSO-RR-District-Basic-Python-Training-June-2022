def add(*Numbers):
    Solution = 0
    Length = len(Numbers)
    print(Length)
    for i in range(0,len(Numbers)):
        Solution = Solution + Numbers[i]
    print("The Solution of Sum is",Solution)

add(2,3)
add(4,6,7)

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)