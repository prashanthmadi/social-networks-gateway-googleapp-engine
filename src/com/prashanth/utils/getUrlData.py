from com.prashanth.constants import SocialConstants
from google.appengine.api import urlfetch
import logging
import re
import urllib

def extractDataFromUrl(url):
    try:
        ufile = urllib.urlopen(url)
        if ufile.info().gettype() == 'text/plain':
            return ufile.read()
    except IOError:
        return 'problem reading url:', url

def extractFacebookLongLivedTokenData(shrtlivedtoken):
    longtokenurl = "https://graph.facebook.com/oauth/access_token"
    inputfields = {
    "grant_type" : "fb_exchange_token",
    "client_id" : SocialConstants.FACEBOOK_APP_ID,
    "client_secret" : SocialConstants.FACEBOOK_APP_SECRET,
    "fb_exchange_token" : shrtlivedtoken
    }
    
    result = makePostRequest(longtokenurl, inputfields);
    logging.error(result.__str__)
    splittedresult = re.split(r'&', result.__str__)
    if len(splittedresult) > 1 :
        facebookLongLivedTokenData = {}
        facebookLongLivedTokenData['longliveaccesstoken'] = splittedresult[0]
        facebookLongLivedTokenData['expires'] = splittedresult[1]
        return facebookLongLivedTokenData
    else:
        return None

def makePostRequest(urlValue, inputfields):
    form_data = urllib.urlencode(inputfields)
    try:
        result = urlfetch.fetch(url=urlValue,
                        payload=form_data,
                        method=urlfetch.POST,
                        headers={'Content-Type': 'application/x-www-form-urlencoded'})
        return result
    except urlfetch.Error, e:
        logging.error(e)
        return None
    
def makeGetRequest(urlValue):
    try:
        result = urlfetch.fetch(urlValue)
        return result 
    except urlfetch.Error, e:
        logging.error(e)
        return None

def extractFacebookProfileData():
    
    FacebookData = {}
    
    
    return FacebookData
    
