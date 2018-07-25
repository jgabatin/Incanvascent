import webapp2
import os
import jinja2
import json
from google.appengine.ext import ndb
from google.appengine.api import users
from models import Visitor


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

class Tutorial( webapp2.RequestHandler ):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/instructions.html")

        self.response.write( start_template.render())



#route mapping
app = webapp2.WSGIApplication([
    ('/', Main_Page),
    ('/tutorial', Tutorial),
], debug=True)
