#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import wsgiref.handlers, os
from google.appengine.ext import webapp
import webapp2
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render('home.html', {}))

class About(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render('about.html', {}))

class Contact(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render('contact.html', {}))

class Portfolio(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render('portfolio.html', {}))

class WebAd(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render('webad.html', {}))

app = webapp2.WSGIApplication([('/', MainHandler), ('/webad', WebAd), ('/about', About), ('/contact', Contact), ('/portfolio', Portfolio)],
                              debug=True)

if __name__ == "__main__":
    main()