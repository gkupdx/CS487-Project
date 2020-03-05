#stringsGen
import numpy as np
import pandas as pd
import string
import random

# part of the StringuX attributes. The string attribute is completed in 
# two steps. first generate the random part of the string (randomString())
# then tack on the string of Xs to the end (fullString()). 
def randomString(stringLength = 7):
    # generate a string of a fixed length
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def fullString():
    # append 45 Xs to the string. Split into to 
    trailingX ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # 45 Xs
    return "{}{}".format(randomString(7),trailingX)             # concatenate output

def stringFour(maxtuples):
    #STRING4 DATA
    string4 = np.chararray(0)
    string4 = np.dtype('U52')

    # maxtuples must be divisible by 4 or the output will error, 
    # since the arrays will not be of equal lengths, otherwise.  
    N = maxtuples%4
    if(N == 0):
        string4 = ("AAAAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        return string4
    if(N == 1): 
        string4 = ("HHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        return string4
    if(N == 2):
        string4 = ("OOOOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        return string4
    if(N == 3):
        string4 = ("VVVVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        return string4
    else:    
        return "error"

# generate strings attributes stringu1 and stringu2
def string_u(maxtuples):            
    stringu1 = np.chararray(0)     # allocate char array
    stringu1 = np.dtype('U52')     # set size to allow for 52 char string
    stringu2 = np.chararray(0)     
    stringu2 = np.dtype('U52')     
    string4 = np.chararray(0)
    string4 = np.dtype('U52')

    milestones = [15, 30, 45, 60, 75, 90, 100] # values to track completeness
    N = maxtuples
    for i in range(maxtuples):          # fill the array with the strings 
        stringu1 = np.append(stringu1, fullString())  # to size maxtuples
        stringu2 = np.append(stringu2, fullString())  # to size maxtuples
        string4 = np.append(string4, stringFour(i))   # fill array with one of 4 outputs

        percentage_complete = (100.0 * (i+1) / N)   # this part tracks the work
        while len(milestones) > 0 and percentage_complete >= milestones[0]:
            print("{}% complete".format(milestones[0]))
            #remove that milestone from the list
            milestones = milestones[1:]
    return stringu1, stringu2, string4



