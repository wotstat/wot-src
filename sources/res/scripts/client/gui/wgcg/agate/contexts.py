import typing
from enum import Enum
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType
if typing.TYPE_CHECKING:
    from typing import Dict, List

class InventoryEntitlementsCtx(CommonWebRequestCtx):
    __slots__ = (b'__entitlementCodes',)

    def __init__(self, entitlementCodes=(), waitingID=b''):
        super(InventoryEntitlementsCtx, self).__init__(waitingID)
        self.__entitlementCodes = entitlementCodes
        return

    def getRequestType(self):
        return WebRequestDataType.AGATE_INVENTORY_ENTITLEMENTS

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getEntitlementCodes(self):
        return self.__entitlementCodes


class AgateGetInventoryEntitlementsCtx(CommonWebRequestCtx):

    class _FilterKeys(Enum):
        CODE = b'code'
        TAG = b'tag'

    class _FilterOperators(Enum):
        IN = b'in'
        NOT_IN = b'not_in'
        EQ = b'eq'
        NEQ = b'neq'

    __slots__ = (b'__entitlementsFilter',)

    def __init__(self, entitlementsFilter, waitingID=b''):
        self.__entitlementsFilter = entitlementsFilter
        super(AgateGetInventoryEntitlementsCtx, self).__init__(waitingID=waitingID)
        return

    def getRequestType(self):
        return WebRequestDataType.AGATE_GET_INVENTORY_ENTITLEMENTS_V5

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getEntitlementsFilter(self):
        return self.__entitlementsFilter

    @classmethod
    def createFilterByTags(cls, tags):
        tagsFilter = {b'key': (cls._FilterKeys.TAG.value), 
           b'operator': (cls._FilterOperators.IN.value), 
           b'value': tags}
        return {b'filter': [tagsFilter]}

    @classmethod
    def createFilterByCodes(cls, codes):
        operator, value = cls.__makeRequestArgsForValues(codes)
        return {b'filter': [
                     {b'key': (cls._FilterKeys.CODE.value), 
                        b'operator': operator, 
                        b'value': value}]}

    @classmethod
    def __makeRequestArgsForValues(cls, valuesList):
        if len(valuesList) > 1:
            return (cls._FilterOperators.IN.value, valuesList)
        return (cls._FilterOperators.EQ.value, valuesList[0])
