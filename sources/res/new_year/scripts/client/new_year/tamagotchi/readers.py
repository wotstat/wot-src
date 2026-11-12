import typing
from helpers.time_utils import ONE_MINUTE, getServerUTCTime
from new_year.ny_constants import TamagotchiState
from new_year.tamagotchi.dto.leaderboard import Leaderboard
from new_year.tamagotchi.dto.config import Config
from new_year.tamagotchi.dto.player_info import PlayerInfo
from new_year.tamagotchi.dto.player_stats import PlayerStats
_OptDict = typing.Optional[typing.Dict]
_SeasonList = typing.List[Config.Season.Dto]
_TopConfigList = typing.List[Config.Season.TopConfig.Dto]
_CumulativeDto = typing.Optional[Config.Cumulative.Dto]

def _getUserDataSectionName(cumulative):
    if cumulative:
        return b'cumulative_leaderboard'
    return b'leaderboard'


def _readRewards(rawRewards):
    if not rawRewards:
        return {}
    return rawRewards


def _readStatRewards(rawRewards):
    if not rawRewards:
        return {}
    return _readRewards(rawRewards.get(b'rewards'))


def _readTopConfig(rawTops):
    result = []
    for top in rawTops:
        topDto = Config.Season.TopConfig.Dto()
        topDto.startPos = top[b'start_pos']
        topDto.endPos = top[b'end_pos']
        if b'rewards' in top:
            topDto.rewards = _readRewards(top[b'rewards'])
        result.append(topDto)

    return result


def _readDrawReward(giftReward, drawRewardDto):
    if giftReward is None:
        return
    else:
        drawRewardDto.count = giftReward[b'count']
        if b'rewards' in giftReward:
            drawRewardDto.rewards = _readRewards(giftReward[b'rewards'])
        return


def _readCumulativeConfig(rawCumulative, seasons, eventStartTime, eventEndTime):
    if not isinstance(rawCumulative, dict):
        return None
    else:
        cumulativeDto = Config.Cumulative.Dto()
        cumulativeDto.positionReward = rawCumulative.get(b'position_reward') or b''
        cumulativeDto.topConfig = _readTopConfig(rawCumulative[b'rewards_to_position'])
        _readDrawReward(rawCumulative.get(b'gift_reward'), cumulativeDto.drawReward)
        cumulativeSeasons = [season for season in seasons if season.cumulative]
        if cumulativeSeasons:
            cumulativeDto.startTime = rawCumulative.get(b'start_time', cumulativeSeasons[0].startTime)
            cumulativeDto.endTime = rawCumulative.get(b'end_time', cumulativeSeasons[-1].endTime)
            cumulativeDto.rewardTime = rawCumulative.get(b'reward_time', cumulativeSeasons[-1].rewardTime)
        else:
            cumulativeDto.startTime = rawCumulative.get(b'start_time', eventStartTime)
            cumulativeDto.endTime = rawCumulative.get(b'end_time', eventEndTime)
            cumulativeDto.rewardTime = rawCumulative.get(b'reward_time', cumulativeDto.endTime)
        return cumulativeDto


def _readUserData(userData, cumulative=False):
    userDto = Leaderboard.User.Dto()
    if not userData:
        return userDto
    section = userData.get(_getUserDataSectionName(cumulative))
    if not section:
        return userDto
    userDto.position = section.get(b'position') or 0
    userDto.points = section.get(b'points') or 0
    userDto.pointsByNextPlayer = section.get(b'points_by_next_player') or 0
    userDto.pointsByNextTop = section.get(b'points_by_next_top') or 0
    userDto.rewardsPlaces = section.get(b'rewards_places') or 0
    userDto.upDown = section.get(b'up_down') or 0
    if section.get(b'rewards'):
        userDto.rewards = _readRewards(section[b'rewards'])
    return userDto


def readTamagotchiLeaderboardUser(rawData, cumulative=False):
    userData = rawData.get(b'user_data')
    if not userData or _getUserDataSectionName(cumulative) not in userData:
        return None
    return _readUserData(userData, cumulative=cumulative)


