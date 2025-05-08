import random as r

rand_num = r.randint(0,100)
user_num = None
tries = 0
guessed = False

print("--------Number Guessing Game--------")
print("*Enter '999' at any point to stop the game.")

while(user_num != rand_num):
    tries += 1
    user_num = int(input("Guess the number generated(0-99): "))

    if user_num == 999:
        print("Thank You for playing!!! Bye...")
        break
    elif user_num < rand_num:
        print("Try again with a larger number!")
    elif user_num > rand_num:
        print("Try again with a smaller number!")
    else:
        guessed = True

if guessed:
    print("Good Job!!!, You guessed the number in", tries, "tries!!!")