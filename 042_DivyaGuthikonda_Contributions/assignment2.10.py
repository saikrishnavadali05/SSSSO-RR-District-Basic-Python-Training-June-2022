#Write a script to print all the rows of a csv file. (hint : use pandas library).
import csv
with open("user.csv",newline='')as csvfile:
    data=csv.reader(csvfile,delimiter=' ',quotechar='|')
    for row in data:
        print(','.join(row))
#output
'''
Username_____Identifier___Onetimepwd______Recoverycode_First_name__Last_name__Department___Location
booker12_____9012_________12se74__________rb9012_______Rachel______Booker_____Sales________Manchester
grey07_______2070_________04ap67__________lg2070_______Laura_______Grey_______Depot________London
johnson81____4081_________30no86__________cj4081_______Craig_______Johnson____Depot________London
jenkins46____9346_________14ju73__________mj9346_______Mary________Jenkins____Engineering__Manchester
smith79______5079_________09ja61__________js5079_______Jamie_______Smith______Engineering__Manchester
'''