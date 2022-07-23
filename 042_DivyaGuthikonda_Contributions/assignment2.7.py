#Given a string print all the lowercase characters, upper case characters and numeric characters and their counts.

def Count(str):
    upper=0
    lower=0 
    num=0

    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        else : 
         if(str[i].islower()):
            lower += 1
         else:
            if str[i].isdigit():
             num += 1
    print('Number of Upper case letters:', upper)
    print('Number of Lower case letters:', lower)
    print('Number of digits in the given string:', num)

str ="This is Divya assigned with 10 RollNumber"
Count(str)
#output
#Number of Upper case letters: 4
#Number of Lower case letters: 29
#Number of digits in the given string: 2
