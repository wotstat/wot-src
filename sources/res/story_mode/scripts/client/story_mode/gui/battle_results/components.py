from gui.battle_results.components import base
from gui.server_events.bonuses import getNonQuestBonuses, mergeBonuses
from gui.impl.gen import R
from gui.shared.gui_items.Vehicle import getUserName
from helpers import dependency
from items import vehicles
from skeletons.gui.game_control import IBattlePassController
from story_mode.skeletons.story_mode_controller import IStoryModeController
from story_mode_common.configs.story_mode_missions import missionsSchema
from story_mode.gui.shared.utils import getRewardList

class FinishResultItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        return reusable.getPersonalTeamResult()


class FinishReasonItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        finishReason = reusable.common.finishReason
        rReason = R.strings.sm_battle.finish.reason
        return rReason.num(finishReason, rReason.default)()


class MissionIdItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        return record[b'avatar'][b'missionId']


class IsForceOnboardingItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        return record[b'avatar'][b'isForceOnboarding']


class VehicleNameItem(base.StatsItem):
    __slots__ = ()
    _storyModeCtrl = dependency.descriptor(IStoryModeController)

    def _convert(self, record, reusable):
        mission = self._storyModeCtrl.missions.getMission(record[b'avatar'][b'missionId'])
        if mission is None:
            return b''
        else:
            return getUserName(vehicles.makeVehicleTypeByName(mission.vehicle.name))


class VehicleBlock(base.StatsBlock):

    def setRecord(self, result, reusable):
        vehicleInfo = reusable.getPersonalVehiclesInfo(result[b'personal'])
        self.addNextComponent(base.DirectStatsItem(b'deathReason', vehicleInfo.deathReason))
        self.addNextComponent(base.DirectStatsItem(b'damageDealt', vehicleInfo.damageDealt))
        self.addNextComponent(base.DirectStatsItem(b'kills', vehicleInfo.kills))
        self.addNextComponent(base.DirectStatsItem(b'damageAssisted', vehicleInfo.damageAssisted + vehicleInfo.equipmentDamageAssisted))
        self.addNextComponent(base.DirectStatsItem(b'damageBlockedByArmor', vehicleInfo.damageBlockedByArmor))
        return


class RewardsBlock(base.StatsBlock):
    __slots__ = ()
    _battlePass = dependency.descriptor(IBattlePassController)

    def setRecord(self, result, reusable):
        progressInfo = result[b'personal'][b'avatar'].get(b'progressionInfo', {})
        missionSettings = missionsSchema.getModel()
        if missionSettings is None:
            return
        else:
            rewardsList = getRewardList(progressInfo, self._battlePass.isActive(), True)
            bonuses = []
            for rewardRecord in rewardsList:
                for rewardName, rewardData in rewardRecord.iteritems():
                    for item in getNonQuestBonuses(rewardName, rewardData):
                        bonuses.append(item)

            for item in mergeBonuses(bonuses):
                self.addNextComponent(base.DirectStatsItem(b'', item))

            return


class ProgressionInfoItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        return record[b'avatar'].get(b'progressionInfo', {})
