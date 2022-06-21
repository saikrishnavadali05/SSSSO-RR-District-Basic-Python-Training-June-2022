#dictionary
student_details={
    "NAME":"DAGGULA LAXMI CHAYA DEVI",
    "GENDER":"FEMALE",
    "CLASS":"BTECH 3RD YEAR",
    "BRANCH":"CSE"
}
#printing Entire dictinary
print(student_details)
#printing each key value pair separatly
for key,value in student_details.items():
    print(key,":",value)
#printing only values
for key,value in student_details.items():
    print(value)
#method2
print(student_details["NAME"])
print(student_details["GENDER"])
print(student_details["CLASS"])
print(student_details["BRANCH"])
