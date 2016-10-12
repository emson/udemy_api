import os

class Settings(object):
    """Settings for this module"""

    def udemy_client(self):
        """Udemy client ID"""
        return os.environ['UDEMY_CLIENT']

    def udemy_secret(self):
        """Udemy secret key"""
        return os.environ['UDEMY_SECRET']


