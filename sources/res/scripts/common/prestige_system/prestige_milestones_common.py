from __future__ import absolute_import
from typing import Optional, Dict, Set, Any, Union
from copy import copy
from constants import IS_CLIENT
from debug_utils import LOG_DEBUG_DEV, LOG_DEBUG
from dossiers2.custom.cache import getCache as getDossiers2Cache, buildCache as buildDossiers2Cache
VehCDType = int
PrestigeLevelType = int
InvoiceStatusType = int
ErrorStrType = str
MilestoneData = Dict[str, Any]
MilestonesType = Dict[PrestigeLevelType, MilestoneData]
MilestonesCacheType = Dict[VehCDType, Dict[PrestigeLevelType, MilestonesType]]
OverrideItem = Dict[str, Union[MilestonesType, Set[VehCDType], bool]]

class PrestigeMilestonesConfig(object):

    def __init__(self, config):
        self._config = config
        if IS_CLIENT:
            self.__cache = {}
            if self._config:
                computePrestigeMilestonesCache(config, self.__cache)
        else:
            self.__cache = getCache()
        return

    @property
    def milestones(self):
        return self.__cache[b'prestigeMilestones']


def getCache():
    return _g_cache


def computePrestigeMilestonesCache(config, cache=None, dossiers2Cache=None):
    LOG_DEBUG_DEV(b'computePrestigeMilestonesCache config', config)
    if cache is None:
        cache = getCache()
    if not config[b'enabled']:
        LOG_DEBUG(b'computePrestigeMilestonesCache PrestigeMilestonesSystem disabled, cache will be cleared')
        cache[b'prestigeMilestones'] = {}
        cache[b'enabled'] = False
        return
    else:
        cache[b'enabled'] = True
        _dossier2Cache = dossiers2Cache
        if _dossier2Cache is None:
            if not getDossiers2Cache():
                buildDossiers2Cache()
            _dossier2Cache = getDossiers2Cache()
        cache[b'prestigeMilestones'] = computeMilestonesCache(config[b'defaultMilestones'], config[b'milestonesOverrides'], config[b'enabledVehLevels'], _dossier2Cache[b'vehiclesByLevel'])
        return


def computeMilestonesCache(defaultMilestones, overrideItems, enabledVehicleLevels, vehiclesByLevel):
    vehicleMilestones = {}
    for level in enabledVehicleLevels:
        vehicleMilestones.update({vehCD: copy(defaultMilestones) for vehCD in vehiclesByLevel[level]})

    for override in overrideItems:
        applyOverrideMilestones(vehicleMilestones, override)

    return vehicleMilestones


def applyOverrideMilestones(vehicleMilestones, override):
    for vehicleCD in override[b'vehicles']:
        if override[b'enabled']:
            for prestigeLevel, milestone_data in override[b'milestones'].items():
                vehicleMilestones[vehicleCD][prestigeLevel] = milestone_data

        elif vehicleCD in vehicleMilestones:
            vehicleMilestones.pop(vehicleCD)

    return


_g_cache = {}
