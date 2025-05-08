#def outer_calculate(a,b):
   # def add_two_number(a,b):
       # return a+b
    #sum1=add_two_number(a,b)
    # return sum1+5
#result=outer_calculate(5,9)
#print(result)

#def addition(num):
    #if num:
        # call same function by reducing number by 1
        #return num + addition(num - 1)
    #else:
        #return 0

#def display_student(name, age):
    #print(name, age)

#showstudent = display_student
#showstudent("Emma", 26)

#for i in range(3,31):
    #if i%2==0:
       # print(list[i],sep=",")
    #else:
       # continue
#Exercise 9: Find the largest item from a given list
#x = [4, 6, 8, 24, 12, 2]

#print(max(x))

#str1 = "James"
#print(str1[::2])

#str1 = "JhonDipPeta"
#print(str1[4:7:1])

#str2 = "JaSonAy"
#print(str2[2:5:1])

#list1 = [100, 200, 300, 400, 500]
#print(list1[::-1])

#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
#list3 = [i + j for i, j in zip(list1, list2)]
#print(list3)

#numbers = [1, 2, 3, 4, 5, 6, 7]
# result list
#res = []
#for i in numbers:
    # calculate square and add to the result list
 #   res.append(i * i * i)
#print(res)

#list1 = ["Hello ", "take "]
#list2 = ["Dear", "Sir"]
#list3 = [x + y for x in list1 for y in list2]
#print(list3)

#list1 = [10, 20, 30, 40]
#list2 = [100, 200, 300, 400]

#for x, y in zip(list1, list2[::-1]):
    #print(x, y)

#list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#res = list(filter(None, list1))
#print(res)

#list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

# solution
#list1[2][2].append(7000)
#print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#print(list1[2])#["c", ["d", "e", ["f", "g"], "k"], "l"]
#print(list1[2][1])["d", "e", ["f", "g"], "k"]
#print(list1[2][1][2])["f", "g"]
# sub list to add
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)