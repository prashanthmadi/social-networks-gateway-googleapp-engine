from com.prashanth.dao.facebookdao import gettotalFacebookFeed, \
    storeProcessedFeed, storeIndexData
from com.prashanth.searchengine.preprocess.FrequencyCount import freqCount, \
    feedDistance
from com.prashanth.searchengine.preprocess.Tokenizer import tokenizerSimple
from com.prashanth.searchengine.preprocess.WordRM import removecommonWord, \
    removestopWord
from com.prashanth.searchengine.preprocess.porterstemmer import \
    porterOnTotalLine
import re
    
    
def preProcessProcedure(inputData):
    inputData = inputData.lower()  # converting to lower case
    inputData = inputData.replace(r'\n', " ")  # removing new lines
    inputData = re.sub(r'[^\w\d\s]+', ' ', inputData)  # removing punctuations and junk
    inputData = removestopWord(inputData)  # removing stop words
    inputData = removecommonWord(inputData)  # removing common words
    inputData = re.sub(r'[\s]+', ' ', inputData)  # removing extra spaces
    inputData = tokenizerSimple(inputData)  # tokenize data
    inputData = porterOnTotalLine(inputData)  # apply porter stemmer to get root words
    outData = freqCount(inputData)  # get the frequency count 
    return outData


def preProcessStore():
    totalFeeds = gettotalFacebookFeed()
    bigDataIndexDict = {}
    for currentFeedData in totalFeeds:
        processedData = {}
        processedContent = preProcessProcedure(currentFeedData.feed_message)
        ProcessedRegDict = dict(processedContent);
        
        # store feeds with word into dict to build a index datastore
        for currentWord in ProcessedRegDict:
            wordFeedsList = []
            if bigDataIndexDict.has_key(currentWord):
                wordFeedsList = bigDataIndexDict[currentWord]
            wordFeedsList.append(currentFeedData.feed_id)
            bigDataIndexDict[currentWord] = wordFeedsList
            
        # store pre processed data into datastore
        if sum(processedContent.values()) > 0 : 
            processedData['message'] = ProcessedRegDict
            processedData['id'] = currentFeedData.feed_id
            processedData['distance'] = feedDistance(ProcessedRegDict)
            storeProcessedFeed(processedData)
    
    # storing index data
    for currentWord in bigDataIndexDict:
        indexData = {}
        indexData['word'] = currentWord
        indexData['feedlist'] = bigDataIndexDict[currentWord]
        storeIndexData(indexData)
    return "Pre Process Completed"
