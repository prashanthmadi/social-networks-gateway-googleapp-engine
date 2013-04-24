from com.prashanth.utils.getUrlData import extractDataFromUrl
import cgi
import jinja2
import os
import simplejson
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class RPCHandler(webapp2.RequestHandler):
    def post(self):
        url = cgi.escape(self.request.get('url'))
        result = extractDataFromUrl(url);
        self.response.out.write(simplejson.dumps(result))

app = webapp2.WSGIApplication([('/rpc', RPCHandler)],
                              debug=True)
