from enum import Enum
from frameworks.wulf import Array
from new_year.gui.impl.gen.view_models.common.ny_event_state_model import NyEventStateModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.ny_with_roman_numbers_model import NyWithRomanNumbersModel

class State(Enum):
    SAD = b'sad'
    NORMAL = b'normal'
    FUN = b'fun'
    PAUSE = b'pause'
    EMPTY = b''


class RaidState(Enum):
    RAID = b'raid'
    LOOT = b'loot'
    EMPTY = b''


class PetNeed(Enum):
    FOOD = b'food'
    FUN = b'fun'
    ACTIVITY = b'activity'
    RAID = b'raid'
    NONE = b'none'


class NewYearMainWidgetModel(NyWithRomanNumbersModel):
    __slots__ = (b'onClick', b'onPetClick')

    def __init__(self, properties=25, commands=2):
        super(NewYearMainWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def eventState(self):
        return self._getViewModel(1)

    @staticmethod
    def getEventStateType():
        return NyEventStateModel

    def getAnimationType(self):
        return self._getString(2)

    def setAnimationType(self, value):
        self._setString(2, value)
        return

    def getLobbyMode(self):
        return self._getBool(3)

    def setLobbyMode(self, value):
        self._setBool(3, value)
        return

    def getUserLanguage(self):
        return self._getString(4)

    def setUserLanguage(self, value):
        self._setString(4, value)
        return

    def getLevelRoman(self):
        return self._getString(5)

    def setLevelRoman(self, value):
        self._setString(5, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(6)

    def setCurrentPoints(self, value):
        self._setNumber(6, value)
        return

    def getNextPoints(self):
        return self._getNumber(7)

    def setNextPoints(self, value):
        self._setNumber(7, value)
        return

    def getIsExtendedAnim(self):
        return self._getBool(8)

    def setIsExtendedAnim(self, value):
        self._setBool(8, value)
        return

    def getIsVisible(self):
        return self._getBool(9)

    def setIsVisible(self, value):
        self._setBool(9, value)
        return

    def getIsEnabled(self):
        return self._getBool(10)

    def setIsEnabled(self, value):
        self._setBool(10, value)
        return

    def getIsInited(self):
        return self._getBool(11)

    def setIsInited(self, value):
        self._setBool(11, value)
        return

    def getIsActiveWidgetTransitionShown(self):
        return self._getBool(12)

    def setIsActiveWidgetTransitionShown(self, value):
        self._setBool(12, value)
        return

    def getLevel(self):
        return self._getNumber(13)

    def setLevel(self, value):
        self._setNumber(13, value)
        return

    def getProgress(self):
        return self._getNumber(14)

    def setProgress(self, value):
        self._setNumber(14, value)
        return

    def getIsFirstEntrance(self):
        return self._getBool(15)

    def setIsFirstEntrance(self, value):
        self._setBool(15, value)
        return

    def getIsPetEntrance(self):
        return self._getBool(16)

    def setIsPetEntrance(self, value):
        self._setBool(16, value)
        return

    def getPetState(self):
        return State(self._getString(17))

    def setPetState(self, value):
        self._setString(17, value.value)
        return

    def getRaidState(self):
        return RaidState(self._getString(18))

    def setRaidState(self, value):
        self._setString(18, value.value)
        return

    def getProgressState(self):
        return self._getBool(19)

    def setProgressState(self, value):
        self._setBool(19, value)
        return

    def getPetNeed(self):
        return self._getArray(20)

    def setPetNeed(self, value):
        self._setArray(20, value)
        return

    @staticmethod
    def getPetNeedType():
        return unicode

    def getBonusValue(self):
        return self._getNumber(21)

    def setBonusValue(self, value):
        self._setNumber(21, value)
        return

    def getMaxBonusValue(self):
        return self._getNumber(22)

    def setMaxBonusValue(self, value):
        self._setNumber(22, value)
        return

    def getPetLevelNeed(self):
        return self._getNumber(23)

    def setPetLevelNeed(self, value):
        self._setNumber(23, value)
        return

    def getIsDay(self):
        return self._getBool(24)

    def setIsDay(self, value):
        self._setBool(24, value)
        return

    def _initialize(self):
        super(NewYearMainWidgetModel, self)._initialize()
        self._addViewModelProperty(b'eventState', NyEventStateModel())
        self._addStringProperty(b'animationType', b'none')
        self._addBoolProperty(b'lobbyMode', True)
        self._addStringProperty(b'userLanguage', b'')
        self._addStringProperty(b'levelRoman', b'')
        self._addNumberProperty(b'currentPoints', 0)
        self._addNumberProperty(b'nextPoints', 1)
        self._addBoolProperty(b'isExtendedAnim', False)
        self._addBoolProperty(b'isVisible', True)
        self._addBoolProperty(b'isEnabled', True)
        self._addBoolProperty(b'isInited', False)
        self._addBoolProperty(b'isActiveWidgetTransitionShown', False)
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'progress', 0)
        self._addBoolProperty(b'isFirstEntrance', True)
        self._addBoolProperty(b'isPetEntrance', True)
        self._addStringProperty(b'petState')
        self._addStringProperty(b'raidState', RaidState.EMPTY.value)
        self._addBoolProperty(b'progressState', False)
        self._addArrayProperty(b'petNeed', Array())
        self._addNumberProperty(b'bonusValue', 0)
        self._addNumberProperty(b'maxBonusValue', 0)
        self._addNumberProperty(b'petLevelNeed', 2)
        self._addBoolProperty(b'isDay', False)
        self.onClick = self._addCommand(b'onClick')
        self.onPetClick = self._addCommand(b'onPetClick')
        return
