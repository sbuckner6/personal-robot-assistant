import os


class Houndify():
    CLIENT_ID = ''
    CLIENT_KEY = ''
    USER_ID = 'admin'

# has to extend object so Flask can use...not pythonic, I know :/
class Config(object):
    TITLE = 'Your Personal Robot Assistant?'
    SECRET_KEY = os.environ.get('SECRET_KEY') or ''
    Houndify = Houndify()
