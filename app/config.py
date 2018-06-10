import os


class Houndify():
    CLIENT_ID = 'ITdB6ME9dOrTRQxm3xNqXA=='
    CLIENT_KEY = 'JdPOb2p80vQPyfBC5cC3efUxgRpg_FoqWyScW3fumvSBvZP0Dk3pVc-czYuerEqoG3NLnNaTgjrccEQGnxrZIg=='
    USER_ID = 'admin'

# has to extend object so Flask can use...not pythonic, I know :/
class Config(object):
    TITLE = 'Your Personal Robot Assistant?'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uF83-9WI2-9Sp1-o39S-aQ1z'
    Houndify = Houndify()
