from google.appengine.ext import db


class FBUserData(db.Model):
    id = db.StringProperty()
    name = db.StringProperty()
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    link = db.StringProperty()
    username = db.StringProperty()
    gender = db.StringProperty()
    timezone = db.IntegerProperty()
    locale = db.StringProperty()
    verified = db.BooleanProperty()
    updated_time = db.StringProperty()
    access_token = db.StringProperty()
    expires = db.StringProperty()

class feedDataStore(db.Model):
    feed_from_name = db.StringProperty()
    feed_from_id = db.StringProperty()
    feed_type = db.StringProperty()
    feed_id = db.StringProperty()
    feed_message = db.TextProperty()
    feed_likes = db.IntegerProperty()
    feed_comments = db.IntegerProperty()
    feed_created_time = db.StringProperty()
    feed_updated_time = db.StringProperty()
    
class feedProcessedStore(db.Model):
    feed_id = db.StringProperty()
    feed_processed_message = db.StringProperty()
    feed_distance =db.FloatProperty()
    
class dataIndexStore(db.Model):
    indexWord = db.StringProperty()
    total_feed_list = db.StringListProperty()