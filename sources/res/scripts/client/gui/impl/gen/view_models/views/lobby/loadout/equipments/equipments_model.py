from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.loadout.base_loadout_model import BaseLoadoutModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.opt_device_slot_model import OptDeviceSlotModel

class EquipmentsModel(BaseLoadoutModel):
    __slots__ = (b'onGetMoreCurrency',)

    def __init__(self, properties=8, commands=2):
        super(EquipmentsModel, self).__init__(properties=properties, commands=commands)
        return

    def getEquipCoinCount(self):
        return self._getNumber(1)

    def setEquipCoinCount(self, value):
        self._setNumber(1, value)
        return

    def getHasChanges(self):
        return self._getBool(2)

    def setHasChanges(self, value):
        self._setBool(2, value)
        return

    def getSimpleEquipments(self):
        return self._getArray(3)

    def setSimpleEquipments(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getSimpleEquipmentsType():
        return OptDeviceSlotModel

    def getDeluxEquipments(self):
        return self._getArray(4)

    def setDeluxEquipments(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getDeluxEquipmentsType():
        return OptDeviceSlotModel

    def getTrophyEquipments(self):
        return self._getArray(5)

    def setTrophyEquipments(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getTrophyEquipmentsType():
        return OptDeviceSlotModel

    def getModernizedEquipments(self):
        return self._getArray(6)

    def setModernizedEquipments(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getModernizedEquipmentsType():
        return OptDeviceSlotModel

    def getHasModernizedEquipmentToDisassemble(self):
        return self._getBool(7)

    def setHasModernizedEquipmentToDisassemble(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(EquipmentsModel, self)._initialize()
        self._addNumberProperty(b'equipCoinCount', 0)
        self._addBoolProperty(b'hasChanges', False)
        self._addArrayProperty(b'simpleEquipments', Array())
        self._addArrayProperty(b'deluxEquipments', Array())
        self._addArrayProperty(b'trophyEquipments', Array())
        self._addArrayProperty(b'modernizedEquipments', Array())
        self._addBoolProperty(b'hasModernizedEquipmentToDisassemble', False)
        self.onGetMoreCurrency = self._addCommand(b'onGetMoreCurrency')
        return
