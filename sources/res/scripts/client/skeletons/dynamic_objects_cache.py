class IBattleDynamicObjectsCache(object):

    def getConfig(self, arenaType):
        raise NotImplementedError
        return

    def getFeaturesConfig(self, feature):
        raise NotImplementedError
        return

    def load(self, arenaType):
        raise NotImplementedError
        return

    def unload(self, arenaType):
        raise NotImplementedError
        return
