from skeletons.gui.platform.controller import IPlatformRequestController

class IProductFetchController(IPlatformRequestController):

    def getProducts(self, showWaiting=True):
        raise NotImplementedError
        return

    def isUndefined(self):
        raise NotImplementedError
        return


class ISubscriptionsFetchController(IProductFetchController):

    def getProducts(self, showWaiting=True):
        raise NotImplementedError
        return


class IUserSubscriptionsFetchController(IProductFetchController):

    def getProducts(self, showWaiting=True):
        raise NotImplementedError
        return

    def resetFetch(self):
        raise NotImplementedError
        return
