from frameworks.wulf import ViewModel

class CriticalDamageGroupModel(ViewModel):
    __slots__ = ()
    CRITICAL_DEVICES = b'criticalDevices'
    DESTROYED_DEVICES = b'destroyedDevices'
    DESTROYED_TANKMENS = b'destroyedTankmen'

    def __init__(self, properties=2, commands=0):
        super(CriticalDamageGroupModel, self).__init__(properties=properties, commands=commands)
        return

    def getDamageGroup(self):
        return self._getString(0)

    def setDamageGroup(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(CriticalDamageGroupModel, self)._initialize()
        self._addStringProperty(b'damageGroup', b'')
        self._addStringProperty(b'value', b'')
        return
