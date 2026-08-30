from __future__ import absolute_import
import struct, time
from future.utils import viewitems
from past.builtins import intern, xrange
import ResMgr, nations, quest_xml_source
from items import _xml, ItemsPrices, vehicles
from items.vehicles import VEHICLE_CLASS_TAGS
from constants import ITEM_DEFS_PATH, IS_CLIENT, IS_WEB, EVENT_TYPE, PERSONAL_MISSION_FREE_TOKEN_NAME, PERSONAL_MISSION_2_FREE_TOKEN_NAME, PERSONAL_MISSION_FINAL_PAWN_COST, PERSONAL_MISSION_2_FINAL_PAWN_COST, COMMON_ROLE_TO_ROLE_TYPE, COMMON_ROLE
from nations import ALLIANCES_TAGS
from personal_missions_constants import VEHICLE_RESTRICTION_MIN_LEVEL, VEHICLE_RESTRICTION_MAX_LEVEL
from soft_exception import SoftException
if IS_CLIENT:
    from helpers import i18n
elif IS_WEB:
    from web_stubs import i18n
POTAPOV_QUEST_XML_PATH = ITEM_DEFS_PATH + b'potapov_quests/'
_FALLOUT_BATTLE_TAGS = frozenset((b'classic', b'multiteam'))
_ALLOWED_TAG_NAMES = (
 b'initial', b'final') + tuple(_FALLOUT_BATTLE_TAGS) + tuple(VEHICLE_CLASS_TAGS) + tuple(ALLIANCES_TAGS) + tuple(COMMON_ROLE.ALL)
g_cache = None
g_tileCache = None
g_seasonCache = None

class PQ_BRANCH():
    REGULAR = 0
    PERSONAL_MISSION_2 = 2
    PERSONAL_MISSION_3 = 4
    ALL = (
     REGULAR, PERSONAL_MISSION_2, PERSONAL_MISSION_3)
    NAME_TO_TYPE = {b'regular': REGULAR, 
       b'pm2': PERSONAL_MISSION_2, 
       b'pm3': PERSONAL_MISSION_3}
    TYPE_TO_NAME = dict(zip(NAME_TO_TYPE.values(), NAME_TO_TYPE.keys()))
    V1_BRANCHES = (
     REGULAR,
     PERSONAL_MISSION_2)
    V2_BRANCHES = (
     PERSONAL_MISSION_3,)
    BRANCH_GROUPS = [
     V1_BRANCHES, V2_BRANCHES]


PM_BRANCH_TO_FREE_TOKEN_NAME = {(PQ_BRANCH.REGULAR): PERSONAL_MISSION_FREE_TOKEN_NAME, 
   (PQ_BRANCH.PERSONAL_MISSION_2): PERSONAL_MISSION_2_FREE_TOKEN_NAME}
PM_BRANCH_TO_FINAL_PAWN_COST = {(PQ_BRANCH.REGULAR): PERSONAL_MISSION_FINAL_PAWN_COST, 
   (PQ_BRANCH.PERSONAL_MISSION_2): PERSONAL_MISSION_2_FINAL_PAWN_COST}

def isPotapovQuestBranchEnabled(gameParams, branch):
    if branch == PQ_BRANCH.REGULAR:
        return gameParams[b'misc_settings'][b'isRegularQuestEnabled']
    if branch == PQ_BRANCH.PERSONAL_MISSION_2:
        return gameParams[b'misc_settings'][b'isPM2QuestEnabled']
    if branch == PQ_BRANCH.PERSONAL_MISSION_3:
        return gameParams[b'misc_settings'][b'isPM3QuestEnabled']
    return False


def isPotapovQuestTileEnabled(gameParams, pqType):
    return pqType.tileID not in gameParams[b'misc_settings'][b'disabledPMOperations']


def isPotapovQuestEnabled(gameParams, questID):
    return questID not in gameParams[b'misc_settings'][b'disabledPersonalMissions']


def isPotapovQuestBranchTileAndMissionEnabled(gameParams, pqType):
    return isPotapovQuestBranchEnabled(gameParams, pqType.branch) and isPotapovQuestTileEnabled(gameParams, pqType) and isPotapovQuestEnabled(gameParams, pqType.id)


