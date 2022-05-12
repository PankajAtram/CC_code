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
        chname = self.request.get('cname')
        url = "http://universities.hipolabs.com/search?name="+ chname
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        name = data[0]['name']
        coname = data[0]['country']
        ccode = data[0]['alpha_two_code']
        domain = data[0]['domains'][0]
        statepro = data[0]['state-province']
        template_values = {
            "name": name,
            "coname": coname,
            "ccode" : ccode,
            "domain": domain,
           "statepro": statepro

        }
        path = os.path.join(os.path.dirname(__file__),'result.html')
        self.response.out.write(template.render(path,template_values))

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)