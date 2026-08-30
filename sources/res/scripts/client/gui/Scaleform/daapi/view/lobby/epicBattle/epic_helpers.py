import logging
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import time_formatters, text_styles
from gui.periodic_battles.models import AlertData, PrimeTimeStatus
from helpers import dependency, i18n, time_utils
from items import vehicles
from items.components.supply_slot_categories import SlotCategories
from shared_utils import first
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.game_control import IEpicBattleMetaGameController
_logger = logging.getLogger(__name__)
FRONTLINE_HIDDEN_TAG = b'fr_hidden'
_EPIC_GAME_PARAMS = {b'artillery': {b'cooldownTime': b'Cooldown', 
                  b'delay': b'Deployment', 
                  b'areaRadius': b'Dispersion', 
                  b'shotsNumber': b'Shells', 
                  b'duration-artillery': b'Duration'}, 
   b'bomber': {b'cooldownTime': b'Cooldown', 
               b'delay': b'Deployment', 
               b'areaLength_areaWidth-dropArea': b'Targeted Area', 
               b'bombsNumber': b'Bombs', 
               b'shellCompactDescr': b'Stun'}, 
   b'recon': {b'cooldownTime': b'Cooldown', 
              b'delay-recon': b'Deployment_ReconFlight', 
              b'#epic_battle:abilityInfo/params/recon/revealedArea/value': b'Revealed Area', 
              b'entitiesToSearch/Vehicle/spottingDuration': b'Spotting Duration'}, 
   b'inspire': {b'cooldownTime': b'Cooldown', 
                b'radius': b'Effect Radius', 
                b'duration-inspire': b'Duration', 
                b'increaseFactors/crewRolesFactor': b'Crew Performance', 
                b'selfIncreaseFactors/crewRolesFactor': b'Self crew Perfomance', 
                b'inactivationDelay': b'Effect Cooldown'}, 
   b'smoke': {b'cooldownTime': b'Cooldown', 
              b'minDelay': b'Deployment', 
              b'areaLength_areaWidth-targetedArea': b'Targeted Area (length, width)', 
              b'projectilesNumber': b'Grenades', 
              b'totalDuration': b'Smoke Lifetime', 
              b'attrFactorMods/circularVisionRadius': b'visionRadiusFactor', 
              b'attrFactorMods/crewRolesFactor': b'crewRoles'}, 
   b'passive_engineering': {b'resupplyCooldownFactor': b'Resupply Circle Refresh', 
                            b'resupplyHealthPointsFactor': b'Resupply Speed', 
                            b'captureSpeedFactor': b'Capture Speed', 
                            b'captureBlockBonusTime': b'Capture Block Time', 
                            b'resupplyShellsFactor': b'Speed of shells supply'}, 
   b'arcade_minefield': {b'cooldownTime': b'Cooldown', 
                         b'bombsNumber-minefield': b'Mines', 
                         b'mineParams/lifetime': b'Duration_MineField', 
                         b'mineParams/shell': b'Stun'}, 
   b'regenerationKit': {b'cooldownTime': b'Cooldown', 
                        b'healTime': b'HealTime', 
                        b'healthRegenPerTick': b'RegenPerTick', 
                        b'initialHeal': b'InitialHeal', 
                        b'resupplyHealthPointsFactor': b'ResupplyHealthPointsFactor', 
                        b'#epic_battle:abilityInfo/params/fl_regenerationKit/minesDamageReduceFactor/value': b'MinesDamageReduceFactor'}, 
   b'stealthRadar': {b'passiveCircularVisionRadius': b'PassiveCircularVisionRadius', 
                     b'duration-stealth_radar': b'Duration_Stealth', 
                     b'cooldownTime': b'Cooldown', 
                     b'inactivationDelay': b'ActivationDelay', 
                     b'overridableFactors/invisibility': b'InvisibilityAdditiveTerm', 
                     b'increaseFactors/demaskMovingFactor': b'DemaskMovingFactor', 
                     b'increaseFactors/demaskFoliageFactor': b'DemaskFoliageFactor'}}

