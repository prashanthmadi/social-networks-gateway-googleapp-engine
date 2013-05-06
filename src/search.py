from com.prashanth.constants import SocialConstants
import jinja2
import logging
import os
import webapp2

path = os.path.join(os.path.split(__file__)[0], "statichtml")
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path))

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values = {
                "searchQuery" : "",
                           }
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render(template_values))

class SearchResult(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        searchQuery = str(self.request.get('searchQuery'))
        template_values = {
                       "searchQuery" : searchQuery,
        }
        logging.debug(searchQuery)
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render(template_values))



app = webapp2.WSGIApplication([('/search', MainPage), ('/searchresult',)],
                              debug=True)
