# Pascal Case 
'''
First letter of the variable name should be capital, 
along with the firstletter of every new componded together
should also be capital
'''
MessageToProgrammers = "Be Careful with the syntax"
print(MessageToProgrammers)

# Camel Case
'''
The First letter of the variabel name should be small,
along with the firstletter of every new componded together
should be capital
'''
myName = "My Name is Nageshwari"
print(myName)

# Snake Case
'''
snake case seperates the words with an underscore, 
if every letter is capitalized it is known as screaming snake case
'''
my_share_in_a_field = 10
print(my_share_in_a_field)

import pyttsx3
note = pyttsx3.init()
note.say("The most widely used naming convension for naming the variables is Sanke Case")
note.runAndWait()