class PQ_STATE():
    NONE = 0
    UNLOCKED = 1
    NEED_GET_MAIN_REWARD = 2
    MAIN_REWARD_GOTTEN = 3
    NEED_GET_ADD_REWARD = 4
    NEED_GET_ALL_REWARDS = 5
    ALL_REWARDS_GOTTEN = 6
    NEXT_STATE = {NONE: (
            UNLOCKED, NEED_GET_MAIN_REWARD, NEED_GET_ALL_REWARDS), 
       UNLOCKED: (
                NEED_GET_MAIN_REWARD, NEED_GET_ALL_REWARDS), 
       NEED_GET_MAIN_REWARD: (
                            MAIN_REWARD_GOTTEN, ALL_REWARDS_GOTTEN), 
       MAIN_REWARD_GOTTEN: (
                          NEED_GET_ADD_REWARD,), 
       NEED_GET_ADD_REWARD: (
                           ALL_REWARDS_GOTTEN,), 
       NEED_GET_ALL_REWARDS: (
                            ALL_REWARDS_GOTTEN,)}
    NEED_GET_REWARD = (
     NEED_GET_MAIN_REWARD, NEED_GET_ADD_REWARD, NEED_GET_ALL_REWARDS)
    COMPLETED = (ALL_REWARDS_GOTTEN, NEED_GET_ALL_REWARDS, NEED_GET_ADD_REWARD)


class PQ_FLAG():
    NONE = 0
    PAUSE = 1


PQ_REWARD_BY_DEMAND = {1: (
     PQ_STATE.NEED_GET_MAIN_REWARD, PQ_STATE.NEED_GET_ALL_REWARDS), 
   2: (
     PQ_STATE.NEED_GET_ADD_REWARD, PQ_STATE.NEED_GET_ALL_REWARDS), 
   3: (
     PQ_STATE.NEED_GET_MAIN_REWARD, PQ_STATE.NEED_GET_ADD_REWARD, PQ_STATE.NEED_GET_ALL_REWARDS)}

def init():
    global g_cache
    global g_seasonCache
    global g_tileCache
    g_seasonCache = SeasonCache()
    g_tileCache = TileCache()
    g_cache = PQCache()
    return


class SeasonCache():

    def __init__(self):
        self.__seasonsInfo = {}
        self.__readSeasons()
        return

    def getSeasonInfo(self, seasonID):
        if seasonID not in self.__seasonsInfo:
            raise SoftException(b'Invalid season id (%s)' % (seasonID,))
        return self.__seasonsInfo[seasonID]

    def __readSeasons(self):
        xmlPath = POTAPOV_QUEST_XML_PATH + b'/seasons.xml'
        section = ResMgr.openSection(xmlPath)
        if section is None:
            _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
        self.__seasonsInfo = idToSeason = {}
        ids = {}
        for sname, ssection in section.items():
            ctx = (None, xmlPath)
            if sname in ids:
                _xml.raiseWrongXml(ctx, b'', b'season name is not unique')
            seasonID = _xml.readInt(ctx, ssection, b'id', 0, 15)
            if seasonID in idToSeason:
                _xml.raiseWrongXml(ctx, b'id', b'is not unique')
            basicInfo = {b'name': sname}
            if IS_CLIENT or IS_WEB:
                basicInfo[b'userString'] = i18n.makeString(ssection.readString(b'userString'))
                basicInfo[b'description'] = i18n.makeString(ssection.readString(b'description'))
            ids[sname] = seasonID
            idToSeason[seasonID] = basicInfo

        return


