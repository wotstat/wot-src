from external_strings_utils import strtobool, InvalidStringValueException
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from constants import SPA_ATTRS

class SPAFlags(object):

    def __init__(self, syncData):
        super(SPAFlags, self).__init__()
        self.__account = None
        self.__syncData = syncData
        self.__cache = {}
        self.__ignore = True
        return

    def onAccountBecomePlayer(self):
        self.__ignore = False
        return

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True
        return

    def setAccount(self, account):
        self.__account = account
        return

    def synchronize(self, diff):
        cacheDiff = diff.get(b'cache', None)
        spaCache = cacheDiff.get(b'SPA', None) if cacheDiff else None
        itemDiff = {}
        if spaCache:
            for key in SPA_ATTRS.toClientAttrs():
                value = spaCache.get(key, None)
                if value:
                    try:
                        itemDiff[key] = strtobool(value)
                    except InvalidStringValueException:
                        itemDiff[key] = value

        synchronizeDicts(itemDiff, self.__cache.setdefault(b'spaFlags', {}))
        return

    def getFlag(self, flagName):
        if self.__cache and b'spaFlags' in self.__cache:
            return self.__cache[b'spaFlags'].get(flagName, None)
        else:
            return
