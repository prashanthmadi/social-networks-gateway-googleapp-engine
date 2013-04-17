from google.appengine.ext import db


class FBUserData(db.Model):
    accesstoken = db.StringProperty()
    name = db.StringProperty() 
    email = db.StringProperty()
