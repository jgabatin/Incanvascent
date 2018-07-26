import webapp2
import os
import jinja2
import json
import math
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
from models import Visitor, Song


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader( os.path.dirname(__file__) ),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# Sign In stuff
class Main_Page( webapp2.RequestHandler ):
    def get( self ):

        current_user = users.get_current_user()
        if not current_user:
            start_template = jinja_current_directory.get_template("templates/main_page.html")
            jinja_values = {
            'signin_page_url' : users.create_login_url('/'),
            }
            self.response.write( start_template.render( jinja_values ))
        else:
            #datastore
            current_key = ndb.Key('Visitor', current_user.user_id() )
            current_visitor = current_key.get()
            if not current_visitor:
                current_visitor = Visitor(key=current_key, name=current_user.nickname(), email=current_user.email(), id=current_user.user_id() )
            current_visitor.put()

            #display
            with_user_template = jinja_current_directory.get_template("templates/home_page.html")
            jinja_values = {
            'name' : current_user.nickname(),
            'user_addr' : current_user.email(),
            'user_id' : current_user.user_id(),
            'signout_page_url' : users.create_logout_url('/'),
            }
            self.response.write( with_user_template.render( jinja_values ))


class Tutorial_Page( webapp2.RequestHandler ):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/instructions.html")
        self.response.write( start_template.render())


class Piano_Page( webapp2.RequestHandler ):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/piano_page.html")
        #get key from "?key=" in url
        key_string = self.request.get('key')
        #translating key string from URL to an actual key
        key = ndb.Key(urlsafe=key_string)
        selected_song = key.get()

        self.response.write( start_template.render({'song_object' : json.dumps(selected_song.to_dict(), indent=2) }) )


class Select_Song_Page( webapp2.RequestHandler ):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/select_song_page.html")
        my_query = Song.query().fetch();
        self.response.write( start_template.render({'query_of_songs' : my_query}) )


# class Song_Handler(webapp2.RequestHandler):
#     def get(self):
#         #getting javascript
#         key = json.loads(self.request.body.get('data'))
#         logging.info("get handler test")
#         logging.info( key )
#
#         song_key = ndb.Key("Song", key )
#         selected_song = song_key.get()
#         #sending info from python to javascript (a different part from js to python)
#         self.response.headers['Content-Type'] = "application/json"
#         self.response.write(json.dumps(selected_song.serialize()))

# class Piano_Page( webapp2.RequestHandler ):
#     def get(self):
#         start_template = jinja_current_directory.get_template("templates/piano_page.html")
#         self.response.write( start_template.render() )
#
#
# class Select_Song_Page( webapp2.RequestHandler ):
#     def get(self):
#         start_template = jinja_current_directory.get_template("templates/select_song_page.html")
#         my_query = Song.query().fetch();
#         self.response.write( start_template.render({'query_of_songs' : my_query}) )
#
#
# class Song_Handler(webapp2.RequestHandler):
#     def get(self):
#         #getting javascript
#         requestObject = json.loads(self.request.body)
#         key = requestObjet.get('data')
#         print( key )
#
#         song_key = ndb.Key("Song", key )
#         selected_song = song_key.get()
#         #sending info from python to javascript (a different part from js to python)
#         self.response.headers['Content-Type'] = "application/json"
#         self.response.write(json.dumps(selected_song.serialize()))


class Add_Song_Page( webapp2.RequestHandler ):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/add_song_page.html")
        self.response.write( start_template.render())

    def post(self):
        notes = []
        for i in self.request.get("notes"):
            notes.append(i.upper())
        # Get next whole square root
        type = int(math.ceil( math.sqrt(len( notes )) ))
        name = self.request.get("name")
        artist = self.request.get("artist")


        search = Song(name=name, artist=artist, note_progression=notes, type=type )
        search.put()

        variables = {
            'song_name' : search.name,
            'song_artist' : search.artist,
            'song_notes' : search.note_progression,
            'song_type' : search.type,
        }

        start_template = jinja_current_directory.get_template("templates/home_page.html")
        self.response.write( start_template.render(variables))

class About_Us( webapp2.RequestHandler ):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/aboutus.html")
        self.response.write( start_template.render())


#route mapping
app = webapp2.WSGIApplication([
    ('/', Main_Page),
    ('/tutorial', Tutorial_Page),
    ('/piano', Piano_Page),
    ('/select_song', Select_Song_Page),
    ('/add_song', Add_Song_Page),
    ('/aboutus', About_Us),
    # ('/get_song', Song_Handler),


], debug=True)
