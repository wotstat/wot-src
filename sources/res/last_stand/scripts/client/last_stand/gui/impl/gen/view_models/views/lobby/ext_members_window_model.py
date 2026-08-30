from enum import Enum
from last_stand.gui.impl.gen.view_models.views.lobby.event_difficulty_model import EventDifficultyModel
from gui.impl.gen.view_models.views.lobby.platoon.members_window_model import MembersWindowModel

class PrebattleTypes(Enum):
    LASTSTAND = b'lastStand'


class ExtMembersWindowModel(MembersWindowModel):
    __slots__ = ()

    def __init__(self, properties=23, commands=3):
        super(ExtMembersWindowModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def eventDifficulty(self):
        return self._getViewModel(17)

    @staticmethod
    def getEventDifficultyType():
        return EventDifficultyModel

    def getSelectedDifficulty(self):
        return self._getNumber(18)

    def setSelectedDifficulty(self, value):
        self._setNumber(18, value)
        return

    def getSelectionDisabled(self):
        return self._getBool(19)

    def setSelectionDisabled(self, value):
        self._setBool(19, value)
        return

    def getIsInSearch(self):
        return self._getBool(20)

    def setIsInSearch(self, value):
        self._setBool(20, value)
        return

    def getIsCommander(self):
        return self._getBool(21)

    def setIsCommander(self, value):
        self._setBool(21, value)
        return

    def getHasFreeSlots(self):
        return self._getBool(22)

    def setHasFreeSlots(self, value):
        self._setBool(22, value)
        return

    def _initialize(self):
        super(ExtMembersWindowModel, self)._initialize()
        self._addViewModelProperty(b'eventDifficulty', EventDifficultyModel())
        self._addNumberProperty(b'selectedDifficulty', 1)
        self._addBoolProperty(b'selectionDisabled', False)
        self._addBoolProperty(b'isInSearch', False)
        self._addBoolProperty(b'isCommander', False)
        self._addBoolProperty(b'hasFreeSlots', False)
        return
