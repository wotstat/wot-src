from enum import Enum
from frameworks.wulf import ViewModel

class PetTvAnimation(Enum):
    OFF = b'off'
    WALK = b'walk'
    FOOD = b'food'
    CARE = b'care'
    ACTIVITY = b'activity'


class NyPetTvScreenViewModel(ViewModel):
    __slots__ = (b'onAnimationFinished', b'onResetToIdle')

    def __init__(self, properties=2, commands=2):
        super(NyPetTvScreenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsRaidActive(self):
        return self._getBool(0)

    def setIsRaidActive(self, value):
        self._setBool(0, value)
        return

    def getAnimation(self):
        return PetTvAnimation(self._getString(1))

    def setAnimation(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(NyPetTvScreenViewModel, self)._initialize()
        self._addBoolProperty(b'isRaidActive', False)
        self._addStringProperty(b'animation', PetTvAnimation.OFF.value)
        self.onAnimationFinished = self._addCommand(b'onAnimationFinished')
        self.onResetToIdle = self._addCommand(b'onResetToIdle')
        return
