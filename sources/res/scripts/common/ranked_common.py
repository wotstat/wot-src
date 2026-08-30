import season_common

def getShieldsConfig(rankedConfig, now):
    result = {}
    res, seasonInfo = season_common.getSeason(rankedConfig, now)
    if not res:
        return result
    _, _, seasonID, cycleID = seasonInfo
    season = rankedConfig[b'seasons'].get(seasonID)
    if season:
        cycle = season[b'cycles'].get(cycleID, {})
        result.update(cycle.get(b'shields', rankedConfig[b'shields']))
    return result


class SwitchState(object):
    ENABLED = b'enabled'
    DISABLED = b'disabled'
    HIDDEN = b'hidden'
    ALL = (b'enabled', b'disabled', b'hidden')
