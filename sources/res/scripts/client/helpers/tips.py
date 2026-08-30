import typing, logging, random, re
from collections import namedtuple
import nations
from account_helpers import AccountSettings
from account_helpers.AccountSettings import ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON
from account_helpers.AccountSettings import WATCHED_PRE_BATTLE_TIPS_SECTION
from constants import ARENA_GUI_TYPE, IS_DEVELOPMENT
from gui.battle_pass.battle_pass_helpers import isBattlePassActiveSeason
from gui.doc_loaders.prebattle_tips_loader import getPreBattleTipsConfig
from gui.impl.gen import R
from gui.shared.utils.functions import replaceHyphenToUnderscore
from gui.shared.system_factory import registerBattleTipCriteria, registerBattleTipsCriteria, collectBattleTipsCriteria
from helpers import dependency
from realm import CURRENT_REALM
from skeletons.gui.game_control import IBattleRoyaleController, IRankedBattlesController, IVehiclePostProgressionController
if typing.TYPE_CHECKING:
    from typing import Optional
_logger = logging.getLogger(__name__)
_RANDOM_TIPS_PATTERN = b'^(tip\\d+)'
_EPIC_BATTLE_TIPS_PATTERN = b'^(epicTip\\d+)'
_EPIC_RANDOM_TIPS_PATTERN = b'^(epicRandom\\d+)'
_RANKED_BATTLES_TIPS_PATTERN = b'^(ranked\\d+)'
_BATTLE_ROYALE_TIPS_PATTERN = b'^(battleRoyale\\d+$)'
_ST_PATRICK_PATTERN = b'^(stPatrick\\d+$)'
_WINBACK_TIPS_PATTERN = b'^(winback\\d+$)'
_MAPBOX_TIPS_PATTERN = b'^(mapbox\\d+)'
_DEV_MAPS_PATTERN = b'^(devMaps\\d+)'

class _BattleLoadingTipPriority(object):
    GENERIC = 1
    PRECEDING = 2


class TipData(namedtuple(b'_BattleLoadingTipData', b'status, body, icon')):

    def isValid(self):
        return self.status != R.invalid() or self.body != R.invalid() or self.icon != R.invalid()


class TipsCriteria(object):
    __slots__ = (b'_ctx', b'_tipsValidator')

    def __init__(self, *_):
        super(TipsCriteria, self).__init__()
        self._ctx = {b'arenaType': (self._getArenaGuiType())}
        self._tipsValidator = self._getTipsValidator()
        return

    def setContext(self, ctx):
        self._ctx.update(ctx)
        _logger.info(b'Tips context for battle: %s', self._ctx)
        return

    def find(self):
        foundTip = self._findRandomTip()
        if foundTip is not None:
            foundTip.markWatched()
            return foundTip.getData()
        else:
            return TipData(R.invalid(), R.invalid(), R.invalid())

    def _findRandomTip(self):
        suitableTips = filter(self._suitableTipPredicate, self._getTargetList())
        precedingTips = [tip for tip in suitableTips if tip.getPriority() == _BattleLoadingTipPriority.PRECEDING]
        if _logger.isEnabledFor(logging.INFO):
            _logger.info(b'Suitable preceding tips: %s', precedingTips)
            _logger.info(b'Suitable tips: %s', suitableTips)
        foundTip = None
        if precedingTips:
            foundTip = random.choice(precedingTips)
        elif suitableTips:
            foundTip = random.choice(suitableTips)
        return foundTip

    def _getArenaGuiType(self):
        return

    def _getTipsValidator(self):
        return _TipsValidator()

    def _suitableTipPredicate(self, tip):
        if tip is None or self._tipsValidator is None:
            return False
        return self._tipsValidator.validateRegularTip(tipFilter=tip.tipFilter, ctx=self._ctx)

    def _getTargetList(self):
        _logger.error(b'Method _getTargetList has to be overridden')
        return []


