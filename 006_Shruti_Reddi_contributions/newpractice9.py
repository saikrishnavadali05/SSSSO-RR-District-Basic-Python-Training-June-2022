#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]

#res_dict = dict(zip(keys, values))
#print(res_dict)

#dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#dict3 = dict1.copy()
#dict3.update(dict2)
#print(dict3)

#sampleDict = { "class": { "student": { "name": "Mike", "marks": { "physics": 70,  "history": 80   } }
   # }
#}

#print(sampleDict['class']['student']['marks']['history'])

#employees = ['Kelly', 'Emma']
#defaults = {"designation": 'Developer', "salary": 8000}

#res = dict.fromkeys(employees, defaults)
#print(res)

# Individual data
#print(res['Emma'])

#sample_dict = {
  #  "name": "Kelly",
    #"age": 25,
    #"salary": 8000,
    #"city": "New york"}

#print(sample_dict["name"],sample_dict["salary"] )

#sample_dict.pop("name")
#print(sample_dict)
#sample_dict.pop("salary")
#print(sample_dict)

#sample_dict = {'a': 100, 'b': 200, 'c': 300}
#if 200 in sample_dict.values():
    #print('200 present in a dict')

#sample_dict = {
  #"name": "Kelly",
  #"age":25,
  #"salary": 8000,
  #"city": "New york"}


#sample_dict["location"] = sample_dict.pop("city")
#print(sample_dict)

#sample_dict = {
 # 'Physics': 82,
  #'Math': 65,
  #'history': 75}
#print(min(sample_dict))

#sample_dict = {
    #'emp1': {'name': 'Jhon', 'salary': 7500},
    #'emp2': {'name': 'Emma', 'salary': 8000},
    #'emp3': {'name': 'Brad', 'salary': 500}
#}

#sample_dict['emp3']['salary'] = 8500
#print(sample_dict)

#sample_set = {"Yellow", "Orange", "Black"}
#sample_list = ["Blue", "Green", "Red"]
#sample_set1=set(sample_list)
#sample=sample_set.union(sample_set1)
#print(sample)

#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
#set=set1.intersection(set2)
#print(set)

#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
#print(set1.union(set2))

#set1 = {10, 20, 30}
#set2 = {20, 40, 50}

#print(set1-set2)

#set1 = {10, 20, 30, 40, 50}
#set1.difference_update({10, 20, 30})
#print(set1)

#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}

#print(set2.intersection(set1))

#tuple1 = (10, 20, 30, 40, 50)
#print(tuple1[::-1])

#tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
#print(tuple1[1][1])

#tuple1= (50)
##print(tuple1)

#tuple1 = (10, 20, 30, 40)
#print(tuple1[0])
#print(tuple1[1])
#print(tuple1[2])
#print(tuple1[3])

#tuple1 = (11, 22)
#tuple2 = (99, 88)
#tuple1, tuple2 = tuple2, tuple1
#print(tuple1)
#print(tuple2)

#tuple1 = (11, 22, 33, 44, 55, 66)

#tuple2 = tuple1[3:-1]
#print(tuple2)

#tuple1 = (11, [22, 33], 44, 55)
#tuple1[1][0] = 222
#print(tuple1)

#tuple1 = (50, 10, 60, 70, 50)
#print(tuple1.count(50))

def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))