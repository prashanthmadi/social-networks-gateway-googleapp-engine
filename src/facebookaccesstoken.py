from com.prashanth.utils.facebookutil import facebookMain
import jinja2
import os
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class FacebookGraphApiHandler(webapp2.RequestHandler):
    def post(self):
        shrtlivedtoken = str(self.request.get('shrtlivedtoken'))
        resultdata = facebookMain(shrtlivedtoken)
        if resultdata is None:
            self.response.out.write("error while extracting token")
        else:    
            self.response.out.write(resultdata)

app = webapp2.WSGIApplication([('/rpc', FacebookGraphApiHandler)],
                              debug=True)
