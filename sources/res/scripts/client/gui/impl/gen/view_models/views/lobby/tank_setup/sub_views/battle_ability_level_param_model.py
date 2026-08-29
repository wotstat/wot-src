from frameworks.wulf import ViewModel

class BattleAbilityLevelParamModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(BattleAbilityLevelParamModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getValueTemplate(self):
        return self._getString(1)

    def setValueTemplate(self, value):
        self._setString(1, value)
        return

    def getValue(self):
        return self._getString(2)

    def setValue(self, value):
        self._setString(2, value)
        return

    def getName(self):
        return self._getString(3)

    def setName(self, value):
        self._setString(3, value)
        return

    def getSign(self):
        return self._getString(4)

    def setSign(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(BattleAbilityLevelParamModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'valueTemplate', b'')
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'sign', b'')
        return
