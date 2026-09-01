from constants import DEATH_REASON_ALIVE
from epic_constants import EPIC_BATTLE_TEAM_ID
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.settings import ICONS_SIZES
from gui.battle_results.components import base, shared, style, ranked
from gui.battle_results.components.base import PropertyValue
from gui.battle_results.components.personal import fillKillerInfoBlock, NO_OWNER_DEATH_REASON_IDS
from gui.battle_results.reusable import sort_keys
from gui.battle_results.reusable.avatars import AvatarInfo
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.gui_items.Vehicle import getSmallIconPath, getIconPath
from helpers import dependency, i18n
from messenger.m_constants import USER_TAG
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext
_STAT_VALUES_VO_REPLACER = {b'damageAssisted': b'damageAssistedSelf', 
   b'damageAssistedStun': b'damageAssistedStunSelf'}
_STAT_STUN_FIELD_NAMES = (b'damageAssistedStun', b'stunNum', b'stunDuration')

def _getStunFilter():
    lobbyContext = dependency.instance(ILobbyContext)
    filters = ()
    if not lobbyContext.getServerSettings().spgRedesignFeatures.isStunEnabled():
        filters += _STAT_STUN_FIELD_NAMES
    return filters


class TeamPlayerNameBlock(shared.PlayerNameBlock):
    __slots__ = (b'igrType',)

    def setPlayerInfo(self, playerInfo):
        super(TeamPlayerNameBlock, self).setPlayerInfo(playerInfo)
        self.igrType = playerInfo.igrType
        return

    def setRecord(self, result, reusable):
        self.setPlayerInfo(result)
        return


class RegularVehicleStatsBlock(base.StatsBlock):
    __slots__ = (b'_isObserver', b'achievements', b'achievementsCount', b'vehicleState', b'vehicleStatePrefix', b'vehicleStateSuffix', b'killerID', b'deathReason', b'isPrematureLeave', b'vehicleName', b'vehicleShortName', b'vehicleIcon', b'vehicleSort', b'isPersonal', b'isTeamKiller', b'kills', b'tkills', b'realKills', b'xp', b'damageDealt', b'vehicles', b'playerID', b'player', b'statValues', b'fortResource', b'squadIndex', b'isPersonalSquad', b'xpSort', b'intCD', b'rank', b'rankIcon', b'suffixBadgeIcon', b'isKilledByTeamKiller', b'playerRank', b'respawns', b'badge', b'hasSelectedBadge', b'suffixBadgeStripIcon')

    def __init__(self, meta=None, field=b'', *path):
        super(RegularVehicleStatsBlock, self).__init__(meta, field, *path)
        self._isObserver = False
        self.isPersonal = None
        self.isPersonalSquad = None
        self.isTeamKiller = False
        self.isKilledByTeamKiller = False
        self.vehicleSort = None
        self.suffixBadgeIcon = None
        self.suffixBadgeStripIcon = None
        self.hasSelectedBadge = False
        return

    def setRecord(self, result, reusable):
        player = result.player
        avatar = reusable.avatars.getAvatarInfo(player.dbID)
        noPenalties = not avatar.hasPenalties()
        self.suffixBadgeIcon = None
        self.suffixBadgeStripIcon = None
        if avatar is not None:
            self.hasSelectedBadge = avatar.badge > 0
            if self.hasSelectedBadge:
                self._setBadge(result, reusable)
            if avatar.suffixBadge:
                self.suffixBadgeIcon = style.makeBadgeIcon(avatar.suffixBadge)
                stripImg = R.images.gui.maps.icons.library.badges.strips.c_64x24.dyn((b'strip_{}').format(avatar.suffixBadge))
                self.suffixBadgeStripIcon = backport.image(stripImg()) if stripImg else b''
        self._processVehicles(result)
        self._setPlayerInfo(player)
        self._setTotalStats(result, noPenalties)
        self._setVehiclesStats(result, reusable)
        if not self.isPersonal or noPenalties:
            self._setAchievements(result, reusable)
        if not self._isObserver:
            self._setVehicleState(result, reusable)
        return

    def _setBadge(self, result, reusable):
        self.badge = PropertyValue(result, reusable)
        return

    def _processVehicles(self, result):
        self._setVehicleInfo(result.vehicle)
        return

    def _setVehicleInfo(self, vehicle):
        if vehicle is not None:
            self._isObserver = vehicle.isObserver
            self.intCD = vehicle.intCD
            self.vehicleName = vehicle.userName
            self.vehicleShortName = vehicle.shortUserName
            self.vehicleIcon = getSmallIconPath(vehicle.name)
            self.vehicles = [{b'icon': (getIconPath(vehicle.name))}]
        return

    def _setPlayerInfo(self, player):
        self.playerID = player.dbID
        self.player = player
        self.squadIndex = player.squadIndex
        return

    def _setTotalStats(self, result, noPenalties):
        self.kills = kills = result.kills
        self.tkills = teamKills = result.tkills
        self.realKills = kills - teamKills
        self.damageDealt = result.damageDealt
        if noPenalties:
            self.xp = result.xp
            self.xpSort = result.xp
        else:
            self.xp = 0
            self.xpSort = 0
        return

    def _setVehiclesStats(self, result, reusable):
        self.statValues = (
         (
          self.isPersonal, result.getVehiclesIterator()), reusable)
        return

    def _setAchievements(self, result, reusable):
        achievements = result.getAchievements()
        self.achievementsCount = len(achievements)
        self.achievements = PropertyValue(achievements, reusable)
        return

    def _setVehicleState(self, result, reusable):
        if self._isObserver:
            return
        self.killerID = result.killerID
        self.deathReason = result.deathReason
        if self.isPersonal and reusable.personal.avatar.isPrematureLeave:
            state = backport.text(R.strings.battle_results.common.vehicleState.prematureLeave())
            self.vehicleState = state
            self.vehicleStatePrefix = state
        elif self.deathReason > DEATH_REASON_ALIVE:
            if self.killerID:
                fillKillerInfoBlock(self, self.deathReason, self.killerID, reusable, result)
            elif self.deathReason in NO_OWNER_DEATH_REASON_IDS:
                state = backport.text(R.strings.battle_results.common.vehicleState.dyn((b'dead{}').format(self.deathReason), R.invalid)())
                self.vehicleState = state
        else:
            self.vehicleState = backport.text(R.strings.battle_results.common.vehicleState.alive())
        self.isTeamKiller = result.isTeamKiller
        return


