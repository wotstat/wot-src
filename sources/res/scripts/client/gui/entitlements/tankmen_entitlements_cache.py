import BigWorld, logging
from collections import namedtuple
import typing
from enum import Enum
from adisp import adisp_process
from functools import partial
from gui.wgcg.agate.contexts import AgateGetInventoryEntitlementsCtx
from helpers import dependency
from skeletons.gui.web import IWebController
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, List
_logger = logging.getLogger(__name__)
Entitlement = namedtuple(b'Entitlement', b'code, tags, amount')

class _FilterKeys(Enum):
    CODE = b'code'
    TAG = b'tag'


class _FilterOperators(Enum):
    IN = b'in'
    NOT_IN = b'not_in'
    EQ = b'eq'
    NEQ = b'neq'


_DELAY = 1

class TankmenEntitlementsCache(object):
    __slots__ = (b'__balanceCache', b'__isSyncing')
    __web = dependency.descriptor(IWebController)

    def __init__(self):
        self.__balanceCache = {}
        self.__isSyncing = False
        return

    def getBalance(self):
        return self.__balanceCache

    def update(self, entitlementsFilter, onResponseCallback):
        self.__request(self.__createFilterByTags([entitlementsFilter]), onResponseCallback)
        return

    def updateWithDelay(self, filter, onResponseCallback):
        BigWorld.callback(_DELAY, partial(self.__request, self.__createFilterByTags([filter]), onResponseCallback))
        return

    def clear(self):
        self.__balanceCache.clear()
        self.__isSyncing = False
        return

    @adisp_process
    def __request(self, entitlementsFilter, onResponseCallback):
        if self.__isSyncing:
            onResponseCallback(False, self.__isSyncing)
            return
        if self.__web.isAvailable():
            try:
                self.__isSyncing = True
                response = yield self.__web.sendRequest(ctx=AgateGetInventoryEntitlementsCtx(entitlementsFilter))
            finally:
                self.__isSyncing = False

            if response.isSuccess():
                result = response.data.get(b'balance', [])
                self.__balanceCache.update({entitlement[b'code']: self.__createEntitlementFromResponse(entitlement) for entitlement in result})
            else:
                _logger.warning(b'Failed to get entitlements data. Code: %s.', response.getCode())
            if callable(onResponseCallback):
                onResponseCallback(response.isSuccess(), self.__isSyncing)
        else:
            _logger.warning(b'Failed to get entitlements data. Web controller is unavailable')
            if callable(onResponseCallback):
                onResponseCallback(False, self.__isSyncing)
        return

    def __createEntitlementFromResponse(self, response):
        return Entitlement(response.get(b'code', b''), response.get(b'tags', []), response.get(b'amount', 0))

    def __createFilterByTags(self, tags):
        tagsFilter = {b'key': (_FilterKeys.TAG.value), 
           b'operator': (_FilterOperators.IN.value), 
           b'value': tags}
        return self.__createFilter([tagsFilter])

    def __createFilter(self, filters):
        return {b'filter': filters}
