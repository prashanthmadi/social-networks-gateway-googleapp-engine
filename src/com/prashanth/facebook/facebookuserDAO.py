from com.prashanth.db.Facebookdb import FBUserData

def storeFBUserData(params):
    fbuserdata = FBUserData()
    fbuserdata.accesstoken = params['']
    fbuserdata.name = params['']
    fbuserdata.email = params['']
    fbuserdata.put()
