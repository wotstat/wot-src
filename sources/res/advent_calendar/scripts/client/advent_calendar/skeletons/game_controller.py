from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Optional
    from gui.server_events.event_items import Quest
    from Event import Event
    from advent_calendar.helpers.server_settings import AdventCalendarConfig
    from gui.shared.gui_items.loot_box import LootBox
    from helpers.server_settings import LootBoxesTooltipConfig

class IAdventCalendarController(IGameController):
    onConfigChanged = None
    onDoorsStateChanged = None
    onDoorOpened = None
    onLootBoxesConfigChanged = None

    @property
    def isActive(self):
        raise NotImplementedError
        return

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def isInActivePhase(self):
        raise NotImplementedError
        return

    def isAvailableAndActivePhase(self):
        raise NotImplementedError
        return

    def isAvailableAndPostActivePhase(self):
        raise NotImplementedError
        return

    def isInPostActivePhase(self):
        raise NotImplementedError
        return

    def isFirstEventDay(self):
        raise NotImplementedError
        return

    def awaitDoorOpenQuestCompletion(self, dayID, currency):
        raise NotImplementedError
        return

    def progressionQuestMayBeCompleted(self, openedDoorsAmount=None):
        raise NotImplementedError
        return

    @property
    def config(self):
        raise NotImplementedError
        return

    @property
    def startDate(self):
        raise NotImplementedError
        return

    @property
    def postEventStartDate(self):
        raise NotImplementedError
        return

    @property
    def postEventEndDate(self):
        raise NotImplementedError
        return

    def getDoorOpenQuestName(self, day):
        raise NotImplementedError
        return

    def getDoorOpenTokenName(self, day):
        raise NotImplementedError
        return

    def getDoorOpenTimeUI(self, doorId):
        raise NotImplementedError
        return

    def getCurrentDayNumber(self):
        raise NotImplementedError
        return

    @property
    def getCurrentTime(self):
        raise NotImplementedError
        return

    def getQuestByDayId(self, dayId):
        raise NotImplementedError
        return

    def isDoorOpened(self, dayID):
        raise NotImplementedError
        return

    @property
    def progressionRewardQuestsOrdered(self):
        raise NotImplementedError
        return

    @property
    def completedAwardsQuests(self):
        raise NotImplementedError
        return

    @property
    def lootBoxesTooltipConfig(self):
        raise NotImplementedError
        return

    def getRewardsLootBox(self):
        raise NotImplementedError
        return

    def getAdventCalendarGroupedQuestsRewards(self):
        raise NotImplementedError
        return
