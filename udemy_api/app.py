#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from settings import *
from aws_handler import *

class App:
    """Main application entry"""

    COURSES_URL = 'https://www.udemy.com/api-2.0/courses?page_size=100'

    def __init__(self):
        self.settings    = Settings()
        self.aws_handler = AwsHandler()

    def pull(self, url):
        if url == None:
            raise ValueError("URL can't be None")
        resp = requests.get(url, auth=(self.settings.udemy_client(), self.settings.udemy_secret()))
        # resp_as_dict = json.loads(resp.text)
        return resp.text

    def handler(self):
        """Run the application"""
        courses_page = self.pull(App.COURSES_URL)
        s3 = self.aws_handler.client()
        # buckets = s3.buckets.all()
        # return next((bucket for bucket in buckets)).name
        # key = '20161012/udemy/courses/1.json'
        key = '20161012udemycourses1.json'
        s3.Bucket('coursenut-datalake').put_object(Key=key, Body=courses_page)


a = App()
a.handler()
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

