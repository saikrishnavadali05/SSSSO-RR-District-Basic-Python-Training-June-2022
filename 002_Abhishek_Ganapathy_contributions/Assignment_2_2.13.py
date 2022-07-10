import random
Count = 0
s=open("Assignment_2_2.13_Input.txt","r")
m=s.readlines()
o=random.choice(m)
print("The String is",o)
Length = len(o)
print("The length of the sentence is",Length)
for i in range(0,Length):
    if(o[i].isdigit()):
        Count = Count + 1
print("The number of digits in this sentence is",Count)
s.close()