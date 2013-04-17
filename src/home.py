import webapp2
import jinja2
import os
from com.prashanth.constants import SocialConstants

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values = {
                       "appid" : SocialConstants.FACEBOOK_APP_ID,
                       "channelUrl" : SocialConstants.SOCIAL_CHANNEL
                           
        }

        template = JINJA_ENVIRONMENT.get_template('facebook.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
