
def maximum(number1, number2):
    max_of_two_numbers = max(number1, number2)
    return max_of_two_numbers

def minimum(number1, number2):
    min_of_two_numbers = min(number1, number2)
    return min_of_two_numbers

def average(number1, number2):
    avg_of_two_numbers = number1 + number2/2
    return avg_of_two_numbers

def addition(number1, number2):
    sum_of_two_numbers = number1 + number2
    return sum_of_two_numbers

def product(number1, number2):
    product_of_two_numbers = number1 * number2
    return product_of_two_numbers

a = int(input("Enter a number of your choice: "))
b = int(input("Enter another of your choice: "))

minimum_number = minimum(a, b)
print("Minimum of %d and %d is '%d'"%(a, b, minimum_number))

maximum_number = maximum(a, b)
print("Maximum of %d and %d is '%d'"%(a, b, maximum_number))

average_of_numbers = average(a, b)
print("Average of %d and %d is '%f'"%(a, b, average_of_numbers))

sum_of_numbers = addition(a, b)
print("Sum of %d and %d is '%d'"%(a, b, sum_of_numbers))

product_of_numbers = product(a, b)
print("Product of %d and %d is '%d'"%(a, b, product_of_numbers))






