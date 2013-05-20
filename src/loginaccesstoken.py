from com.prashanth.social.twitter.twitterOauth import twLogin
from com.prashanth.utils.facebookutil import facebookMain
import jinja2
import os
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class SocialLoginDataHandler(webapp2.RequestHandler):
    def post(self):
        loginType = str(self.request.get('loginType'))
        if(loginType == "twitter"):
            self.response.out.write(twLogin())
        elif(loginType == "facebook"):
            shrtlivedtoken = str(self.request.get('shrtlivedtoken'))
            resultdata = facebookMain(shrtlivedtoken)
            if resultdata is None:
                self.response.out.write("error while extracting token")
            else:
                self.response.out.write(resultdata)

app = webapp2.WSGIApplication([('/loginaccesstoken', SocialLoginDataHandler)],
                              debug=True)
