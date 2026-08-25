from frameworks.wulf import ViewModel

class BattleAbilityAltTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleAbilityAltTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getVideoName(self):
        return self._getString(1)

    def setVideoName(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(BattleAbilityAltTooltipModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'videoName', b'')
        self._addStringProperty(b'description', b'')
        return