class _RandomTipsCriteria(TipsCriteria):

    def _getTargetList(self):
        return _randomTips

    def _getArenaGuiType(self):
        return ARENA_GUI_TYPE.RANDOM


class _EpicBattleTipsCriteria(TipsCriteria):

    def find(self):
        tipData = super(_EpicBattleTipsCriteria, self).find()
        return TipData(tipData.status, tipData.body, R.invalid())

    def _getTargetList(self):
        return _epicBattleTips

    def _getArenaGuiType(self):
        return ARENA_GUI_TYPE.EPIC_BATTLE


class _EventTipsCriteria(TipsCriteria):

    def find(self):
        return TipData(R.strings.tips.eventTitle(), R.strings.tips.eventMessage(), R.images.gui.maps.icons.battleLoading.tips.event())


class _DevMapsTipsCriteria(TipsCriteria):

    def _getTargetList(self):
        return _devMapsTips


class _RankedTipsCriteria(TipsCriteria):

    def _getTargetList(self):
        return _rankedTips


class _EpicRandomTipsCriteria(TipsCriteria):

    def _getTargetList(self):
        return _epicRandomTips


class _WinbackTipsCriteria(TipsCriteria):

    def _getTargetList(self):
        return _winbackTips

    def _getArenaGuiType(self):
        return ARENA_GUI_TYPE.WINBACK


class BattleRoyaleTipsCriteria(TipsCriteria):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    def __init__(self, arenaVisitor):
        super(BattleRoyaleTipsCriteria, self).__init__()
        self._arenaVisitor = arenaVisitor
        return

    def find(self):
        foundTip = self.__getSquadTip() or self._findRandomTip()
        if foundTip is not None:
            foundTip.markWatched()
            tipData = foundTip.getData()
            tipIcon = self.__getTipIcon(foundTip.getTipId())
            if tipIcon != R.invalid():
                tipData = TipData(tipData.status, tipData.body, tipIcon)
            return tipData
        return TipData(R.invalid(), R.invalid(), R.invalid())

    def _getTargetList(self):
        if self.__battleRoyaleController.isStPatrick():
            return _stPatrickTips
        return _battleRoyaleTips

    def _getArenaGuiType(self):
        return ARENA_GUI_TYPE.BATTLE_ROYALE

    @dependency.replace_none_kwargs(battleRoyaleController=IBattleRoyaleController)
    def __getSquadTip(self, battleRoyaleController=None):
        if not battleRoyaleController.isInRandomSquadSubMode():
            return
        curSeason = battleRoyaleController.getCurrentSeason()
        if not curSeason:
            return
        curSeasonID = curSeason.getSeasonID()
        squadTipShownForSeasonID = AccountSettings.getSettings(ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON)
        if curSeasonID == squadTipShownForSeasonID:
            return
        AccountSettings.setSettings(ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON, curSeasonID)
        return _buildBattleLoadingTip(b'battleRoyale6', R.strings.tips.battleRoyale6())

    def __getTipIcon(self, tipId):
        if self.__battleRoyaleController.isStPatrick():
            res = R.images.battle_royale.gui.maps.st_patrick.icons.battleLoading.tips.dyn(tipId)
            if res.exists():
                return res()
            tipId = tipId.replace(b'stPatrick', b'battleRoyale')
        geometryName = replaceHyphenToUnderscore(self._arenaVisitor.getArenaType().geometryName)
        geometryTipId = (b'_').join((tipId, geometryName))
        return R.images.battle_royale.gui.maps.icons.battleLoading.tips.dyn(geometryTipId, R.invalid)()


class _MapboxTipsCriteria(TipsCriteria):

    def _getTargetList(self):
        return _mapboxTips

    def _getArenaGuiType(self):
        return ARENA_GUI_TYPE.MAPBOX


