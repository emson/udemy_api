"""
.. module: udemy_api.config.udemy_api_config
    :copyright: (c) 2016 by Black Bee Ltd., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
"""

import ConfigParser

# --- Config keys ---
UDEMY_SECTION = 'Udemy'
UDEMY_CLIENT_ID = 'udemy_client_id'
UDEMY_CLIENT_SECRET = 'udemy_client_secret'
UDEMY_COURSES_URL = 'udemy_courses_url'
AWS_SECTION = 'AWS'
AWS_BUCKET = 'aws_bucket'

class SettingsConfig(ConfigParser.RawConfigParser):
    def __init__(self, config_file):
        defaults = {}
        ConfigParser.RawConfigParser.__init__(self, defaults=defaults)
        self.read(config_file)
        # if not self.has_section(UDEMY_SECTION):
        #    self.add_section(UDEMY_SECTION)

