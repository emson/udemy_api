"""
.. module: udemy_api
    :copyright: (c) 2016 by Black Bee Ltd., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
"""
from __future__ import print_function

import os
import json
import boto3
import requests

from config.settings_config import SettingsConfig, UDEMY_SECTION,\
    UDEMY_CLIENT_ID, UDEMY_CLIENT_SECRET, UDEMY_COURSES_URL,\
    AWS_SECTION, AWS_BUCKET


print('Loading function...')


def lambda_handler(event, context):
    """Main AWS Lambda entry point"""
    aws_bucket   = config().get(AWS_SECTION, AWS_BUCKET)
    courses_url  = config().get(UDEMY_SECTION, UDEMY_COURSES_URL)
    courses_page = pull(courses_url)
    key = generate_key()
    store(aws_bucket, key, courses_page)
    return courses_page


def generate_key(opts=None):
    """Generate the bucket key. e.g. 20161012/udemy/courses/1.json"""
    return '20161012udemycourses1.json'


def config(config_file=os.path.join(os.path.dirname(__file__), 'config',
    'settings.cfg')):
    """Access the config parser"""
    return SettingsConfig(config_file=config_file)


def pull(url):
    if url == None:
        raise ValueError("URL can't be None")
    udemy_client_id     = config().get(UDEMY_SECTION, UDEMY_CLIENT_ID)
    udemy_client_secret = config().get(UDEMY_SECTION, UDEMY_CLIENT_SECRET)
    resp = requests.get(url, auth=(udemy_client_id, udemy_client_secret))
    return resp.text


def store(bucket, key, value):
    """Write the contents of page to the bucket"""
    s3 = boto3.resource('s3')
    # buckets = s3.buckets.all()
    # return next((bucket for bucket in buckets)).name
    # key = '20161012/udemy/courses/1.json'
    s3.Bucket(bucket).put_object(Key=key, Body=value)


# if __name__ == "__main__":
#     print lambda_handler()


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

