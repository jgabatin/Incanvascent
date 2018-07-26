from google.appengine.ext import ndb

class Visitor(ndb.Model):
    name = ndb.StringProperty(required=False)
    email = ndb.StringProperty(required=False)
    id = ndb.StringProperty(required=False)
    favorite_songs = ndb.StringProperty(repeated=False)

class Song(ndb.Model):
    name = ndb.StringProperty(required=False)
    artist = ndb.StringProperty(required=False)
    note_progression = ndb.StringProperty(repeated=True)
    type = ndb.IntegerProperty(required=False)
    image = ndb.BlobProperty()


    def serialize( self ):
        return {
            'name' : self.name,
            'artist' : self.artist,
            'note_progression' : self.note_progression,
            'type' : self.type,
            'image' : self.image,
        }
