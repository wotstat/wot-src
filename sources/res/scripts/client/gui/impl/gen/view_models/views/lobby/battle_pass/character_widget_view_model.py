from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class CharacterWidgetViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CharacterWidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTankman(self):
        return self._getString(0)

    def setTankman(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getVoiceTag(self):
        return self._getString(2)

    def setVoiceTag(self, value):
        self._setString(2, value)
        return

    def getSkills(self):
        return self._getArray(3)

    def setSkills(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getSkillsType():
        return unicode

    def getTooltipId(self):
        return self._getString(4)

    def setTooltipId(self, value):
        self._setString(4, value)
        return

    def getIsPaidReward(self):
        return self._getBool(5)

    def setIsPaidReward(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(CharacterWidgetViewModel, self)._initialize()
        self._addStringProperty(b'tankman', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'voiceTag', b'')
        self._addArrayProperty(b'skills', Array())
        self._addStringProperty(b'tooltipId', b'')
        self._addBoolProperty(b'isPaidReward', False)
        return