class ExactTipsCriteria(TipsCriteria):
    __slots__ = (b'_exactTip',)

    def __init__(self, _exactTipPattern):
        self._exactTip = readTips(_exactTipPattern)
        super(ExactTipsCriteria, self).__init__()
        return

    def find(self):
        if self._exactTip:
            return self._exactTip[0].getData()
        return TipData(R.invalid(), R.invalid(), R.invalid())


registerBattleTipCriteria(ARENA_GUI_TYPE.EVENT_BATTLES, _EventTipsCriteria)
registerBattleTipCriteria(ARENA_GUI_TYPE.RANKED, _RankedTipsCriteria)
registerBattleTipCriteria(ARENA_GUI_TYPE.BATTLE_ROYALE, BattleRoyaleTipsCriteria)
registerBattleTipCriteria(ARENA_GUI_TYPE.WINBACK, _WinbackTipsCriteria)
registerBattleTipCriteria(ARENA_GUI_TYPE.MAPBOX, _MapboxTipsCriteria)
registerBattleTipsCriteria(ARENA_GUI_TYPE.EPIC_RANGE, _EpicBattleTipsCriteria)
registerBattleTipsCriteria((ARENA_GUI_TYPE.EPIC_RANDOM, ARENA_GUI_TYPE.EPIC_RANDOM_TRAINING), _EpicRandomTipsCriteria)

def getTipsCriteria(arenaVisitor):
    if IS_DEVELOPMENT:
        exactTipID = getattr(getTipsCriteria, b'exactTipID', None)
        if exactTipID:
            return ExactTipsCriteria(b'^(' + exactTipID + b')')
    criteriaCls = collectBattleTipsCriteria(arenaVisitor.gui.guiType)
    if criteriaCls is None:
        return _getRandomTipsCriteria(arenaVisitor)
    else:
        return criteriaCls(arenaVisitor)


def showExactTip(exactTipID):
    getTipsCriteria.exactTipID = exactTipID if exactTipID else None
    return


def readTips(pattern):
    result = []
    tipsPattern = re.compile(pattern)
    for tipID, descriptionResId in R.strings.tips.items():
        if tipID:
            reMatch = tipsPattern.match(tipID)
            if reMatch is not None:
                if tipID not in _tipsConfig:
                    _logger.warning(b'Tips by tipID(%s) not in prebattle_tips.xml', tipID)
                else:
                    result.append(_buildBattleLoadingTip(tipID, descriptionResId()))

    return result


def _buildBattleLoadingTip(tipID, descriptionResID):
    tipConfig = _tipsConfig.get(tipID)
    tipFilter = tipConfig.get(b'filter')
    if tipFilter is not None and tipFilter[b'preceding'] is not None:
        tip = _PrecedingBattleLoadingTip()
        tip.setShowLimit(tipFilter[b'preceding'][b'showTimes'])
    else:
        tip = _BattleLoadingTip()
    tip.build(tipID, descriptionResID, tipConfig)
    return tip


def _getRandomTipsCriteria(arenaVisitor):
    if arenaVisitor.extra.isMapsInDevelopmentEnabled():
        return _DevMapsTipsCriteria()
    return _RandomTipsCriteria()


def _getTipIconRes(tipID, group):
    res = R.images.gui.maps.icons.battleLoading.tips.dyn(tipID)
    if res.exists():
        return res()
    return R.images.gui.maps.icons.battleLoading.groups.dyn(group)()


class _TipsValidator(object):

    def __init__(self):
        super(_TipsValidator, self).__init__()
        self._validatorsList = (
         _BattlesValidator(),
         _ArenaGuiTypeValidator(),
         _TagsValidator(),
         _LevelValidator(),
         _NationValidator(),
         _VehicleClassValidator(),
         _RealmsValidator(),
         _BattlePassValidator(),
         _RankedBattlesValidator(),
         _PostProgressionValidator(),
         _ChassisTypeValidator(),
         _VehPropertyValidator(),
         _MechanicsValidator())
        return

    def validateRegularTip(self, tipFilter, ctx=None):
        if not tipFilter:
            return True
        for validator in self._validatorsList:
            if not validator.validate(tipFilter, ctx):
                return False

        return True


