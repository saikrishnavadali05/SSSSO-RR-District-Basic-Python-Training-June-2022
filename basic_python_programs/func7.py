"""
Write a program to remove characters from a string starting from zero up 
to n and return a new string.

For example:
remove_chars("python", 2) so output must be thon. Here we need to remove 
first four characters from a string.
"""

def remove_chars(word, n):
    print('given string:', word)
    #fill the code

if __name__ == "__main__":
    print("Removing characters from a string")
    print(remove_chars("python", 2))
    print(remove_chars("language", 4))



#solution
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

if __name__ == "__main__":
    print("Removing characters from a string")
    print(remove_chars("python", 2))
    print(remove_chars("language", 4))