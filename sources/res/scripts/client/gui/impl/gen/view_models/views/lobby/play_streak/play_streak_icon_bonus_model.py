from enum import IntEnum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class DogTagType(IntEnum):
    ENGRAVING = 0
    BACKGROUND = 1


class PlayStreakIconBonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(PlayStreakIconBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getDogTagType(self):
        return DogTagType(self._getNumber(8))

    def setDogTagType(self, value):
        self._setNumber(8, value.value)
        return

    def getIsPeriodic(self):
        return self._getBool(9)

    def setIsPeriodic(self, value):
        self._setBool(9, value)
        return

    def getOverlayType(self):
        return self._getString(10)

    def setOverlayType(self, value):
        self._setString(10, value)
        return

    def _initialize(self):
        super(PlayStreakIconBonusModel, self)._initialize()
        self._addNumberProperty(b'dogTagType')
        self._addBoolProperty(b'isPeriodic', False)
        self._addStringProperty(b'overlayType', b'')
        return