class EpicVehicleStatsBlock(RegularVehicleStatsBlock):
    __slots__ = (b'__allAdded',)

    def __init__(self, meta=None, field=b'', *path):
        super(EpicVehicleStatsBlock, self).__init__(meta, field, *path)
        self.vehicles = []
        self.__allAdded = False
        return

    def _processVehicles(self, result):
        for vehicleInfo in result.vehicles:
            self._setVehicleInfo(vehicleInfo.vehicle)

        return

    def _setVehicleInfo(self, vehicle):
        self.vehicles.append({b'icon': (getIconPath(vehicle.name)), b'label': (vehicle.shortUserName)})
        return

    def setRecord(self, result, reusable):
        super(EpicVehicleStatsBlock, self).setRecord(result, reusable)
        self.playerRank = 0
        avatar = reusable.avatars.getAvatarInfo(result.player.dbID)
        extensionInfo = avatar.extensionInfo
        if extensionInfo is not None and b'playerRank' in extensionInfo:
            self.playerRank = extensionInfo[b'playerRank']
        self.respawns = result.respawns
        return

    def getVO(self):
        if len(self.vehicles) > 1 and not self.__allAdded:
            self.vehicles.insert(0, {b'label': (i18n.makeString(BATTLE_RESULTS.ALLVEHICLES)), b'icon': (RES_ICONS.MAPS_ICONS_LIBRARY_EPICVEHICLESALL)})
            self.__allAdded = True
        return super(EpicVehicleStatsBlock, self).getVO()


class StrongholdVehicleStatsBlock(RegularVehicleStatsBlock):
    pass


