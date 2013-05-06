from com.prashanth.constants import SocialConstants
from com.prashanth.dao.facebookdao import storeTotalFacebookFeed, storeUserData
from com.prashanth.utils.getData import makePostRequest, makeGetRequest
from urlparse import parse_qsl
import json
import logging
import re
#
# facebookCurrentProfile(longaccestokendetails['access_token'])
#
# facebookPageFeedWithNext(longaccestokendetails['access_token'], "usaa", "/feed", 40)
#
#
#
def facebookMain(shrtlivedtoken):
    longaccestokendetails = extractFacebookLongLivedTokenData(shrtlivedtoken)
    totalCurrentProfileData = {}
    if longaccestokendetails is not None:
        if longaccestokendetails.has_key("access_token"):
            totalCurrentProfileData = facebookCurrentProfile(longaccestokendetails['access_token'])
            totalCurrentProfileData['access_token'] = longaccestokendetails['access_token']
            if longaccestokendetails.has_key("expires"):
                totalCurrentProfileData['expires'] = longaccestokendetails['expires']
            storeUserData(totalCurrentProfileData)
            return "success"
        else:
            logging.error("doesnt contain access token in facebookMain")    
            return None    
    else:
        logging.error("doesnt contain access token in facebookMain") 
        return None
    

def extractFacebookLongLivedTokenData(shrtlivedtoken):
    longtokenurl = "https://graph.facebook.com/oauth/access_token"
    inputfields = {
    "grant_type" : "fb_exchange_token",
    "client_id" : SocialConstants.FACEBOOK_APP_ID,
    "client_secret" : SocialConstants.FACEBOOK_APP_SECRET,
    "fb_exchange_token" : shrtlivedtoken
    }
    result = makePostRequest(longtokenurl, inputfields);
    if result is not None:
        splittedresult = re.split(r'&', result)
        if len(splittedresult) > 1 :
            facebookLongLivedTokenData = {}
            for currentparam in splittedresult:
                splittedcurrentparam = re.split(r'=', currentparam)
                if len(splittedcurrentparam) > 1:                
                    facebookLongLivedTokenData[splittedcurrentparam[0]] = splittedcurrentparam[1]
            return facebookLongLivedTokenData
        else:
            logging.error("error in extracting facebook long lived token")
            return None
    else:
        logging.error("error in extracting facebook long lived token")    
        return None

def facebookCurrentProfile(accesstoken):
    if accesstoken is not None:
        params = {'access_token' : accesstoken}
        totalCurrentProfileData = facebookGraphRequest("me", params)
        return totalCurrentProfileData

def facebookFriendsList(accesstoken):
    if accesstoken is not None:
        params = {'access_token' : accesstoken, 'fields' : 'friends'}
        totalFriendsList = facebookGraphRequest("me", params)
        return totalFriendsList

def facebookPageFeed(pagehandle, pageextraContent, params):       
        fbPageFeed = facebookGraphRequest(pagehandle + pageextraContent, params)
        return fbPageFeed

def facebookPageFeedWithNext(accesstoken, pagehandle, pageextraContent, totalNoOfCalls):
    totalCurrentPageFeed = {}
    params = {'access_token' : accesstoken}
    totalCurrentPageFeed = facebookPageFeed(pagehandle, pageextraContent, params)
    storeTotalFacebookFeed(totalCurrentPageFeed)
    params['limit'] = "25"
    for currentCounter in range(totalNoOfCalls):
        logging.debug("graph request for feed count-- " + str(currentCounter))
        if(totalCurrentPageFeed.has_key('paging')):
            if(totalCurrentPageFeed['paging'].has_key('next')):  
                parsedNxtUrl = parse_qsl(totalCurrentPageFeed['paging']['next'])
                tempurlparams = dict(parsedNxtUrl)
                if tempurlparams.has_key('until') :
                    params['until'] = tempurlparams['until']
                    totalCurrentPageFeed = facebookPageFeed(pagehandle , pageextraContent, params)
                    storeTotalFacebookFeed(totalCurrentPageFeed)
    return totalCurrentPageFeed

def facebookGraphRequest(requestmethod, params):
    graphrequest = SocialConstants.FACEBOOK_GRAPH_URL + requestmethod + "?method=GET&format=json"
    if len(params) > 0 :
        paramdata = ""
        for currentkey in params.keys():
            paramdata += "&" + currentkey + "=" + params[currentkey]
        graphrequest += paramdata
    logging.debug("graph request -- " + graphrequest)
    return json.loads(makeGetRequest(graphrequest))
