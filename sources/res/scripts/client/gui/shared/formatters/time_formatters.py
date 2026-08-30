from __future__ import absolute_import, division
import math, time
from gui.Scaleform.locale.MENU import MENU
from gui.impl import backport
from helpers import i18n, time_utils
from rent_common import SeasonRentDuration
from constants import GameSeasonType
from season_common import getDateFromSeasonID
_SEASON_TYPE_KEY = {(GameSeasonType.EPIC): b'epic', 
   (GameSeasonType.RANKED): b'ranked'}

class RentDurationKeys(object):
    SEASON = b'season'
    CYCLE = b'cycle'
    CYCLES = b'cycles'
    TIME = b'time'
    DAYS = b'days'
    HOURS = b'hours'
    MINUTES = b'minutes'
    BATTLES = b'battles'
    WINS = b'wins'


def defaultFormatter(key, countType, count, ctx=None):
    kwargs = ctx.copy() if ctx else {}
    kwargs[countType] = count
    return i18n.makeString((key % countType), **kwargs)


def formatDate(dateFormat, timestamp):
    return time.strftime(i18n.makeString(dateFormat), time_utils.getTimeStructInLocal(timestamp))


def formatTime(timeLeft, divisor, timeStyle=None):
    formattedTime = str(int(math.ceil(float(timeLeft) / divisor)))
    if timeStyle:
        formattedTime = timeStyle(formattedTime)
    return formattedTime


def getTimeLeftInfo(timeLeft, timeStyle=None):
    if timeLeft > 0 and timeLeft != float(b'inf'):
        if timeLeft > time_utils.ONE_DAY:
            return (RentDurationKeys.DAYS, formatTime(timeLeft, time_utils.ONE_DAY, timeStyle))
        return (RentDurationKeys.HOURS, formatTime(timeLeft, time_utils.ONE_HOUR, timeStyle))
    return (b'inf', b'')


def getTimeLeftStr(localization, timeLeft, timeStyle=None, ctx=None, formatter=None):
    if ctx is None:
        ctx = {}
    if formatter is None:
        formatter = defaultFormatter
    result = b''
    timeKey, formattedTime = getTimeLeftInfo(timeLeft, timeStyle)
    if timeKey != b'inf':
        result = formatter(localization, timeKey, formattedTime, ctx)
    return result


def getDueDateOrTimeStr(finishTime, localization=b'', isShortDateFormat=False):
    if not finishTime or time_utils.isPast(finishTime):
        return b''
    if time_utils.isToday(finishTime):
        strTime = backport.getShortTimeFormat(finishTime)
    elif isShortDateFormat:
        strTime = backport.getShortDateFormat(finishTime)
    else:
        strTime = backport.getLongDateFormat(finishTime)
    if localization:
        return (b' ').join([localization, strTime])
    return strTime


def getTimeDurationStr(seconds, useRoundUp=False):
    return time_utils.getTillTimeString(seconds, MENU.TIME_TIMEVALUE, useRoundUp)


def getTillTimeByResource(seconds, resource, useMinutesRoundUp=False, removeLeadingZeros=False, useHoursRoundUp=False):

    def stringGen(key, **kwargs):
        return backport.text(resource.dyn(key)(), **kwargs)

    return time_utils.getTillTimeString(seconds, isMinutesRoundUp=useMinutesRoundUp, sourceStrGenerator=stringGen, removeLeadingZeros=removeLeadingZeros, isHoursRoundUp=useHoursRoundUp)


class RentLeftFormatter(object):

    def __init__(self, rentInfo, isIGR=False):
        super(RentLeftFormatter, self).__init__()
        self.__rentInfo = rentInfo
        self.__isIGR = isIGR
        self.__localizationRootKey = b'#menu:vehicle/rentLeft/%s'
        return

    def getRentLeftStr(self, localization=None, timeStyle=None, ctx=None, formatter=None, strForSpecialTimeFormat=b''):
        activeSeasonRent = self.__rentInfo.getActiveSeasonRent()
        if activeSeasonRent is not None:
            resultStr = self.getRentSeasonLeftStr(activeSeasonRent, localization, formatter, timeStyle, ctx)
        elif self.__rentInfo.getTimeLeft() > 0:
            if strForSpecialTimeFormat:
                finishTime = self.__rentInfo.getTimeLeft() + time_utils.getCurrentTimestamp()
                resultStr = self.getUntilTimeLeftStr(finishTime, strForSpecialTimeFormat)
            else:
                resultStr = self.getRentTimeLeftStr(localization, timeStyle, ctx, formatter)
        elif self.__rentInfo.battlesLeft:
            resultStr = self.getRentBattlesLeftStr(localization, formatter)
        elif self.__rentInfo.winsLeft > 0:
            resultStr = self.getRentWinsLeftStr(localization, formatter)
        else:
            resultStr = b''
        return resultStr

    def getRentTimeLeftStr(self, localization=None, timeStyle=None, ctx=None, formatter=None):
        if self.__isIGR:
            return b''
        else:
            if localization is None:
                localization = self.__localizationRootKey
            return getTimeLeftStr(localization, self.__rentInfo.getTimeLeft(), timeStyle, ctx, formatter)

    def getUntilTimeLeftStr(self, finishTime, localization=b''):
        if self.__isIGR:
            return b''
        return getDueDateOrTimeStr(finishTime, localization)

    def getRentBattlesLeftStr(self, localization=None, formatter=None):
        if localization is None:
            localization = self.__localizationRootKey
        if formatter is None:
            formatter = defaultFormatter
        battlesLeft = self.__rentInfo.battlesLeft
        if battlesLeft > 0:
            return formatter(localization, RentDurationKeys.BATTLES, battlesLeft)
        else:
            return b''

    def getRentWinsLeftStr(self, localization=None, formatter=None):
        if localization is None:
            localization = self.__localizationRootKey
        if formatter is None:
            formatter = defaultFormatter
        winsLeft = self.__rentInfo.winsLeft
        if winsLeft > 0:
            return formatter(localization, RentDurationKeys.WINS, winsLeft)
        else:
            return b''

    def getRentSeasonLeftStr(self, rentData, localization=None, formatter=None, timeStyle=None, ctx=None):
        ctx = ctx or {}
        if localization is None:
            localization = self.__localizationRootKey
        if formatter is None:
            formatter = defaultFormatter
        identifier = None
        timeLeftString = b''
        extraData = {}
        if rentData.seasonType == GameSeasonType.RANKED:
            identifier, timeLeftString, extraData = self.getRentRankedSeasonLeftStr(rentData, timeStyle)
        elif rentData.seasonType == GameSeasonType.EPIC:
            return i18n.makeString(localization % _SEASON_TYPE_KEY[rentData.seasonType] + b'/base')
        ctx.update(extraData)
        if not identifier:
            return b''
        else:
            return formatter(localization % _SEASON_TYPE_KEY[rentData.seasonType] + b'/%s', identifier, timeLeftString, ctx)

    def getRentRankedSeasonLeftStr(self, rentData, timeStyle):
        ctx = {}
        timeLeft = self.__rentInfo.getTimeLeft()
        timeLeftString = formatTime(timeLeft, time_utils.ONE_DAY, timeStyle)
        identifier = RentDurationKeys.DAYS
        if rentData.duration == SeasonRentDuration.ENTIRE_SEASON and timeLeft > time_utils.ONE_WEEK:
            timeLeftString, _ = getDateFromSeasonID(rentData.seasonID)
            identifier = RentDurationKeys.SEASON
        return (identifier, timeLeftString, ctx)
