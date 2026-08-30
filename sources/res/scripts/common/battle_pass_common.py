from __future__ import absolute_import
import bisect, struct, time
from collections import namedtuple
from future.utils import viewitems, viewvalues
from past.builtins import xrange
import typing
from enum import Enum, unique
from battle_pass_integration import getBattlePassByGameMode
from constants import ARENA_BONUS_TYPE, MAX_VEHICLE_LEVEL, OFFER_TOKEN_PREFIX
from debug_utils import LOG_ERROR, LOG_CODEPOINT_WARNING
from items import parseIntCompactDescr, vehicles
from optional_bonuses import BONUS_MERGERS
if typing.TYPE_CHECKING:
    from typing import Dict, Generator, Sequence, Tuple, Union, List
BATTLE_PASS_TOKEN_PREFIX = b'battle_pass:'
BATTLE_PASS_TOKEN_PASS = BATTLE_PASS_TOKEN_PREFIX + b'pass:'
BATTLE_PASS_ENTITLEMENT_PASS = BATTLE_PASS_TOKEN_PASS.replace(b':', b'_')
BATTLE_PASS_SHOP_ENTITLEMENT_PASS = b'battle_pass_shop_'
BATTLE_PASS_OFFER_TOKEN_PREFIX = OFFER_TOKEN_PREFIX + BATTLE_PASS_TOKEN_PREFIX
BATTLE_PASS_Q_CHAIN_TOKEN_PREFIX = BATTLE_PASS_TOKEN_PREFIX + b'q_chain:'
BATTLE_PASS_RANDOM_QUEST_TOKEN_PREFIX = BATTLE_PASS_TOKEN_PREFIX + b'random_quest:'
BATTLE_PASS_TOKEN_TROPHY_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'trophy:'
BATTLE_PASS_TOKEN_TROPHY_GIFT_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'trophy_gift:'
BATTLE_PASS_TOKEN_NEW_DEVICE_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'new_device:'
BATTLE_PASS_TOKEN_NEW_DEVICE_GIFT_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'new_device_gift:'
BATTLE_PASS_TOKEN_MODERNIZED_DEVICE_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'modernized_device:'
BATTLE_PASS_TOKEN_MODERNIZED_DEVICE_GIFT_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'modernized_device_gift:'
BATTLE_PASS_TOKEN_BATTLE_BOOSTER_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'battle_booster:'
BATTLE_PASS_TOKEN_BATTLE_BOOSTER_GIFT_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'battle_booster_gift:'
BATTLE_PASS_TOKEN_BLUEPRINT_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'blueprint:'
BATTLE_PASS_TOKEN_BLUEPRINT_GIFT_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'blueprint_gift:'
BATTLE_PASS_TOKEN_BROCHURE_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'brochure:'
BATTLE_PASS_TOKEN_BROCHURE_GIFT_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'brochure_gift:'
BATTLE_PASS_TOKEN_GUIDE_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'guide:'
BATTLE_PASS_TOKEN_GUIDE_GIFT_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'guide_gift:'
BATTLE_PASS_TOKEN_CREW_BOOK_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'crewbook:'
BATTLE_PASS_TOKEN_CREW_BOOK_GIFT_OFFER = BATTLE_PASS_OFFER_TOKEN_PREFIX + b'crewbook_gift:'
BATTLE_PASS_TOKEN_3D_STYLE = BATTLE_PASS_TOKEN_PREFIX + b'3D_style:'
BATTLE_PASS_RANDOM_QUEST_ID_PREFIX = b'battle_pass_random'
BATTLE_PASS_CHOICE_REWARD_OFFER_TOKENS = (
 BATTLE_PASS_TOKEN_TROPHY_OFFER, BATTLE_PASS_TOKEN_NEW_DEVICE_OFFER, BATTLE_PASS_TOKEN_MODERNIZED_DEVICE_OFFER,
 BATTLE_PASS_TOKEN_BATTLE_BOOSTER_OFFER, BATTLE_PASS_TOKEN_BLUEPRINT_OFFER, BATTLE_PASS_TOKEN_BROCHURE_OFFER,
 BATTLE_PASS_TOKEN_GUIDE_OFFER, BATTLE_PASS_TOKEN_CREW_BOOK_OFFER)
