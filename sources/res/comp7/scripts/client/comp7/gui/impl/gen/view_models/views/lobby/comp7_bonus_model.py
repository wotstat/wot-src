from enum import IntEnum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class DogTagType(IntEnum):
    ENGRAVING = 0
    BACKGROUND = 1


class Comp7BonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(Comp7BonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getDogTagType(self):
        return DogTagType(self._getNumber(9))

    def setDogTagType(self, value):
        self._setNumber(9, value.value)
        return

    def getIsPeriodic(self):
        return self._getBool(10)

    def setIsPeriodic(self, value):
        self._setBool(10, value)
        return

    def getOverlayType(self):
        return self._getString(11)

    def setOverlayType(self, value):
        self._setString(11, value)
        return

    def getItem(self):
        return self._getString(12)

    def setItem(self, value):
        self._setString(12, value)
        return

    def getGroupName(self):
        return self._getString(13)

    def setGroupName(self, value):
        self._setString(13, value)
        return

    def getClaimed(self):
        return self._getBool(14)

    def setClaimed(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(Comp7BonusModel, self)._initialize()
        self._addNumberProperty(b'dogTagType')
        self._addBoolProperty(b'isPeriodic', False)
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'item', b'')
        self._addStringProperty(b'groupName', b'')
        self._addBoolProperty(b'claimed', False)
        return
