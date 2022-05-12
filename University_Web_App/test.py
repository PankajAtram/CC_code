import os
import json
import urllib
import webapp2

from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path,template_values))

    def post(self):
        cname = self.request.get('cname')
        

        url = "http://universities.hipolabs.com/search?name="+cname
        data = urllib.urlopen(url).read()
        data = json.loads(data)

        name = data[0]['name']

        template_values = {
            'cname' : name
        }

        path = os.path.join(os.path.dirname(__file__),'result.html')
        self.response.out.write(template.render(path,template_values))

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)