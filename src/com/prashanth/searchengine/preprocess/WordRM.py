from com.prashanth.CurrentPath import constantFilesPathDir
from com.prashanth.utils.getData import fileRead

def stopWords():
    fileData = fileRead(constantFilesPathDir(), "StopWords")
    totalStopWords = fileData.splitlines()
    return totalStopWords

def commonWords():
    fileData = fileRead(constantFilesPathDir(), "CommonWords")
    totalCommonWords = fileData.splitlines()
    return totalCommonWords

def stopWordRemoval(currentData, totalstopWords):
    outputData=""
    splittedCurrentData= currentData.split(" ")
    for currentinSplit in splittedCurrentData:
        counter=False
        for stopWord in totalstopWords:
            if currentinSplit == stopWord:
                counter =True
        if counter == False:
            outputData+=currentinSplit
        outputData+=" "             
    return outputData

def commonWordRemoval(currentData, totalcommonWords):
    outputData=""
    splittedCurrentData= currentData.split(" ")
    for currentinSplit in splittedCurrentData:
        counter=False
        for commonWord in totalcommonWords:
            if currentinSplit == commonWord:
                counter = True
        if counter == False:
            outputData+=currentinSplit
        outputData+=" "
    return outputData

def removestopWord(totalData):
    contentWithoutStop = ""
    totalStopWords = stopWords()
    for currentLine in totalData.splitlines():
        contentWithoutStop += stopWordRemoval(currentLine, totalStopWords)
    return contentWithoutStop

def removecommonWord(totalData):
    contentWithoutCommon = ""
    totalCommonWords = commonWords()
    for currentLine in totalData.splitlines():
        contentWithoutCommon += commonWordRemoval(currentLine, totalCommonWords)
    return contentWithoutCommon
