from __future__ import absolute_import
import adisp

class IPurchaseCache(object):

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    @adisp.adisp_async
    def requestPurchaseByID(self, pId, callback=None):
        return

    def getCachedPurchase(self, pId):
        return

    def getProductCode(self, pId):
        return

    def canBeRequestedFromProduct(self, data):
        return False
