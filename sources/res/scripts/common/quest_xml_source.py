import time, ArenaType, ResMgr, nations, constants
from soft_exception import SoftException
from copy import deepcopy
from pprint import pformat
from bonus_readers import readBonusSection, readUTC, timeDataToUTC, checkLogExtInfoLen
from constants import VEHICLE_CLASS_INDICES, ARENA_BONUS_TYPE, EVENT_TYPE, IGR_TYPE, ATTACK_REASONS, QUEST_RUN_FLAGS, DEFAULT_QUEST_START_TIME, DEFAULT_QUEST_FINISH_TIME, ROLE_LABEL_TO_TYPE, ACCOUNT_ATTR, QUESTS_SUPPORTED_EXCLUDE_TAGS, MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL, ALL_EVENT_TYPES_FOR_BONUSES, EXTENSIONS_BONUSES
from debug_utils import LOG_WARNING
from dossiers2.custom.layouts import accountDossierLayout, vehicleDossierLayout, StaticSizeBlockBuilder, BinarySetDossierBlockBuilder
from dossiers2.custom.records import RECORD_DB_IDS
from items import vehicles
from optional_bonuses import StripVisitor
from battle_results import getBattleResultsNames
_WEEKDAYS = {b'Mon': 1, b'Tue': 2, b'Wed': 3, b'Thu': 4, b'Fri': 5, b'Sat': 6, b'Sun': 7}
_YEAR = 31556926
MAX_BONUS_LIMIT = 1000000

class XMLNode(object):
    __slots__ = (b'name', b'value', b'questClientConditions', b'relatedGroup', b'info', b'bonus', b'bonusDelayed', b'groupContent', b'scripts')

    def __init__(self, name=b''):
        self.name = intern(name)
        self.value = []
        self.questClientConditions = []
        self.relatedGroup = b''
        self.info = {}
        self.bonus = {}
        self.bonusDelayed = {}
        self.groupContent = None
        self.scripts = b''
        return

    def __repr__(self):
        dump = {b'name': (self.name), 
           b'conditions': (self.questClientConditions), 
           b'nested': (self.value)}
        if self.relatedGroup:
            dump.update(group=self.relatedGroup)
        return pformat(dump, indent=4)

    def getChildNode(self, name, relatedGroup=None):
        childNode = None
        for subnode in self.value:
            if not isinstance(subnode, XMLNode):
                continue
            if subnode.name == name or relatedGroup is not None and subnode.relatedGroup == relatedGroup:
                childNode = subnode
                break

        return childNode

    def getFirstChildValue(self):
        if len(self.value) == 0:
            return None
        else:
            return self.value[0]

    def isExistChildNode(self, nodeName):
        for child in self.value:
            if isinstance(child, XMLNode):
                if child.name == nodeName or child.isExistChildNode(nodeName):
                    return True

        return False

    def addChild(self, childNode, needClientInfo=True):
        self.value.append(childNode)
        if not needClientInfo:
            return
        if isinstance(childNode, XMLNode):
            self.questClientConditions.append((childNode.name, childNode.questClientConditions))
        else:
            self.questClientConditions.append((b'value', childNode))
        return


