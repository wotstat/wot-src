from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shell_slot_model import ShellSlotModel

class ShellsSetupModel(BaseSetupModel):
    __slots__ = (b'onShellUpdate',)

    def __init__(self, properties=10, commands=8):
        super(ShellsSetupModel, self).__init__(properties=properties, commands=commands)
        return

    def getShellsTempString(self):
        return self._getString(5)

    def setShellsTempString(self, value):
        self._setString(5, value)
        return

    def getInstalledCount(self):
        return self._getNumber(6)

    def setInstalledCount(self, value):
        self._setNumber(6, value)
        return

    def getMaxCount(self):
        return self._getNumber(7)

    def setMaxCount(self, value):
        self._setNumber(7, value)
        return

    def getClipCount(self):
        return self._getNumber(8)

    def setClipCount(self, value):
        self._setNumber(8, value)
        return

    def getSlots(self):
        return self._getArray(9)

    def setSlots(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getSlotsType():
        return ShellSlotModel

    def _initialize(self):
        super(ShellsSetupModel, self)._initialize()
        self._addStringProperty(b'shellsTempString', b'')
        self._addNumberProperty(b'installedCount', 0)
        self._addNumberProperty(b'maxCount', 0)
        self._addNumberProperty(b'clipCount', 1)
        self._addArrayProperty(b'slots', Array())
        self.onShellUpdate = self._addCommand(b'onShellUpdate')
        return
