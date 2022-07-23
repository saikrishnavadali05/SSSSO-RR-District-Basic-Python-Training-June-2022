"""
20.Write a script that accepts a comma separated list of characters 
(and words) and prints an underscore _ separated list of characters (and words) 
in the sorted order as shown below :
Input: b,c,a,d,a,e,b,f 
Output: a_a_b_b_c_d_e_f. 
Next apply this logic to words. Input : om sri sai ram. Output : om_ram_sai_sri

"""
Input_from_user = input("Enter the letters separated by a comma:")
b = "_".join(sorted(Input_from_user.replace(",","")))
print(b)

Input_from_user1 = input("Enter the words:")
c = "_".join(sorted(Input_from_user1.split()))
print(c)
