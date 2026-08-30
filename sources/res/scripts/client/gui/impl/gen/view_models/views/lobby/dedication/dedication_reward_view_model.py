from frameworks.wulf import Array, ViewModel

class DedicationRewardViewModel(ViewModel):
    __slots__ = ()
    BATTLES_150K = b'150'
    BATTLES_200K = b'200'
    BATTLES_250K = b'250'
    BATTLES_300K = b'300'

    def __init__(self, properties=2, commands=0):
        super(DedicationRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMainRewards(self):
        return self._getArray(0)

    def setMainRewards(self, value):
        self._setArray(0, value)
        return

    def getLevel(self):
        return self._getString(1)

    def setLevel(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(DedicationRewardViewModel, self)._initialize()
        self._addArrayProperty(b'mainRewards', Array())
        self._addStringProperty(b'level', b'')
        return