BATTLE_PASS_CHOICE_REWARD_OFFER_GIFT_TOKENS = (
 BATTLE_PASS_TOKEN_TROPHY_GIFT_OFFER, BATTLE_PASS_TOKEN_NEW_DEVICE_GIFT_OFFER,
 BATTLE_PASS_TOKEN_MODERNIZED_DEVICE_GIFT_OFFER, BATTLE_PASS_TOKEN_BATTLE_BOOSTER_GIFT_OFFER,
 BATTLE_PASS_TOKEN_BLUEPRINT_GIFT_OFFER, BATTLE_PASS_TOKEN_BROCHURE_GIFT_OFFER, BATTLE_PASS_TOKEN_GUIDE_GIFT_OFFER,
 BATTLE_PASS_TOKEN_CREW_BOOK_GIFT_OFFER)
BATTLE_PASS_CHOICE_REWARD_OFFER_TOKEN_FREE_POSTFIX = b'free:'
BATTLE_PASS_CHOICE_REWARD_OFFER_TOKEN_PAID_POSTFIX = b'paid:'
BATTLE_PASS_PDATA_KEY = b'battlePass'
BATTLE_PASS_CONFIG_NAME = b'battlePass_config'
BATTLE_PASS_SELECT_BONUS_NAME = b'battlePassSelectToken'
BATTLE_PASS_STYLE_PROGRESS_BONUS_NAME = b'styleProgressToken'
BATTLE_PASS_Q_CHAIN_BONUS_NAME = b'battlePassQuestChainToken'
BATTLE_PASS_RANDOM_QUEST_BONUS_NAME = b'randomQuestToken'
NON_VEH_CD = 0
NON_CHAPTER_ID = 0
MAX_NON_CHAPTER_POINTS = 1000000
MAX_POST_PROGRESSION_POINTS = 1000000
MAX_POST_PROGRESSION_LEVEL = 10000
BATTLE_PASS_TOKEN_LIFETIME = 4320
HOLIDAY_SEASON_OFFSET = 1000
STARTER_PACK_LOGGING_PARTNER_ID = 19
BATTLE_PASS_COST_CURRENCIES = {
 b'gold'}
BP_TANKMEN_ENTITLEMENT_TAG_PREFIX = b'tankmen_bp'
BATTLE_PASS_TICKETS_EVENT = b'battlePass'
BATTLE_PASS_CATEGORY_PATH = b'/battlepass/battlepass/'

class BattlePassTankmenSource(object):
    PROGRESSION = b'progression'
    SHOP = b'shop'
    ALL = (PROGRESSION, SHOP)


@unique
class FinalReward(str, Enum):
    BATTLE_QUEST = b'battleQuest'
    PROGRESSIVE_STYLE = b'progressiveStyle'
    STYLE = b'style'
    TANKMAN = b'tankman'
    VEHICLE = b'vehicle'
    ATTACHMENTS_SET = b'attachments_set'


@unique
class CurrencyBP(Enum):
    BIT = b'bpbit'
    TALER = b'bptaler'


class BattlePassRewardReason(object):
    DEFAULT = 0
    BATTLE = 1
    PURCHASE_BATTLE_PASS = 2
    PURCHASE_BATTLE_PASS_LEVELS = 3
    INVOICE = 4
    STYLE_UPGRADE = 5
    SELECT_REWARD = 6
    PURCHASE_BATTLE_PASS_MULTIPLE = 7
    SELECT_CHAPTER = 8
    PURCHASE_BATTLE_PASS_WITH_LEVELS = 9
    PURCHASE_REASONS = (
     PURCHASE_BATTLE_PASS, PURCHASE_BATTLE_PASS_LEVELS, PURCHASE_BATTLE_PASS_MULTIPLE,
     PURCHASE_BATTLE_PASS_WITH_LEVELS)
    REASONS_WITH_STARTER_PACK = (
     PURCHASE_BATTLE_PASS, PURCHASE_BATTLE_PASS_MULTIPLE, PURCHASE_BATTLE_PASS_WITH_LEVELS)


class BattlePassState(object):
    BASE = 0
    POST = 1
    COMPLETED = 2
    PAUSED = 3


class BattlePassConsts(object):
    REWARD_FREE = b'free'
    REWARD_PAID = b'paid'
    REWARD_BOTH = b'both'
    RARE_REWARD_TAG = b'rare'
    FREE_MASK = 1
    PAID_MASK = 2
    FAKE_QUEST_ID = b'battlePassFakeQuestID'
    MINIMAL_CHAPTER_NUMBER = 1


