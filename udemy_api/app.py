#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from settings import *


class App:
    """Main application entry"""

    COURSES_URL = 'https://www.udemy.com/api-2.0/courses'

    def __init__(self):
        self.settings = Settings()

    def pull(self, url):
        if url == None:
            raise ValueError("URL can't be None")
        resp = requests.get(url, auth=(self.settings.udemy_client(), self.settings.udemy_secret()))
        return json.loads(resp.text)

    def handler(self):
        """Run the application"""
        return self.pull(App.COURSES_URL)



a = App()
print a.handler()
# print s.udemy_secret()
# r = requests.get('https://www.udemy.com/api-2.0/courses', auth=(s.udemy_client(), s.udemy_secret()))
# # resp = json.dumps(r.text, sort_keys=True, indent=4, separators=(',', ': '))
# # print resp

# courses = json.loads(r.text)
# print courses.keys()
# # print type(courses['results'])
# results = courses['results']
# print len(results)
# print results[0]
# # print json.dumps(results[0])
# print r.status_code
# print r.headers['content-type']

# # ------