class RegularVehicleStatValuesBlock(base.StatsBlock):
    __slots__ = (b'_isPersonal', b'_filters', b'shots', b'hits', b'explosionHits', b'damageDealt', b'sniperDamageDealt', b'directHitsReceived', b'piercingsReceived', b'noDamageDirectHitsReceived', b'explosionHitsReceived', b'damageBlockedByArmor', b'teamHitsDamage', b'spotted', b'damagedKilled', b'damageAssisted', b'damageAssistedStun', b'stunNum', b'stunDuration', b'capturePoints', b'mileage', b'__rawDamageAssistedStun', b'__rawStunNum')
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, meta=None, field=b'', *path):
        super(RegularVehicleStatValuesBlock, self).__init__(meta, field, *path)
        self._filters = set()
        return

    def setPersonal(self, flag):
        self._isPersonal = flag
        return

    def addFilters(self, filters):
        self._filters.update(filters)
        return

    def setRecord(self, result, reusable):
        self.__rawDamageAssistedStun = result.damageAssistedStun
        self.__rawStunNum = result.stunNum
        if self.__rawStunNum == 0:
            self.addFilters(_STAT_STUN_FIELD_NAMES)
        self.shots = style.getIntegralFormatIfNoEmpty(result.shots)
        self.hits = (result.directEnemyHits, result.piercingEnemyHits)
        self.explosionHits = style.getIntegralFormatIfNoEmpty(result.explosionHits)
        self.damageDealt = style.getIntegralFormatIfNoEmpty(result.damageDealt)
        self.sniperDamageDealt = style.getIntegralFormatIfNoEmpty(result.sniperDamageDealt)
        self.directHitsReceived = style.getIntegralFormatIfNoEmpty(result.directHitsReceived)
        self.piercingsReceived = style.getIntegralFormatIfNoEmpty(result.piercingsReceived)
        self.noDamageDirectHitsReceived = style.getIntegralFormatIfNoEmpty(result.noDamageDirectHitsReceived)
        self.explosionHitsReceived = style.getIntegralFormatIfNoEmpty(result.explosionHitsReceived)
        self.damageBlockedByArmor = style.getIntegralFormatIfNoEmpty(result.damageBlockedByArmor)
        self.teamHitsDamage = (result.tkills, result.tdamageDealt)
        self.spotted = style.getIntegralFormatIfNoEmpty(result.spotted)
        self.damagedKilled = (result.damaged, result.kills)
        self.damageAssisted = style.getIntegralFormatIfNoEmpty(result.damageAssisted)
        self.damageAssistedStun = style.getIntegralFormatIfNoEmpty(result.damageAssistedStun)
        self.stunNum = style.getIntegralFormatIfNoEmpty(result.stunNum)
        self.stunDuration = style.getFractionalFormatIfNoEmpty(result.stunDuration)
        self.capturePoints = (result.capturePoints, result.droppedCapturePoints)
        self.mileage = result.mileage
        return

    def getVO(self):
        vo = []
        for component in self._components:
            field = component.getField()
            if field in list(self._filters):
                continue
            value = component.getVO()
            if self._isPersonal and field in _STAT_VALUES_VO_REPLACER:
                field = _STAT_VALUES_VO_REPLACER[field]
            vo.append(style.makeStatValue(field, value))

        return vo


class RankedVehicleStatValuesBlock(RegularVehicleStatValuesBlock):
    __slots__ = (b'xp', b'xpForAttack', b'xpForAssist', b'xpOther')

    def setRecord(self, result, reusable):
        super(RankedVehicleStatValuesBlock, self).setRecord(result, reusable)
        self.xp = result.xp - result.xpPenalty
        self.xpForAttack = result.xpForAttack - result.xpPenalty
        self.xpForAssist = result.xpForAssist
        self.xpOther = result.xpOther
        return


class StrongholdVehicleStatValuesBlock(RegularVehicleStatValuesBlock):
    __slots__ = (b'artilleryFortEquipDamageDealt',)

    def setRecord(self, result, reusable):
        super(StrongholdVehicleStatValuesBlock, self).setRecord(result, reusable)
        self.artilleryFortEquipDamageDealt = style.getIntegralFormatIfNoEmpty(result.artilleryFortEquipDamageDealt)
        if result.artilleryFortEquipDamageDealt == 0:
            self.addFilters((b'artilleryFortEquipDamageDealt',))
        return