class TileCache(object):

    def __init__(self):
        self.__tilesInfo = {}
        self.__readTiles()
        return

    def getTileInfo(self, tileID):
        if tileID not in self.__tilesInfo:
            raise SoftException(b'Invalid tile id (%s)' % (tileID,))
        return self.__tilesInfo[tileID]

    def __iter__(self):
        return iter(viewitems(self.__tilesInfo))

    def __readTiles(self):
        xmlPath = POTAPOV_QUEST_XML_PATH + b'/tiles.xml'
        section = ResMgr.openSection(xmlPath)
        if section is None:
            _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
        self.__tilesInfo = idToTile = {}
        ids = {}
        for tname, tsection in section.items():
            if tname == b'quests':
                continue
            ctx = (
             None, xmlPath)
            if tname in ids:
                _xml.raiseWrongXml(ctx, b'', b'tile name is not unique')
            seasonID = _xml.readInt(ctx, tsection, b'seasonID')
            g_seasonCache.getSeasonInfo(seasonID)
            tileID = _xml.readInt(ctx, tsection, b'id', 0, 15)
            if tileID in idToTile:
                _xml.raiseWrongXml(ctx, b'id', b'is not unique')
            chainsCount = _xml.readInt(ctx, tsection, b'chainsCount', 1, 15)
            chainsCountToUnlockNext = _xml.readInt(ctx, tsection, b'chainsCountToUnlockNext', 0, 15)
            nextTileIDs = frozenset(int(tileID) for tileID in _xml.readString(ctx, tsection, b'nextTileIDs').split())
            achievements = {}
            basicInfo = {b'name': tname, 
               b'chainsCount': chainsCount, 
               b'nextTileIDs': nextTileIDs, 
               b'chainsCountToUnlockNext': chainsCountToUnlockNext, 
               b'questsInChain': (_xml.readInt(ctx, tsection, b'questsInChain', 1, 100)), 
               b'price': (ItemsPrices._tuplePrice(_xml.readPrice(ctx, tsection, b'price'))), 
               b'achievements': achievements, 
               b'seasonID': seasonID, 
               b'tokens': (set(_xml.readString(ctx, tsection, b'tokens').split()))}
            if tsection.has_key(b'achievements'):
                for aname, asection in tsection[b'achievements'].items():
                    _, aid = aname.split(b'_')
                    achievements[int(aid)] = asection.asString

                if len(achievements) < basicInfo[b'chainsCount']:
                    _xml.raiseWrongXml(ctx, b'achievements', b'wrong achievement number')
            if IS_CLIENT or IS_WEB:
                basicInfo[b'userString'] = i18n.makeString(tsection.readString(b'userString'))
                basicInfo[b'description'] = i18n.makeString(tsection.readString(b'description'))
                basicInfo[b'iconID'] = i18n.makeString(tsection.readString(b'iconID'))
            ids[tname] = tileID
            idToTile[tileID] = basicInfo

        return


