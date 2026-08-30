from enum import Enum
from frameworks.wulf import ViewModel

class BattleType(Enum):
    SOLO = b'solo'
    PLATOON = b'platoon'
    TEAM = b'team'


class AnimationState(Enum):
    NONE = b'none'
    FIRSTSHOW = b'firstShow'
    IDLEBLINK = b'idleBlink'


class BattleTypeSelectorViewModel(ViewModel):
    __slots__ = (b'onSelectTab',)

    def __init__(self, properties=3, commands=1):
        super(BattleTypeSelectorViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedTab(self):
        return BattleType(self._getString(0))

    def setSelectedTab(self, value):
        self._setString(0, value.value)
        return

    def getAnimationState(self):
        return AnimationState(self._getString(1))

    def setAnimationState(self, value):
        self._setString(1, value.value)
        return

    def getIsHintShown(self):
        return self._getBool(2)

    def setIsHintShown(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(BattleTypeSelectorViewModel, self)._initialize()
        self._addStringProperty(b'selectedTab', BattleType.SOLO.value)
        self._addStringProperty(b'animationState', AnimationState.NONE.value)
        self._addBoolProperty(b'isHintShown', False)
        self.onSelectTab = self._addCommand(b'onSelectTab')
        return
