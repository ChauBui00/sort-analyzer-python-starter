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
# print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")


# startTime = time.time()
# def selectionSort(anArray):
#     for fillSlot in range(len(anArray) - 1):
#         # Find position of minimum element
#         minPosition = fillSlot
#         for i in range(fillSlot + 1, len(anArray)):
#             if anArray[i] < anArray[minPosition]:
#                 minPosition = i
#         # Swap fillSot and the minPosition
#         anArray[fillSlot], anArray[minPosition] = anArray[minPosition], anArray[fillSlot]
# selectionSort(reversedData)
# endTime = time.time()
# total_Time= endTime - startTime
# print(f"Selection Sort Random Data: {total_Time} seconds")

result = (2.4880409240722656 +  2.4667487144470215 + 2.487828016281128)/3

print(f"\nThe average time is: {result} seconds")