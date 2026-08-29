EARLY_ACCESS_PREFIX = b'early_access'
EARLY_ACCESS_PDATA_KEY = b'earlyAccess'
EARLY_ACCESS_POSTPR_KEY = b'postprogression'

def earlyAccessInitialData():
    return {b'currentSeason': None}


def isEarlyAccessToken(tokenName):
    return tokenName.startswith(EARLY_ACCESS_PREFIX)


def makeEarlyAccessToken(seasonID):
    return (b':').join((EARLY_ACCESS_PREFIX, (b'season_{}').format(seasonID)))


def getGroupName(groupName):
    if groupName == EARLY_ACCESS_POSTPR_KEY:
        return (b'_').join((EARLY_ACCESS_PREFIX, (b'{}').format(groupName)))
    return (b'_').join((EARLY_ACCESS_PREFIX, (b'cycle_{}').format(groupName)))


def getQuestFinisherName(seasonID):
    return (b'_').join((EARLY_ACCESS_PREFIX, (b'quests_finisher_season_{}').format(seasonID)))
