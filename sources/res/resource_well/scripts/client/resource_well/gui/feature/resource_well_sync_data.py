from __future__ import absolute_import
from typing import Dict
from account_helpers import AccountSyncData
from resource_well_common.feature_constants import RESOURCE_WELL_PDATA_KEY
from shared_utils.account_helpers.diff_utils import synchronizeDicts

class ResourceWellSyncData(object):

    def __init__(self):
        self.__cache = {}
        return

    def clear(self):
        self.__cache.clear()
        return

    def getSeason(self):
        return self.__cache.get(b'season', 0)

    def getCurrentPoints(self):
        return self.__cache.get(b'points', 0)

    def getBalance(self):
        return self.__cache.get(b'balance', {})

    def getReward(self):
        return self.__cache.get(b'reward', set())

    def getCurrentRewardID(self):
        return self.__cache.get(b'currentRewardId', b'')

    def getInitialNumberAmounts(self):
        return self.__cache.get(b'initialAmounts', {})

    def update(self, clientDiff):
        isFullSync = AccountSyncData.isFullSyncDiff(clientDiff)
        if isFullSync:
            self.__cache.clear()
        synchronizeDicts(clientDiff[RESOURCE_WELL_PDATA_KEY], self.__cache)
        return
