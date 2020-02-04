# Djernaes/Ku
# CS487P Project Part 1
# string generation code 
# for Wisconsin Benchmark Test

#prj part1
import numpy as np
import pandas as pd
from sklearn.utils.extmath import cartesian
import csv


# for stringu1, stringu2 
# these are the building blocks the 
# strings are made of  
a = [chr(x) for x in range(ord('A'), ord('W'))] 
b ="XXXXXXXXXXXXXXXXXXXXXXXXX"
c = [chr(x) for x in range(ord('A'), ord('W'))] 
d ="XXXXXXXXXXXXXXXXXXXXXXXX" 
e = [chr(x) for x in range(ord('A'), ord('W'))] 

# to compute all possible permutations 
result1 = cartesian([a,c,e])
"""produces strings collection of [A, A, A], [A, A, B], ...,[B, A, C],..., etc."""

#convert string datatypes to allow for 52 character strings
result1 = result1.astype('U52')
# adding first set of 24 x
"""result is A, XXXX...XXXX, A, A"""
result2 = np.insert(result1,1,b, axis=1) 
# adding second set of x
""" result is A XXX...XXX A XXX...XXX A """
result3 = np.insert(res2,3,d, axis=1) # adding second set of x
""" random shuffle used for Stringu2"""
resShuffle = np.random.shuffle(result3) 
#print(np.shape(resC))

#READ file output back into strip the comma separations
#to generate 52 character strings for stringu1
df = pd.read_csv('temp.csv')
res = df[list('01234')].astype(str).sum(1)  
res.to_csv('stringu1.csv')

#generate the random set for stringu2.
resRand = result3
resRand.to_csv('stringu2.csv')


#STRING4 DATA
string4 = np.chararray(120)
string4 = string4.astype('U52')
#print(np.shape(string4)) //size check
#create a matching sized set of TENKTUP by appending the cycle of four, 2662 times 
for i in range(2662):
  string4 = np.append(string4,"AAAAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
  string4 = np.append(string4,"HHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
  string4 = np.append(string4,"OOOOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
  string4 = np.append(string4,"VVVVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

#print(string4)

#convert to pandas dataframe for ease of CSV file creation
string4 = pd.DataFrame(string4)
string4.to_csv('string_4.csv')

       



