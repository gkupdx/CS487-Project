#dataGen.py
# Djernaes/Ku
# CS487 "Scalable" Wisconsin Benchmark Implementation Project

# note: need stringsGen.py as a dependency
import numpy as np
import pandas as pd
import string
from stringsGen import string_u

# generate 'maxtuples' per given input 
def dataGenerator(maxtuples):
    #Uniques
    unique_1 = np.arange(0,maxtuples)
    unique_3 = np.arange(0,maxtuples)
    unique2 = np.arange(0,maxtuples) #  unique2 (id numbers 0 to size-1)
    unique1 = np.random.permutation(unique_1) # unique1 is a random ordering of numbers from 0 to size-1
    unique3 = np.random.permutation(unique_3) # randomized unique1
    #Raw integers
    two = unique1[0:] % 2
    four = unique1 % 4
    ten = unique1 % 10
    twenty = unique1 % 20
    #Percentages
    onePercent = unique1 % 100
    tenPercent = unique1 % 10
    twentyPercent = unique1 % 5
    fiftyPercent = unique1 % 2
    evenOnePercent = onePercent * 2
    oddOnePercent = (onePercent * 2) + 1

    stringu1 = np.chararray(maxtuples)    # allocate char array
    stringu1 = np.dtype('U52')     # set size to allow for 52 char string
    stringu2 = np.chararray(maxtuples)    # allocate char array
    stringu2 = np.dtype('U52')     # set size to allow for 52 char string
    string4 = np.chararray(maxtuples)
    string4 = np.dtype('U52')


    # see stringsGen.py for function def
    # capture the return value as 3 separate attributes
    stringu1, stringu2, string4 = string_u(maxtuples)
    
    #assemble attributes for dataframe export
    df2 = pd.DataFrame(list(zip(unique1, unique2, two, four, ten, twenty, onePercent, tenPercent, twentyPercent, 
        fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4)), 
        columns = ['unique1', 'unique2', 'two', 'four', 'ten', 'twenty', 'onePercent', 'tenPercent', 'twentyPercent',
        'fiftyPercent', 'unique3', 'evenOnePercent', 'oddOnePercent', 'stringu1', 'stringu2','string4'])

    return df2   


"""  main()  """ 
# NOTE: maxtuples must be divisible by 4, otherwise program 
# will error. This is due to string4's attribute structure.
# 10K, 100K, 1M will all work... (1M might take a while to complete.) 
maxtuples = 104
df = dataGenerator(maxtuples) 

""" test output, print to screen """
#print(testTup)

# export to CSV file
# Rename output file with desired title 
""" uncomment the next line to output to file """
df.to_csv('hundred.csv', index = True)
print("file complete")