class _BattleLoadingTip(object):
    __slots__ = (b'_tipId', b'_statusResId', b'_iconResId', b'_descriptionResId', b'_tipFilter')

    def __init__(self):
        super(_BattleLoadingTip, self).__init__()
        self._tipId = None
        self._statusResId = R.invalid()
        self._iconResId = R.invalid()
        self._descriptionResId = R.invalid()
        self._tipFilter = None
        return

    def build(self, tipID, descriptionResID, config):
        if config is not None:
            self._statusResId = R.strings.tips.dyn(config[b'status'])()
            self._iconResId = _getTipIconRes(tipID, config[b'group'])
            self._tipFilter = config[b'filter']
        self._tipId = tipID
        self._descriptionResId = descriptionResID
        return

    @property
    def tipFilter(self):
        return self._tipFilter

    def markWatched(self):
        return

    def getPriority(self):
        return _BattleLoadingTipPriority.GENERIC

    def getTipId(self):
        return self._tipId

    def getData(self):
        return TipData(self._statusResId, self._descriptionResId, self._iconResId)

    def __repr__(self):
        return self._tipId


class _PrecedingBattleLoadingTip(_BattleLoadingTip):
    __slots__ = (b'_showLimit', b'_watchedTimes')

    def __init__(self):
        super(_PrecedingBattleLoadingTip, self).__init__()
        self._showLimit = 0
        return

    def setShowLimit(self, limit):
        self._showLimit = limit
        return

    def markWatched(self):
        _increaseTipWatchedCounter(self._tipId)
        return

    def getPriority(self):
        watchedTimes = _getTipWatchedCounter(self._tipId)
        if watchedTimes < self._showLimit:
            return _BattleLoadingTipPriority.PRECEDING
        return _BattleLoadingTipPriority.GENERIC


class _ChassisTypeValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        chassisType = tipFilter[b'chassisType']
        return chassisType < 0 or ctx[b'vehicleType'].chassisType == chassisType


class _VehPropertyValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        requiredProperty = tipFilter[b'vehProperty']
        return not requiredProperty or getattr(ctx[b'vehicleType'], requiredProperty, False)


class _MechanicsValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        mechanics = tipFilter[b'mechanics']
        if mechanics is None:
            return True
        else:
            included = mechanics[b'include']
            if included and not included & ctx[b'vehicleType'].vehicleMechanics:
                return False
            excluded = mechanics[b'exclude']
            return not excluded or not excluded & ctx[b'vehicleType'].vehicleMechanics


class _BattlesValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        battlesCount = ctx.get(b'battlesCount')
        minBattles, maxBattles = tipFilter[b'minBattles'], tipFilter[b'maxBattles']
        return minBattles <= battlesCount and (not maxBattles or battlesCount <= maxBattles)


class _ArenaGuiTypeValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        expected = tipFilter[b'arenaTypes']
        actual = ctx[b'arenaType']
        return not expected or actual in expected


class _TagsValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        requiredTags = tipFilter[b'tags']
        tags = ctx[b'vehicleType'].tags
        return not requiredTags or requiredTags.issubset(tags)


class _LevelValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        possibleLevels = tipFilter[b'levels']
        level = ctx[b'vehicleType'].level
        return not possibleLevels or str(level) in possibleLevels


class _NationValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        vehicleNationId = ctx[b'vehicleType'].nationID
        if vehicleNationId == nations.NONE_INDEX:
            return False
        possibleNations = tipFilter[b'nations']
        nation = nations.NAMES[vehicleNationId]
        return not possibleNations or nation in possibleNations