class Source(object):

    def __init__(self):
        return

    def readFromExternalFile(self, path, gStartTime, gFinishTime, curTime):
        ResMgr.purge(path)
        section = ResMgr.openSection(path)
        if section is None:
            raise SoftException(b"Can not open '%s'" % path)
        if not section.has_key(b'quests'):
            return {}
        else:
            return self.__readXML(section[b'quests'], curTime, gStartTime, gFinishTime)

    def readFromInternalFile(self, path, curTime):
        ResMgr.purge(path)
        section = ResMgr.openSection(path)
        if section is None:
            raise SoftException(b"Can not open '%s'" % path)
        if not section.has_key(b'quests'):
            return {}
        else:
            return self.__readXML(section[b'quests'], curTime)

    def readFromString(self, xml, curTime):
        section = ResMgr.DataSection(b'root').createSectionFromString(xml)
        if not section.has_key(b'quests'):
            return {}
        return self.__readXML(section[b'quests'], curTime)

    def __readXML(self, section, curTime, gStartTime=DEFAULT_QUEST_START_TIME, gFinishTime=DEFAULT_QUEST_FINISH_TIME):
        nodes = {}
        for typeName, questSection in section.items():
            enabled = questSection.readBool(b'enabled', False)
            if not enabled:
                continue
            eventType = EVENT_TYPE.NAME_TO_TYPE[typeName]
            mainNode = XMLNode(b'main')
            mainNode.info = info = self.__readHeader(eventType, questSection, curTime, gStartTime, gFinishTime)
            if not info[b'announceTime'] <= curTime <= info[b'finishTime']:
                LOG_WARNING(b'Skipping outdated quest', info[b'id'], curTime, info[b'announceTime'], info[b'finishTime'])
                continue
            if eventType == EVENT_TYPE.GROUP:
                mainNode.groupContent = tuple(self.__readGroupContent(questSection))
            conditionReaders = self.__getConditionReaders(eventType)
            availableBonuses = self.__getAvailableBonuses(eventType)
            commonNode = XMLNode(b'common')
            bonusNode = XMLNode(b'bonus')
            bonusDelayedNode = XMLNode(b'bonusDelayed')
            prebattleNode = XMLNode(b'preBattle')
            battleNode = XMLNode(b'battle')
            prebattleNode.addChild(battleNode)
            accountNode = XMLNode(b'account')
            prebattleNode.addChild(accountNode)
            vehicleNode = XMLNode(b'vehicle')
            prebattleNode.addChild(vehicleNode)
            postbattleNode = XMLNode(b'postBattle')
            mainNode.addChild(prebattleNode)
            mainNode.addChild(postbattleNode)
            mainNode.addChild(commonNode)
            mainNode.addChild(bonusNode)
            mainNode.addChild(bonusDelayedNode)
            info[b'isIGR'] = accountNode.isExistChildNode(b'igrType')
            conditions = questSection[b'conditions']
            if conditions and conditions.has_key(b'preBattle'):
                condition = conditions[b'preBattle']
                if condition.has_key(b'account'):
                    self.__readBattleResultsConditionList(conditionReaders, condition[b'account'], accountNode)
                if eventType in EVENT_TYPE.LIKE_BATTLE_QUESTS:
                    if condition.has_key(b'vehicle'):
                        self.__readBattleResultsConditionList(conditionReaders, condition[b'vehicle'], vehicleNode)
                    if condition.has_key(b'battle'):
                        self.__readBattleResultsConditionList(conditionReaders, condition[b'battle'], battleNode)
            if eventType in EVENT_TYPE.LIKE_BATTLE_QUESTS and conditions and conditions.has_key(b'postBattle'):
                condition = conditions[b'postBattle']
                self.__readBattleResultsConditionList(conditionReaders, condition, postbattleNode)
            if conditions and conditions.has_key(b'common'):
                condition = conditions[b'common']
                self.__readBattleResultsConditionList(conditionReaders, condition, commonNode)
            if conditions and conditions.has_key(b'description'):
                description = conditions[b'description']
                mainNode.questClientConditions.append((b'description', self.__readMetaSection(description)))
            daily = commonNode.getChildNode(b'daily')
            info[b'isDaily'] = daily is not None
            weekly = commonNode.getChildNode(b'weekly')
            info[b'isWeekly'] = weekly is not None
            groupBy = commonNode.getChildNode(b'groupBy')
            info[b'groupBy'] = groupBy.getChildNode(b'groupName').getFirstChildValue() if groupBy else None
            inrow = commonNode.getChildNode(b'inrow')
            unit = commonNode.getChildNode(b'unit')
            bonusLimit = commonNode.getChildNode(b'bonusLimit')
            cumulative = commonNode.getChildNode(b'cumulative')
            cumulativeExt = commonNode.getChildNode(b'cumulativeExt')
            cumulativeSum = commonNode.getChildNode(b'cumulativeSum')
            vehicleKills = commonNode.getChildNode(b'vehicleKills')
            battles = commonNode.getChildNode(b'battles')
            battleCount = battles.getChildNode(b'count').getFirstChildValue() if battles else None
            if bonusLimit is None:
                bonusLimitNode = XMLNode(b'bonusLimit')
                bonusLimitNode.addChild(1 if eventType in EVENT_TYPE.ONE_BONUS_QUEST else MAX_BONUS_LIMIT)
                commonNode.addChild(bonusLimitNode)
            if eventType in EVENT_TYPE.LIKE_BATTLE_QUESTS:
                if (cumulative or cumulativeExt or cumulativeSum or unit or vehicleKills) and inrow:
                    raise SoftException(b'battleQuest: Unexpected tags (vehicleKills, cumulative, cumulativeExtcumulativeSum, unit/cumulative, unit/cumulativeExt) with inrow')
                if not (cumulative or cumulativeExt or cumulativeSum or unit or vehicleKills or bonusLimit or battles) and (daily or weekly or groupBy):
                    raise SoftException(b'battleQuest: daily, weekly and groupBy should be used with cumulative, cumulativeExt, cumulativeSum, unit, vehicleKills, bonusLimit or battles tags')
                if battles and not battleCount:
                    raise SoftException(b'Invalid battles section')
            elif eventType in EVENT_TYPE.LIKE_TOKEN_QUESTS:
                if cumulative or cumulativeExt or cumulativeSum or unit or vehicleKills or groupBy or battles:
                    raise SoftException(b'tokenQuest: Unexpected tags (cumulative, cumulativeExt, cumulativeSum, unit, vehicleKills, groupBy, battles)')
                if not bonusLimit and (daily or weekly):
                    raise SoftException(b'tokenQuest: daily or weekly should be used with bonusLimit tag')
            mainNode.bonus = readBonusSection(availableBonuses, questSection[b'bonus'], eventType)
            mainNode.bonusDelayed = readBonusSection(availableBonuses, questSection[b'bonusDelayed'], eventType)
            if constants.IS_DYNUPDATER:
                from account_helpers.ServiceTokenDispatcher import ServiceTokenDispatcher
                ServiceTokenDispatcher.validateFromQuest(mainNode.bonus, info[b'id'])
                ServiceTokenDispatcher.validateFromQuest(mainNode.bonusDelayed, info[b'id'])
            if eventType in (EVENT_TYPE.NT_QUEST, EVENT_TYPE.PERSONAL_MISSION):
                mainNode.scripts = questSection[b'scripts'].asString if questSection.has_key(b'scripts') else b''
            questClientData = dict(info)
            questClientData[b'bonus'] = deepcopy(mainNode.bonus)
            if mainNode.bonusDelayed is not None:
                questClientData[b'bonus'].update(mainNode.bonusDelayed)
            questClientData[b'bonusDelayed'] = deepcopy(mainNode.bonusDelayed)
            if eventType != EVENT_TYPE.PERSONAL_MISSION:
                questClientData[b'conditions'] = mainNode.questClientConditions
            if mainNode.groupContent:
                questClientData[b'groupContent'] = mainNode.groupContent
            self.__stripServerQuestData(questClientData)
            mainNode.info[b'questClientData'] = questClientData
            nodes.setdefault(eventType, []).append(mainNode)

        return nodes

    def __stripServerQuestData(self, questClientData):
        questClientData.pop(b'serverOnly', None)
        questClientData[b'bonus'] = StripVisitor().walkBonuses(questClientData[b'bonus'])
        questClientData[b'bonusDelayed'] = StripVisitor().walkBonuses(questClientData[b'bonusDelayed'])
        return

    def __readHeader(self, eventType, questSection, curTime, gStartTime, gFinishTime):

        def timeFormatTest(testTime):
            testHour, testMinute = testTime
            if testHour < 0 or testHour > 24 or testMinute < 0 or testMinute > 59 or testHour == 24 and testMinute != 0:
                raise SoftException(b'Bad time format. (%02d:%02d) must be HH:MM, 00:00 to 24:00' % (testHour, testMinute))
            testTime = str(testHour).zfill(2) + b':' + str(testMinute).zfill(2)
            return testTime

        id = questSection.readString(b'id', b'')
        checkLogExtInfoLen(id, b'quests')
        if not id:
            raise SoftException(b'Quest id must be specified.')
        if questSection.has_key(b'name'):
            questName = self.__readMetaSection(questSection[b'name'])
        else:
            questName = b''
        if questSection.has_key(b'description'):
            description = self.__readMetaSection(questSection[b'description'])
        else:
            description = b''
        startTime = readUTC(questSection, b'startTime', gStartTime)
        finishTime = readUTC(questSection, b'finishTime', gFinishTime)
        progressExpiryTime = readUTC(questSection, b'progressExpiryTime', finishTime)
        defaultAnnounceTime = gStartTime if gStartTime != DEFAULT_QUEST_START_TIME else startTime
        announceTime = readUTC(questSection, b'announceTime', defaultAnnounceTime)
        weekDayNames = questSection.readString(b'weekDays', b'').split()
        weekDays = set([_WEEKDAYS[val] for val in weekDayNames])
        intervalsInString = questSection.readString(b'activeTimeIntervals', b'').split()
        makeHM = lambda hm: tuple(int(v) for v in hm.split(b':'))
        makeIntervals = lambda intervals: tuple(makeHM(v) for v in intervals.split(b'_'))
        activeTimeIntervals = [makeIntervals(i) for i in intervalsInString]
        for intervalStartTime, intervalFinishTime in activeTimeIntervals:
            intervalStart = timeFormatTest(intervalStartTime)
            intervalFinish = timeFormatTest(intervalFinishTime)
            if intervalFinishTime <= intervalStartTime:
                raise SoftException(b'Interval finish time (%s) must be later than interval start time (%s)' % (
                 intervalFinish, intervalStart))

        if announceTime < gStartTime:
            raise SoftException(b'Invalid announce time. announceTime:%s < gStartTime:%s' % (announceTime, gStartTime))
        if startTime < announceTime:
            raise SoftException(b'Invalid announce time. startTime:%s < announceTime:%s' % (startTime, announceTime))
        if startTime < gStartTime:
            raise SoftException(b'Invalid start time. startTime:%s < gStartTime:%s' % (startTime, gStartTime))
        if finishTime > gFinishTime:
            raise SoftException(b'Invalid finish time. finishTime:%s > gFinishTime:%s' % (finishTime, gFinishTime))
        if progressExpiryTime < finishTime:
            raise SoftException(b'Invalid progress expiry time. progressExpiryTime:%s < finishTime:%s' % (
             progressExpiryTime, finishTime))
        requiredToken = questSection.readString(b'requiredToken', b'')
        if eventType == EVENT_TYPE.PERSONAL_QUEST:
            if not requiredToken:
                raise SoftException(b'Personal quest must contain tag <requiredToken> with not empty token')
        runFlags = []
        if questSection.has_key(b'run'):
            for flagName, flagValue in questSection[b'run'].items():
                if flagName == b'on':
                    runFlags.append(QUEST_RUN_FLAGS.NAME_TO_TYPE[flagValue.asString])

        tOption = curTime > time.time()
        showCongrats = questSection.readBool(b'showCongrats', eventType in (EVENT_TYPE.PERSONAL_MISSION,))
        onlyForPeripheriesList = questSection.readString(b'peripheryIDs', b'')
        info = {b'id': id, 
           b'hidden': (questSection.readBool(b'hidden', False)), 
           b'serverOnly': (questSection.readBool(b'serverOnly', False)), 
           b'name': questName, 
           b'type': eventType, 
           b'description': description, 
           b'saveProgress': (questSection.readBool(b'saveProgress', True)), 
           b'progressExpiryTime': progressExpiryTime, 
           b'weekDays': weekDays, 
           b'activeTimeIntervals': activeTimeIntervals, 
           b'startTime': (startTime if not tOption else time.time() - 300), 
           b'finishTime': finishTime, 
           b'announceTime': announceTime, 
           b'disableGui': (questSection.readBool(b'disableGui', False)), 
           b'showCongrats': showCongrats, 
           b'requiredToken': requiredToken, 
           b'Toption': (None if not tOption else startTime), 
           b'priority': (questSection.readInt(b'priority', 0)), 
           b'uiDecoration': (questSection.readInt(b'uiDecoration', 0)), 
           b'peripheryIDs': ({int(p) for p in onlyForPeripheriesList.split()} if onlyForPeripheriesList else set()), 
           b'runFlags': runFlags, 
           b'showPostBattleStat': (questSection.readBool(b'showPostBattleStat', False)), 
           b'saveBonusHistory': (questSection.readBool(b'saveBonusHistory', False))}
        if eventType == EVENT_TYPE.MOTIVE_QUEST:
            extraSubsectionsNames = (b'advice', b'requirements', b'congratulation')
            for subsectionName in extraSubsectionsNames:
                if questSection.has_key(subsectionName):
                    info[subsectionName] = self.__readMetaSection(questSection[subsectionName])

        if eventType == EVENT_TYPE.RANKED_QUEST:
            if finishTime > curTime + _YEAR:
                raise SoftException(b"'finishTime' section is missing or too far into the future", info[b'id'])
            seasonSectionName = b'conditions/common/season'
            if questSection.has_key(seasonSectionName):
                season = questSection[seasonSectionName].asInt
            else:
                raise SoftException(b"'season' condition is compulsory", info[b'id'])
            cycleSectionName = b'conditions/common/cycle'
            if questSection.has_key(cycleSectionName):
                cycle = questSection[cycleSectionName].asInt
            else:
                cycle = None
            info[b'subtype'] = questSection[b'subtype'].asString
            info[b'ranked'] = (
             season, cycle)
        if eventType in EVENT_TYPE.QUESTS_WITH_SHOP_BUTTON:
            info[b'shopButton'] = questSection.readString(b'shopButton', b'hide')
        if questSection.has_key(b'notificationText'):
            info[b'notificationText'] = self.__readMetaSection(questSection[b'notificationText'])
        if eventType == EVENT_TYPE.TOKEN_QUEST:
            info[b'delayed'] = questSection.readBool(b'delayed', False)
        return info

    def __readGroupContent(self, questSection):
        if not questSection.has_key(b'groupContent'):
            raise SoftException(b"'groupContent' section is compulsory")
        return questSection.readString(b'groupContent').split()

    def __getConditionReaders(self, eventType):
        condition_readers = {b'greater': (self.__readCondition_DateTimeOrFloat), 
           b'equal': (self.__readCondition_DateTimeOrFloat), 
           b'less': (self.__readCondition_DateTimeOrFloat), 
           b'lessOrEqual': (self.__readCondition_DateTimeOrFloat), 
           b'greaterOrEqual': (self.__readCondition_DateTimeOrFloat), 
           b'and': (self.__readBattleResultsConditionList), 
           b'or': (self.__readBattleResultsConditionList), 
           b'not': (self.__readBattleResultsConditionList), 
           b'token': (self.__readBattleResultsConditionList), 
           b'quest': (self.__readBattleResultsConditionList), 
           b'id': (self.__readCondition_string), 
           b'consume': (self.__readCondition_consume), 
           b'inClan': (self.__readListOfInts), 
           b'vehiclesUnlocked': (self.__readBattleResultsConditionList), 
           b'vehiclesLocked': (self.__readBattleResultsConditionList), 
           b'vehiclesOwned': (self.__readBattleResultsConditionList), 
           b'vehiclesUnlockedAndOwned': (self.__readBattleResultsConditionList), 
           b'classes': (self.__readVehicleFilter_classes), 
           b'levels': (self.__readVehicleFilter_levels), 
           b'nations': (self.__readVehicleFilter_nations), 
           b'types': (self.__readVehicleFilter_types), 
           b'roles': (self.__readVehicleFilter_roles), 
           b'excludeTags': (self.__readVehicleFilter_excludeTags), 
           b'dossier': (self.__readBattleResultsConditionList), 
           b'record': (self.__readCondition_dossierRecord), 
           b'average': (self.__readCondition_int), 
           b'GR': (self.__readBattleResultsConditionList), 
           b'igrType': (self.__readCondition_IGRType), 
           b'premium': (self.__readCondition_bool), 
           b'special': (self.__readCondition_bool), 
           b'premiumPlus': (self.__readCondition_bool), 
           b'premiumVip': (self.__readCondition_bool), 
           b'isPremiumQuestsEnabled': (self.__readCondition_bool), 
           b'premiumSubs': (self.__readCondition_bool), 
           b'premiumSubsDailyAttendance': (self.__readCondition_bool), 
           b'isPremiumSubsDQEnabled': (self.__readCondition_bool), 
           b'daily': (self.__readCondition_true), 
           b'weekly': (self.__readCondition_true), 
           b'bonusLimit': (self.__readCondition_int), 
           b'isTutorialCompleted': (self.__readCondition_bool), 
           b'isBattleMattersEnabled': (self.__readCondition_bool), 
           b'isTankAcademyEnabled': (self.__readCondition_bool), 
           b'activeProgression': (self.__readCondition_string), 
           b'isSteamAllowed': (self.__readCondition_bool), 
           b'totalBattles': (self.__readBattleResultsConditionList), 
           b'lastLogout': (self.__readBattleResultsConditionList), 
           b'relativeToUTC': (self.__readBattleResultsConditionList), 
           b'accountPrimaryTypes': (self.__readListOfInts), 
           b'accountSecondaryTypes': (self.__readListOfInts), 
           b'accountAttributes': (self.__readListAccountAttributes), 
           b'externalData': (self.__readBattleResultsConditionList), 
           b'externalDataItem': (self.__readBattleResultsConditionList), 
           b'source': (self.__readCondition_string), 
           b'paramName': (self.__readCondition_string), 
           b'mapsTraining': (self.__readBattleResultsConditionList), 
           b'mapsCompleted': (self.__readBattleResultsConditionList), 
           b'scenariosCompleted': (self.__readBattleResultsConditionList), 
           b'difficulty': (self.__readCondition_int)}
        if eventType in EVENT_TYPE.LIKE_BATTLE_QUESTS:
            condition_readers.update({b'value': (self.__readCondition_bool), 
               b'win': (self.__readConditionComplex_true), 
               b'isAlive': (self.__readConditionComplex_true), 
               b'isSquad': (self.__readCondition_bool), 
               b'clanMembership': (self.__readCondition_string), 
               b'unitSize': (self.__readCondition_int), 
               b'allAlive': (self.__readCondition_true), 
               b'aliveCnt': (self.__readCondition_int), 
               b'achievements': (self.__readCondition_achievements), 
               b'hasReceivedMultipliedXP': (self.__readCondition_bool), 
               b'multiDamageEvent': (self.__readBattleResultsConditionList), 
               b'killedByShot': (self.__readCondition_int), 
               b'damagedByShot': (self.__readCondition_int), 
               b'multiStunEvent': (self.__readBattleResultsConditionList), 
               b'stunnedByShot': (self.__readCondition_int), 
               b'unitVehicleDamage': (self.__readBattleResultsConditionList), 
               b'unitVehicleKills': (self.__readBattleResultsConditionList), 
               b'unitVehicleDescr': (self.__readBattleResultsConditionList), 
               b'vehicleDamage': (self.__readBattleResultsConditionList), 
               b'vehicleStun': (self.__readBattleResultsConditionList), 
               b'vehicleKills': (self.__readBattleResultsConditionList), 
               b'vehicleDescr': (self.__readBattleResultsConditionList), 
               b'clanKills': (self.__readBattleResultsConditionList), 
               b'lvlDiff': (self.__readCondition_int), 
               b'classesDiversity': (self.__readCondition_int), 
               b'limittedTime': (self.__readCondition_int), 
               b'rammingInfo': (self.__readCondition_rammingInfo), 
               b'distance': (self.__readCondition_int), 
               b'whileMoving': (self.__readCondition_true), 
               b'whileEnemyMoving': (self.__readCondition_int), 
               b'soloAssist': (self.__readCondition_true), 
               b'fireStarted': (self.__readCondition_true), 
               b'whileEnemyInvisible': (self.__readCondition_true), 
               b'whileInvisible': (self.__readCondition_true), 
               b'attackReason': (self.__readCondition_attackReason), 
               b'enemyImmobilized': (self.__readCondition_true), 
               b'enemyInvader': (self.__readCondition_true), 
               b'eventCount': (self.__readCondition_true), 
               b'whileFullHealth': (self.__readCondition_true), 
               b'whileEnemyFullHealth': (self.__readCondition_true), 
               b'allInSpecifiedClasses': (self.__readCondition_true), 
               b'enemyIsNotSpotted': (self.__readCondition_true), 
               b'installedModules': (self.__readBattleResultsConditionList), 
               b'installedNonDefaultModulesCount': (self.__readBattleResultsConditionList), 
               b'allCrewMembersHaveSelectedSkill': (self.__readCondition_true), 
               b'postProgressionLevel': (self.__readBattleResultsConditionList), 
               b'allAvailableShellTypesLoaded': (self.__readCondition_true), 
               b'guns': (self.__readCondition_installedModules), 
               b'engines': (self.__readCondition_installedModules), 
               b'chassis': (self.__readCondition_installedModules), 
               b'turrets': (self.__readCondition_installedModules), 
               b'radios': (self.__readCondition_installedModules), 
               b'optionalDevice': (self.__readCondition_installedModules), 
               b'optionalDeviceCount': (self.__readBattleResultsConditionList), 
               b'consumables': (self.__readBattleResultsConditionList), 
               b'equipment': (self.__readCondition_consumables), 
               b'equipmentCount': (self.__readBattleResultsConditionList), 
               b'goodies': (self.__readBattleResultsConditionList), 
               b'goodiesCount': (self.__readBattleResultsConditionList), 
               b'correspondedCamouflage': (self.__readConditionComplex_true), 
               b'correspondedDecal': (self.__readConditionComplex_true), 
               b'correspondedPaint': (self.__readConditionComplex_true), 
               b'correspondedStyle': (self.__readConditionComplex_true), 
               b'correspondedModification': (self.__readConditionComplex_true), 
               b'correspondedProjectionDecal': (self.__readConditionComplex_true), 
               b'correspondedPersonalNumber': (self.__readConditionComplex_true), 
               b'customization': (self.__readBattleResultsConditionList), 
               b'styleId': (self.__readCondition_int), 
               b'correspondedEquipment': (self.__readCondition_correspondedEquipment), 
               b'unit': (self.__readBattleResultsConditionList), 
               b'results': (self.__readBattleResultsConditionList), 
               b'key': (self.__readCondition_keyResults), 
               b'max': (self.__readCondition_int), 
               b'total': (self.__readCondition_false), 
               b'compareWithMaxHealth': (self.__readCondition_true), 
               b'plus': (self.__readBattleResultsConditionList), 
               b'exceptUs': (self.__readCondition_true), 
               b'compareWithDeathCount': (self.__readCondition_true), 
               b'mapCamouflageKind': (self.__readBattleFilter_CamouflageKind), 
               b'bonusTypes': (self.__readBattleFilter_BonusTypes), 
               b'geometryNames': (self.__readBattleFilter_GeometryNames), 
               b'battles': (self.__readBattleResultsConditionList), 
               b'count': (self.__readCondition_int), 
               b'upperLimit': (self.__readCondition_true), 
               b'unique': (self.__readBattleResultsConditionList), 
               b'uniqueBy': (self.__readCondition_groupBy), 
               b'inrow': (self.__readCondition_true), 
               b'groupBy': (self.__readBattleResultsConditionList), 
               b'groupName': (self.__readCondition_groupBy), 
               b'cumulative': (self.__readCondition_cumulative), 
               b'cumulativeExt': (self.__readBattleResultsConditionList), 
               b'cumulativeSum': (self.__readCondition_cumulativeSum), 
               b'crits': (self.__readBattleResultsConditionList), 
               b'destroyed': (self.__readBattleResultsConditionList), 
               b'tankman': (self.__readBattleResultsConditionList), 
               b'critical': (self.__readBattleResultsConditionList), 
               b'crit': (self.__readBattleResultsConditionList), 
               b'critName': (self.__readCritName), 
               b'unregularAmmo': (self.__readCondition_true), 
               b'isNotLeaver': (self.__readCondition_true), 
               b'isFirstBlood': (self.__readConditionComplex_true), 
               b'winAloneAgainstVehicleCount': (self.__readCondition_int), 
               b'enemyClans': (self.__readBattleResultsConditionList)})
        if eventType in (EVENT_TYPE.BATTLE_QUEST, EVENT_TYPE.PERSONAL_QUEST):
            condition_readers.update({b'red': (self.__readListOfInts), 
               b'silver': (self.__readListOfInts), 
               b'gold': (self.__readListOfInts), 
               b'black': (self.__readListOfInts), 
               b'clanDBIDs': (self.__readListOfInts)})
        if eventType in (EVENT_TYPE.RANKED_QUEST,):
            condition_readers.update({b'season': (self.__readCondition_int), 
               b'cycle': (self.__readCondition_int), 
               b'rank': (self.__readBattleResultsConditionList), 
               b'step': (self.__readCondition_int), 
               b'maxRank': (self.__readBattleResultsConditionList), 
               b'ladderPts': (self.__readBattleResultsConditionList)})
        if eventType in (EVENT_TYPE.HANGAR_QUEST,):
            condition_readers.update({b'moduleBuySell': (self.__readBattleResultsConditionList)})
        return condition_readers

    def __getAvailableBonuses(self, eventType):
        bonusTypes = {
         1, 2, 3, 4, 5, 6, 7, 8, 9, 
         10, 
         11, 12, 13, 14, 15, 16, 17, 
         18, 19, 
         20, 21, 22, 23, 
         24, 25, 26, 27, 28, 
         29, 
         30, 31, 32, 33, 34, 
         35, 
         36, 37} | EXTENSIONS_BONUSES.get(ALL_EVENT_TYPES_FOR_BONUSES, set())
        if eventType in (EVENT_TYPE.BATTLE_QUEST, EVENT_TYPE.PERSONAL_QUEST, EVENT_TYPE.NT_QUEST):
            bonusTypes.update((b'xp', b'tankmenXP', b'xpFactor', b'creditsFactor', b'freeXPFactor', b'tankmenXPFactor'))
        if eventType in (EVENT_TYPE.NT_QUEST,):
            bonusTypes.update((b'vehicleXP', b'vehicleXPFactor'))
        if eventType in (EVENT_TYPE.RANKED_QUEST,):
            bonusTypes.update((b'optionalDevice',))
        bonusTypes |= EXTENSIONS_BONUSES.get(eventType, set())
        return bonusTypes

    def __readCondition_groupBy(self, _, section, node):
        s = section.asString
        if s not in (b'vehicle', b'nation', b'class', b'level'):
            raise SoftException(b'Unknown groupBy name %s' % s)
        node.addChild(s)
        return

    def __readCondition_installedModules(self, _, section, node):
        modules = set()
        for module in section.asString.split():
            if b':' in module:
                nationName, name = module.split(b':')
                nationID = nations.INDICES[nationName]
            elif node.name != b'optionalDevice':
                raise SoftException(b'module must be like nation:inNationName')
            name = module
            if node.name == b'guns':
                nationModules = vehicles.g_cache.guns(nationID)
            elif node.name == b'engines':
                nationModules = vehicles.g_cache.engines(nationID)
            elif node.name == b'turrets':
                nationModules = vehicles.g_cache.turrets(nationID)
            elif node.name == b'chassis':
                nationModules = vehicles.g_cache.chassis(nationID)
            elif node.name == b'radios':
                nationModules = vehicles.g_cache.radios(nationID)
            elif node.name == b'optionalDevice':
                idx = vehicles.g_cache.optionalDeviceIDs()[name]
                modules.add(vehicles.g_cache.optionalDevices()[idx].compactDescr)
                break
            else:
                raise SoftException(b'Unknown tag %s' % node.name)
            for descr in nationModules.itervalues():
                if descr.name == name:
                    modules.add(descr.compactDescr)
                    break
            else:
                raise SoftException(b'Unknown module(%s) %s' % (node.name, module))

        node.addChild(modules)
        return

    def __readCondition_consumables(self, _, section, node):
        modules = set()
        name = section.asString
        if node.name == b'equipment':
            idx = vehicles.g_cache.equipmentIDs()[name]
            modules.add(vehicles.g_cache.equipments()[idx].compactDescr)
        else:
            raise SoftException(b'Unknown consumables(%s)' % node.name)
        node.addChild(modules)
        return

    def __readCondition_correspondedEquipment(self, _, section, node):
        equipment = set()
        for name, sub in section.items():
            if name in (b'title', b'description'):
                node.questClientConditions.append((name, self.__readMetaSection(sub)))
                continue
            if name in (b'hideInGui',):
                node.questClientConditions.append((name, True))
                continue
            if name in (b'tags',):
                tags = set(sub.readString(b'', b'').split())
                if not tags:
                    raise SoftException(b'Empty tags for corresponded equipment is not allowed')
                equipment = {equipment.compactDescr for idx, equipment in vehicles.g_cache.equipments().iteritems() if tags == tags & equipment.tags}
                if not equipment:
                    raise SoftException((b'No corresponded equipments for tags {}').format(tags))
                continue
            if name in (b'ignoreBoostersCompatibility',):
                currentNode = XMLNode(name)
                currentNode.addChild(True)
                node.addChild(currentNode)

        equipmentNode = XMLNode(b'equipment')
        equipmentNode.addChild(equipment)
        node.addChild(equipmentNode)
        return

    def __readCritName(self, _, section, node):
        critName = section.asString
        if critName not in vehicles.VEHICLE_DEVICE_TYPE_NAMES + vehicles.VEHICLE_TANKMAN_TYPE_NAMES:
            raise SoftException(b'Invalid crit name (%s)' % critName)
        node.addChild(critName)
        return

    def __readCondition_cumulative(self, _, section, node):
        description = None
        for name, sub in section.items():
            if name == b'description':
                description = sub
                break

        for name, sub in section.items():
            results = XMLNode(b'results')
            if name in (b'meta', b'title', b'description'):
                continue
            if name not in getBattleResultsNames():
                raise SoftException(b"Unsupported misc variable '%s'" % name)
            key = XMLNode(b'key')
            key.addChild(name)
            relation = XMLNode(b'greaterOrEqual')
            relation.relatedGroup = intern(b'operator')
            relation.addChild(sub.asFloat)
            if description is not None:
                results.questClientConditions.append((b'description', self.__readMetaSection(description)))
            results.addChild(key)
            results.addChild(relation)
            node.addChild(results)

        return

    def __readCondition_cumulativeSum(self, conditionReaders, section, node):
        for name, sub in section.items():
            if name == b'description':
                node.questClientConditions.append((b'description', self.__readMetaSection(sub)))
                break

        for name, sub in section.items():
            if name in (b'meta', b'title', b'description'):
                continue
            subNode = XMLNode(name)
            if name == b'sum':
                for _name, _sub in sub.items():
                    if _name not in getBattleResultsNames():
                        raise SoftException(b"Unsupported misc variable '%s'" % _name)
                    subNode.addChild(_name)

            if name in (b'greater', b'equal', b'less', b'lessOrEqual', b'greaterOrEqual'):
                conditionReaders[name](conditionReaders, sub, subNode)
            node.addChild(subNode)

        return

    def __readBattleResultsConditionList(self, conditionReaders, section, node):
        for name, sub in section.items():
            if name in (b'meta', b'title', b'description'):
                node.questClientConditions.append((name, self.__readMetaSection(sub)))
                continue
            if name in (b'hideInGui',):
                node.questClientConditions.append((name, True))
                continue
            if name in (b'progressID',):
                node.questClientConditions.append((name, sub.readString(b'', b'')))
                continue
            subNode = XMLNode(name)
            if name in (b'greater', b'equal', b'less', b'lessOrEqual', b'greaterOrEqual'):
                subNode.relatedGroup = intern(b'operator')
            conditionReaders[name](conditionReaders, sub, subNode)
            node.addChild(subNode)

        return

    def __readConditionComplex_true(self, conditionReaders, section, node):
        for name, sub in section.items():
            if name in (b'title', b'description'):
                node.questClientConditions.append((name, self.__readMetaSection(sub)))
                continue
            if name in (b'hideInGui',):
                node.questClientConditions.append((name, True))
                continue
            if name in (b'progressID',):
                node.questClientConditions.append((name, sub.readString(b'', b'')))
                continue
            node.addChild(True)

        return

    def __readCondition_achievements(self, _, section, node):
        dossierRecordDBIDs = set()
        for achievement in section.asString.split():
            values = achievement.split(b':')
            if len(values) == 2:
                dossierRecordDBIDs.add(RECORD_DB_IDS[values[0], values[1]])
            else:
                raise SoftException(b'Invalid achievement format (%s). Must be blockName:record.' % achievement)

        node.addChild(dossierRecordDBIDs)
        return

    def __readCondition_string(self, _, section, node):
        node.addChild(section.asString)
        return

    def __readCondition_rammingInfo(self, _, section, node):
        rammingConditions = set([rammingCondition for rammingCondition in section.asString.split()])
        for rammingCondition in rammingConditions:
            if rammingCondition not in (b'stayedAlive', b'dealtMoreDamage'):
                raise SoftException(b'Unsupported kill by ramming condition %s, must be one of (%s %s)' % (
                 rammingCondition, b'stayedAlive', b'dealtMoreDamage'))

        node.addChild(rammingConditions)
        return

    def __readCondition_dossierRecord(self, _, section, node):
        record = section.asString
        records = record.split(b':')
        if len(records) == 2:
            blockName, rec = records
            for blockBuilder in accountDossierLayout + vehicleDossierLayout:
                if type(blockBuilder) not in (StaticSizeBlockBuilder, BinarySetDossierBlockBuilder):
                    continue
                if blockBuilder.name == blockName:
                    if rec in blockBuilder.recordsLayout or rec.startswith(b'tankExpert') or rec.startswith(b'mechanicEngineer') or rec.startswith(b'collectorVehicle'):
                        break
            else:
                raise SoftException(b'Invalid dossier record %s' % (record,))

        else:
            raise SoftException(b'Old or invalid dossier record format (%s)' % (record,))
        node.addChild(record)
        return

    def __readCondition_keyResults(self, _, section, node):
        name = section.asString
        if name not in getBattleResultsNames():
            raise SoftException(b"Unsupported battle result variable '%s'" % name)
        node.addChild(name)
        return

    def __readCondition_true(self, _, section, node):
        node.addChild(True)
        return

    def __readCondition_false(self, _, section, node):
        node.addChild(False)
        return

    def __readCondition_bool(self, _, section, node):
        node.addChild(section.asBool)
        return

    def __readCondition_int(self, _, section, node):
        node.addChild(section.asInt)
        return

    def __readCondition_float(self, _, section, node):
        node.addChild(section.asFloat)
        return

    def __readCondition_DateTimeOrFloat(self, _, section, node):
        try:
            value = timeDataToUTC(section.asString, None)
        except SoftException as e:
            try:
                value = section.asFloat
            except ValueError:
                raise e

        node.addChild(value)
        return

    def __readCondition_consume(self, _, section, node):
        node.addChild(section.asInt)
        node.addChild(section.has_key(b'force'))
        return

    def __readCondition_attackReason(self, _, section, node):
        attackReason = section.asInt
        if not 0 <= attackReason < len(ATTACK_REASONS):
            raise SoftException(b'Invalid attack reason index')
        node.addChild(section.asInt)
        return

    def __readCondition_set(self, _, section, node):
        node.addChild(set([int(id) for id in section.asString.split()]))
        return

    def __readCondition_IGRType(self, _, section, node):
        igrType = section.asInt
        if igrType not in IGR_TYPE.RANGE:
            raise SoftException(b'Invalid IGR type %s' % (igrType,))
        node.addChild(igrType)
        return

    def __readBattleFilter_GeometryNames(self, _, section, node):
        arenaIDs = []
        for geometryName in section.asString.split():
            initialLen = len(arenaIDs)
            for id, descr in ArenaType.g_cache.iteritems():
                if descr.geometryName == geometryName:
                    arenaIDs.append(id)

            if initialLen == len(arenaIDs):
                raise SoftException(b'Unknown geometry name %s' % geometryName)

        node.addChild(set(arenaIDs))
        return

    def __readBattleFilter_BonusTypes(self, _, section, node):
        res = []
        for bonusType in section.asString.split():
            bonusType = int(bonusType)
            if bonusType not in ARENA_BONUS_TYPE.RANGE:
                raise SoftException(b'Unknown bonus type %s' % bonusType)
            res.append(bonusType)

        if len(set(res)) != len(res):
            raise SoftException(b'Duplicate bonus types %s' % res)
        node.addChild(res)
        return

    def __readBattleFilter_CamouflageKind(self, _, section, node):
        camouflageKindLst = set([vehicles.CAMOUFLAGE_KINDS[c] for c in section.asString.split()])
        node.addChild(camouflageKindLst)
        return

    def __readVehicleFilter_classes(self, _, section, node):
        classes = set([VEHICLE_CLASS_INDICES[cls] for cls in section.asString.split()])
        node.addChild(classes)
        return

    def __readVehicleFilter_levels(self, _, section, node):
        res = set()
        for level in section.asString.split():
            if MIN_VEHICLE_LEVEL <= int(level) <= MAX_VEHICLE_LEVEL:
                res.add(int(level))
            else:
                raise SoftException(b'Unsupported vehicle level %s' % level)

        node.addChild(res)
        return

    def __readListOfInts(self, _, section, node):
        node.addChild(set([int(val) for val in section.asString.split()]))
        return

    def __readVehicleFilter_nations(self, _, section, node):
        nationsLst = set([nations.INDICES[nation] for nation in section.asString.split()])
        node.addChild(nationsLst)
        return

    def __readVehicleFilter_types(self, _, section, node):
        node.addChild(set(self.__readVehicleTypeList(section)))
        return

    def __readVehicleTypeList(self, section):
        typeNames = section.asString.split()
        return [vehicles.makeVehicleTypeCompDescrByName(typeName) for typeName in typeNames]

    def __readVehicleFilter_roles(self, _, section, node):
        roles = set([ROLE_LABEL_TO_TYPE[role] for role in section.asString.split()])
        node.addChild(roles)
        return

    def __readVehicleFilter_excludeTags(self, _, section, node):
        tags = set(section.asString.split())
        diff = tags.difference(QUESTS_SUPPORTED_EXCLUDE_TAGS)
        if diff:
            raise SoftException(b'Unsupported vehicle exclude tags %s' % diff)
        node.addChild(tags)
        return

    def __readListAccountAttributes(self, _, section, node):
        attrs = 0
        for attr in section.asString.split():
            val = getattr(ACCOUNT_ATTR, attr, None)
            if val is None:
                raise SoftException((b'Unknown attribute name: {}').format(attr))
            attrs += val

        node.addChild(attrs)
        return

    def __readMetaSection(self, section):
        if section is None:
            return {}
        else:
            meta = {}
            for local, sub in section.items():
                meta[local.strip()] = sub.readString(b'', b'').strip()

            return meta


def collectSections(root):
    sections = []
    pmQuestSection = ResMgr.openSection(root)
    if pmQuestSection is not None:
        for k, s in pmQuestSection.items():
            sectionPath = root + b'/' + k
            if k.endswith(b'.xml'):
                sections.append(sectionPath)
            elif s is not None:
                sections.extend(collectSections(sectionPath))

    return sections
