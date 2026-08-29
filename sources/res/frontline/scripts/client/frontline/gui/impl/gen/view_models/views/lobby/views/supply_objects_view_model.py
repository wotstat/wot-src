from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.supply_objects_model import SupplyObjectsModel
from frontline.gui.impl.gen.view_models.views.lobby.views.supply_params_model import SupplyParamsModel

class SupplyObjectsViewModel(ViewModel):
    __slots__ = (b'onSupplySelected', b'onClose')

    def __init__(self, properties=6, commands=2):
        super(SupplyObjectsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFullScreen(self):
        return self._getBool(0)

    def setIsFullScreen(self, value):
        self._setBool(0, value)
        return

    def getSupplyTeam(self):
        return self._getNumber(1)

    def setSupplyTeam(self, value):
        self._setNumber(1, value)
        return

    def getSupplyHullDamageFactor(self):
        return self._getReal(2)

    def setSupplyHullDamageFactor(self, value):
        self._setReal(2, value)
        return

    def getSupplyTurretDamageFactor(self):
        return self._getReal(3)

    def setSupplyTurretDamageFactor(self, value):
        self._setReal(3, value)
        return

    def getSupplyObjects(self):
        return self._getArray(4)

    def setSupplyObjects(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getSupplyObjectsType():
        return SupplyObjectsModel

    def getSupplyParams(self):
        return self._getArray(5)

    def setSupplyParams(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getSupplyParamsType():
        return SupplyParamsModel

    def _initialize(self):
        super(SupplyObjectsViewModel, self)._initialize()
        self._addBoolProperty(b'isFullScreen', False)
        self._addNumberProperty(b'supplyTeam', 0)
        self._addRealProperty(b'supplyHullDamageFactor', 0.0)
        self._addRealProperty(b'supplyTurretDamageFactor', 0.0)
        self._addArrayProperty(b'supplyObjects', Array())
        self._addArrayProperty(b'supplyParams', Array())
        self.onSupplySelected = self._addCommand(b'onSupplySelected')
        self.onClose = self._addCommand(b'onClose')
        return
