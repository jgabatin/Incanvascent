from google.appengine.ext import ndb

class Visitor(ndb.Model):
    name = ndb.StringProperty(required=False)
    email = ndb.StringProperty(required=False)
    id = ndb.StringProperty(required=False)
    page_view_count = ndb.IntegerProperty(required=True)
    past_songs = ndb.StringProperty(repeated=False)
