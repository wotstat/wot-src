class IPlatformWebApi(object):

    def getType(self):
        raise NotImplementedError
        return

    def isInited(self):
        raise NotImplementedError
        return

    def isConnected(self):
        raise NotImplementedError
        return
