# range function
#1
a = [0,1,2,3,4,5,6,7]
print(a[0:8:2])  #[0, 2, 4, 6]
#or
print(list(range(0,8,2))) #[0, 2, 4, 6]

#2
print(list(range(20,3,-4))) # [20, 16, 12, 8, 4]

#3
print(list(range(-12,13,6))) #[-12, -6, 0, 6, 12]

#4
print(range(2,5)) #range(2, 5) (to print same we have to write in print function)
print(list(range(2,5))) #[2, 3, 4] (to print list of that funtion write this code)

#5
print(range(12, -3, -3)) #range(12, -3, -3)
print(list(range(12, -3, -3))) #[12, 9, 6, 3, 0]

#6
print(range(10,30,10)) #range(10, 30, 10)
print(list(range(10,30,10))) # [10, 20]

