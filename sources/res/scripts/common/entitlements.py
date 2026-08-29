class EntitlementsData(object):

    def __init__(self):
        self.__validEntitlements = set()
        self.__validationQueue = set()
        return

    def getValidEntitlements(self):
        return self.__validEntitlements

    def addValidEntitlementsToCache(self, entitlementIDsList):
        self.__validEntitlements.update(entitlementIDsList)
        return

    def isEntitlementValid(self, entitlementID):
        return entitlementID in self.__validEntitlements

    def addEntitlementToValidationQueue(self, entitlementID):
        self.__validationQueue.add(entitlementID)
        return

    def getValidationQueue(self):
        return list(self.__validationQueue)


g_entitlementsData = EntitlementsData()