MASK_TO_REWARD = {(BattlePassConsts.FREE_MASK): (BattlePassConsts.REWARD_FREE), 
   (BattlePassConsts.PAID_MASK): (BattlePassConsts.REWARD_PAID)}

class BattlePassStatsCommon(object):
    _CNT_SEASONS_FORMAT = b'<I'
    _SEASON_ID_FORMAT = b'<I'
    _OTHER_STATS_FORMAT = b'<3I'
    OtherStats = namedtuple(b'OtherStats', b'battles maxBase maxPost')
    SeasonStats = namedtuple(b'SeasonStats', b'seasonID vehCDs vehPoints reachedCaps otherStats')

    @staticmethod
    def _packList(inputList):
        return struct.pack(b'<I', len(inputList)) + struct.pack((b'<{}I').format(len(inputList)), *inputList)

    @staticmethod
    def _unpackList(packed, offset):
        listLen, = struct.unpack_from(b'<I', packed, offset)
        offset += struct.calcsize(b'<I')
        return (
         struct.unpack_from((b'<{}I').format(listLen), packed, offset),
         offset + struct.calcsize((b'<{}I').format(listLen)))

    @staticmethod
    def makeSeasonStats(seasonID, vehiclePoints, seasonStats):
        vehCDs = []
        vehPoints = []
        for vehCD, vehCDPoints in viewitems(vehiclePoints):
            vehCDs.append(vehCD)
            vehPoints.append(vehCDPoints)

        return BattlePassStatsCommon.SeasonStats(seasonID, tuple(vehCDs), tuple(vehPoints), tuple(seasonStats[b'reachedCaps']), BattlePassStatsCommon.OtherStats(seasonStats[b'battles'], sum(chapterStats.points for chapterStats in viewvalues(seasonStats.get(b'chaptersStats', {}))), seasonStats.get(b'maxPost', 0)))

    @staticmethod
    def packSeasonStats(seasonStats):
        res = []
        res.append(struct.pack(BattlePassStatsCommon._SEASON_ID_FORMAT, seasonStats.seasonID))
        res.append(BattlePassStatsCommon._packList(seasonStats.vehCDs))
        res.append(BattlePassStatsCommon._packList(seasonStats.vehPoints))
        res.append(BattlePassStatsCommon._packList(seasonStats.reachedCaps))
        res.append(struct.pack(BattlePassStatsCommon._OTHER_STATS_FORMAT, *tuple(seasonStats.otherStats)))
        return (b'').join(res)

    @staticmethod
    def unpackSeasonStats(packed, offset=0):
        seasonID, = struct.unpack_from(BattlePassStatsCommon._SEASON_ID_FORMAT, packed, offset)
        offset += struct.calcsize(BattlePassStatsCommon._SEASON_ID_FORMAT)
        vehCDs, offset = BattlePassStatsCommon._unpackList(packed, offset)
        vehPoints, offset = BattlePassStatsCommon._unpackList(packed, offset)
        reachedCaps, offset = BattlePassStatsCommon._unpackList(packed, offset)
        battles, maxBase, maxPost = struct.unpack_from(BattlePassStatsCommon._OTHER_STATS_FORMAT, packed, offset)
        offset += struct.calcsize(BattlePassStatsCommon._OTHER_STATS_FORMAT)
        return (
         BattlePassStatsCommon.SeasonStats(seasonID, vehCDs, vehPoints, reachedCaps, BattlePassStatsCommon.OtherStats(battles, maxBase, maxPost)), offset)

    @staticmethod
    def packSeasonStatsWithPrevStats(prevPackedStats, seasonStats):
        cntPackedSeasons, = struct.unpack_from(BattlePassStatsCommon._CNT_SEASONS_FORMAT, prevPackedStats)
        offset = struct.calcsize(BattlePassStatsCommon._CNT_SEASONS_FORMAT)
        return struct.pack(BattlePassStatsCommon._CNT_SEASONS_FORMAT, cntPackedSeasons + 1) + prevPackedStats[offset:] + BattlePassStatsCommon.packSeasonStats(seasonStats)

    @staticmethod
    def unpackAllSeasonStats(packedStats, curOffset=0):
        result = []
        cntSeasons, = struct.unpack_from(BattlePassStatsCommon._CNT_SEASONS_FORMAT, packedStats, curOffset)
        curOffset += struct.calcsize(BattlePassStatsCommon._CNT_SEASONS_FORMAT)
        for _ in xrange(cntSeasons):
            curSeasonStats, curOffset = BattlePassStatsCommon.unpackSeasonStats(packedStats, curOffset)
            result.append(curSeasonStats)

        return (result, curOffset)

    @staticmethod
    def getEmptyPackedSeasonStats():
        return struct.pack(BattlePassStatsCommon._CNT_SEASONS_FORMAT, 0)

    @staticmethod
    def initialSeasonStatsData():
        return {b'chaptersStats': {}, b'nonChapterPoints': 0, 
           b'battles': 0, 
           b'reachedCaps': (set())}

    @staticmethod
    def initialChapterData():
        return {b'points': 0, 
           b'level': 0, 
           b'styleLevel': 0}


