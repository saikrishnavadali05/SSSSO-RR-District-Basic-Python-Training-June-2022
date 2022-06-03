"""
Define a function that accepts roll number and returns whether the student 
is present or absent.

given roll numbers
roll_numbers = [23,43,22,56] 

"""

#solution

def numbers(roll):
    roll_numbers = [23,43,22,56]
    if roll in roll_numbers:
        print("Yes, the roll number is present")
    else:
         print("No, the roll number is not present")

if __name__ == "__main__":

    roll = int(input("Enter the number"))
    numbers(roll)