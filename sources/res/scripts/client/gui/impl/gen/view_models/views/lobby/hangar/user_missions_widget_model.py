from frameworks.wulf import ViewModel

class UserMissionsWidgetModel(ViewModel):
    __slots__ = (b'onPresenterDisappear', b'onWidgetUnmounted')

    def __init__(self, properties=3, commands=2):
        super(UserMissionsWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsBattlePassActive(self):
        return self._getBool(0)

    def setIsBattlePassActive(self, value):
        self._setBool(0, value)
        return

    def getIsAnyEntryPointAvailable(self):
        return self._getBool(1)

    def setIsAnyEntryPointAvailable(self, value):
        self._setBool(1, value)
        return

    def getAreMissionsActive(self):
        return self._getBool(2)

    def setAreMissionsActive(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(UserMissionsWidgetModel, self)._initialize()
        self._addBoolProperty(b'isBattlePassActive', False)
        self._addBoolProperty(b'isAnyEntryPointAvailable', False)
        self._addBoolProperty(b'areMissionsActive', True)
        self.onPresenterDisappear = self._addCommand(b'onPresenterDisappear')
        self.onWidgetUnmounted = self._addCommand(b'onWidgetUnmounted')
        return
