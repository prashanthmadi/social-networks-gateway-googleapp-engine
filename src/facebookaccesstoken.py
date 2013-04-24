from com.prashanth.utils.getUrlData import extractFacebookLongLivedTokenData
import jinja2
import os
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class FacebookLongLivedLoginHandler(webapp2.RequestHandler):
    def post(self):
        shrtlivedtoken = str(self.request.get('shrtlivedtoken'))
        resultdata = extractFacebookLongLivedTokenData(shrtlivedtoken)
        if resultdata is None:
            self.response.out.write("error while extracting token")
        else:    
            self.response.out.write(resultdata)

app = webapp2.WSGIApplication([('/rpc', FacebookLongLivedLoginHandler)],
                              debug=True)