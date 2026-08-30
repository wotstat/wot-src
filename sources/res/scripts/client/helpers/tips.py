import logging, random, re
from collections import namedtuple
import nations
from account_helpers import AccountSettings
from account_helpers.AccountSettings import WATCHED_PRE_BATTLE_TIPS_SECTION
from constants import ARENA_GUI_TYPE
from gui.battle_pass.battle_pass_helpers import isBattlePassActiveSeason
from gui.doc_loaders.prebattle_tips_loader import readPreBattleTips
from gui.impl.gen import R
from gui.shared.utils.functions import replaceHyphenToUnderscore
from gui.shared.system_factory import registerBattleTipCriteria, registerBattleTipsCriteria, collectBattleTipsCriteria
from helpers import dependency
from realm import CURRENT_REALM
from skeletons.gui.game_control import IRankedBattlesController, IVehiclePostProgressionController
_logger = logging.getLogger(__name__)
_PREBATTLE_TIPS_XML_PATH = b'gui/prebattle_tips.xml'
_RANDOM_TIPS_PATTERN = b'^(tip\\d+)'
_EPIC_BATTLE_TIPS_PATTERN = b'^(epicTip\\d+)'
_EPIC_RANDOM_TIPS_PATTERN = b'^(epicRandom\\d+)'
_RANKED_BATTLES_TIPS_PATTERN = b'^(ranked\\d+)'
_BATTLE_ROYALE_TIPS_PATTERN = b'^(battleRoyale\\d+$)'
_COMP7_TIPS_PATTERN = b'^(comp7\\d+$)'
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


class _Comp7TipsCriteria(TipsCriteria):

    def _getTargetList(self):
        return _comp7Tips

    def _getArenaGuiType(self):
        return ARENA_GUI_TYPE.COMP7


class BattleRoyaleTipsCriteria(TipsCriteria):

    def __init__(self, arenaVisitor):
        super(BattleRoyaleTipsCriteria, self).__init__()
        self._arenaVisitor = arenaVisitor
        return

    def find(self):
        foundTip = self._findRandomTip()
        if foundTip is not None:
            foundTip.markWatched()
            tipData = foundTip.getData()
            geometryName = replaceHyphenToUnderscore(self._arenaVisitor.getArenaType().geometryName)
            geomertyIconResId = _tryGetTipIconRes((b'_').join((foundTip.getTipId(), geometryName)))
            if geomertyIconResId != R.invalid():
                tipData = TipData(tipData.status, tipData.body, geomertyIconResId)
            return tipData
        return TipData(R.invalid(), R.invalid(), R.invalid())

    def _getTargetList(self):
        return _battleRoyaleTips

    def _getArenaGuiType(self):
        return ARENA_GUI_TYPE.BATTLE_ROYALE


class _MapboxTipsCriteria(TipsCriteria):

    def _getTargetList(self):
        return _mapboxTips

    def _getArenaGuiType(self):
        return ARENA_GUI_TYPE.MAPBOX


registerBattleTipCriteria(ARENA_GUI_TYPE.EVENT_BATTLES, _EventTipsCriteria)
registerBattleTipCriteria(ARENA_GUI_TYPE.RANKED, _RankedTipsCriteria)
registerBattleTipCriteria(ARENA_GUI_TYPE.BATTLE_ROYALE, BattleRoyaleTipsCriteria)
registerBattleTipCriteria(ARENA_GUI_TYPE.COMP7, _Comp7TipsCriteria)
registerBattleTipCriteria(ARENA_GUI_TYPE.MAPBOX, _MapboxTipsCriteria)
registerBattleTipsCriteria(ARENA_GUI_TYPE.EPIC_RANGE, _EpicBattleTipsCriteria)
registerBattleTipsCriteria((ARENA_GUI_TYPE.EPIC_RANDOM, ARENA_GUI_TYPE.EPIC_RANDOM_TRAINING), _EpicRandomTipsCriteria)

def getTipsCriteria(arenaVisitor):
    criteriaCls = collectBattleTipsCriteria(arenaVisitor.gui.guiType)
    if criteriaCls is None:
        return _getRandomTipsCriteria(arenaVisitor)
    else:
        return criteriaCls(arenaVisitor)


def _readTips(tips, tipsConfig, logger):
    result = []
    for tipID, descriptionResId in tips:
        if tipID not in tipsConfig:
            logger.warning(b'Tips by tipID(%s) not in prebattle_tips.xml', tipID)
        else:
            result.append(_buildBattleLoadingTip(tipID, descriptionResId(), tipsConfig))

    return result


