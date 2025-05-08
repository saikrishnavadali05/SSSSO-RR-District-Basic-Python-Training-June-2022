NumList1 = [10, 20, 30]
NumList2 = [5, 2, 3]
res_list = []
Mul_list=[]

  
def calculate_add(NumList1,Numlist2):
  for i in range(0, len(NumList1)):
    res_list.append(NumList1[i] + NumList2[i])

calculate_add(NumList1,NumList2)
print(str(res_list))

def calculate_mul(NumList1,Numlist2):
  for i in range(0, len(NumList1)):
    Mul_list.append(NumList1[i] * NumList2[i])

calculate_mul(NumList1,NumList2)
print(str(Mul_list))

