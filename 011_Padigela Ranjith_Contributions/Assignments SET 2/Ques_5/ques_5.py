"""
Given a list of numbers write a program to calculate the sum of odd and
even numbers and print the same. 
Accept from the user the count of numbers and the actual numbers.
"""
nums = input("Enter the numbers with separated by spaces only:  ")
lst = []
for i in nums.split():
    lst.append(i)

def Even_Odd_sum(lst):
    Even_sum = 0
    Odd_sum = 0
    cnt_Even_no = 0
    cnt_Odd_no = 0
    cnt_actual_no = 0
    for i in lst:
        if int(i) % 2 == 0:
            Even_sum += int(i)
            cnt_Even_no += 1
        if int(i) % 2 != 0:
            Odd_sum += int(i)
            cnt_Odd_no += 1
        cnt_actual_no += 1
    print("The even sum is",Even_sum,"\nThe Odd sum is",Odd_sum,"\nThe coutn of even num is",cnt_Even_no, "\nThe count of odd num is",cnt_Odd_no,"\nThe count of actual numbers is ",cnt_actual_no)
    return ""
results = Even_Odd_sum(lst)

print(results)