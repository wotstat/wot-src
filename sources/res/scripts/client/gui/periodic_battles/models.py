import logging
from functools import partial
import typing
from enum import Enum
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.utils.decorators import ReprInjector
from gui.shared.utils.functions import makeTooltip
from helpers import time_utils
from shared_utils import collapseIntervals, findFirst, first, CONST_CONTAINER
if typing.TYPE_CHECKING:
    from gui.impl.gen_utils import DynAccessor
    from season_common import GameSeason, GameSeasonCycle
_logger = logging.getLogger(__name__)

class PrimeTimeStatus(CONST_CONTAINER):
    NOT_SET = 1
    FROZEN = 2
    NOT_AVAILABLE = 3
    AVAILABLE = 4


class PeriodType(Enum):
    UNDEFINED = b'undefined'
    BEFORE_SEASON = b'beforeSeason'
    BETWEEN_SEASONS = b'betweenSeasons'
    AFTER_SEASON = b'afterSeason'
    BEFORE_CYCLE = b'beforeCycle'
    BETWEEN_CYCLES = b'betweenCycles'
    AFTER_CYCLE = b'afterCycle'
    AVAILABLE = b'available'
    FROZEN = b'frozen'
    NOT_AVAILABLE = b'notAvailable'
    ALL_NOT_AVAILABLE = b'allNotAvailable'
    STANDALONE_NOT_AVAILABLE = b'standaloneNotAvailable'
    NOT_AVAILABLE_END = b'notAvailableEnd'
    ALL_NOT_AVAILABLE_END = b'allNotAvailableEnd'
    STANDALONE_NOT_AVAILABLE_END = b'standaloneNotAvailableEnd'
    NOT_SET = b'notSet'
    ALL_NOT_SET = b'allNotSet'
    STANDALONE_NOT_SET = b'standaloneNotSet'


PERIOD_TO_STANDALONE = {(PeriodType.FROZEN): (PeriodType.FROZEN), 
   (PeriodType.AVAILABLE): (PeriodType.AVAILABLE), 
   (PeriodType.NOT_AVAILABLE): (PeriodType.STANDALONE_NOT_AVAILABLE), 
   (PeriodType.ALL_NOT_AVAILABLE): (PeriodType.STANDALONE_NOT_AVAILABLE), 
   (PeriodType.NOT_SET): (PeriodType.STANDALONE_NOT_SET), 
   (PeriodType.ALL_NOT_SET): (PeriodType.STANDALONE_NOT_SET), 
   (PeriodType.NOT_AVAILABLE_END): (PeriodType.STANDALONE_NOT_AVAILABLE_END), 
   (PeriodType.ALL_NOT_AVAILABLE_END): (PeriodType.STANDALONE_NOT_AVAILABLE_END)}

@ReprInjector.simple(b'userName', b'timestamp', b'techData')
class PeriodBorder(object):
    __slots__ = (b'userName', b'timestamp', b'techData')
    _TECH_FIELD_FMT = b'{techName}{fieldName}'

    def __init__(self, userName, timestamp):
        self.userName = userName
        self.timestamp = timestamp
        self.techData = {b'Name': b'', 
           b'Time': b'', 
           b'Date': b'', 
           b'Delta': b''}
        return

    def delta(self, now):
        return abs(now - self.timestamp)

    def setTechName(self, techName):
        data = self.techData
        for fieldName in data:
            data[fieldName] = self._TECH_FIELD_FMT.format(techName=techName, fieldName=fieldName)

        return


