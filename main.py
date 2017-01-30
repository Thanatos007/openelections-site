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
import webapp2
import csv
import json
import StringIO

def process_csv_data(csv_data):
    precinct_to_votes = {}
    is_header = True
    f = StringIO.StringIO(csv_data)
    rows = csv.reader(f, delimiter=',')
    for row in rows:
        if is_header:
            is_header: False
            continue
    return precinct_to_votes

class UploadHandler(webapp2.RequestHandler):
    def post(self):
        csv_data = self.request.POST.get('csv_file').file.read()
        self.response.out.write(csv_data)
        for key in results:
            self.response.out.write(json.dumps(results[key]) + "<br>")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/upload', UploadHandler)
], debug=True)
