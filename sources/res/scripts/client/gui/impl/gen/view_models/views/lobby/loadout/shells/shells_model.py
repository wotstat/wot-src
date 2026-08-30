from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.loadout.base_loadout_model import BaseLoadoutModel
from gui.impl.gen.view_models.views.lobby.loadout.shells.shell_model import ShellModel

class ShellsModel(BaseLoadoutModel):
    __slots__ = (b'onShellUpdate',)

    def __init__(self, properties=7, commands=2):
        super(ShellsModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasChanges(self):
        return self._getBool(1)

    def setHasChanges(self, value):
        self._setBool(1, value)
        return

    def getAmmoMaxSize(self):
        return self._getNumber(2)

    def setAmmoMaxSize(self, value):
        self._setNumber(2, value)
        return

    def getInstalledCount(self):
        return self._getNumber(3)

    def setInstalledCount(self, value):
        self._setNumber(3, value)
        return

    def getClip(self):
        return self._getNumber(4)

    def setClip(self, value):
        self._setNumber(4, value)
        return

    def getAutoloadEnabled(self):
        return self._getBool(5)

    def setAutoloadEnabled(self, value):
        self._setBool(5, value)
        return

    def getShells(self):
        return self._getArray(6)

    def setShells(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getShellsType():
        return ShellModel

    def _initialize(self):
        super(ShellsModel, self)._initialize()
        self._addBoolProperty(b'hasChanges', False)
        self._addNumberProperty(b'ammoMaxSize', 0)
        self._addNumberProperty(b'installedCount', 0)
        self._addNumberProperty(b'clip', 0)
        self._addBoolProperty(b'autoloadEnabled', False)
        self._addArrayProperty(b'shells', Array())
        self.onShellUpdate = self._addCommand(b'onShellUpdate')
        return
