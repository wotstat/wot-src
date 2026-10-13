from __future__ import absolute_import
from past.builtins import cmp
from constants import DEATH_REASON_ALIVE
from gui.battle_results.reusable import sort_keys
from gui.battle_results.components import base, common
from halloween_common.halloween_constants import INVALID_BATTLE_PLACE

class HwPhaseItem(base.StatsItem):

    def _convert(self, value, reusable):
        return reusable.getPersonalVehiclesInfo(value).hwPhase


class HwPhasesCountItem(base.StatsItem):

    def _convert(self, value, reusable):
        return reusable.getPersonalVehiclesInfo(value).hwPhasesCount


class HwEffectivenessArtefactKeysItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return reusable.getPersonalVehiclesInfo(value).effectivenessKeys


class HwBossArtefactKeysItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return reusable.getPersonalVehiclesInfo(value).bossKeys


class HwHangarLoot(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return reusable.getPersonalVehiclesInfo(value).hwHangarLoot


class PersonalFirstTeamItemSortKey(sort_keys.TeamItemSortKey):
    __slots__ = (b'_sortKey',)

    def __init__(self, vehicleInfo, compareKey):
        super(PersonalFirstTeamItemSortKey, self).__init__(vehicleInfo)
        self._sortKey = compareKey
        return

    def _cmp(self, other):
        sortKey = self._sortKey
        return cmp(getattr(other.info, sortKey), getattr(self.info, sortKey))


class HWAfkSortKey(sort_keys.TeamItemSortKey):
    __slots__ = ()

    def _cmp(self, other):
        return cmp(self._isAfk(self.info), self._isAfk(other.info))

    @staticmethod
    def _isAfk(info):
        return getattr(info, b'hwTeamFightPlace') == INVALID_BATTLE_PLACE


class HWVehicleStatsBlock(base.StatsBlock):
    __slots__ = (b'playerDBID', b'playerName', b'vehicleName', b'vehicleType', b'vehicleCD', b'vehicleLvl', b'clanAbbrev', b'artefactKeys', b'isPlayer', b'squadID', b'isOwnSquad', b'killerName', b'deathReason', b'kills', b'damageDealt', b'badgeID', b'badgeSuffixID', b'hwVehiclesRespawnCount', b'hasPenalties', b'hwBossFightDamage', b'hwHangarLoot')

    def __init__(self, meta=None, field=b'', *path):
        super(HWVehicleStatsBlock, self).__init__(meta, field, *path)
        self.playerDBID = 0
        self.playerName = b''
        self.vehicleName = b''
        self.vehicleType = b''
        self.vehicleCD = 0
        self.vehicleLvl = -1
        self.clanAbbrev = b''
        self.artefactKeys = 0
        self.killerName = b''
        self.deathReason = -1
        self.kills = 0
        self.damageDealt = 0
        self.isPlayer = False
        self.squadID = -1
        self.isOwnSquad = False
        self.badgeID = 0
        self.badgeSuffixID = 0
        self.hwVehiclesRespawnCount = 0
        self.hasPenalties = False
        self.hwBossFightDamage = 0
        self.hwHangarLoot = {}
        return

    def setRecord(self, result, reusable):
        super(HWVehicleStatsBlock, self).setRecord(result, reusable)
        self.playerDBID = result.player.dbID
        self.playerName = result.player.realName
        self.vehicleName = result.vehicle.userName
        self.vehicleType = result.vehicle.type
        self.vehicleCD = result.vehicle.intCD
        self.vehicleLvl = result.vehicle.level
        self.clanAbbrev = result.player.clanAbbrev
        self.artefactKeys = result.totalKeys
        self.hwBossFightDamage = result.hwBossFightDamage
        self.deathReason = result.deathReason
        self.kills = result.kills
        self.damageDealt = result.damageDealt
        self.isPlayer = self.playerDBID == reusable.personal.avatar.accountDBID
        self.squadID = result.player.squadIndex
        self.hasPenalties = result.avatar.hasPenalties()
        self.hwVehiclesRespawnCount = result.hwVehiclesRespawnCount
        personalInfo = reusable.getPlayerInfo()
        personalPrebattleID = personalInfo.prebattleID if personalInfo.squadIndex else 0
        self.isOwnSquad = personalPrebattleID != 0 and personalPrebattleID == result.player.prebattleID
        avatar = reusable.avatars.getAvatarInfo(result.player.dbID)
        self.badgeID = avatar.badge if avatar else 0
        self.badgeSuffixID = avatar.suffixBadge
        if self.deathReason > DEATH_REASON_ALIVE:
            if result.killerID:
                killerVehicle = reusable.getPlayerInfoByVehicleID(result.killerID)
                self.killerName = killerVehicle.fakeName
        return


class HWBattlesTeamStatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        allies, _ = reusable.getBiDirectionTeamsIterator(result, sortKey=(lambda info: (
         HWAfkSortKey(info),
         PersonalFirstTeamItemSortKey(info, b'totalKeys'),
         PersonalFirstTeamItemSortKey(info, b'hwTeamContribution'),
         PersonalFirstTeamItemSortKey(info, b'kills'))))
        for item in allies:
            block = HWVehicleStatsBlock()
            block.setRecord(item, reusable)
            self.addComponent(self.getNextComponentIndex(), block)

        return


class HWBattleFinishResultBlock(common.RegularFinishResultBlock):

    def setRecord(self, result, reusable):
        teamRes = reusable.getPersonalTeamResult()
        self.shortResultLabel = teamRes
        self.fullResultLabel = b''
        self.finishReasonLabel = b''
        self.finishReasonClarificationLabel = b''
        return
