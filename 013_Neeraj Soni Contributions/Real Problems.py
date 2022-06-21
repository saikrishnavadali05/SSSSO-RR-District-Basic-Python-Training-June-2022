from gettext import find


Girish_info_string = "Girish is very good boy who helps everyone and also Girish participates in all the sports and cultural meet. Girish hobbies are playing virtual games and also watching movies."
word = "Girish"
My_string = Girish_info_string
if word in My_string:
    print("success")

# For Loop
two_word_string = "Multiplewishes"
for ch_index, ch in enumerate(two_word_string, start =0):
   print("waiting for character index to be greater than 8")
   if ch_index > 8:
    print(ch_index)

# For numvers
#numbers_list = [23,24,25,27]
#for number in numbers_list:
 #   print(number)

# Example from book
s = "Multiple_wishes"
"""
Name s is attached to 'Multiple_wishes' string. When you call str(s) the
interpreter puts 'Multiple_wishes' instead of s and then calls str('Multiple_wishes').
"""
print(str(s))
print(repr(s))
for x in range(1, 7):
    print(str(x).rjust(2), str(x*x).rjust(5), sep=":", end=" ")
    # Note use of 'end' in the above
    print(str(x*x*x).rjust(4), end=" ")
    print(str(x*x*x*x).rjust(4), end=" ")
    print(str(x*x).rjust(6))

print()
for x in range(1, 5):
    print('{0:2d} {1:4d} {2:4d}'.format(x, x*x, x*x*x))
print()
print('12'.zfill(10))
print('3.14159265'.zfill(5))
print('-3.14'.zfill(6))
print('{0:2} {1:2} {2:2}'.format('company', 'and', 'Multiple_wishes'))
print()
print("PI value is approximately {0:.5f}".format(3.14159265))
print('{0} is {1}'.format('Country', 'India'))
print('{1} {2} {0}'.format('Country', 'India', 'is'))
print('Our {key} is {data}'.format(key='country', data='india'))
print('{0} {company}'.format('Multiple_wishes', company='dream'))