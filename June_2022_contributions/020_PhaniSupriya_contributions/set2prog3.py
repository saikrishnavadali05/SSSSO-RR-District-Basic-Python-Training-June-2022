
#factorial and n+nn+nnn
num = int(input("enter any number: "))
def factorial(n):
   return 1 if(n==1 or n==0) else n * factorial(n-1);
print("factorial of",num,"is",num,'! =',factorial(num))


def compute(num):
   n1=int("%s" %num)
   n2=int("%s%s" %(num,num))
   n3=int("%s%s%s" %(num,num,num))
   Res= n1+n2+n3
   return Res;
print("Output of n+nn+nnn is:",compute(num))

