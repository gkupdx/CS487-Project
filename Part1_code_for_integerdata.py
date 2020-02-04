# Grady Ku
# CS487 "Scalable" Wisconsin Benchmark Implementation Project
import numpy as np
import random
import csv

# Only need to generate 50 tuples per relation for the sample data
def IntegerGenerator(i, index, unique1Value):
    #Uniques
    list2 = np.arange(0, 50, 1) # list2 for unique2 (no deletion of elements done)
    array2 = list2.tolist() # store np.list2 as a regular list
    unique2 = array2[i] #DECLARED KEY

    unique1 = unique1Value
    unique3 = unique1

    #Raw integers
    two = unique1 % 2
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

    #To export tuples into a .csv file
    with open('integer_data3.csv', 'a') as integer_data:
        to_csv = csv.writer(integer_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        to_csv.writerow([unique1, unique2, two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent])

    ### TESTED ATTRIBUTES: (unique1, unique2, unique3, ten, onePercent, & oddOnePercent) ###

# FUNCTION CALL
n = 0 # counter to keep track of position in list2
list1 = np.arange(0, 50, 1)
array1 = list1.tolist() # store np.list1 as a regular list
list_size = len(array1) # need to keep track of how many items are in list at a given point in the while loop
index = random.randrange(list_size) # pick an arbitrary index value from the size available
while n < 50:
  list_size = len(array1) # keeps track of how many items are in list at a given point of time
  index = random.randrange(list_size) # pick an arbitrary index value from the size available
  unique1Value = array1[index]
  IntegerGenerator(n, index, unique1Value)
  n = n + 1; # increment counter by 1 to move to the next element for unique2
  array1.pop(index) # remove the indexed element from list because we don't want to pick it again