def getVehicleLevel(vehTypeCompDescr):
    _, nationID, innationID = parseIntCompactDescr(vehTypeCompDescr)
    return vehicles.g_list.getList(nationID)[innationID].level


def getBattlePassPassTokenName(season, chapter):
    return BATTLE_PASS_TOKEN_PASS + (b'{}:{}').format(season, chapter)


def getBattlePassPassEntitlementName(season):
    return (b'{}{}').format(BATTLE_PASS_ENTITLEMENT_PASS, season)


def getBattlePassShopEntitlementName(season):
    return (b'{}{}').format(BATTLE_PASS_SHOP_ENTITLEMENT_PASS, season)


def getSeasonAndChapterFromBattlePassToken(tokenID):
    seasonAndChapter = tokenID.split(BATTLE_PASS_TOKEN_PASS)[-1].split(b':')
    return (int(seasonAndChapter[0]), int(seasonAndChapter[1]))


def isBattlePassPassToken(token):
    return token.startswith(BATTLE_PASS_TOKEN_PASS)


def getLevel(curPoints, levelPoints, prevLevel=0):
    if prevLevel >= len(levelPoints):
        return prevLevel
    if curPoints < levelPoints[prevLevel]:
        return prevLevel
    if curPoints >= levelPoints[-1]:
        return len(levelPoints)
    if levelPoints[prevLevel] <= curPoints < levelPoints[prevLevel + 1]:
        return prevLevel + 1
    return bisect.bisect_right(levelPoints, curPoints, prevLevel)


def getPostProgressionLevel(curPoints, cyclePoints, prevLevel=0):
    levelsInCycle = len(cyclePoints)
    if not levelsInCycle:
        return prevLevel
    pointsPerCycle = cyclePoints[-1]
    cyclesDone, pointsInCurrentCycle = curPoints // pointsPerCycle, curPoints % pointsPerCycle
    levelInCurrentCycle = bisect.bisect_right(cyclePoints, pointsInCurrentCycle)
    currentLevelByPoints = cyclesDone * levelsInCycle + levelInCurrentCycle
    return max(prevLevel, currentLevelByPoints)


def getMaxAvalable3DStyleProgressInChapter(seasonID, chapter, tokensIds):
    level = 0
    if not isPostProgressionChapter(chapter):
        prefixStyleTokenInChapter = (b'{}{}:{}').format(BATTLE_PASS_TOKEN_3D_STYLE, seasonID, chapter)
        for token in tokensIds:
            if token.startswith(prefixStyleTokenInChapter):
                _, _, _, _, levelStyle = token.split(b':')
                levelStyle = int(levelStyle)
                if levelStyle > level:
                    level = levelStyle

    return level


def get3DStyleProgressToken(seasonID, chapter, progressLevel):
    return (b'{}{}:{}:{}').format(BATTLE_PASS_TOKEN_3D_STYLE, seasonID, chapter, progressLevel)


def getPresentLevel(rawLevel):
    return rawLevel + 1


def isPostProgressionChapter(chapterID):
    return chapterID and chapterID % 10 == 0


def getPostProgressionChapterID(seasonNum):
    return seasonNum * 10


def getPostProgressionLevelInCycleForRewards(cycleLength, level):
    return (level - 1) % cycleLength + 1


def mergeRewards(storage, rewardsToMerge):
    for key, value in viewitems(rewardsToMerge):
        if key in BONUS_MERGERS:
            BONUS_MERGERS[key](storage, key, value, False, 1, None)
        else:
            LOG_CODEPOINT_WARNING()

    return


