import sys
first_list1=[]
for i in sys.argv[1:]:
    first_list1.append(int(i))
t1=tuple(first_list1)
dup_set1=set(t1)
print(sum(dup_set1))

# PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> python assignment6.py 1 2 2 3 4 3 1
# 10
# PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> 


