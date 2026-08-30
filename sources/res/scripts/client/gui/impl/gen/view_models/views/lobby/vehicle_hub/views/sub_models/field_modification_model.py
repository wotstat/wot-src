from frameworks.wulf import ViewModel

class FieldModificationModel(ViewModel):
    __slots__ = (b'onVehiclePostProgression',)
    HIDDEN = 0
    LOCKED = 1
    UNLOCKED = 2

    def __init__(self, properties=2, commands=1):
        super(FieldModificationModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getNumber(0)

    def setState(self, value):
        self._setNumber(0, value)
        return

    def getCounter(self):
        return self._getNumber(1)

    def setCounter(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(FieldModificationModel, self)._initialize()
        self._addNumberProperty(b'state', 0)
        self._addNumberProperty(b'counter', 0)
        self.onVehiclePostProgression = self._addCommand(b'onVehiclePostProgression')
        return
