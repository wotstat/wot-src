from frameworks.wulf import ViewModel

class LockedTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LockedTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getKeyName(self):
        return self._getString(0)

    def setKeyName(self, value):
        self._setString(0, value)
        return

    def getIsUnlocked(self):
        return self._getBool(1)

    def setIsUnlocked(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(LockedTooltipModel, self)._initialize()
        self._addStringProperty(b'keyName', b'')
        self._addBoolProperty(b'isUnlocked', False)
        return
