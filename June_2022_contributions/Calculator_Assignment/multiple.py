def multi_Number(n1,n2,n3,n4):
    numbers = [n1,n2,n3,n4]
    eve_list = []
    for num in numbers:
      if (num%2 == 0):
            eve_list.append(num)
            #print(eve_list)
    result =1
    for x in eve_list:
        result = result * x
  
    return result