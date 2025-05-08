'''Write a program to print this pattern (hint : use \t and \n wherever required).

         *
     * python *
   * is  *  a    *
 * good  * programming * language *
* to * learn * for * beginners *
'''
li=['python','is ',' a   ','good','programming','language','to','learn','for','beginners']
def inserterr(l):
    if l==[]:
        return " *"
    else:
        a=""
        for i in l:
            a+="* "
            a+=i
        a+="*"
        return a
            
j=0
while j<=len(li):
    print(" "*(len(li)-j),inserterr(li[:j]))
    li=li[j:]
    j+=1
print()