class EpicVehicleStatValuesBlock(base.StatsBlock):
    __slots__ = (b'_team', b'_isPersonal', b'_filters', b'shots', b'directHits', b'piercingHits', b'explosionHits', b'damageDealt', b'sniperDamageDealt', b'destructiblesDamageDealt', b'equipmentDamageDealt', b'directHitsReceived', b'piercingsReceived', b'noDamageDirectHitsReceived', b'explosionHitsReceived', b'damageBlockedByArmor', b'teamHitsDamage', b'spotted', b'damagedKilled', b'damageAssisted', b'equipmentDamageAssisted', b'damageAssistedStun', b'stunNum', b'capturePoints', b'timesDestroyed', b'teamSpecificStat', b'__rawDamageAssistedStun', b'__rawStunNum')

    def __init__(self, meta=None, field=b'', *path):
        super(EpicVehicleStatValuesBlock, self).__init__(meta, field, *path)
        self._filters = set()
        return

    def setPersonal(self, flag):
        self._isPersonal = flag
        return

    def addFilters(self, filters):
        self._filters.update(filters)
        return

    def setRecord(self, result, reusable):
        self.timesDestroyed = str(result.deathCount)
        self._team = result.player.team
        if self._team == EPIC_BATTLE_TEAM_ID.TEAM_ATTACKER:
            self.teamSpecificStat = (b'{0}/{1}').format(result.numCaptured, result.numDestroyed)
        else:
            numDestructiblesDefended = reusable.common.numDefended
            self.teamSpecificStat = (b'{0}/{1}').format(result.numDefended, numDestructiblesDefended)
        self.__rawDamageAssistedStun = result.damageAssistedStun
        self.__rawStunNum = result.stunNum
        if self.__rawStunNum == 0:
            self.addFilters(_STAT_STUN_FIELD_NAMES)
        self.shots = style.getIntegralFormatIfNoEmpty(result.shots)
        self.directHits = style.getIntegralFormatIfNoEmpty(result.directEnemyHits)
        self.piercingHits = style.getIntegralFormatIfNoEmpty(result.piercingEnemyHits)
        self.explosionHits = style.getIntegralFormatIfNoEmpty(result.explosionHits)
        self.damageDealt = style.getIntegralFormatIfNoEmpty(result.damageDealt)
        self.sniperDamageDealt = style.getIntegralFormatIfNoEmpty(result.sniperDamageDealt)
        self.destructiblesDamageDealt = style.getIntegralFormatIfNoEmpty(result.destructiblesDamageDealt)
        self.equipmentDamageDealt = style.getIntegralFormatIfNoEmpty(result.equipmentDamageDealt)
        self.directHitsReceived = style.getIntegralFormatIfNoEmpty(result.directHitsReceived)
        self.piercingsReceived = style.getIntegralFormatIfNoEmpty(result.piercingsReceived)
        self.noDamageDirectHitsReceived = style.getIntegralFormatIfNoEmpty(result.noDamageDirectHitsReceived)
        self.explosionHitsReceived = style.getIntegralFormatIfNoEmpty(result.explosionHitsReceived)
        self.damageBlockedByArmor = style.getIntegralFormatIfNoEmpty(result.damageBlockedByArmor)
        self.teamHitsDamage = (result.tkills, result.tdamageDealt)
        self.spotted = style.getIntegralFormatIfNoEmpty(result.spotted)
        self.damagedKilled = (result.damaged, result.kills)
        self.damageAssisted = style.getIntegralFormatIfNoEmpty(result.damageAssisted)
        self.equipmentDamageAssisted = style.getIntegralFormatIfNoEmpty(result.equipmentDamageAssisted)
        self.damageAssistedStun = style.getIntegralFormatIfNoEmpty(result.damageAssistedStun)
        self.stunNum = style.getIntegralFormatIfNoEmpty(result.stunNum)
        self.capturePoints = (result.capturePoints, result.droppedCapturePoints)
        return

    def getVO(self):
        vo = []
        _TEAM_SPECIFIC_STAT_REPLACE = {(EPIC_BATTLE_TEAM_ID.TEAM_ATTACKER): b'atkObjectives', (EPIC_BATTLE_TEAM_ID.TEAM_DEFENDER): b'defObjectives'}
        for component in self._components:
            field = component.getField()
            if field in self._filters:
                continue
            if field == b'teamSpecificStat':
                field = _TEAM_SPECIFIC_STAT_REPLACE[self._team]
            value = component.getVO()
            if self._isPersonal and field in _STAT_VALUES_VO_REPLACER:
                field = _STAT_VALUES_VO_REPLACER[field]
            vo.append(style.makeStatValue(field, value))

        return vo


class AllRegularVehicleStatValuesBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        isPersonal, iterator = result
        add = self.addNextComponent
        stunFilter = _getStunFilter()
        for vehicle in iterator:
            block = RegularVehicleStatValuesBlock()
            block.setPersonal(isPersonal)
            block.addFilters(stunFilter)
            block.setRecord(vehicle, reusable)
            add(block)

        return


class AllEpicVehicleStatValuesBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        isPersonal, iterator = result
        add = self.addNextComponent
        stunFilter = _getStunFilter()
        for vehicle in iterator:
            block = EpicVehicleStatValuesBlock()
            block.setPersonal(isPersonal)
            block.addFilters(stunFilter)
            block.setRecord(vehicle, reusable)
            add(block)

        return


class AllStrongholdVehicleStatValuesBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        isPersonal, iterator = result
        add = self.addNextComponent
        stunFilter = _getStunFilter()
        for vehicle in iterator:
            block = StrongholdVehicleStatValuesBlock()
            block.setPersonal(isPersonal)
            block.addFilters(stunFilter)
            block.setRecord(vehicle, reusable)
            add(block)

        return


class PersonalVehiclesRegularStatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        info = reusable.getPersonalVehiclesInfo(result)
        add = self.addNextComponent
        stunFilter = _getStunFilter()
        for data in info.getVehiclesIterator():
            block = RegularVehicleStatValuesBlock()
            block.setPersonal(True)
            block.addFilters(stunFilter)
            block.setRecord(data, reusable)
            add(block)

        return


class PersonalVehiclesRankedStatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        info = reusable.getPersonalVehiclesInfo(result)
        add = self.addNextComponent
        stunFilter = _getStunFilter()
        for data in info.getVehiclesIterator():
            block = RankedVehicleStatValuesBlock()
            block.setPersonal(True)
            block.addFilters(stunFilter)
            block.setRecord(data, reusable)
            add(block)

        return


class PersonalVehiclesEpicStatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        info = reusable.getPersonalVehiclesInfo(result)
        add = self.addNextComponent
        stunFilter = _getStunFilter()
        for data in info.getVehiclesIterator():
            block = EpicVehicleStatValuesBlock()
            block.setPersonal(True)
            block.addFilters(stunFilter)
            block.setRecord(data, reusable)
            add(block)

        return


class PersonalVehiclesStrongholdStatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        info = reusable.getPersonalVehiclesInfo(result)
        add = self.addNextComponent
        stunFilter = _getStunFilter()
        for data in info.getVehiclesIterator():
            block = StrongholdVehicleStatValuesBlock()
            block.setPersonal(True)
            block.addFilters(stunFilter)
            block.setRecord(data, reusable)
            add(block)

        return


class TeamStatsBlock(base.StatsBlock):
    __slots__ = (b'__class',)

    def __init__(self, class_, meta=None, field=b'', *path):
        super(TeamStatsBlock, self).__init__(meta, field, *path)
        self.__class = class_
        return

    def setRecord(self, result, reusable):
        personalInfo = reusable.getPlayerInfo()
        personalDBID = personalInfo.dbID
        if personalInfo.squadIndex:
            personalPrebattleID = personalInfo.prebattleID
        else:
            personalPrebattleID = 0
        for idx, item in enumerate(result):
            if item.vehicle is not None and item.vehicle.isObserver:
                continue
            player = item.player
            isPersonal = player.dbID == personalDBID
            if isPersonal:
                player.addTag(USER_TAG.CURRENT)
            block = self.__class()
            block.vehicleSort = idx
            block.isPersonal = isPersonal
            block.isPersonalSquad = personalPrebattleID != 0 and personalPrebattleID == player.prebattleID
            block.setRecord(item, reusable)
            self.addComponent(self.getNextComponentIndex(), block)

        return


class RegularTeamStatsBlock(TeamStatsBlock):
    __slots__ = ()

    def __init__(self, meta=None, field=b'', *path):
        super(RegularTeamStatsBlock, self).__init__(RegularVehicleStatsBlock, meta, field, *path)
        return


class EpicTeamStatsBlock(TeamStatsBlock):
    __slots__ = ()

    def __init__(self, meta=None, field=b'', *path):
        super(EpicTeamStatsBlock, self).__init__(EpicVehicleStatsBlock, meta, field, *path)
        return


class StrongholdTeamStatsBlock(TeamStatsBlock):
    __slots__ = ()

    def __init__(self, meta=None, field=b'', *path):
        super(StrongholdTeamStatsBlock, self).__init__(StrongholdVehicleStatsBlock, meta, field, *path)
        return


