#program for removing all the duplicate elements in the list using set()
dup_list =[1,7,9,11,7,1,9]
print("the original list is :"+str(dup_list))
dup_list=list(set(dup_list))                                        #using set() to remove duplicate elements
print("the list after removing of duplicate elements:" +str(dup_list))
