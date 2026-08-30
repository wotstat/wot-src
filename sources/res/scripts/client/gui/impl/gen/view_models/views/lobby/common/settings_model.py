from frameworks.wulf import ViewModel

class SettingsModel(ViewModel):
    __slots__ = (b'onUpdateSetting',)

    def __init__(self, properties=1, commands=1):
        super(SettingsModel, self).__init__(properties=properties, commands=commands)
        return

    def getReadOnly(self):
        return self._getBool(0)

    def setReadOnly(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(SettingsModel, self)._initialize()
        self._addBoolProperty(b'readOnly', False)
        self.onUpdateSetting = self._addCommand(b'onUpdateSetting')
        return
