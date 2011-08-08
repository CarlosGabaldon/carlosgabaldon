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
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template


class Post(object):
    """Post"""
    def __init__(self, title, content, ancillary_content = None, author="anonymous"):
        self.title = title
        self.content = content
        self.ancillary_content = ancillary_content
        self.author = author

class Handler(webapp.RequestHandler):
  
    def render(self, template_name, response=None):

        if response is None:
            response = {}

        path = os.path.join(os.path.dirname(__file__), template_name)
        self.response.out.write(template.render(path, response))

class MainHandler(Handler):
    def get(self):
        posts = [Post(title ="Html 5 Rocks", 
                      content="I love it..", 
                      author="Carlos"),
                 Post(title ="CSS3 and you", 
                      content="How to start..",
                      ancillary_content="CSS is Magic!"),
                 Post(title ="JavaScript Today", 
                      content="Modern JavaScript is ..")]
        
        response = dict(posts=posts)
        self.render(template_name='templates/posts.html', response=response)


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
