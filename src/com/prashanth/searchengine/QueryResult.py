from com.prashanth.db.Facebookdb import dataIndexStore, feedProcessedStore, \
    feedDataStore
from com.prashanth.searchengine.preprocess.PreProcesser import \
    preProcessProcedure
import logging

def queryPreProcess(query):
    return preProcessProcedure(query)
    
def getDocsWithWord(word):
    query = dataIndexStore.all()
    query.filter("indexWord =", word)
    result =query.get()
    if result is None:
        return None
    else:
        return result.total_feed_list

def gettotalDocsForSentense(totalqueryWords):
    totalDocsList = [] 
    for eachWord in totalqueryWords:
        currentWordDocs = getDocsWithWord(eachWord)
        if currentWordDocs is not None:
            totalDocsList.extend(currentWordDocs)
    return totalDocsList
       
def queryProcess(query):
    totalqueryWords = dict(queryPreProcess(query))
    totalDocsList = gettotalDocsForSentense(totalqueryWords)
    if len(totalDocsList) > 0:
        totaldocswithProcessedDataList = getFeedsWithDocIds(totalDocsList)
        totalOriginalDocsWithDataList =getOriginalFeedWithDocIds(totalDocsList)
        return totalOriginalDocsWithDataList
    else:
        return None
#    for currentDocData in totaldocswithDataList:
#        currentDocDataFeed = currentDocData.feed_processed_message
#        currentDocDataDistance =currentDocData.feed_distance
#        logging.debug(currentDocData)
    
        

def getFeedWithDocId(currentDocId):
    query = feedProcessedStore.all()
    query.filter("feed_id =", currentDocId)
    return query.get()


def getFeedsWithDocIds(totalDocsList):
    totalDocListWithProcessedFeed = [] 
    for currentDocId in totalDocsList:
        currentDocData = getFeedWithDocId(currentDocId)
        if currentDocData is not None:
            totalDocListWithProcessedFeed.append(currentDocData)
    return totalDocListWithProcessedFeed

def getOriginalFeedWithDocId(currentDocId):
    query = feedDataStore.all()
    query.filter("feed_id =", currentDocId)
    return query.get()

def getOriginalFeedWithDocIds(totalDocsList):
    totalDocListWithFeed = [] 
    for currentDocId in totalDocsList:
        currentDocData = getOriginalFeedWithDocId(currentDocId)
        if currentDocData is not None:
            totalDocListWithFeed.append(currentDocData)
    return totalDocListWithFeed


