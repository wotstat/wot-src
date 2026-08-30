class IPromoLogger(object):

    def logAction(self, **kwargs):
        raise NotImplementedError
        return

    def logTeaserAction(self, teaserData, **kwargs):
        raise NotImplementedError
        return

    def getLoggingFuture(self, teaserData=None, **kwargs):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return
