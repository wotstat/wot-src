from __future__ import absolute_import
import typing
from account_helpers import AccountSyncData
from open_bundle_common.constants import OPEN_BUNDLE_PDATA_KEY
from shared_utils.account_helpers.diff_utils import synchronizeDicts
if typing.TYPE_CHECKING:
    from typing import Dict

class OpenBundleSyncData(object):

    def __init__(self):
        self.__cache = {}
        return

    def clear(self):
        self.__cache.clear()
        return

    def update(self, clientDiff):
        isFullSync = AccountSyncData.isFullSyncDiff(clientDiff)
        if isFullSync:
            self.__cache.clear()
        synchronizeDicts(clientDiff[OPEN_BUNDLE_PDATA_KEY], self.__cache)
        return

    def getTrackedByNameSections(self, bundleID):
        return (self.__cache.get(bundleID) or {}).get(b'trackedByNameSections') or {}
