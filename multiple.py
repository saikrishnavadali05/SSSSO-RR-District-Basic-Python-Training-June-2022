result=0
x= int(input('enter a number'))
y= int(input('enter a number'))
a= int(input('enter a number'))
d= int(input('enter a number'))
l1=[x,y,a,d]
for num in l1:
    if num % 2 != 0:
        print('no even number')
number_of_elements = len(l1)
if(number_of_elements<3):
    print('insufficient inputs')
else:
    print('sufficient inputs')
for i in l1:
    if not i % 2 :
       result*=i
print('product of even numbers is:',result)
if not x:
    print("You didn't enter a number")
else:
    print("Good job")
    if not y:
        print("You didn't enter a number")
    else:
        print("Good job")
        if not a:
            print("You didn't enter a number")
        else:
            print("Good job")
            if not d:
                print("You didn't enter a number")
            else:
                print("Good job")