class PQCache(object):

    def __init__(self, auxData=None):
        self.__potapovQuestIDToQuestType = {}
        self.__questUniqueIDToPotapovQuestID = {}
        self.__tileIDchainIDToPotapovQuestID = {}
        self.__tileIDchainIDToFinalPotapovQuestID = {}
        self.__tileIDchainIDToInitialPotapovQuestID = {}
        self.__readQuestList(auxData=auxData)
        return

    def questByPotapovQuestID(self, potapovQuestID):
        if potapovQuestID not in self.__potapovQuestIDToQuestType:
            raise SoftException(b'Invalid potapov quest id (%s)' % (potapovQuestID,))
        return self.__potapovQuestIDToQuestType[potapovQuestID]

    def hasPotapovQuest(self, potapovQuestID):
        return potapovQuestID in self.__potapovQuestIDToQuestType

    def getPotapovQuests(self):
        return self.__potapovQuestIDToQuestType

    def questByUniqueQuestID(self, uniqueQuestID):
        return self.questByPotapovQuestID(self.getPotapovQuestIDByUniqueID(uniqueQuestID))

    def isPotapovQuest(self, uniqueQuestID):
        return uniqueQuestID in self.__questUniqueIDToPotapovQuestID

    def questListByTileIDChainID(self, tileID, chainID):
        return self.__tileIDchainIDToPotapovQuestID[tileID, chainID]

    def finalPotapovQuestIDByTileIDChainID(self, tileID, chainID):
        return self.__tileIDchainIDToFinalPotapovQuestID[tileID, chainID]

    def initialPotapovQuestIDByTileIDChainID(self, tileID, chainID):
        return self.__tileIDchainIDToInitialPotapovQuestID[tileID, chainID]

    def getPotapovQuestIDByUniqueID(self, uniqueQuestID):
        if uniqueQuestID not in self.__questUniqueIDToPotapovQuestID:
            raise SoftException(b'Invalid potapov quest name (%s)' % (uniqueQuestID,))
        return self.__questUniqueIDToPotapovQuestID[uniqueQuestID]

    def branchByPotapovQuestID(self, potapovQuestID):
        return PQ_BRANCH.TYPE_TO_NAME[self.questByPotapovQuestID(potapovQuestID).branch]

    def getPotapovQuestNameByQuestID(self, questID):
        return self.questByPotapovQuestID(questID).generalQuestID

    def getPotapovQuestIDByName(self, questName):
        return self.getPotapovQuestIDByUniqueID((b'{}_main').format(questName))

    def __iter__(self):
        return iter(viewitems(self.__questUniqueIDToPotapovQuestID))

    def __readQuestList(self, auxData=None):
        xmlPath = POTAPOV_QUEST_XML_PATH + b'/list.xml'
        section = ResMgr.openSection(xmlPath)
        if section is None:
            _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
        self.__potapovQuestIDToQuestType = idToQuest = {}
        self.__questUniqueIDToPotapovQuestID = questUniqueNameToPotapovQuestID = {}
        self.__tileIDchainIDToPotapovQuestID = tileIDchainIDToPotapovQuestID = {}
        self.__tileIDchainIDToFinalPotapovQuestID = tileIDchainIDToFinalPotapovQuestID = {}
        self.__tileIDchainIDToInitialPotapovQuestID = tileIDchainIDToInitialPotapovQuestID = {}
        ids = {}
        curTime = int(time.time())
        xmlSource = quest_xml_source.Source()
        for qname, qsection in section.items():
            splitted = qname.split(b'_')
            ctx = (None, xmlPath)
            if qname in ids:
                _xml.raiseWrongXml(ctx, b'', b'potapov quest name is not unique')
            potapovQuestID = _xml.readInt(ctx, qsection, b'id', 0, 1023)
            if potapovQuestID in idToQuest:
                _xml.raiseWrongXml(ctx, b'id', b'is not unique')
            questBranchName, tileID, chainID, internalID = splitted
            isPM3 = questBranchName == b'pm3'
            tileInfo = g_tileCache.getTileInfo(int(tileID))
            if 1 <= chainID <= tileInfo[b'chainsCount']:
                _xml.raiseWrongXml(ctx, b'', b'quest chainID must be between 1 and %s' % tileInfo[b'chainsCount'])
            if 1 <= internalID <= tileInfo[b'questsInChain']:
                _xml.raiseWrongXml(ctx, b'', b'quest internalID must be between 1 and %s' % tileInfo[b'chainsCount'])
            minLevel = _xml.readInt(ctx, qsection, b'minLevel', VEHICLE_RESTRICTION_MIN_LEVEL, VEHICLE_RESTRICTION_MAX_LEVEL)
            maxLevel = _xml.readInt(ctx, qsection, b'maxLevel', minLevel, VEHICLE_RESTRICTION_MAX_LEVEL)
            basicInfo = {b'name': qname, 
               b'id': potapovQuestID, 
               b'branch': (PQ_BRANCH.NAME_TO_TYPE[questBranchName]), 
               b'tileID': (int(tileID)), 
               b'chainID': (int(chainID)), 
               b'internalID': (int(internalID)), 
               b'minLevel': minLevel, 
               b'maxLevel': maxLevel, 
               b'requiredUnlocks': (frozenset(int(unlock) for unlock in _xml.readString(ctx, qsection, b'requiredUnlocks').split()))}
            rewardByDemand = qsection.readInt(b'rewardByDemand', 0)
            if rewardByDemand != 0 and rewardByDemand not in PQ_REWARD_BY_DEMAND.keys():
                raise SoftException(b'Unexpected value for rewardByDemand')
            basicInfo[b'rewardByDemand'] = rewardByDemand
            tags = _readTags(ctx, qsection, b'tags')
            basicInfo[b'tags'] = tags
            if questBranchName == b'regular':
                if not tags & VEHICLE_CLASS_TAGS:
                    _xml.raiseWrongXml(ctx, b'tags', b'quest vehicle class is not specified')
            if questBranchName == b'fallout':
                if not tags & _FALLOUT_BATTLE_TAGS:
                    _xml.raiseWrongXml(ctx, b'tags', b'quest fallout type is not specified')
            if questBranchName == b'pm2':
                if not tags & ALLIANCES_TAGS:
                    _xml.raiseWrongXml(ctx, b'tags', b'quest vehicle alliance is not specified')
            if isPM3:
                if not tags & COMMON_ROLE.ALL:
                    _xml.raiseWrongXml(ctx, b'tags', b'quest vehicle role is not specified')
            if IS_CLIENT or IS_WEB:
                basicInfo[b'userString'] = i18n.makeString(qsection.readString(b'userString'))
                basicInfo[b'shortUserString'] = i18n.makeString(qsection.readString(b'shortUserString'))
                basicInfo[b'description'] = qsection.readString(b'description')
                basicInfo[b'advice'] = qsection.readString(b'advice')
            questPath = (b'').join([POTAPOV_QUEST_XML_PATH, 39, questBranchName, 40, tileID, 41, 
             chainID, 
             39, qname, 42])
            questCtx = (None, questPath)
            nodes = xmlSource.readFromInternalFile(questPath, curTime, auxData)
            nodes = nodes.get(EVENT_TYPE.POTAPOV_QUEST, None)
            if nodes is None:
                _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Potapov quests are not specified.')
            if isPM3 and len(nodes) != 2 or not isPM3 and len(nodes) != 4:
                _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Main and additional quest should be presented.')
            qinfo = nodes[0].info
            if not qinfo[b'id'].endswith(b'main'):
                _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Main quest must be first.')
            if qinfo[b'id'] in questUniqueNameToPotapovQuestID:
                _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Duplicate name detected.')
            questUniqueNameToPotapovQuestID[qinfo[b'id']] = potapovQuestID
            basicInfo[b'mainQuestID'] = qinfo[b'id']
            if IS_CLIENT or IS_WEB:
                basicInfo[b'mainQuestInfo'] = qinfo[b'questClientData']
            if not isPM3:
                qinfo = nodes[1].info
                if not qinfo[b'id'].endswith(b'main_award_list'):
                    _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Main award list quest must be second.')
                if qinfo[b'id'] in questUniqueNameToPotapovQuestID:
                    _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Duplicate name detected.')
                questUniqueNameToPotapovQuestID[qinfo[b'id']] = potapovQuestID
                basicInfo[b'mainAwardListQuestID'] = qinfo[b'id']
                if IS_CLIENT or IS_WEB:
                    basicInfo[b'mainAwardListQuestInfo'] = qinfo[b'questClientData']
            else:
                basicInfo[b'mainAwardListQuestID'] = None
                basicInfo[b'mainAwardListQuestInfo'] = None
            qinfo = nodes[1].info if isPM3 else nodes[2].info
            if not qinfo[b'id'].endswith(b'add'):
                _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Add quest must be third.')
            if qinfo[b'id'] in questUniqueNameToPotapovQuestID:
                _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Duplicate name detected.')
            questUniqueNameToPotapovQuestID[qinfo[b'id']] = potapovQuestID
            basicInfo[b'addQuestID'] = qinfo[b'id']
            if IS_CLIENT or IS_WEB:
                basicInfo[b'addQuestInfo'] = qinfo[b'questClientData']
            if not isPM3:
                qinfo = nodes[3].info
                if not qinfo[b'id'].endswith(b'add_award_list'):
                    _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Add award list quest must be fourth.')
                if qinfo[b'id'] in questUniqueNameToPotapovQuestID:
                    _xml.raiseWrongXml(questCtx, b'potapovQuest', b'Duplicate name detected.')
                questUniqueNameToPotapovQuestID[qinfo[b'id']] = potapovQuestID
                basicInfo[b'addAwardListQuestID'] = qinfo[b'id']
                if IS_CLIENT or IS_WEB:
                    basicInfo[b'addAwardListQuestInfo'] = qinfo[b'questClientData']
            else:
                basicInfo[b'addAwardListQuestID'] = None
                basicInfo[b'addAwardListQuestInfo'] = None
            idToQuest[potapovQuestID] = PQType(basicInfo)
            ids[qname] = potapovQuestID
            key = (int(tileID), int(chainID))
            tileIDchainIDToPotapovQuestID.setdefault(key, set()).add(potapovQuestID)
            if b'final' in tags:
                tileIDchainIDToFinalPotapovQuestID[key] = potapovQuestID
            if b'initial' in tags:
                tileIDchainIDToInitialPotapovQuestID[key] = potapovQuestID

        ResMgr.purge(xmlPath, True)
        return


