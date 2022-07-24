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

intro(Firstname="Sahruthaa", Lastname="reddy", Age=21, Phone=92345525021)
intro(Firstname="sagarika", Lastname="rao", Email="sagarikarao@nomail.com", Country="india", Age=25, Phone=9555652525)