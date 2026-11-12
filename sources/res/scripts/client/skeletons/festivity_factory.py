class IFestivityFactory(object):

    def getRequester(self):
        raise NotImplementedError
        return

    def getRaidRequester(self):
        return

    def getProcessor(self):
        raise NotImplementedError
        return

    def getController(self):
        raise NotImplementedError
        return

    def getDataSyncKey(self):
        raise NotImplementedError
        return

    def getChildControllerInterface(self):
        raise NotImplementedError
        return
