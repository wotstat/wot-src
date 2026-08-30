from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shell_mechanic_column_config_model import ShellMechanicColumnConfigModel

class ShellMechanicSubtypesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ShellMechanicSubtypesModel, self).__init__(properties=properties, commands=commands)
        return

    def getMechanic(self):
        return self._getString(0)

    def setMechanic(self, value):
        self._setString(0, value)
        return

    def getColumnConfigs(self):
        return self._getArray(1)

    def setColumnConfigs(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getColumnConfigsType():
        return ShellMechanicColumnConfigModel

    def _initialize(self):
        super(ShellMechanicSubtypesModel, self)._initialize()
        self._addStringProperty(b'mechanic', b'')
        self._addArrayProperty(b'columnConfigs', Array())
        return