class ClassifierByClass(object):

    def __init__(self, questTags):
        vehClasses = list(questTags & VEHICLE_CLASS_TAGS)
        if len(vehClasses) != 1:
            raise SoftException(b'Potapov quest with tags %s has more than one vehicle class' % str(questTags))
        self.vehClass = vehClasses[0]
        return

    @property
    def classificationAttr(self):
        return self.vehClass

    def matchVehicle(self, vehicleType):
        vehClass = tuple(vehicles.VEHICLE_CLASS_TAGS & vehicleType.tags)[0]
        return vehClass == self.vehClass


class ClassifierByAlliance(object):

    def __init__(self, questTags):
        alliances = list(questTags & ALLIANCES_TAGS)
        if len(alliances) != 1:
            raise SoftException(b'Potapov quest with tags %s has more than one alliance' % str(questTags))
        self.alliance = alliances[0]
        return

    @property
    def classificationAttr(self):
        return self.alliance

    def matchVehicle(self, vehicleType):
        nationID = vehicleType.id[0]
        return nations.NAMES[nationID] in nations.ALLIANCE_TO_NATIONS[self.alliance]


class ClassifierByRole(object):

    def __init__(self, questTags):
        commonRoles = COMMON_ROLE.ALL & questTags
        if len(commonRoles) != 1:
            raise SoftException(b'Potapov quest with tags %s must have exactly one common role' % str(questTags))
        self.commonRole = commonRole = next(iter(commonRoles))
        self.roles = COMMON_ROLE_TO_ROLE_TYPE[commonRole]
        return

    @property
    def classificationAttr(self):
        return self.commonRole

    def matchVehicle(self, vehicleType):
        return vehicleType.role in self.roles


