def add(numList):
    if len(numList)!=4:
        return -1;
    s=0;
    for i in numList:
        if int(i)%2==0:
            s+=int(i)
    if s==0:
        return 0;
    return s;
def multiple(numList):
    if len(numList)!=4:
        return -1;
    mul=1;
    for i in numList:
        if int(i)%2==0:
            mul*=int(i)
    if mul==1:
        return 0;
    return mul;
from add import add
from multiple import multiple
class LessNumberException(Exception):
    pass
class NoEvenNumberException(Exception):
    pass
oper,num=input().split()
numList = num.split(',')
file = open("output.txt",'a')
try:
    if oper=="add":
        res = add(numList)
        if res==-1:
            raise LessNumberException
        elif res==0:
            raise NoEvenNumberException
        
    elif oper=="multiple":
        res = multiple(numList)
        if res==-1:
            raise LessNumberException
        elif res==1:
            raise NoEvenNumberException
    file.write("The output is "+str(res)+"\n")
except LessNumberException:
    file.write("Count of Input Number should be four\n");
except NoEvenNumberException:
    file.write("No Even number present\n");
file.close();
    


