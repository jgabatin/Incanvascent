import webapp2
import os
import jinja2
import json
import math
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
                current_visitor = Visitor(key=current_key, name=current_user.nickname(), email=current_user.email(), id=current_user.user_id(), page_view_count=0 )
            current_visitor.page_view_count += 1
            current_visitor.put()

            #display
            with_user_template = jinja_current_directory.get_template("templates/home_page.html")
            jinja_values = {
            'name' : current_user.nickname(),
            'user_addr' : current_user.email(),
            'user_id' : current_user.user_id(),
            'signout_page_url' : users.create_logout_url('/'),
            'number_of_views' : current_visitor.page_view_count,
            }
            self.response.write( with_user_template.render( jinja_values ))


class Tutorial_Page( webapp2.RequestHandler ):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/instructions.html")
        self.response.write( start_template.render())



# class Home_Page(webapp2.RequestHandler):
#     def get(self):
#


class Piano_Page( webapp2.RequestHandler ):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/piano_page.html")

        # song_id = self.request.get("ID") #SET LATER
        song_key = ndb.Key("Song", 5629499534213120)


        selected_song = song_key.get()
        python_to_js = {
            'note_progression' : selected_song.note_progression,
        }
        # json.dump(python_to_js)

        self.response.write( start_template.render( {'box' : selected_song.type} ) )


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


#         if not search_term:
#             search_term = "dog"
#         else:
#             lterm = search_term.lower()
#             key = ndb.Key('Searches', lterm )
#             search = key.get()
#             if not search:
#                 search = Searches(key=key, count=0, word=lterm)
#
#             search.increment()
#             search.put()
#             # my_query = Searches.query( Searches.word == search_term.lower() ).fetch()
#             # if len(my_query) == 0:
#             #     currentSearch = Searches( word=search_term.lower(), count=1 )
#             #     currentSearch.put()
#             #     #UPDATE AND CREATED
#             # else:
#             #     currentSearch = my_query[0]
#             #     currentSearch.increment()
#             #     currentSearch.put()
#
#         params = {
#             'api_key' : 'kDwqshKjeeNJJIx4voC5ZCYOxATfEzsV',
#             'q' : search_term,
#             'limit' : 56,
#             # 'rating': 'g'
#         }
#         form_data = urllib.urlencode(params)
#         api_url = 'http://api.giphy.com/v1/gifs/search?' + form_data
#
#         response = urllib2.urlopen(api_url)
#         content = json.loads(response.read())
#         #loads() = load string
#
#         gif_urls = []
#         for img in content['data']:
#             url = img['images']['original']['url']
#             gif_urls.append(url)
#
#         template = jinja_environment.get_template('output.html')
#         variables = {
#             # 'content': content,
#             'gif_urls' : gif_urls,
#             'search_term' : search_term,
#             # 'header' : '<a href="http://localhost:8080">New Search</a> | <a href="http://localhost:8080/recent">Recent Searches</a> | <a href="http://localhost:8080/popular">Popular Searches</a>',
#         }
#
#         self.response.write(template.render(variables))


#route mapping
app = webapp2.WSGIApplication([
    ('/', Main_Page),
    ('/tutorial', Tutorial_Page),
    ('/piano', Piano_Page),
    ('/add_song', Add_Song_Page),

], debug=True)
