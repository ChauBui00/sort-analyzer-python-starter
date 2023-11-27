# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

startTime = time.time()
def bubbleSort(anArray):
    for numCompare in range(len(anArray)-1, 0, -1):
        for i in range(numCompare):
           
            firstNum = anArray[i]
            secNum = anArray[i+1]


            if firstNum > secNum:
                anArray[i] = secNum
                anArray[i + 1] = firstNum
bubbleSort(randomData)
endTime = time.time()
print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

import math
result = (4.811554431915283 + 4.717653512954712 + 5.5849692821502686)/3
print(result)