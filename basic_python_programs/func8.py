"""
Write a function to return True if the first and last number of a given list is same. 
If numbers are different then return False.

given list are

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

"""















#solution
def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

if __name__ == "__main__":
    numbers_x = [10, 20, 30, 40, 10]
    print("result is", first_last_same(numbers_x))

    numbers_y = [75, 65, 35, 75, 30]
    print("result is", first_last_same(numbers_y))