
import webapp2
import os
import jinja2
import time

from google.appengine.ext import ndb


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader( os.path.dirname(__file__) )
)



class Main_Page(webapp2.RequestHandler):
    def get( self ):
        template = jinja_current_directory.get_template("templates/main_page.html")
        self.response.write( template.render() )





#route mapping
app = webapp2.WSGIApplication([
    ('/', Main_Page),
], debug=True)a




# class Responses( ndb.Model ):
#     n1 = ndb.StringProperty(required=True)
#
#
#
# class Mad_Libs(webapp2.RequestHandler):
#     def get(self):
#         input_template = jinja_current_directory.get_template("templates/input.html")
#         self.response.write( input_template.render() )
#
#     def post(self):
#         output_template = jinja_current_directory.get_template( "templates/output.html")
#         noun1 = self.request.get("noun1")
#
#
#         save_response = Responses(n1=noun1, v1=verb1, n2=noun2, a1=adj1, a2=adj2, v2=verb2, v3=verb3, v4=verb4, n3=noun3, time_stamp=time.time())
#         save_response.put()
#
#         user_input = {
#             "noun1" : "<span>" + noun1 + "</span>",
#             "verb1" : "<span>" + verb1 + "</span>",
#             "noun2" : "<span>" + noun2 + "</span>",
#             "adj1" : "<span>" + adj1 + "</span>",
#             "adj2" : "<span>" + adj2 + "</span>",
#             "verb2" : "<span>" + verb2 + "</span>",
#             "verb3" : "<span>" + verb3 + "</span>",
#             "verb4" : "<span>" + verb4 + "</span>",
#             "noun3" : "<span>" + noun3 + "</span>",
#             "button" : '<a href="https://mad-libs-210517.appspot.com/all"><button id="prev_But">Previous Responses</button></a>',
#             "again" : '<a href="https://mad-libs-210517.appspot.com/"><button id="again_But">Play Again</button></a>',
#         }
#         self.response.write(output_template.render(user_input))
#
#
#
# class previousResponses( webapp2.RequestHandler ):
#     def get( self ):
#         output_template = jinja_current_directory.get_template( "templates/output.html")
#         my_query = Responses.query()
#
#         all_responses = my_query.order(Responses.time_stamp).fetch()
#         self.response.write(output_template.render({"again2" :'<a href="https://mad-libs-210517.appspot.com/"><button id="again_But">Play Again</button></a>'}))
#         for i in range( len(all_responses) ):
#             current = all_responses[i]
#             user_input = {
#                 "noun1" : "<span>" + current.n1 + "</span>",
#                 "verb1" : "<span>" + current.v1 + "</span>",
#                 "noun2" : "<span>" + current.n2 + "</span>",
#                 "adj1" : "<span>" + current.a1 + "</span>",
#                 "adj2" : "<span>" + current.a2 + "</span>",
#                 "verb2" : "<span>" + current.v2 + "</span>",
#                 "verb3" : "<span>" + current.v3 + "</span>",
#                 "verb4" : "<span>" + current.v4 + "</span>",
#                 "noun3" : "<span>" + current.n3 + "</span>",
#                 "hr" : "<hr>",
#             }
#             self.response.write(output_template.render(user_input))