class PQType(object):
    __slots__ = (b'id', b'tags', b'isInitial', b'isFinal', b'branch', b'classifier', b'tileID', b'chainID', b'internalID', b'requiredUnlocks', b'generalQuestID', b'mainQuestID', b'mainAwardListQuestID', b'addQuestID', b'addAwardListQuestID', b'mainQuestInfo', b'addQuestInfo', b'userString', b'shortUserString', b'description', b'advice', b'minLevel', b'maxLevel', b'rewardByDemand', b'mainAwardListQuestInfo', b'addAwardListQuestInfo')

    def __init__(self, basicInfo):
        self.id = basicInfo[b'id']
        self.tags = tags = basicInfo[b'tags']
        self.isInitial = b'initial' in tags
        self.isFinal = b'final' in tags
        self.minLevel = basicInfo[b'minLevel']
        self.maxLevel = basicInfo[b'maxLevel']
        self.rewardByDemand = basicInfo[b'rewardByDemand']
        self.branch = basicInfo[b'branch']
        self.tileID = basicInfo[b'tileID']
        self.chainID = basicInfo[b'chainID']
        self.internalID = basicInfo[b'internalID']
        self.requiredUnlocks = basicInfo[b'requiredUnlocks']
        self.generalQuestID = basicInfo[b'name']
        self.mainQuestID = basicInfo[b'mainQuestID']
        self.mainAwardListQuestID = basicInfo[b'mainAwardListQuestID']
        self.addQuestID = basicInfo[b'addQuestID']
        self.addAwardListQuestID = basicInfo[b'addAwardListQuestID']
        if self.branch == PQ_BRANCH.REGULAR:
            self.classifier = ClassifierByClass(self.tags)
        elif self.branch == PQ_BRANCH.PERSONAL_MISSION_2:
            self.classifier = ClassifierByAlliance(self.tags)
        elif self.branch == PQ_BRANCH.PERSONAL_MISSION_3:
            self.classifier = ClassifierByRole(self.tags)
        else:
            raise SoftException(b'wrong potapov quest branch: %i' % self.branch)
        if IS_CLIENT or IS_WEB:
            self.mainQuestInfo = basicInfo[b'mainQuestInfo']
            self.mainAwardListQuestInfo = basicInfo[b'mainAwardListQuestInfo']
            self.addQuestInfo = basicInfo[b'addQuestInfo']
            self.addAwardListQuestInfo = basicInfo[b'addAwardListQuestInfo']
            self.userString = basicInfo[b'userString']
            self.shortUserString = basicInfo[b'shortUserString']
            self.description = basicInfo[b'description']
            self.advice = basicInfo[b'advice']
        return

    def getMajorTag(self):
        return self.classifier.classificationAttr

    def maySelectQuest(self, unlockedQuests):
        return len(self.requiredUnlocks - frozenset(unlockedQuests)) == 0

    def maySelectQuestToPawn(self, unlockedQuests):
        result = True
        requiredQuestIds = self.requiredUnlocks - frozenset(unlockedQuests)
        for requiredQuestId in requiredQuestIds:
            pqType = g_cache.questByPotapovQuestID(requiredQuestId)
            result &= pqType.maySelectQuest(unlockedQuests)

        return result

    def tryUnlockNextTile(self, potapovQuestsProgress):
        if not self.isFinal:
            return (False, [])
        tileInfo = g_tileCache.getTileInfo(self.tileID)
        nextTileIDs = tileInfo[b'nextTileIDs']
        if len(nextTileIDs) == 0:
            return (False, [])
        chainsCountToUnlockNext = tileInfo[b'chainsCountToUnlockNext']
        if chainsCountToUnlockNext == 0:
            return (False, [])
        completedQuestsCount = 0
        toUnlock = set()
        for chainID in xrange(1, tileInfo[b'chainsCount'] + 1):
            finalQuestID = g_cache.finalPotapovQuestIDByTileIDChainID(self.tileID, chainID)
            _, state = potapovQuestsProgress.get(finalQuestID)
            if state >= PQ_STATE.NEED_GET_ADD_REWARD:
                completedQuestsCount += 1
            elif state == PQ_STATE.NONE:
                toUnlock.add(finalQuestID)

        return (
         completedQuestsCount >= chainsCountToUnlockNext, toUnlock)

    @property
    def isPM3(self):
        return self.branch == PQ_BRANCH.PERSONAL_MISSION_3


