from __future__ import absolute_import
import resource_helper
from vehicles.mechanics.mechanic_constants import VehicleMechanic
_PREBATTLE_TIPS_XML_PATH = b'gui/prebattle_tips.xml'
_PRECEDING_DEFAULT_SHOW_TIMES = 1
DEFAULT_STATUS = b'payAttention'
DEFAULT_GROUP = b'all'
_OPTIONAL_FILTER_FLAGS = (b'isBattlePassActiveSeason', b'isRankedYearRewardEnabled', b'isRankedLeaderboardEnabled', b'isRankedShopEnabled', b'isPostProgressionEnabled')

def _readPreBattleTips():
    filters = {}
    tips = {}
    ctx, root = resource_helper.getRoot(_PREBATTLE_TIPS_XML_PATH)
    for _, filterSection in resource_helper.getIterator(ctx, root[b'filters']):
        filterId = filterSection.readString(b'id')
        filters[filterId] = {b'minBattles': (filterSection.readInt(b'minBattles', 0)), 
           b'maxBattles': (filterSection.readInt(b'maxBattles', 0)), 
           b'arenaTypes': (_readPossibleValues(filterSection, b'arenaTypes')), 
           b'nations': (_readPossibleValues(filterSection, b'nations')), 
           b'levels': (_readPossibleValues(filterSection, b'levels')), 
           b'vehicleClass': (_readPossibleValues(filterSection, b'vehicleClass')), 
           b'tags': (_readPossibleValues(filterSection, b'tags')), 
           b'realms': (_readPossibleValues(filterSection, b'realms')), 
           b'preceding': (_readPrecedingData(filterSection)), 
           b'chassisType': (filterSection.readInt(b'chassisType', -1)), 
           b'vehProperty': (filterSection.readString(b'vehProperty', None)), 
           b'mechanics': (_readMechanicsData(filterSection[b'mechanics']))}
        for key in _OPTIONAL_FILTER_FLAGS:
            if filterSection.has_key(key):
                filters[filterId][key] = filterSection.readBool(key)

    for _, tipsSection in resource_helper.getIterator(ctx, root[b'tips']):
        filterId = tipsSection.readString(b'filter')
        tipId = tipsSection.readString(b'id')
        status = tipsSection.readString(b'status', DEFAULT_STATUS)
        group = tipsSection.readString(b'group', DEFAULT_GROUP)
        tipConfig = filters.get(filterId)
        tips[tipId] = {b'filter': tipConfig, 
           b'status': status, 
           b'group': group}

    resource_helper.purgeResource(_PREBATTLE_TIPS_XML_PATH)
    return tips


def _readPossibleValues(filterSection, key):
    return frozenset(filterSection.readString(key).split())


def _readPrecedingData(section):
    precedingData = None
    if section[b'preceding'] is not None:
        precedingData = {b'showTimes': (section[b'preceding'].readInt(b'showTimes', _PRECEDING_DEFAULT_SHOW_TIMES))}
    return precedingData


def _readMechanicsData(section):
    if section is None:
        return
    else:
        mechanicsData = {}
        for mechanicsKey in (b'include', b'exclude'):
            rawMechanics = section.readString(mechanicsKey).split()
            mechanicsData[mechanicsKey] = frozenset(VehicleMechanic(mechanic) for mechanic in rawMechanics)

        return mechanicsData


def getPreBattleTipsConfig():
    global _preBattleTipsConfig
    if _preBattleTipsConfig is None:
        _preBattleTipsConfig = _readPreBattleTips()
    return _preBattleTipsConfig


_preBattleTipsConfig = None
