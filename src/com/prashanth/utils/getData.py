from google.appengine.api import urlfetch
import logging
import os
import urllib

def extractDataFromUrl(url):
    try:
        ufile = urllib.urlopen(url)
        if ufile.info().gettype() == 'text/plain':
            return ufile.read()
    except IOError:
        return 'problem reading url:', url


def makePostRequest(urlValue, inputfields):
    form_data = urllib.urlencode(inputfields)
    try:
        result = urlfetch.fetch(url=urlValue,
                        payload=form_data,
                        method=urlfetch.POST,
                        headers={'Content-Type': 'application/x-www-form-urlencoded'})
        if result.status_code == 200:
            return result.content
        else:
            return None
    except urlfetch.Error, e:
        logging.error(e)
        return None
    
def makeGetRequest(urlValue):
    try:
        result = urlfetch.fetch(urlValue)
        return result.content 
    except urlfetch.Error, e:
        logging.error(e)
        return None

def fileRead(directory, fileName):
    path = os.path.join(directory, fileName)
    return file(path, 'rb').read()


    
