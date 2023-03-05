# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:36:20 2022

@author: User
"""
import pandas as pd
import numpy as np


def split(word):
    return [char for char in word]

def convert(s):
    str1 = ""
    return(str1.join(s))
#κάνω ένα διάνυσμα σε string

#Remove lines starting with #
with open("C:/Users/User/OneDrive - University of Patras/Επιφάνεια εργασίας/converter/unsat5", "r") as input:
    with open("C:/Users/User/OneDrive - University of Patras/Επιφάνεια εργασίας/converter/new_unsat5.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if substring contain in a line then don't write it
            if "#" not in line.strip("\n"):
                output.write(line)

#The conversion script
#where x in the line bellow should be the file in form eg. 'example.txt'

test1 = open("C:/Users/User/OneDrive - University of Patras/Επιφάνεια εργασίας/converter/new_unsat5.txt" , "r")
      

df2 = pd.read_csv(test1,header=None)
    
index = df2.index
number_of_rows = len(index) 

new=[]
for i in range(0,number_of_rows ):
    word=df2.iloc[i , 0]
    obj = split(word)
    lst = list(obj)
    new.append(lst)
      
     
cnf=[]
for i in range(len(new)):
    for j in range(len(lst)):
        if new[i][j]=='0':
            cnf.append(-(j+1))
            cnf.append(' ')
        elif new[i][j]=='1': 
            cnf.append(j+1)
            cnf.append(' ')
        else:
            cnf.append('')
    cnf.append(0)
    cnf.append(' ')

my_array = np.array(cnf)

a=str(len(lst))
b=str(len(new))



#New file creation, give name in line bellow

f=open('C:/Users/User/OneDrive - University of Patras/Επιφάνεια εργασίας/converter/dimac_unsat5.txt', 'w')
f.write("p cnf " + a + " " + b +"\n")
f.close()

#Give name again here
with open('C:/Users/User/OneDrive - University of Patras/Επιφάνεια εργασίας/converter/dimac_unsat5.txt', 'a') as g:
    for i in range(len(my_array)):
        if my_array[i]=='0':
            g.write(str(my_array[i]))
            g.write('\n')
        else:
            g.write(str(my_array[i]))
            
g.close()
      
 