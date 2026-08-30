from debug_utils import LOG_ERROR
from dossiers2.ui.achievements import ACHIEVEMENT_TYPE
from gui.battle_results import stored_sorting
from gui.battle_results.components import base
from gui.battle_results.components.style import makeTeamKillerText
from gui.battle_results.pbs_helpers.common import getAchievementCustomData, getVehicleLevel
from gui.shared.gui_items.dossier.achievements import MarkOnGunAchievement

class TrueFlag(base.StatsItem):

    def _convert(self, value, reusable):
        return True


class FalseFlag(base.StatsItem):

    def _convert(self, value, reusable):
        return False


class ClientIndexItem(base.StatsItem):

    def _convert(self, value, reusable):
        return reusable.clientIndex


class PlayerNameBlock(base.StatsBlock):
    __slots__ = (b'_dbID', b'fakeNameLabel', b'realNameLabel', b'clanLabel', b'fullNameLabel', b'regionLabel', b'isTeamKiller', b'tags')

    def __init__(self, meta=None, field=b'', *path):
        super(PlayerNameBlock, self).__init__(meta, field, *path)
        self._dbID = 0
        return

    def setTeamKillerInfo(self):
        self.realNameLabel = makeTeamKillerText(self.realNameLabel)
        self.fullNameLabel = makeTeamKillerText(self.fullNameLabel)
        self.isTeamKiller = True
        return

    def setPlayerInfo(self, playerInfo):
        self._dbID = playerInfo.dbID
        self.fakeNameLabel = playerInfo.fakeName
        self.realNameLabel = playerInfo.realName
        self.clanLabel = playerInfo.clanAbbrev
        self.fullNameLabel = playerInfo.getFullName()
        self.regionLabel = playerInfo.getRegionCode()
        self.tags = playerInfo.tags
        return

    def setRecord(self, result, reusable):
        if reusable is not None:
            self.setPlayerInfo(reusable.getPlayerInfo(self._dbID))
        else:
            LOG_ERROR(b'Player is not found', result, reusable)
        return


class WasInBattleItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return reusable.wasInBattle()


class WasInEpicBattleItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        from constants import ARENA_BONUS_TYPE
        return value[b'common'][b'bonusType'] == ARENA_BONUS_TYPE.EPIC_BATTLE


class SortingBlock(base.StatsBlock):
    __slots__ = (b'__setting', b'criteria', b'direction')

    def __init__(self, setting, meta=None, field=b'', *path):
        super(SortingBlock, self).__init__(meta, field, *path)
        self.criteria = None
        self.direction = None
        self.__setting = setting
        return

    @property
    def settingKey(self):
        return self.__setting

    def getVO(self):
        self.criteria, self.direction = stored_sorting.readStatsSorting(self.__setting)
        return super(SortingBlock, self).getVO()

    def setRecord(self, result, reusable):
        return


class RegularSortingBlock(SortingBlock):
    __slots__ = ()

    def __init__(self, meta=None, field=b'', *path):
        super(RegularSortingBlock, self).__init__(stored_sorting.STATS_REGULAR_SORTING, meta, field, *path)
        return


class AchievementIcon(base.StatsBlock):
    __slots__ = (b'big', b'small')

    def __init__(self, meta=None, field=b'', *path):
        super(AchievementIcon, self).__init__(meta, field, *path)
        self.small = b''
        self.big = b''
        return

    def setRecord(self, result, reusable):
        self.small = result
        return


class AchievementBlock(base.StatsBlock):
    __slots__ = (b'type', b'block', b'icon', b'specialIcon', b'title', b'description', b'hasRibbon', b'customData', b'isUnique', b'rank', b'i18nValue', b'inactive', b'isRare', b'rareIconID', b'arenaType', b'vehicleLevel')

    def setUnique(self, value):
        self.isUnique = value
        return

    def setRecord(self, result, reusable):
        if result.getType() != ACHIEVEMENT_TYPE.SERIES:
            self.rank = result.getValue()
            self.i18nValue = result.getI18nValue()
        icons = result.getIcons()
        specialIcon = icons.get(MarkOnGunAchievement.IT_95X85, None)
        recordName = result.getRecordName()
        customData = getAchievementCustomData(result)
        self.type = recordName[1]
        self.block = result.getBlock()
        self.icon = result.getSmallIcon() if specialIcon is None else b''
        self.specialIcon = specialIcon
        self.title = result.getUserName()
        self.description = result.getUserDescription()
        self.hasRibbon = result.hasRibbon()
        self.customData = customData
        if reusable:
            self.arenaType = reusable.common.arenaBonusType
            self.vehicleLevel = getVehicleLevel(reusable)
        return


class AchievementsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, record, reusable):
        for achievement, isUnique in record:
            component = AchievementBlock()
            component.setUnique(isUnique)
            component.setRecord(achievement, reusable)
            self.addComponent(self.getNextComponentIndex(), component)

        return


class BiDiStatsBlock(base.StatsBlock):
    __slots__ = ()

    @property
    def left(self):
        component = self.getComponent(0)
        return component

    @property
    def right(self):
        component = self.getComponent(1)
        return component
