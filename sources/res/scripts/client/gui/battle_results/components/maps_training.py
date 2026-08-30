import logging
from ArenaType import parseTypeID
from gui.battle_results.components import base
from gui.server_events.bonuses import getNonQuestBonuses
from helpers import dependency
from maps_training_common.helpers import getMapsTrainingAwards
from maps_training_common.maps_training_constants import MAX_SCENARIO_PROGRESS
from skeletons.gui.game_control import IMapsTrainingController
_logger = logging.getLogger(__name__)
_IMAGES_FOLDER_PATH = b'../maps/icons/maps_training/battle_result/'
_BG_FOLDER_PATH = _IMAGES_FOLDER_PATH + b'background/'
_BG_IMAGE_FORMAT = b'{team_result}.png'
_STAT_ICON_PATH = _IMAGES_FOLDER_PATH + b'{0}.png'
_STAT_ICON_TOOLTIP_PATH = _IMAGES_FOLDER_PATH + b'tooltip/{0}.png'
_STAT_FIELD_NAMES = (b'damageDealt', b'damageBlockedByArmor')
BATTLE_STATS_KILLS = b'kills'
BATTLE_STATS_RESULT_FIELDS = {BATTLE_STATS_KILLS: b'kills'}
BATTLE_STATS_ICONS = {BATTLE_STATS_KILLS: b'statIconDestroyed'}

class BattleGoalsBlock(base.StatsBlock):

    def setRecord(self, result, reusable):
        vseBattleResults = result[b'personal'][b'avatar'][b'vseBattleResults']
        for vehClass, goalResult in vseBattleResults.iteritems():
            self.addNextComponent(base.DirectStatsItem(vehClass, goalResult))

        return


class BattleDurationItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, result, reusable):
        return result[b'common'][b'duration']


class StatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        info = reusable.getPersonalVehiclesInfo(result[b'personal'])
        for statType, statFieldName in BATTLE_STATS_RESULT_FIELDS.iteritems():
            statVal = info.__getattribute__(statFieldName)
            self.addNextComponent(base.DirectStatsItem(b'', {b'id': statType, 
               b'value': statVal}))

        questKills = 0
        vseBattleResults = result[b'personal'][b'avatar'][b'vseBattleResults']
        for goal, kills in vseBattleResults.itervalues():
            if goal == 0:
                continue
            questKills += goal if kills > goal else kills

        self.addNextComponent(base.DirectStatsItem(b'', {b'id': b'questKills', 
           b'value': questKills}))
        return


class GeometryIdItem(base.StatsItem):

    def _convert(self, result, reusable):
        typeId = reusable.common.arenaType.getID()
        _, geometryID = parseTypeID(typeId)
        return geometryID


class TeamItem(base.StatsItem):

    def _convert(self, result, reusable):
        return result[b'personal'][b'avatar'][b'team']


class VehicleBlock(base.StatsBlock):

    def setRecord(self, result, reusable):
        vehicle = reusable.getPersonalVehiclesInfo(result[b'personal']).vehicle
        self.addNextComponent(base.DirectStatsItem(b'type', vehicle.type))
        self.addNextComponent(base.DirectStatsItem(b'name', vehicle.name))
        return


class MTProgressMixin(object):
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)

    def _getScenarioData(self, result, reusable):
        typeId = reusable.common.arenaType.getID()
        _, geometryID = parseTypeID(typeId)
        vehType = reusable.getPersonalVehiclesInfo(result[b'personal']).vehicle.type
        team = result[b'personal'][b'avatar'][b'team']
        config = self.mapsTrainingController.getConfig()
        rewardsConfig = config.get(b'rewards', {}).get(geometryID, {})
        scenarioConfig = config.get(b'scenarios', {}).get(geometryID, {}).get(team, {}).get(vehType, {})
        playerProgress = result[b'personal'][b'avatar'][b'scenarioProgress']
        return (
         scenarioConfig, rewardsConfig, playerProgress)


class DoneValueItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, result, reusable):
        return result[b'personal'][b'avatar'][b'scenarioProgress'][b'result']


class ScenarioProgressBlock(base.StatsBlock, MTProgressMixin):
    __slots__ = ()

    def setRecord(self, result, reusable):
        scenarioConfig, _, playerProgress = self._getScenarioData(result, reusable)
        totalTargets = sum(scenarioConfig[b'goals'].values())
        self.addNextComponent(base.DirectStatsItem(b'', (
         totalTargets,
         playerProgress[b'level'] > 0,
         playerProgress[b'level'] > 0 and playerProgress[b'prevBest'] > 0)))
        return


class RewardsBlock(base.StatsBlock, MTProgressMixin):
    __slots__ = ()

    def setRecord(self, result, reusable):
        _, rewardsConfig, playerProgress = self._getScenarioData(result, reusable)
        bonus = getMapsTrainingAwards(rewardsConfig, playerProgress[b'prevBest'], playerProgress[b'level'], result[b'personal'][b'avatar'][b'mt_mapComplete'])
        for rewardName, rewardData in bonus.iteritems():
            for item in getNonQuestBonuses(rewardName, rewardData):
                self.addNextComponent(base.DirectStatsItem(b'', item))

        return


class AccountProgressBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        hasImproved = result[b'personal'][b'avatar'][b'mt_progressImproved']
        self.addNextComponent(base.DirectStatsItem(b'hasImproved', hasImproved))
        return


class WasDoneItem(base.StatsItem, MTProgressMixin):

    def _convert(self, result, reusable):
        _, __, playerProgress = self._getScenarioData(result, reusable)
        return playerProgress[b'prevBest'] == MAX_SCENARIO_PROGRESS