@ReprInjector.simple(b'now', b'periodType', b'seasonBorderLeft', b'seasonBorderRight', b'cycleBorderLeft', b'cycleBorderRight', b'primeDelta')
class PeriodInfo(object):
    __slots__ = (b'now', b'periodType', b'seasonBorderLeft', b'seasonBorderRight', b'cycleBorderLeft', b'cycleBorderRight', b'primeDelta', b'borders')

    def __init__(self, now, pType, seasonLeft=None, seasonRight=None, cycleLeft=None, cycleRight=None, primeDelta=0):
        self.now = now
        self.periodType = pType
        self.seasonBorderLeft = self.__addBorderTechName(seasonLeft, b'leftSeason')
        self.seasonBorderRight = self.__addBorderTechName(seasonRight, b'rightSeason')
        self.cycleBorderLeft = self.__addBorderTechName(cycleLeft, b'leftCycle')
        self.cycleBorderRight = self.__addBorderTechName(cycleRight, b'rightCycle')
        self.primeDelta = primeDelta
        bordersWithNones = (self.seasonBorderLeft, self.cycleBorderLeft, self.cycleBorderRight, self.seasonBorderRight)
        self.borders = tuple(border for border in bordersWithNones if border is not None)
        return

    @staticmethod
    def defaultDeltaFormatter(resRoot):
        return partial(backport.getTillTimeStringByRClass, stringRClass=resRoot)

    @staticmethod
    def leftSeasonBorder(season):
        if season:
            return PeriodBorder(season.getUserName(), season.getStartDate())
        else:
            return

    @staticmethod
    def rightSeasonBorder(season):
        if season:
            return PeriodBorder(season.getUserName(), season.getEndDate())
        else:
            return

    @staticmethod
    def leftCycleBorder(cycle):
        if cycle:
            return PeriodBorder(cycle.getUserName(), cycle.startDate)
        else:
            return

    @staticmethod
    def rightCycleBorder(cycle):
        if cycle:
            return PeriodBorder(cycle.getUserName(), cycle.endDate)
        else:
            return

    def getVO(self, withBNames=False, withBDeltas=False, deltaFmt=None, timeFmt=None, dateFmt=None):
        result = self.__buildNames() if withBNames else {}
        if deltaFmt is not None:
            self.__buildDeltas(result, deltaFmt, withBDeltas)
        if timeFmt is not None or dateFmt is not None:
            self.__buildDates(result, timeFmt, dateFmt)
        return result

    def __addBorderTechName(self, border, techName):
        if border is not None:
            border.setTechName(techName)
        return border

    def __buildDeltas(self, result, deltaFormatter, bordersDeltas):
        result[b'primeDelta'] = deltaFormatter(self.primeDelta)
        if bordersDeltas:
            for border in self.borders:
                result[border.techData[b'Delta']] = deltaFormatter(border.delta(self.now))

        return

    def __buildDates(self, result, timeFormatter, dateFormatter):
        primeDeltaStamp = self.primeDelta + self.now
        if timeFormatter is not None:
            result[b'primeDeltaTime'] = timeFormatter(primeDeltaStamp)
            for border in self.borders:
                result[border.techData[b'Time']] = timeFormatter(border.timestamp)

        if dateFormatter is not None:
            result[b'primeDeltaDate'] = dateFormatter(primeDeltaStamp)
            for border in self.borders:
                result[border.techData[b'Date']] = dateFormatter(border.timestamp)

        return

    def __buildNames(self):
        return {border.techData[b'Name']: border.userName for border in self.borders}


class PrimeTime(object):

    def __init__(self, peripheryID, periods=None):
        super(PrimeTime, self).__init__()
        self.__peripheryID = peripheryID
        self.__periods = periods or {}
        return

    def hasAnyPeriods(self):
        return bool(self.__periods)

    def getAvailability(self, forTime, cycleEnd):
        periods = self.getPeriodsBetween(forTime, cycleEnd)
        if periods:
            periodsIter = iter(periods)
            currentPeriod = findFirst((lambda (pS, pE): pS <= forTime < pE), periodsIter)
            if currentPeriod is not None:
                _, currentPeriodEnd = currentPeriod
                return (
                 True, currentPeriodEnd - forTime)
            nextPeriod = first(periods)
            if nextPeriod is not None:
                nextPeriodStart, _ = nextPeriod
                return (
                 False, nextPeriodStart - forTime)
        return (
         False, 0)

    def getNextPeriodStart(self, fromTime, tillTime, includeBeginning=False):
        periods = self.getPeriodsBetween(fromTime, tillTime, includeBeginning=includeBeginning)
        if periods:
            nextPeriod = first(periods)
            if nextPeriod is not None:
                nextPeriodStart, _ = nextPeriod
                return nextPeriodStart
        return

    def getPeriodsActiveForTime(self, periodTime, preferPeriodBounds=False):
        return self.getPeriodsBetween(periodTime, periodTime, preferPeriodBounds=preferPeriodBounds)

    def getPeriodsBetween(self, startTime, endTime, includeBeginning=True, includeEnd=True, preferPeriodBounds=False):
        periods = []
        startDateTime = time_utils.getDateTimeInUTC(startTime)
        startTimeDayStart, _ = time_utils.getDayTimeBoundsForUTC(startTime)
        weekDay = startDateTime.isoweekday()
        while startTimeDayStart <= endTime:
            if weekDay in self.__periods:
                for (startH, startM), (endH, endM) in self.__periods[weekDay]:
                    periodStartTime = startTimeDayStart + startH * time_utils.ONE_HOUR + startM * time_utils.ONE_MINUTE
                    periodEndTime = startTimeDayStart + endH * time_utils.ONE_HOUR + endM * time_utils.ONE_MINUTE
                    if startTime < periodEndTime and periodStartTime <= endTime:
                        if not includeBeginning and startTime > periodStartTime:
                            continue
                        if not includeEnd and endTime < periodEndTime:
                            continue
                        if preferPeriodBounds:
                            periods.append((periodStartTime, periodEndTime))
                        else:
                            periods.append((max(startTime, periodStartTime), min(endTime, periodEndTime)))

            if weekDay == time_utils.WEEK_END:
                weekDay = time_utils.WEEK_START
            else:
                weekDay += 1
            startTimeDayStart += time_utils.ONE_DAY

        return collapseIntervals(periods)


