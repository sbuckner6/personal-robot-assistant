from houndify import houndify
from config import Config


class HoundifyAccessObject:

    class __instance:
        def __init__(self):
            self.text_client = houndify.TextHoundClient(
                clientID=Config.Houndify.CLIENT_ID,
                clientKey=Config.Houndify.CLIENT_KEY,
                userID=Config.Houndify.USER_ID,
                requestInfo={}
            )

    instance = None

    def __init__(self):
        if not HoundifyAccessObject.instance:
            HoundifyAccessObject.instance = HoundifyAccessObject.__instance()
        else:
            HoundifyAccessObject.instance.text_client = houndify.TextHoundClient(
                clientID=Config.Houndify.CLIENT_ID,
                clientKey=Config.Houndify.CLIENT_KEY,
                userID=Config.Houndify.USER_ID,
                requestInfo={}
            )

    def query(self, querytext):
        return HoundifyAccessObject.instance.text_client.query(querytext)

