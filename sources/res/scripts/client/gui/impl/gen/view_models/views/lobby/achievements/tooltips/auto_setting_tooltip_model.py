from frameworks.wulf import ViewModel

class AutoSettingTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(AutoSettingTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsSwitchedOn(self):
        return self._getBool(0)

    def setIsSwitchedOn(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(AutoSettingTooltipModel, self)._initialize()
        self._addBoolProperty(b'isSwitchedOn', False)
        return
