import os


class DevConfig(object):
    ENV = os.getenv('ENV')
    DATABASE = {
        'default': os.getenv('DB_DRIVE'),
        'mongodb': {
            'drive': 'mongodb',
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'url': os.getenv('DB_URL'),
            'port': os.getenv('DB_PORT'),
            'name': os.getenv('DB_NAME')
        }
    }