def readTips(pattern, tipsConfig):
    tipsPattern = re.compile(pattern)
    tips = [(tipID, descriptionResId) for tipID, descriptionResId in R.strings.tips.items() if tipID and tipsPattern.match(tipID) is not None]
    return _readTips(tips, tipsConfig, _logger)


def _buildBattleLoadingTip(tipID, descriptionResID, tipsConfig):
    tipConfig = tipsConfig.get(tipID)
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


def _tryGetTipIconRes(tipID):
    res = R.images.gui.maps.icons.battleLoading.tips.dyn(tipID)
    if res.exists():
        return res()
    return R.invalid()


class _TipsValidator(object):

    def __init__(self):
        super(_TipsValidator, self).__init__()
        self._validatorsList = (
         _BattlesValidator(),
         _ArenaGuiTypeValidator(),
         _TagsValidator(),
         _NoTagsValidator(),
         _LevelValidator(),
         _NationValidator(),
         _VehicleClassValidator(),
         _RealmsValidator(),
         _BattlePassValidator(),
         _RankedBattlesValidator(),
         _PostProgressionValidator(),
         _ChassisTypeValidator(),
         _VehPropertyValidator(),
         _NotVehPropertyValidator())
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


class _NotVehPropertyValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        requiredProperty = tipFilter[b'notVehProperty']
        return not requiredProperty or not getattr(ctx[b'vehicleType'], requiredProperty, False)


class _BattlesValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        battlesCount = ctx.get(b'battlesCount')
        minBattles, maxBattles = tipFilter[b'minBattles'], tipFilter[b'maxBattles']
        return minBattles <= battlesCount <= maxBattles


class _ArenaGuiTypeValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        expected = tipFilter[b'arenaTypes']
        actual = ctx[b'arenaType']
        return not expected or str(actual) in expected


class _TagsValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        requiredTags = tipFilter[b'tags']
        tags = ctx[b'vehicleType'].tags
        return not requiredTags or requiredTags.issubset(tags)


class _NoTagsValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        requiredTags = tipFilter[b'noTags']
        tags = ctx[b'vehicleType'].tags
        return not requiredTags or not requiredTags.issubset(tags)


class _LevelValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        possibleLevels = tipFilter[b'levels']
        level = ctx[b'vehicleType'].level
        return not possibleLevels or str(level) in possibleLevels


class _NationValidator(object):

    @staticmethod
    def validate(tipFilter, ctx):
        possibleNations = tipFilter[b'nations']
        nation = nations.NAMES[ctx[b'vehicleType'].nationID]
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
    __slots__ = (b'_isYearRewardEnabled', b'_isLeaderboardEnabled', b'_isShopEnabled', b'_isLeagueRewardEnabled')
    _rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self):
        super(_RankedBattlesValidator, self).__init__()
        self._isYearRewardEnabled = self._rankedController.isYearRewardEnabled()
        self._isLeaderboardEnabled = self._rankedController.isYearLBEnabled()
        self._isShopEnabled = self._rankedController.isRankedShopEnabled()
        self._isLeagueRewardEnabled = self._rankedController.isLeagueRewardEnabled()
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
        if b'isRankedLeagueRewardEnabled' in tipFilter:
            if tipFilter[b'isRankedLeagueRewardEnabled'] != self._isLeagueRewardEnabled:
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
_tipsConfig = readPreBattleTips(_PREBATTLE_TIPS_XML_PATH)
_randomTips = readTips(_RANDOM_TIPS_PATTERN, _tipsConfig)
_rankedTips = readTips(_RANKED_BATTLES_TIPS_PATTERN, _tipsConfig)
_epicBattleTips = readTips(_EPIC_BATTLE_TIPS_PATTERN, _tipsConfig)
_epicRandomTips = readTips(_EPIC_RANDOM_TIPS_PATTERN, _tipsConfig)
_battleRoyaleTips = readTips(_BATTLE_ROYALE_TIPS_PATTERN, _tipsConfig)
_comp7Tips = readTips(_COMP7_TIPS_PATTERN, _tipsConfig)
_mapboxTips = readTips(_MAPBOX_TIPS_PATTERN, _tipsConfig)
_devMapsTips = readTips(_DEV_MAPS_PATTERN, _tipsConfig)
