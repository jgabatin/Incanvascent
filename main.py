import webapp2
import os
import jinja2
import json
from google.appengine.ext import ndb
from google.appengine.api import urlfetch


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader( os.path.dirname(__file__) )
)

class Main_Page(webapp2.RequestHandler):
    def get( self ):
        template = jinja_current_directory.get_template("templates/main_page.html")
        self.response.write( template.render() )




class Piano_Keyboard_Handler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template("templates/piano_page.html")
        self.response.write( template.render() )

class  DataEndpoint(webapp2.RequestHandler):
    def post(self):
        print("post")
        requestObject = json.loads(self.request.body)
        userdata = requestObject.get('data')
        myuser= UserData()
        print(list(userdata.keys()))
        myuser.id = userdata.get('id')
        myuser.fullname = userdata.get('fullname')
        myuser.givenname = userdata.get('givenname')
        myuser.imageurl = userdata.get('imageurl')
        myuser.email = userdata.get('email')
        myuser.put()


# #objects for database
class Song(ndb.Model):
    notes_progression = ndb.StringProperty(repeated=True)


class UserData(ndb.Model):
    id = ndb.StringProperty(required=False)
    fullname = ndb.StringProperty(required=False)
    givenname = ndb.StringProperty(required=False)
    imageurl = ndb.StringProperty(required=False)
    email = ndb.StringProperty(required=False)
    # past_songs = ndb.StringProperty(repeated=False)





#route mapping
app = webapp2.WSGIApplication([
    ('/', Main_Page),
    ('/keyboard', Piano_Keyboard_Handler),
    ('/data', DataEndpoint)
], debug=True)
