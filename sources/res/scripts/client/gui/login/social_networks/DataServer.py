import os, base64, hashlib
from SocketServer import ThreadingMixIn
from Event import Event
from Crypto.Cipher import AES
from Crypto.Util import Counter
from debug_utils import LOG_DEBUG
from RequestHandler import RequestHandler
from standalone.login import HttpServer

class DataServer(HttpServer):

    def __init__(self, name):
        HttpServer.__init__(self, name, RequestHandler)
        self.dataReceived = Event()
        return

    def keepData(self, token, spaID, socialNetwork):
        self.dataReceived(token, spaID, socialNetwork)
        return

    def _logStatus(self):
        LOG_DEBUG(self._currentStatus)
        return


class EncryptingDataServer(DataServer):

    def __init__(self, name):
        DataServer.__init__(self, name)
        self._tokenSecret = hashlib.sha1(os.urandom(128)).hexdigest()[:16]
        return

    def keepData(self, token, spaID, socialNetwork):
        cipher = AES.new(self._tokenSecret, AES.MODE_CTR, counter=Counter.new(128))
        token = cipher.decrypt(base64.urlsafe_b64decode(token))
        DataServer.keepData(self, token, spaID, socialNetwork)
        return

    @property
    def tokenSecret(self):
        return self._tokenSecret


class ThreadedDataServer(ThreadingMixIn, DataServer):

    def __init__(self, name):
        DataServer.__init__(self, name)
        return


class EncryptingThreadedDataServer(ThreadingMixIn, EncryptingDataServer):

    def __init__(self, name):
        EncryptingDataServer.__init__(self, name)
        return