def readTamagotchiConfig(rawData):
    result = Config.Dto()
    result.startTime = rawData[b'start_time']
    result.endTime = rawData[b'end_time']
    result.raidScalePoint = rawData[b'raid_scale_point']
    result.currentSeason = None
    leaderboards = rawData[b'leaderboards']
    now = getServerUTCTime()
    for seasonId, season in enumerate(leaderboards[b'seasons'], start=1):
        seasonDto = Config.Season.Dto()
        seasonDto.id = int(seasonId)
        seasonDto.rewardTime = season[b'reward_time']
        seasonDto.startTime = season[b'start_time']
        seasonDto.endTime = season[b'end_time']
        seasonDto.cumulative = bool(season.get(b'cumulative', False))
        seasonDto.resetPoints = bool(season.get(b'reset_points', True))
        seasonDto.positionReward = season.get(b'position_reward') or b''
        seasonDto.topConfig = _readTopConfig(season[b'rewards_to_position'])
        _readDrawReward(season.get(b'gift_reward'), seasonDto.drawReward)
        if seasonDto.startTime <= now <= seasonDto.endTime:
            result.currentSeason = seasonDto
        result.seasons.append(seasonDto)

    result.cumulative = _readCumulativeConfig(leaderboards.get(b'cumulative'), result.seasons, result.startTime, result.endTime)
    for attrName, value in rawData.get(b'states', {}).iteritems():
        state = Config.States.Dto()
        state.min = value[b'scale_sum_level_min']
        state.max = value[b'scale_sum_level_max']
        result.states[attrName] = state

    for attrName, value in rawData[b'indicators'].iteritems():
        indicator = Config.Indicators.Dto()
        indicator.maxPoints = value[b'maxPoint']
        result.indicators[attrName] = indicator
        for state, level in enumerate(value[b'levels']):
            levelDto = Config.Indicators.Level.Dto()
            levelDto.debPercent = level[b'debPercent']
            levelDto.degradation = level[b'degradation']
            levelDto.loyalty = level[b'loyalty']
            levelDto.points = level[b'point']
            levelDto.state = state
            indicator.levels.append(levelDto)

    for item in rawData[b'items']:
        itemDto = result.indicators[item[b'type']].item
        itemDto.id = item[b'id']
        itemDto.dynCurrencyCode = item[b'currency_code']
        itemDto.leaderboardPoint = item[b'leaderboard_point']
        itemDto.currency = item[b'price'][b'currency']
        itemDto.price = item[b'price'][b'amount']
        itemDto.scalePoint = item[b'scale_point']

    return result


def readTamagotchiLeaderboard(rawData, cumulative=False):
    result = Leaderboard.Dto()
    result.updateTime = rawData.get(b'update_time')
    if result.updateTime is None:
        result.updateTime = getServerUTCTime()
    result.nextUpdateTime = rawData.get(b'next_update_time')
    if result.nextUpdateTime is None:
        result.nextUpdateTime = result.updateTime + ONE_MINUTE * 5
    result.isRecalcTime = rawData.get(b'is_recalc_time', False)
    result.cumulative = cumulative
    pageData = rawData[b'page_data']
    pageDto = result.page
    pageDto.totalPage = pageData[b'total_page']
    pageDto.currentPage = pageData[b'current_page']
    for row in pageData[b'leaderboard']:
        rowDto = Leaderboard.Page.Row.Dto()
        rowDto.spaId = row[b'spa_id']
        rowDto.position = row[b'position']
        rowDto.point = row[b'point']
        rowDto.nickname = row[b'nickname']
        rowDto.upDown = row[b'up_down']
        pageDto.leaderboard.append(rowDto)

    result.user = _readUserData(rawData.get(b'user_data'), cumulative=cumulative)
    return result


def _readTamagotchiWeekStat(rawWeekStat):
    weekStat = PlayerStats.WeekStat.Dto()
    weekStat.week = rawWeekStat[b'week'] + 1
    weekStat.position = rawWeekStat[b'position']
    weekStat.point = rawWeekStat[b'point']
    weekStat.isRewarded = rawWeekStat[b'isRewarded']
    weekStat.rewardedDate = rawWeekStat[b'rewarded_date']
    weekStat.rewards = _readStatRewards(rawWeekStat.get(b'rewards'))
    return weekStat


def readTamagotchiPlayerInfo(rawData, lastPlayerInfo=None):
    result = PlayerInfo.Dto()
    result.state = rawData.get(b'state', lastPlayerInfo.state if lastPlayerInfo is not None else TamagotchiState.SAD.value)
    result.leaderboardPoint = rawData[b'leaderboard_point']
    result.cumulativePoint = rawData[b'cumulative_point']
    result.lastUpdateTime = rawData[b'last_update']
    result.indicators = rawData[b'indicators']
    for rawDebHist in rawData[b'deb_history']:
        hist = PlayerInfo.DebHistory.Dto()
        hist.value = rawDebHist[b'value']
        hist.expirationTime = rawDebHist[b'expired_date']
        result.debHistory.append(hist)

    return result


def readTamagotchiPlayerStats(rawData):
    result = PlayerStats.Dto()
    result.leaderboardPoint = rawData[b'leaderboard_point']
    for rawWeekStat in rawData[b'week_stats']:
        result.weekStats.append(_readTamagotchiWeekStat(rawWeekStat))

    rawCumulativeStat = rawData.get(b'cumulative_stat')
    if rawCumulativeStat is not None:
        result.cumulativeStats.append(_readTamagotchiWeekStat(rawCumulativeStat))
    return result
