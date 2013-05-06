from collections import Counter
import math
def freqCount(inputArray):
    outData = Counter()
    for currentData in inputArray:
        outData[currentData] += 1
    return outData

def feedDistance(inputDict):
    squareDist = 0 
    for key in inputDict:
        squareDist += math.pow(inputDict[key], 2)
    return math.sqrt(squareDist)