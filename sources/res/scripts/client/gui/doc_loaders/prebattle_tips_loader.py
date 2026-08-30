import sys, resource_helper
_PRECEDING_DEFAULT_SHOW_TIMES = 1
DEFAULT_STATUS = b'payAttention'
DEFAULT_GROUP = b'all'
_OPTIONAL_FILTER_FLAGS = (b'isBattlePassActiveSeason', b'isRankedYearRewardEnabled', b'isRankedLeaderboardEnabled', b'isRankedShopEnabled', b'isRankedLeagueRewardEnabled', b'isPostProgressionEnabled')

def readPreBattleTips(prebattleXmlPath):
    filters = dict()
    tips = dict()
    ctx, root = resource_helper.getRoot(prebattleXmlPath)
    for _, filterSection in resource_helper.getIterator(ctx, root[b'filters']):
        filterId = filterSection.readString(b'id')
        filters[filterId] = {b'minBattles': (filterSection.readInt(b'minBattles', 0)), 
           b'maxBattles': (filterSection.readInt(b'maxBattles', sys.maxint)), 
           b'arenaTypes': (_readPossibleValues(filterSection, b'arenaTypes')), 
           b'nations': (_readPossibleValues(filterSection, b'nations')), 
           b'levels': (_readPossibleValues(filterSection, b'levels')), 
           b'vehicleClass': (_readPossibleValues(filterSection, b'vehicleClass')), 
           b'tags': (_readPossibleValues(filterSection, b'tags')), 
           b'noTags': (_readPossibleValues(filterSection, b'noTags')), 
           b'realms': (_readPossibleValues(filterSection, b'realms')), 
           b'preceding': (_readPrecedingData(filterSection)), 
           b'chassisType': (filterSection.readInt(b'chassisType', -1)), 
           b'vehProperty': (filterSection.readString(b'vehProperty', None)), 
           b'notVehProperty': (filterSection.readString(b'notVehProperty', None))}
        for key in _OPTIONAL_FILTER_FLAGS:
            if filterSection.has_key(key):
                filters[filterId][key] = filterSection.readBool(key)

    for _, tipsSection in resource_helper.getIterator(ctx, root[b'tips']):
        filterId = tipsSection.readString(b'filter')
        tipId = tipsSection.readString(b'id')
        status = tipsSection.readString(b'status', DEFAULT_STATUS)
        group = tipsSection.readString(b'group', DEFAULT_GROUP)
        tipFiltersConfig = filters.get(filterId)
        tips[tipId] = {b'filter': tipFiltersConfig, 
           b'status': status, 
           b'group': group}

    resource_helper.purgeResource(prebattleXmlPath)
    return tips


def _readPossibleValues(filterSection, key):
    return frozenset(filterSection.readString(key).split())


def _readPrecedingData(section):
    precedingData = None
    if section[b'preceding'] is not None:
        precedingData = {b'showTimes': (section[b'preceding'].readInt(b'showTimes', _PRECEDING_DEFAULT_SHOW_TIMES))}
    return precedingData
