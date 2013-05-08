from com.prashanth.searchengine.QueryResult import queryProcess
import jinja2
import os
import webapp2

path = os.path.join(os.path.split(__file__)[0], "statichtml")
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path))

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values = {
                "searchQuery" : "abc",
                           }
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render(template_values))

class SearchResult(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        searchQuery = str(self.request.get('searchQuery'))
        queryResultDocs = queryProcess(searchQuery)
        error = None
        if queryResultDocs is None:
            error = "No Records Found"
        template_values = {
                       'searchQuery' : searchQuery,
                       'result' :queryResultDocs,
                       'error'  : error
                       }
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render(template_values))



app = webapp2.WSGIApplication([('/search', MainPage), ('/searchresult', SearchResult)],
                              debug=True)
