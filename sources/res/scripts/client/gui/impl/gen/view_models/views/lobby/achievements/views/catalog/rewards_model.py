from enum import IntEnum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class DogTagType(IntEnum):
    ENGRAVING = 0
    BACKGROUND = 1


class RewardsModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(RewardsModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(9)

    def setId(self, value):
        self._setNumber(9, value)
        return

    def getPurpose(self):
        return self._getString(10)

    def setPurpose(self, value):
        self._setString(10, value)
        return

    def getDogTagType(self):
        return DogTagType(self._getNumber(11))

    def setDogTagType(self, value):
        self._setNumber(11, value.value)
        return

    def getBackgroundId(self):
        return self._getNumber(12)

    def setBackgroundId(self, value):
        self._setNumber(12, value)
        return

    def getEngravingId(self):
        return self._getNumber(13)

    def setEngravingId(self, value):
        self._setNumber(13, value)
        return

    def _initialize(self):
        super(RewardsModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'purpose', b'')
        self._addNumberProperty(b'dogTagType')
        self._addNumberProperty(b'backgroundId', 0)
        self._addNumberProperty(b'engravingId', 0)
        return
