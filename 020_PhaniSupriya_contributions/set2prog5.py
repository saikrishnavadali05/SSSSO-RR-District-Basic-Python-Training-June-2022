#sum of odd and even numbers of a given list 

lst = [0,1,2,3,4,5,6,7,8,9]
print("actual count of the given list is :", len(lst))
count_odd = [n for n in lst if n%2!=0]
print("count of odd numbers is :" ,len(count_odd))
print("sum of Odd numbers is :" ,sum(count_odd))
count_even = [n for n in lst if n%2==0]
print("count of even numbers is :" ,len(count_even))
print("sum of even numbers is :" ,sum(count_even))