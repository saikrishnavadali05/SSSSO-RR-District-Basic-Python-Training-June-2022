def add_Number(n1,n2,n3,n4):
    numbers = [n1,n2,n3,n4]
    eve_list = []
    for num in numbers:
      if (num%2 == 0):
            eve_list.append(num)
            #print(eve_list)
    
    #if len(eve_list)  == 0:
     #       print("No even numbers enetered")
      #      quit()
    return sum(eve_list)
