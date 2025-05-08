#l1 = [3, 6, 9, 12, 15, 18, 21]
#l2 = [4, 8, 12, 16, 20, 24, 28]
#listl3=[]
#odd_elements=l1[1::2]

#print(odd_elements)

#even_elements=l2[::2]
#print(even_elements)

#listl3.extend(odd_elements)
#listl3.extend(even_elements)
#print(listl3)

#list1 = [34, 54, 67, 89, 11, 43, 94]

#print("Original list ", list1)
#element = list1.pop(4)
#print("List After removing element at index 4 ", list1)

#list1.insert(2, element)
#print("List after Adding element at index 2 ", list1)

#list1.append(element)
#print("List after Adding element at last ", list1)

#sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#list1=sample_list[0:3:1]
#list2=sample_list[3:6:1]
#list3=sample_list[6:9:1]
#print(list1[::-1])
#print(list2[::-1])
#print(list3[::-1])

#sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

#count_dict={}

#for item in sample_list:
    #if item in count_dict:
       # count_dict[item] += 1
    #else:
       # count_dict[item] = 1

#print("Printing count of each item  ", count_dict)

#first_list = [2, 3, 4, 5, 6, 7, 8]
#second_list = [4, 9, 16, 25, 36, 49, 64]
#result_list = zip(first_list, second_list)
#print(sorted(set(result_list)))

#first_set = {23, 42, 65, 57, 78, 83, 29}
#second_set = {57, 83, 29, 67, 73, 43, 48}

#print("The first set is : ", first_set)
#print("The second set is : ", second_set)

#third_set =first_set.intersection(second_set)
#print("The third set after intersection is :", third_set)

#first_set=first_set - third_set
#print("The first set after removing common elements is :", first_set)

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set.issubset(second_set):
    print(True)
else:
    print(False)

if second_set.issuperset(first_set):
     print(True)
else:
    print(False)

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)