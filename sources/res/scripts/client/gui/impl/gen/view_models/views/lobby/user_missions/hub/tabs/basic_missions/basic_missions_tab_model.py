from frameworks.wulf import ViewModel

class BasicMissionsTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BasicMissionsTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsDailySectionAvailable(self):
        return self._getBool(0)

    def setIsDailySectionAvailable(self, value):
        self._setBool(0, value)
        return

    def getIsWeeklySectionAvailable(self):
        return self._getBool(1)

    def setIsWeeklySectionAvailable(self, value):
        self._setBool(1, value)
        return

    def getIsPMSectionAvailable(self):
        return self._getBool(2)

    def setIsPMSectionAvailable(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(BasicMissionsTabModel, self)._initialize()
        self._addBoolProperty(b'isDailySectionAvailable', False)
        self._addBoolProperty(b'isWeeklySectionAvailable', False)
        self._addBoolProperty(b'isPMSectionAvailable', False)
        return
