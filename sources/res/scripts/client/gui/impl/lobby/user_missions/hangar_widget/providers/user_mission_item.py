from __future__ import absolute_import
from typing import TYPE_CHECKING
from gui.server_events.events_helpers import EventInfoModel
from gui.impl.lobby.user_missions.hangar_widget.utils import DailyMissionItemPacker, WeeklyMissionItemPacker
from gui.shared.missions.packers.bonus import getDailyMissionsBonusPacker, getWeeklyMissionsBonusPacker, weeklyBonusSortKey
if TYPE_CHECKING:
    from gui.server_events.event_items import DailyQuest

class MissionItem(object):
    __slots__ = (b'itemId', b'itemType', b'weight', b'secondaryKey', b'_rawData', b'_isCompleted')

    def __init__(self, itemId, itemType, weight=0, secondaryKey=None):
        self.itemId = itemId
        self.itemType = itemType
        self.weight = weight
        self.secondaryKey = tuple(secondaryKey) if secondaryKey else ()
        self._rawData = None
        self._isCompleted = False
        return

    @property
    def rawData(self):
        return self._rawData

    @rawData.setter
    def rawData(self, value):
        self._rawData = value
        return

    @property
    def isCompleted(self):
        return self._isCompleted

    @isCompleted.setter
    def isCompleted(self, value):
        self._isCompleted = value
        return

    @property
    def countdown(self):
        return 0

    def getMissionPacker(self):
        raise NotImplementedError
        return

    def getBonusPacker(self):
        raise NotImplementedError
        return

    def getRewardsSortKey(self):
        raise NotImplementedError
        return

    def getAnimationId(self):
        raise NotImplementedError
        return


class DailyQuestMissionItem(MissionItem):
    __slots__ = (b'difficulty',)
    _TYPE = b'daily'

    def __init__(self, itemId, weight, difficulty):
        super(DailyQuestMissionItem, self).__init__(itemId, self._TYPE, weight)
        self.difficulty = difficulty
        return

    def __repr__(self):
        return (b'DailyQuest(id={}, type={}, weight={}, difficulty={})').format(self.itemId, self.itemType, self.weight, self.difficulty)

    def setItemType(self, value):
        self.itemType = value
        return

    @property
    def countdown(self):
        dailyQuest = self._rawData
        if dailyQuest.isBonus():
            return EventInfoModel.getDailyProgressResetTimeDelta()
        return super(DailyQuestMissionItem, self).countdown

    def getMissionPacker(self):
        return DailyMissionItemPacker()

    def getBonusPacker(self):
        return getDailyMissionsBonusPacker()

    def getRewardsSortKey(self):
        return

    def getAnimationId(self):
        return b'%s::%s' % (self._TYPE, self.difficulty)


class PremiumDailyQuestMissionItem(MissionItem):
    __slots__ = ()
    _TYPE = b'premium_daily'

    def __init__(self, itemId, weight):
        super(PremiumDailyQuestMissionItem, self).__init__(itemId, self._TYPE, weight)
        return

    def __repr__(self):
        return (b'PremiumDailyQuest(id={}, type={}, weight={})').format(self.itemId, self.itemType, self.weight)

    def getMissionPacker(self):
        return DailyMissionItemPacker()

    def getBonusPacker(self):
        return getDailyMissionsBonusPacker()

    def getRewardsSortKey(self):
        return

    def getAnimationId(self):
        return self.itemId


class WeeklyQuestMissionItem(MissionItem):
    __slots__ = (b'_commonConditionId', b'_specialConditionIds', b'_questId')
    _TYPE = b'weekly'

    def __init__(self, itemId, weight, questId):
        super(WeeklyQuestMissionItem, self).__init__(itemId, self._TYPE, weight)
        self._commonConditionId = 0
        self._specialConditionIds = []
        self._questId = questId
        return

    def __repr__(self):
        return (b'WeeklyQuest(id={}, type={}, weight={}, _commonConditionId={}, _specialConditionIds={})').format(self.itemId, self.itemType, self.weight, self._commonConditionId, self._specialConditionIds)

    @property
    def commonConditionId(self):
        return self._commonConditionId

    @commonConditionId.setter
    def commonConditionId(self, value):
        self._commonConditionId = value
        return

    @property
    def specialConditionIds(self):
        return self._specialConditionIds

    @specialConditionIds.setter
    def specialConditionIds(self, value):
        self._specialConditionIds = value
        return

    def getMissionPacker(self):
        return WeeklyMissionItemPacker()

    def getBonusPacker(self):
        return getWeeklyMissionsBonusPacker()

    def getRewardsSortKey(self):
        return weeklyBonusSortKey

    def getAnimationId(self):
        return b'%s::%s' % (self._TYPE, self._questId)