class AlertData(object):
    _RES_ROOT = None
    _PERIOD_TYPES_WITH_BUTTON = (PeriodType.NOT_AVAILABLE, PeriodType.NOT_AVAILABLE_END, PeriodType.NOT_SET)
    _PERIOD_TYPES_PRIME_ALERT = (
     PeriodType.AVAILABLE, PeriodType.NOT_AVAILABLE_END,
     PeriodType.NOT_SET, PeriodType.ALL_NOT_SET, PeriodType.STANDALONE_NOT_SET,
     PeriodType.NOT_AVAILABLE, PeriodType.ALL_NOT_AVAILABLE, PeriodType.STANDALONE_NOT_AVAILABLE)
    _RES_REASON_ROOT = None
    __slots__ = (b'alertIcon', b'buttonIcon', b'buttonLabel', b'buttonVisible', b'buttonTooltip', b'statusText', b'popoverAlias', b'bgVisible', b'shadowFilterVisible', b'tooltip', b'isSimpleTooltip', b'isWulfTooltip')

    def __init__(self, alertIcon=None, buttonIcon=b'', buttonLabel=b'', buttonVisible=False, buttonTooltip=None, statusText=b'', popoverAlias=None, bgVisible=True, shadowFilterVisible=False, tooltip=None, isSimpleTooltip=False, isWulfTooltip=False):
        self.alertIcon = alertIcon
        self.buttonIcon = buttonIcon
        self.buttonLabel = buttonLabel
        self.buttonVisible = buttonVisible
        self.buttonTooltip = buttonTooltip
        self.statusText = statusText
        self.popoverAlias = popoverAlias
        self.bgVisible = bgVisible
        self.shadowFilterVisible = shadowFilterVisible
        self.tooltip = tooltip
        self.isSimpleTooltip = isSimpleTooltip
        self.isWulfTooltip = isWulfTooltip
        return

    @classmethod
    def construct(cls, periodInfo, serverShortName):
        isPrimeAlert = periodInfo.periodType in cls._PERIOD_TYPES_PRIME_ALERT
        return cls(alertIcon=backport.image(R.images.gui.maps.icons.library.alertBigIcon()) if isPrimeAlert else None, buttonLabel=backport.text(cls._RES_ROOT.button.changeServer()), buttonVisible=periodInfo.periodType in cls._PERIOD_TYPES_WITH_BUTTON, statusText=text_styles.vehicleStatusCriticalText(cls._getAlertLabel(periodInfo, serverShortName)), shadowFilterVisible=isPrimeAlert, tooltip=cls._getTooltip(periodInfo))

    @classmethod
    def constructForVehicle(cls, levelsStr, vehicleIsAvailableForBuy, vehicleIsAvailableForRestore, tooltip=None):
        if cls._RES_REASON_ROOT is None:
            _logger.error(b'AlertData._RES_REASON_ROOT is None. Please define it to use constructForVehicle method!')
        reason = cls._RES_REASON_ROOT.vehicleUnavailable()
        if vehicleIsAvailableForBuy:
            reason = cls._RES_REASON_ROOT.vehicleAvailableForBuy()
        elif vehicleIsAvailableForRestore:
            reason = cls._RES_REASON_ROOT.vehicleAvailableForRestore()
        tooltipValue = tooltip if tooltip is not None else makeTooltip(body=backport.text(reason, levels=levelsStr))
        return cls(alertIcon=backport.image(R.images.gui.maps.icons.library.alertBigIcon()), buttonLabel=backport.text(cls._RES_ROOT.button.moreInfo()), buttonVisible=True, statusText=text_styles.vehicleStatusCriticalText(backport.text(cls._RES_ROOT.unsuitableVehicles(), levels=levelsStr)), shadowFilterVisible=True, tooltip=tooltipValue, isSimpleTooltip=tooltip is None, isWulfTooltip=False)

    def asDict(self):
        return {b'alertIcon': (self.alertIcon), 
           b'buttonIcon': (self.buttonIcon), 
           b'buttonLabel': (self.buttonLabel), 
           b'buttonVisible': (self.buttonVisible), 
           b'buttonTooltip': (self.buttonTooltip), 
           b'statusText': (self.statusText), 
           b'popoverAlias': (self.popoverAlias), 
           b'bgVisible': (self.bgVisible), 
           b'shadowFilterVisible': (self.shadowFilterVisible), 
           b'tooltip': (self.tooltip), 
           b'isSimpleTooltip': (self.isSimpleTooltip), 
           b'isWulfTooltip': (self.isWulfTooltip)}

    @classmethod
    def _getAlertLabel(cls, periodInfo, serverShortName):
        params = cls._getAlertLabelParams(periodInfo)
        params[b'serverName'] = serverShortName
        return backport.text(cls._RES_ROOT.dyn(periodInfo.periodType.value, cls._RES_ROOT.undefined)(), **params)

    @classmethod
    def _getAlertLabelParams(cls, periodInfo):
        return periodInfo.getVO(withBNames=True, deltaFmt=PeriodInfo.defaultDeltaFormatter(cls._RES_ROOT.timeLeft))

    @classmethod
    def _getTooltip(cls, periodInfo):
        return
