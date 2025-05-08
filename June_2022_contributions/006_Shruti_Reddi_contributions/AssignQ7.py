#Write a program to print this pattern (hint : use \t and \n wherever required).

   #      *
   #  * python *
  # * is  *  a    *
 #* good  * programming * language *
#* to * learn * for * beginners *

str_1="*"
new_str=str_1.center(1,)
print(new_str)

str_2="python"
new_str2=str_2.center(8, '*')
print(new_str2)

str_3="is * a"
new_str3=str_3.center(10, '*')
print(new_str3)

str_4="good * programming * language"
new_str4=str_4.center(24, '*')
print(new_str4)

str_5="to * learn * for * beginners"
new_str5=str_5.center(8, '*')
print(new_str5)