def _getAttrName(param):
    return param.split(b'-')[0]


def _cutDigits(value):
    if abs(value) > 99:
        return round(value)
    if abs(value) > 9:
        return round(value, 1)
    return round(value, 3)


def _getFormattedNum(value):
    cutValue = _cutDigits(value)
    if cutValue.is_integer():
        return int(cutValue)
    return cutValue


class AbilityParam(object):

    @classmethod
    def updateParams(cls, curEq, param):
        raise NotImplementedError
        return


class DisplayValuesMixin(object):

    @classmethod
    def _getParamValue(cls, curEq, param):
        raise NotImplementedError
        return


class DirectValuesMixin(DisplayValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        param = _getAttrName(param)
        curValue = getattr(curEq, param)
        return _getFormattedNum(curValue)


class NestedValuesMixin(DisplayValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        param = _getAttrName(param)
        params = param.split(b'/')
        curValue = cls._getEqParam(curEq, params)
        return _getFormattedNum(curValue)

    @classmethod
    def _getEqParam(cls, eq, params):
        data = {}
        if hasattr(eq, params[0]):
            data = getattr(eq, params[0])
        for key in params[1:]:
            if isinstance(data, dict):
                data = data.get(key, {})
            elif hasattr(data, key):
                data = getattr(data, key)

        return data


class PercentValueMixin(DirectValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        value = super(PercentValueMixin, cls)._getParamValue(curEq, param)
        return value * 100 - 100


class AbsPercentValueMixin(DirectValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        value = super(AbsPercentValueMixin, cls)._getParamValue(curEq, param)
        return abs(value * 100 - 100)


class NestedPercentValueMixin(NestedValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        value = super(NestedPercentValueMixin, cls)._getParamValue(curEq, param)
        return value * 100 - 100


class NestedAbsPercentTupleValueMixin(NestedValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        param = _getAttrName(param)
        params = param.split(b'/')
        curValue = cls._getEqParam(curEq, params)
        return abs(_getFormattedNum(curValue[0]) * 100)


class DirectPercentValueMixin(DirectValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        value = super(DirectPercentValueMixin, cls)._getParamValue(curEq, param)
        return value * 100


class NestedDirectPercentValueMixin(NestedValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        value = super(NestedDirectPercentValueMixin, cls)._getParamValue(curEq, param)
        return value * 100


class ReciprocalValuesMixin(DisplayValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        param = _getAttrName(param)
        curValue = getattr(curEq, param)
        curValue = 1 / curValue if curValue != 0 else float(b'inf')
        curValue = curValue * 100 - 100
        return _getFormattedNum(curValue)


class ShellStunValuesMixin(DisplayValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        param = _getAttrName(param)
        curShell = vehicles.getItemByCompactDescr(getattr(curEq, param))
        curValue = curShell.stun.stunDuration if curShell.hasStun else 0
        return _getFormattedNum(curValue)


class NestedShellStunValuesMixin(NestedValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        curValue = 0
        shellID = super(NestedShellStunValuesMixin, cls)._getParamValue(curEq, param)
        curShell = vehicles.getItemByCompactDescr(shellID)
        if curShell:
            curValue = curShell.stun.stunDuration if curShell.hasStun else 0
        return _getFormattedNum(curValue)


class MultiValuesMixin(DisplayValuesMixin):

    @classmethod
    def _getParamValue(cls, curEq, param):
        param = _getAttrName(param)
        params = param.split(b'_')
        length = len(params)
        curValues = [None] * length
        for idx, singleParam in enumerate(params):
            curValues[idx] = _getFormattedNum(getattr(curEq, singleParam))

        return curValues


class TextParam(AbilityParam, DisplayValuesMixin):

    @classmethod
    def updateParams(cls, curEq, param):
        return cls._getParamValue(curEq, param)


class MultiTextParam(AbilityParam, DisplayValuesMixin):

    @classmethod
    def updateParams(cls, curEq, param):
        values = cls._getParamValue(curEq, param)
        unitLocalization = backport.text(R.strings.ingame_gui.marker.meters())
        value = (b' x ').join(str(value) for value in values)
        value = (b'{} {}').format(value, unitLocalization)
        return value


class FixedTextParam(AbilityParam):

    @classmethod
    def updateParams(cls, curEq, param):
        return i18n.makeString(param)


class DirectNumericTextParam(TextParam, DirectValuesMixin):
    pass


class DirectSecondsTextParam(TextParam, DirectValuesMixin):
    pass


class DirectMetersTextParam(TextParam, DirectValuesMixin):
    pass


class NestedNumericTextParam(TextParam, NestedValuesMixin):
    pass


class NestedMetersTextParam(TextParam, NestedValuesMixin):
    pass


class PercentNumericTextParam(TextParam, PercentValueMixin):
    pass


class AbsPercentNumericTextParam(TextParam, AbsPercentValueMixin):
    pass


class NestedPercentNumericTextParam(TextParam, NestedPercentValueMixin):
    pass


class NestedAbsPercentNumbericTextParam(TextParam, NestedAbsPercentTupleValueMixin):
    pass


class DirectPercentNumericTextParam(TextParam, DirectPercentValueMixin):
    pass


class NestedDirectPercentNumericTextParam(TextParam, NestedDirectPercentValueMixin):
    pass


class ReciprocalNumericTextParam(TextParam, ReciprocalValuesMixin):
    pass


class ShellStunSecondsDeltaBarParam(TextParam, ShellStunValuesMixin):
    pass


class NestedShellStunSecondsDeltaBarParam(TextParam, NestedShellStunValuesMixin):
    pass


class MultipleMetersTextParam(MultiTextParam, MultiValuesMixin):
    pass


epicEquipmentParameterFormaters = {b'cooldownTime': (DirectNumericTextParam.updateParams), 
   b'delay': (DirectNumericTextParam.updateParams), 
   b'delay-recon': (DirectNumericTextParam.updateParams), 
   b'areaRadius': (DirectNumericTextParam.updateParams), 
   b'shotsNumber': (DirectNumericTextParam.updateParams), 
   b'duration-inspire': (DirectNumericTextParam.updateParams), 
   b'duration-artillery': (DirectNumericTextParam.updateParams), 
   b'areaLength_areaWidth-targetedArea': (MultipleMetersTextParam.updateParams), 
   b'areaLength_areaWidth-dropArea': (MultipleMetersTextParam.updateParams), 
   b'bombsNumber': (DirectNumericTextParam.updateParams), 
   b'shellCompactDescr': (ShellStunSecondsDeltaBarParam.updateParams), 
   b'#epic_battle:abilityInfo/params/recon/revealedArea/value': (FixedTextParam.updateParams), 
   b'entitiesToSearch/Vehicle/spottingDuration': (NestedNumericTextParam.updateParams), 
   b'minDelay': (DirectNumericTextParam.updateParams), 
   b'projectilesNumber': (DirectNumericTextParam.updateParams), 
   b'totalDuration': (DirectNumericTextParam.updateParams), 
   b'increaseFactors[crewRolesFactor]': (NestedPercentNumericTextParam.updateParams), 
   b'inactivationDelay': (DirectNumericTextParam.updateParams), 
   b'resupplyCooldownFactor': (ReciprocalNumericTextParam.updateParams), 
   b'resupplyHealthPointsFactor': (PercentNumericTextParam.updateParams), 
   b'captureSpeedFactor': (PercentNumericTextParam.updateParams), 
   b'captureBlockBonusTime': (DirectNumericTextParam.updateParams), 
   b'mineParams/lifetime': (NestedNumericTextParam.updateParams), 
   b'mineParams/shell': (NestedShellStunSecondsDeltaBarParam.updateParams), 
   b'healTime': (DirectNumericTextParam.updateParams), 
   b'healthRegenPerTick': (DirectPercentNumericTextParam.updateParams), 
   b'initialHeal': (DirectPercentNumericTextParam.updateParams), 
   b'duration-stealth_radar': (DirectSecondsTextParam.updateParams), 
   b'overridableFactors/invisibility': (NestedDirectPercentNumericTextParam.updateParams), 
   b'increaseFactors/demaskMovingFactor': (NestedPercentNumericTextParam.updateParams), 
   b'increaseFactors/demaskFoliageFactor': (NestedPercentNumericTextParam.updateParams), 
   b'passiveCircularVisionRadius': (DirectMetersTextParam.updateParams), 
   b'bombsNumber-minefield': (DirectNumericTextParam.updateParams), 
   b'increaseFactors/crewRolesFactor': (NestedPercentNumericTextParam.updateParams), 
   b'selfIncreaseFactors/crewRolesFactor': (NestedPercentNumericTextParam.updateParams), 
   b'resupplyShellsFactor': (PercentNumericTextParam.updateParams), 
   b'#epic_battle:abilityInfo/params/fl_regenerationKit/minesDamageReduceFactor/value': (FixedTextParam.updateParams), 
   b'attrFactorMods/circularVisionRadius': (NestedAbsPercentNumbericTextParam.updateParams), 
   b'attrFactorMods/crewRolesFactor': (NestedAbsPercentNumbericTextParam.updateParams), 
   b'radius': (DirectMetersTextParam.updateParams)}

def checkIfVehicleIsHidden(intCD):
    return FRONTLINE_HIDDEN_TAG in vehicles.getVehicleType(intCD).tags


@dependency.replace_none_kwargs(epicController=IEpicBattleMetaGameController)
def isVehLevelUnlockableInBattle(vehLevel, epicController=None):
    return vehLevel in epicController.getModeSettings().unlockableInBattleVehLevels


def getFrontLineSkills():
    epicMetaGameCtrl = dependency.instance(IEpicBattleMetaGameController)
    equipments = vehicles.g_cache.equipments()
    result = []
    for skillID, skillData in epicMetaGameCtrl.getAllSkillsInformation().iteritems():
        skillInfo = dict()
        firstSkill = first(skillData.levels.itervalues())
        skillInfo[b'icon'] = firstSkill.icon
        skillInfo[b'longDescr'] = firstSkill.longDescr
        skillInfo[b'name'] = firstSkill.name
        skillInfo[b'shortDescr'] = firstSkill.shortDescr
        skillInfo[b'skillID'] = skillID
        skillInfo[b'longFilterAlert'] = firstSkill.longFilterAlert
        skillInfo[b'price'] = skillData.price
        skillInfo[b'category'] = first(SlotCategories.ALL.intersection(skillData.tags))
        skillInfo[b'params'] = dict()
        for _, skillLevelData in skillData.levels.iteritems():
            skillInfo.setdefault(b'levels', []).append(skillLevelData.eqID)
            curLvlEq = equipments[skillLevelData.eqID]
            for tooltipIdentifier in curLvlEq.tooltipIdentifiers:
                paramName = _EPIC_GAME_PARAMS.get(skillLevelData.icon, {}).get(tooltipIdentifier)
                if not paramName:
                    _logger.error(b'[ERROR] getFrontLineSkills: Failed to find tooltipInfo %(ttid)s.', {b'ttid': tooltipIdentifier})
                    continue
                param = createEpicParam(curLvlEq, tooltipIdentifier)
                if param:
                    skillInfo[b'params'].setdefault(paramName, []).append(param)
                else:
                    skillInfo[b'params'].setdefault(paramName, [])

        result.append(skillInfo)

    return result


def createEpicParam(curLvlEq, tooltipIdentifier):
    formatter = epicEquipmentParameterFormaters.get(tooltipIdentifier)
    if formatter:
        return formatter(curLvlEq, tooltipIdentifier)
    else:
        return


def getTimeToEndStr(timeStamp):
    return backport.text(R.strings.epic_battle.tooltips.timeToEnd(), timeLeft=_getTimeLeftStr(timeStamp))


def getTimeToStartStr(timeStamp):
    return backport.text(R.strings.epic_battle.tooltips.timeToStart(), timeLeft=_getTimeLeftStr(timeStamp))


def getOfferTokenByGift(tokenID):
    return tokenID.replace(b'_gift', b'')


@dependency.replace_none_kwargs(epicController=IEpicBattleMetaGameController)
def getAlertStatusVO(epicController=None):
    status, timeLeft, _ = epicController.getPrimeTimeStatus()
    showPrimeTimeAlert = status != PrimeTimeStatus.AVAILABLE
    hasAvailableServers = epicController.hasAvailablePrimeTimeServers()
    return AlertData(alertIcon=backport.image(R.images.gui.maps.icons.library.alertBigIcon()) if showPrimeTimeAlert else None, buttonIcon=b'', buttonLabel=backport.text(R.strings.epic_battle.widgetAlertMessageBlock.button()), buttonVisible=showPrimeTimeAlert and hasAvailableServers, buttonTooltip=None, statusText=_getAlertStatusText(timeLeft, hasAvailableServers), popoverAlias=None, bgVisible=True, shadowFilterVisible=showPrimeTimeAlert, tooltip=None, isSimpleTooltip=False)


@dependency.replace_none_kwargs(epicController=IEpicBattleMetaGameController, connectionMgr=IConnectionManager)
def _getAlertStatusText(timeLeft, hasAvailableServers, connectionMgr=None, epicController=None):
    rAlertMsgBlock = R.strings.epic_battle.widgetAlertMessageBlock
    alertStr = b''
    if hasAvailableServers:
        alertStr = backport.text(rAlertMsgBlock.somePeripheriesHalt(), serverName=connectionMgr.serverUserNameShort)
    else:
        currSeason = epicController.getCurrentSeason()
        currTime = time_utils.getCurrentLocalServerTimestamp()
        primeTime = epicController.getPrimeTimes().get(connectionMgr.peripheryID)
        isCycleNow = currSeason and currSeason.hasActiveCycle(currTime) and primeTime and primeTime.getPeriodsBetween(currTime, currSeason.getCycleEndDate())
        if isCycleNow:
            if connectionMgr.isStandalone():
                key = rAlertMsgBlock.singleModeHalt
            else:
                key = rAlertMsgBlock.allPeripheriesHalt
            timeLeftStr = time_formatters.getTillTimeByResource(timeLeft, R.strings.epic_battle.status.timeLeft, removeLeadingZeros=True)
            alertStr = backport.text(key(), time=timeLeftStr)
        else:
            nextSeason = currSeason or epicController.getNextSeason()
            if nextSeason is not None:
                nextCycle = nextSeason.getNextByTimeCycle(currTime)
                if nextCycle is not None:
                    if nextCycle.announceOnly:
                        alertStr = backport.text(rAlertMsgBlock.announcement())
                    else:
                        timeLeftStr = time_formatters.getTillTimeByResource(nextCycle.startDate - currTime, R.strings.epic_battle.status.timeLeft, removeLeadingZeros=True)
                        alertStr = backport.text(rAlertMsgBlock.startIn(), time=timeLeftStr)
            if not alertStr:
                prevSeason = currSeason or epicController.getPreviousSeason()
                if prevSeason is not None:
                    prevCycle = prevSeason.getLastActiveCycleInfo(currTime)
                    if prevCycle is not None:
                        alertStr = backport.text(rAlertMsgBlock.noCycleMessage())
    return text_styles.vehicleStatusCriticalText(alertStr)


def _getTimeLeftStr(timeStamp):
    timeLeft = time_formatters.getTillTimeByResource(timeStamp, R.strings.menu.Time.timeLeftShort, removeLeadingZeros=True)
    return text_styles.stats(timeLeft)