class TwoTeamsStatsBlock(shared.BiDiStatsBlock):
    __slots__ = ()

    def addComponent(self, index, component):
        super(TwoTeamsStatsBlock, self).addComponent(index, component)
        return

    def setRecord(self, result, reusable):
        allies, enemies = reusable.getBiDirectionTeamsIterator(result)
        self.left.setRecord(allies, reusable)
        self.right.setRecord(enemies, reusable)
        return


class RankedResultsTeamStatsBlock(shared.BiDiStatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        allies, enemies = reusable.getBiDirectionTeamsIterator(result, sort_keys.RankedVehicleXpSortKey)
        self.left.setRecord(allies, reusable)
        self.right.setRecord(enemies, reusable)
        return


class RankedResultsTeamDataStatsBlock(base.StatsBlock):
    __slots__ = (b'title', b'titleAlpha', b'teamList')

    def setRecord(self, result, reusable):
        helper = ranked.RankedResultsInfoHelper(reusable)
        winTeam = reusable.common.winnerTeam
        playerTeam = reusable.personal.avatar.team
        lists = []
        listsSteps = []
        isWon = False
        personalDBID = reusable.personal.avatar.accountDBID
        topListBlink = False
        playerCount = 0
        lastXP = 0
        xpAtBorder = 0
        lastListIdx = 0
        standoffInfo = None
        for idx, item in enumerate(result):
            isPlayer = item.player.dbID == personalDBID
            if playerCount == 0:
                isWon = self.__getIsWinTeam(currentTeam=item.player.team, winTeam=winTeam, playerTeam=playerTeam)
                lists, listsSteps = self.__createListsAndSteps(listsData=helper.getListsData(isLoser=not isWon))
            listIdx = self.__getPlayerListIndex(playerIndex=idx, listsSteps=listsSteps)
            dataList = lists[listIdx]
            if lastListIdx != listIdx:
                xpAtBorder = lastXP
                lastListIdx = listIdx
            isTopList = dataList.isTopList()
            if isPlayer:
                stepChanges = reusable.personal.getRankInfo().stepChanges
                updatedStepChanges = reusable.personal.getRankInfo().updatedStepChanges
                standoffInfo = helper.getPlayerStandoff(team=playerTeam, position=idx, stepChanges=stepChanges, updatedStepChanges=updatedStepChanges)
                if isTopList and not topListBlink:
                    topListBlink = True
                    dataList.setListBlink(True)
            else:
                standoffInfo = helper.getStandoff(isTop=isTopList, xp=item.xp - item.xpPenalty, xpToCompare=xpAtBorder, position=idx, isLoser=not isWon, lastStandoffInfo=standoffInfo)
            standoff, _ = standoffInfo
            lastXP = item.xp - item.xpPenalty
            listItem = RankedResultsListItemStatsBlock()
            listItem.setRecord((item, standoff), reusable)
            dataList.appendPlayer(listItem.getVO())
            playerCount += 1

        if playerCount == 0:
            if not winTeam:
                isWon = False
            else:
                isWon = playerTeam != winTeam
            lists, listsSteps = self.__createListsAndSteps(listsData=helper.getListsData(isLoser=not isWon))
        self.__fillIncompleteTeam(playerCount, helper.getPlayersNumber(), lists, listsSteps)
        if isWon:
            self.title = text_styles.highTitle(backport.text(R.strings.ranked_battles.battleResult.winners()))
            self.titleAlpha = 1.0
        else:
            self.title = text_styles.highTitle(backport.text(R.strings.ranked_battles.battleResult.losers()))
            self.titleAlpha = 0.6
        self.teamList = []
        for listOfPlayers in lists:
            if listOfPlayers.getPlayersNumber() > 0:
                self.teamList.append(listOfPlayers.getVO())

        return

    def __getIsWinTeam(self, currentTeam, playerTeam, winTeam):
        if not winTeam:
            isWon = False
        else:
            isPlayerTeam = playerTeam == currentTeam
            if isPlayerTeam:
                isWon = winTeam == playerTeam
            else:
                isWon = winTeam != playerTeam
        return isWon

    @staticmethod
    def __fillIncompleteTeam(membersCount, maxCount, lists, listsSteps):
        for idx in range(membersCount, maxCount):
            listIndex = RankedResultsTeamDataStatsBlock.__getPlayerListIndex(playerIndex=idx, listsSteps=listsSteps)
            dataList = lists[listIndex]
            dataList.appendPlayer(RankedResultsListItemStatsBlock().getVO())

        return

    @staticmethod
    def __getPlayerListIndex(playerIndex, listsSteps):
        indx = 0
        for indx, value in enumerate(listsSteps):
            if playerIndex < value:
                return indx

        return indx

    @staticmethod
    def __createListsAndSteps(listsData):
        lists = []
        count = len(listsData)
        i = 0
        listsSteps = []
        step = 0
        while i < count:
            listBlock = RankedResultsTeamPartDataStatsBlock()
            listBlock.setListResources(listsData[i], i == 0)
            lists.append(listBlock)
            step += listBlock.getListCapacity()
            listsSteps.append(step)
            i += 1

        return (
         lists, listsSteps)


class RankedResultsTeamPartDataStatsBlock(base.StatsBlock):
    __slots__ = (b'listData', b'backgroundType', b'backgroundBlink', b'icon', b'capacity', b'isColorBlind', b'iconType')
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, meta=None, field=b'', *path):
        super(RankedResultsTeamPartDataStatsBlock, self).__init__(meta, field, *path)
        self.listData = []
        self.backgroundType = b''
        self.backgroundBlink = False
        self.icon = b''
        self.iconType = b''
        self.capacity = 0
        self.isColorBlind = False
        return

    def appendPlayer(self, playerItem):
        self.listData.append(playerItem)
        return

    def getPlayersNumber(self):
        return len(self.listData)

    def setListResources(self, listInfo, isTopList=False):
        self.capacity, resources = listInfo
        self.iconType, self.backgroundType, iconMethod = resources
        self.icon = b''
        if isTopList:
            self.icon = iconMethod(self.capacity)
        if self.backgroundType == RANKEDBATTLES_ALIASES.BACKGROUND_STATE_LOSE:
            self.isColorBlind = self.settingsCore.getSetting(b'isColorBlind')
        return

    def setListBlink(self, isBlink):
        self.backgroundBlink = isBlink
        return

    def getListCapacity(self):
        return self.capacity

    def isTopList(self):
        return self.icon != b''


