class IAppearanceCache(object):

    def getAppearance(self, vId, vInfo, callback=None, strCD=None, needLoad=True):
        raise NotImplementedError
        return

    def removeAppearance(self, vId, strCD=None):
        raise NotImplementedError
        return

    def stopLoading(self, vId, strCD=None):
        raise NotImplementedError
        return

    def loadResources(self, compactDescr, prereqs):
        raise NotImplementedError
        return

    def unloadResources(self, compactDescr):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return
