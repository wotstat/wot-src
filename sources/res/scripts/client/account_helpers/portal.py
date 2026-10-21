import typing
from account_helpers.account_data_cache import AccountDataStorage
from portal_common.portal_constants import PDATA_KEY_PORTAL_BATTLES
if typing.TYPE_CHECKING:
    from typing import Dict

class Portal(object):

    def __init__(self):
        self.__accountDataCache = AccountDataStorage(PDATA_KEY_PORTAL_BATTLES, onAccountDataChangeCallback=self.__onAccountDataChanged)
        return

    def clear(self):
        self.__accountDataCache.clear()
        return

    @property
    def _data(self):
        return self.__accountDataCache.accountData

    def getVehicleUpgradeTree(self, vehicle):
        return self.__accountDataCache.accountData[b'vehicleUpgradesMask'].get(vehicle.intCD, 0)

    def getVehicleExperience(self, vehicle):
        return self.__accountDataCache.accountData[b'vehicleExperience'].get(vehicle.intCD, {}).get(b'exp', 0)

    def synchronize(self, isFullSync, diff):
        if self.__accountDataCache.isSynchronizationNeeded(diff):
            self.__accountDataCache.synchronize(isFullSync, diff)
        return

    def __onAccountDataChanged(self, accountData):
        return
