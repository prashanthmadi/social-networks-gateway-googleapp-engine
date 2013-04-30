from com.prashanth.db.Facebookdb import feedDataStore, FBUserData
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
    
    
