from frameworks.wulf import ViewModel

class SerialEnterTabViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SerialEnterTabViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getIsCompleted(self):
        return self._getBool(1)

    def setIsCompleted(self, value):
        self._setBool(1, value)
        return

    def getIsViewed(self):
        return self._getBool(2)

    def setIsViewed(self, value):
        self._setBool(2, value)
        return

    def getIsFinal(self):
        return self._getBool(3)

    def setIsFinal(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(SerialEnterTabViewModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', False)
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isViewed', False)
        self._addBoolProperty(b'isFinal', False)
        return