class PQStorage(object):

    def __init__(self, compDescr=None, storage=None):
        if compDescr is not None:
            self.__compDescr = compDescr
            self.__quests = quests = {}
            if compDescr == b'':
                return
            size = struct.unpack(b'<H', compDescr[:2])[0]
            lst = struct.unpack(b'<%sH' % size, compDescr[2:])
            for i in xrange(size):
                v = lst[i]
                quests[v >> 6 & 1023] = (v >> 3 & 7, v & 7)

        elif storage is not None:
            self.__compDescr = None
            self.__quests = storage
        return

    def keys(self):
        return list(self.__quests)

    def completedPQIDs(self):
        return [k for k, v in viewitems(self.__quests) if v[1] >= PQ_STATE.NEED_GET_MAIN_REWARD]

    def unlockedPQIDs(self):
        return [k for k, v in viewitems(self.__quests) if v[1] >= PQ_STATE.UNLOCKED]

    def __getitem__(self, id):
        return self.__quests[id]

    def __setitem__(self, id, value):
        oldValue = self.__quests.get(id, None)
        if oldValue == value:
            return
        else:
            self.__compDescr = None
            self.__quests[id] = value
            return

    def __contains__(self, id):
        return id in self.__quests

    def get(self, key, default=(
 PQ_FLAG.NONE, PQ_STATE.NONE)):
        return self.__quests.get(key, default)

    def pop(self, id):
        oldValue = self.__quests.get(id, None)
        if oldValue is None:
            return
        else:
            self.__compDescr = None
            self.__quests.pop(id)
            return

    def makeCompDescr(self):
        if self.__compDescr is not None:
            return self.__compDescr
        else:
            quests = self.__quests
            size = len(quests)
            packedValues = [((id & 1023) << 6) + ((flags & 7) << 3) + (state & 7) for id, (flags, state) in viewitems(quests)]
            self.__compDescr = struct.pack((b'<%sH' % (size + 1)), size, *packedValues)
            return self.__compDescr

    def iteritems(self):
        return iter(viewitems(self.__quests))

    def items(self):
        return viewitems(self.__quests)


def _readTags(xmlCtx, section, subsectionName):
    tagNames = _xml.readString(xmlCtx, section, subsectionName).split()
    res = set()
    for tagName in tagNames:
        if tagName not in _ALLOWED_TAG_NAMES:
            _xml.raiseWrongXml(xmlCtx, subsectionName, b"unknown tag '%s'" % tagName)
        res.add(intern(tagName))

    return frozenset(res)


def isPM3Quest(questID):
    branch = questID.split(b'_', 1)[0]
    return branch == PQ_BRANCH.TYPE_TO_NAME[PQ_BRANCH.PERSONAL_MISSION_3]
