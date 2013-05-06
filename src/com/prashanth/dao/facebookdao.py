from com.prashanth.db.Facebookdb import feedDataStore, FBUserData, \
    feedProcessedStore, dataIndexStore
import json
import logging

def storeUserData(currentUserData):
    try:
        currentFBUserHandle = FBUserData()
        currentFBUserHandle.id = currentUserData['id']
        currentFBUserHandle.name = currentUserData['name']
        currentFBUserHandle.first_name = currentUserData['first_name']
        currentFBUserHandle.last_name = currentUserData['last_name']
        currentFBUserHandle.link = currentUserData['link']
        currentFBUserHandle.username = currentUserData['username']
        currentFBUserHandle.gender = currentUserData['gender']
        currentFBUserHandle.timezone = currentUserData['timezone']
        currentFBUserHandle.locale = currentUserData['locale']
        currentFBUserHandle.verified = currentUserData['verified']
        currentFBUserHandle.updated_time = currentUserData['updated_time']
        currentFBUserHandle.access_token = currentUserData['access_token']
        currentFBUserHandle.expires = currentUserData['expires']
        currentFBUserHandle.put()        
    except Exception, e:
        logging.error(e)
        logging.error(currentUserData)

def storeCurrentFacebookFeed(currentFBFeed):
    try:
        feedStoreHandle = feedDataStore()
        feedStoreHandle.feed_id = currentFBFeed['id']
        feedStoreHandle.feed_type = currentFBFeed['type']
        feedStoreHandle.feed_message = currentFBFeed['message']
        feedStoreHandle.feed_from_id = currentFBFeed['from']['id']
        feedStoreHandle.feed_from_name = currentFBFeed['from']['name']
        feedStoreHandle.feed_created_time = currentFBFeed['created_time']
        feedStoreHandle.feed_updated_time = currentFBFeed['updated_time']
        feedStoreHandle.feed_comments = 1
        feedStoreHandle.feed_likes = 1
        feedStoreHandle.put()
    except Exception, e:
        logging.error(e)
        logging.error(currentFBFeed)

def storeTotalFacebookFeed(totalCurrentProfileData):
    for currentFBFeed in totalCurrentProfileData['data']:
        storeCurrentFacebookFeed(currentFBFeed)

def storeProcessedFeed(processedData):
    try:
        processedStoreHandle = feedProcessedStore()
        processedStoreHandle.feed_id = processedData['id']
        processedStoreHandle.feed_processed_message = json.dumps(processedData['message'])
        processedStoreHandle.feed_distance = processedData['distance']
        processedStoreHandle.put()
    except Exception, e:
        logging.error(e)
        logging.error(processedData)
        
def storeIndexData(indexdata):
    try:
        dataIndexHandle = dataIndexStore()
        dataIndexHandle.indexWord = indexdata['word']
        dataIndexHandle.total_feed_list = indexdata['feedlist']
        dataIndexHandle.put()
    except Exception, e:
        logging.error(e)
        logging.error(indexdata)
    
        
def gettotalFacebookFeed():
    return feedDataStore.all()
