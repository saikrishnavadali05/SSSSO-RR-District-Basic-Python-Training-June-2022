#get input from user
user_string=input('Enter a string:')
#using while loop
while ' ' in user_string:
    i=user_string.index(' ')
    print(user_string[:i])
    user_string=user_string[i+1:]
print(user_string)
#using for loop
for_string2=input('Enter a string:')
for s in for_string2.split():
    print(s)

#PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> python assignment1.py
#Enter a string:Love All Serve All Help Ever Hurt Never
#Love
#All
# Serve
# All
# Help
# Ever
# Hurt
# Never
# Enter a string:exit
# exit
# PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions>

  