class RankedResultsListItemStatsBlock(base.StatsBlock):
    __slots__ = (b'nickName', b'nickNameHuge', b'fakeName', b'fakeNameHuge', b'points', b'pointsHuge', b'selected', b'standoff', b'tags')
    settingsCore = dependency.descriptor(ISettingsCore)

    def setRecord(self, result, reusable):
        item, standoff = result
        self.nickName = style.makeRankedNickNameValue(item.player.realName)
        self.nickNameHuge = style.makeRankedNickNameHugeValue(item.player.realName)
        self.fakeName = style.makeRankedNickNameValue(item.player.fakeName)
        self.fakeNameHuge = style.makeRankedNickNameHugeValue(item.player.fakeName)
        self.points = style.makeRankedPointValue(item.xp - item.xpPenalty)
        self.pointsHuge = style.makeRankedPointHugeValue(item.xp - item.xpPenalty)
        self.selected = item.player.dbID == reusable.personal.avatar.accountDBID
        if self.settingsCore.getSetting(b'isColorBlind') and standoff == RANKEDBATTLES_ALIASES.STANDOFF_MINUS:
            standoff = RANKEDBATTLES_ALIASES.STANDOFF_MINUS_BLIND
        self.standoff = standoff
        self.tags = item.player.tags
        return


class BadgeBlock(base.StatsBlock):
    __slots__ = (b'icon', b'content', b'sizeContent', b'isDynamic', b'isAtlasSource')

    def __init__(self, meta=None, field=b'', *path):
        super(BadgeBlock, self).__init__(meta, field, *path)
        self.icon = b''
        self.content = b''
        self.sizeContent = b''
        self.isDynamic = False
        self.isAtlasSource = False
        return

    def setRecord(self, result, reusable):
        player = result.player
        avatar = reusable.avatars.getAvatarInfo(player.dbID)
        badgeInfo = avatar.getFullBadgeInfo()
        if badgeInfo is not None:
            self.icon = badgeInfo.getThumbnailIcon()
            self.isDynamic = badgeInfo.hasDynamicContent()
            self.content = badgeInfo.getDynamicContent()
            self.sizeContent = ICONS_SIZES.X24
        return
