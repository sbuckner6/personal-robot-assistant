from config import Config
from houndify import houndify
from redis import Redis
import sys

class HoundifyAccessObject:

    class __instance:
        def __init__(self):
            self.text_client = houndify.TextHoundClient(
                clientID=Config.Houndify.CLIENT_ID,
                clientKey=Config.Houndify.CLIENT_KEY,
                userID=Config.Houndify.USER_ID,
                requestInfo={}
            )

            self.caching_enabled = False

            try:
                self.redis = Redis(host='redis', port=6379, db=0)
                self.caching_enabled = True
            except:
                print("Unable to connect to Redis instance!")

    instance = None

    def __init__(self):
        if not HoundifyAccessObject.instance:
            HoundifyAccessObject.instance = HoundifyAccessObject.__instance()
        else:
            print("Attempting to reinstantiate singleton")
            # HoundifyAccessObject.instance.text_client = houndify.TextHoundClient(
            #     clientID=Config.Houndify.CLIENT_ID,
            #     clientKey=Config.Houndify.CLIENT_KEY,
            #     userID=Config.Houndify.USER_ID,
            #     requestInfo={}
            # )
            #
            # HoundifyAccessObject.instance.redis = Redis(host='redis', port=6379, db=0)

    def query(self, querytext):
        answer = None
        caching = HoundifyAccessObject.instance.caching_enabled
        if caching:
            HoundifyAccessObject.instance.redis.get(querytext)

        if not answer:
            response = HoundifyAccessObject.instance.text_client.query(querytext)
            answer = response['AllResults'][0]['SpokenResponseLong']
            if caching:
                HoundifyAccessObject.instance.redis.set(querytext, answer)
        else:
            answer = answer.decode('UTF-8')

        return answer