class BattlePassConfig(object):
    REWARD_IDX = 0
    TAGS_IDX = 1

    def __init__(self, config):
        self._config = config
        self._season = config.get(b'season', {})
        self._rewards = config.get(b'rewards', {})
        self._regularChapterIds = set()
        self._extraChapterIds = set()
        self._mainChapterIds = set()
        if not self.chapters:
            return
        for chapterID, chapterData in viewitems(self.chapters):
            if chapterData[b'extra']:
                self._extraChapterIds.add(chapterID)
            elif not isPostProgressionChapter(chapterID):
                self._regularChapterIds.add(chapterID)

        self._mainChapterIds = self._regularChapterIds | self._extraChapterIds
        return

    @property
    def mode(self):
        return self._config.get(b'mode', b'disabled')

    @property
    def seasonID(self):
        return self._season.get(b'seasonID', 0)

    @property
    def seasonNum(self):
        return self._season.get(b'seasonNum', 0)

    @property
    def currentCollectionId(self):
        return self._season.get(b'currentCollectionId', 0)

    @property
    def seasonStart(self):
        return self._season.get(b'seasonStart', 0)

    @property
    def seasonFinish(self):
        return self._season.get(b'seasonFinish', 0)

    @property
    def finalOfferTime(self):
        return self._season.get(b'finalOfferTime', 0)

    @property
    def points(self):
        return self._season.get(b'points', {})

    @property
    def chapters(self):
        return self._season.get(b'chapters', {})

    @property
    def vehLevelCaps(self):
        return self._season.get(b'vehLevelCaps', (0,) * MAX_VEHICLE_LEVEL)

    @property
    def vehCDCaps(self):
        return self._season.get(b'vehCDCaps', {})

    @property
    def isHoliday(self):
        return len(self.chapters) == 1

    @property
    def isPostProgressionPresent(self):
        return not self.isHoliday

    @property
    def postProgressionChapterID(self):
        return getPostProgressionChapterID(self.seasonNum)

    @property
    def postProgressionCycleLength(self):
        return len(self.getChapterLevels(self.postProgressionChapterID))

    def getRewardTypes(self, chapterID):
        if chapterID not in self.chapters:
            LOG_ERROR((b'BattlePass wrong chapter={}, exists: {}').format(chapterID, self.chapters))
            return None
        else:
            return self.chapters[chapterID][b'finalRewardTypes']

    def getChapterLevels(self, chapterID):
        return self.getChapter(chapterID).get(b'levels', (0,))

    def getMaxChapterLevel(self, chapterID):
        if isPostProgressionChapter(chapterID):
            return MAX_POST_PROGRESSION_LEVEL
        if chapterID:
            return len(self.getChapterLevels(chapterID))
        return 0

    def getMaxChapterPoints(self, chapterID):
        if isPostProgressionChapter(chapterID):
            return MAX_POST_PROGRESSION_POINTS
        if chapterID:
            return self.getChapterLevels(chapterID)[-1]
        return MAX_NON_CHAPTER_POINTS

    def getRegularChapterIds(self):
        return self._regularChapterIds

    def getMainChapterIds(self):
        return self._mainChapterIds

    def getExtraChapterIds(self):
        return self._extraChapterIds

    def getBattlePassCost(self, chapterID):
        return self.chapters.get(chapterID, {}).get(b'battlePassCost', {b'gold': 0})

    def getChapterStarterPack(self, chapterID):
        return self.chapters.get(chapterID, {}).get(b'starterPack') or {}

    def getAllRegularChaptersStarterPack(self):
        result = {}
        for chapterID in self._regularChapterIds:
            chapterStarterPack = self.chapters[chapterID].get(b'starterPack') or {}
            mergeRewards(result, chapterStarterPack)

        return result

    def getTankmenScreens(self):
        return self._season.get(b'tankmenScreens', {})

    @staticmethod
    def iterRewardRanges(prevLvl, newLvl, rewardMask):
        return ((fromLvl, toLvl, mask) for fromLvl, toLvl, mask in (
         (
          prevLvl, newLvl, BattlePassConsts.FREE_MASK),
         (
          prevLvl, newLvl, BattlePassConsts.PAID_MASK)) if mask & rewardMask)

    def isGameModeEnabled(self, gameMode):
        return self.points.get(gameMode, {}).get(b'enabled', False)

    def isBuyingAllowed(self):
        return self.isActive(int(time.time()))

    def isActive(self, curTime):
        return (self.isEnabled()) and (self.seasonStart) <= curTime < self.seasonFinish

    def isEnabled(self):
        return self.mode == b'enabled'

    def isPaused(self):
        return self.mode == b'paused'

    def isDisabled(self):
        return self.mode == b'disabled'

    def isSeasonTimeOver(self, curTime):
        return int(curTime) >= self.seasonFinish

    def isExtraChapter(self, chapterID):
        return chapterID in self._extraChapterIds

    def isRegularChapter(self, chapterID):
        return chapterID in self._regularChapterIds

    def getChapterExpireTimestamp(self, chapterID):
        return self.getChapter(chapterID).get(b'expires', 0)

    def getSpecialVehicles(self):
        return self._season.get(b'specialVehicles') or {}

    def getSpecialVehiclesByGameMode(self, gameMode=ARENA_BONUS_TYPE.REGULAR):
        return self.getSpecialVehicles().get(gameMode) or []

    def isSpecialVehicle(self, vehTypeCompDescr, gameMode=ARENA_BONUS_TYPE.REGULAR):
        return vehTypeCompDescr in self.getSpecialVehiclesByGameMode(gameMode)

    def capBonusList(self):
        return self._season.get(b'capBonuses', (0,) * MAX_VEHICLE_LEVEL)

    def capBonus(self, vehLevel):
        return self.capBonusList()[vehLevel - 1]

    def vehicleContribution(self, vehTypeCompDescr):
        return self.vehicleCapacity(vehTypeCompDescr) + self.capBonusForVehTypeCompDescr(vehTypeCompDescr)

    def capBonusForVehTypeCompDescr(self, vehTypeCompDescr):
        return self.capBonusList()[getVehicleLevel(vehTypeCompDescr) - 1]

    def vehicleCapacity(self, vehTypeCompDescr):
        return self.vehCDCaps.get(vehTypeCompDescr, self.vehLevelCaps[getVehicleLevel(vehTypeCompDescr) - 1])

    def bonusPointsList(self, vehTypeCompDescr=None, isWinner=True, gameMode=ARENA_BONUS_TYPE.REGULAR):
        teamKey = b'win' if isWinner else b'lose'
        teamPoints = self.points.get(gameMode, {})
        if vehTypeCompDescr in teamPoints:
            teamPoints = teamPoints[vehTypeCompDescr]
        return teamPoints.get(teamKey) or (0,) * getBattlePassByGameMode(gameMode).getTeamSize()

    def getSeasonRewards(self):
        return self._rewards

    def getChapterRewards(self, chapterID, rewardType):
        return self._rewards.get(chapterID, {}).get(rewardType, {})

    def getTags(self, chapterID, level, rewardType):
        return self.getChapterRewards(chapterID, rewardType).get(level, ({}, tuple()))[BattlePassConfig.TAGS_IDX]

    def getRewardByMask(self, chapterID, level, rewardMask):
        return self.getRewardByType(chapterID, level, MASK_TO_REWARD[rewardMask])

    def getFreeReward(self, chapterID, level):
        return self.getRewardByType(chapterID, level, BattlePassConsts.REWARD_FREE)

    def getPaidReward(self, chapterID, level):
        return self.getRewardByType(chapterID, level, BattlePassConsts.REWARD_PAID)

    def getRewardByType(self, chapterID, level, rewardType):
        if isPostProgressionChapter(chapterID):
            cycleLength = self.postProgressionCycleLength
            level = getPostProgressionLevelInCycleForRewards(cycleLength, level)
        return self.getChapterRewards(chapterID, rewardType).get(level, ({}, tuple()))[BattlePassConfig.REWARD_IDX]

    def getChapterBorders(self, chapterID):
        fromLevel = 1
        toLevel = len(self.getChapterLevels(chapterID))
        return (fromLevel, toLevel)

    def getChapterIDs(self):
        return list(self.chapters)

    def getAvailableStyles(self):
        return tuple(chapter[b'styleId'] for chapter in viewvalues(self.chapters))

    def getChapterStyleID(self, chapterID):
        return self.chapters.get(chapterID, {}).get(b'styleId')

    def getChapter(self, chapterID):
        return self.chapters.get(chapterID, {})