class _VehicleClassValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        possibleClasses = tipFilter[b'vehicleClass']
        vehicleClassTag = ctx[b'vehicleType'].classTag
        return not possibleClasses or vehicleClassTag in possibleClasses


class _RealmsValidator(object):

    @staticmethod
    def validate(tipFilter, _):
        possibleRealms = tipFilter[b'realms']
        return not possibleRealms or CURRENT_REALM in possibleRealms


class _BattlePassValidator(object):
    __slots__ = (b'_isActiveSeason',)

    def __init__(self):
        super(_BattlePassValidator, self).__init__()
        self._isActiveSeason = isBattlePassActiveSeason()
        return

    def validate(self, tipFilter, _):
        if b'isBattlePassActiveSeason' in tipFilter:
            return tipFilter[b'isBattlePassActiveSeason'] == self._isActiveSeason
        return True


class _RankedBattlesValidator(object):
    __slots__ = (b'_isYearRewardEnabled', b'_isLeaderboardEnabled', b'_isShopEnabled')
    _rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self):
        super(_RankedBattlesValidator, self).__init__()
        self._isYearRewardEnabled = self._rankedController.isYearRewardEnabled()
        self._isLeaderboardEnabled = self._rankedController.isYearLBEnabled()
        self._isShopEnabled = self._rankedController.isRankedShopEnabled()
        return

    def validate(self, tipFilter, _):
        if b'isRankedYearRewardEnabled' in tipFilter:
            if tipFilter[b'isRankedYearRewardEnabled'] != self._isYearRewardEnabled:
                return False
        if b'isRankedLeaderboardEnabled' in tipFilter:
            if tipFilter[b'isRankedLeaderboardEnabled'] != self._isLeaderboardEnabled:
                return False
        if b'isRankedShopEnabled' in tipFilter:
            if tipFilter[b'isRankedShopEnabled'] != self._isShopEnabled:
                return False
        return True


class _PostProgressionValidator(object):
    __slots__ = (b'_isPostProgressionEnabled',)
    _postProgressionCtrl = dependency.descriptor(IVehiclePostProgressionController)

    def __init__(self):
        super(_PostProgressionValidator, self).__init__()
        self._isPostProgressionEnabled = self._postProgressionCtrl.isEnabled()
        return

    def validate(self, tipFilter, _):
        if b'isPostProgressionEnabled' in tipFilter:
            return tipFilter[b'isPostProgressionEnabled'] == self._isPostProgressionEnabled
        return True


def _getTipWatchedCounter(tipID):
    cache = _getWatchedCache()
    return cache.get(tipID, 0)


def _increaseTipWatchedCounter(tipID):
    cache = _getWatchedCache()
    counter = cache.get(tipID, 0)
    cache[tipID] = counter + 1
    AccountSettings.setSettings(WATCHED_PRE_BATTLE_TIPS_SECTION, cache)
    return


def _getWatchedCache():
    global _watchedTipsCache
    if _watchedTipsCache is None:
        _watchedTipsCache = AccountSettings.getSettings(WATCHED_PRE_BATTLE_TIPS_SECTION)
    return _watchedTipsCache


_watchedTipsCache = None
_tipsConfig = getPreBattleTipsConfig()
_randomTips = readTips(_RANDOM_TIPS_PATTERN)
_rankedTips = readTips(_RANKED_BATTLES_TIPS_PATTERN)
_epicBattleTips = readTips(_EPIC_BATTLE_TIPS_PATTERN)
_epicRandomTips = readTips(_EPIC_RANDOM_TIPS_PATTERN)
_battleRoyaleTips = readTips(_BATTLE_ROYALE_TIPS_PATTERN)
_stPatrickTips = readTips(_ST_PATRICK_PATTERN)
_winbackTips = readTips(_WINBACK_TIPS_PATTERN)
_mapboxTips = readTips(_MAPBOX_TIPS_PATTERN)
_devMapsTips = readTips(_DEV_MAPS_PATTERN)
