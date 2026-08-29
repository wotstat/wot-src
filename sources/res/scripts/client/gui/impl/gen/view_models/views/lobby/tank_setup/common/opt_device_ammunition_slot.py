from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot
from gui.impl.gen.view_models.views.lobby.tank_setup.common.specializations_model import SpecializationsModel

class OptDeviceAmmunitionSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(OptDeviceAmmunitionSlot, self).__init__(properties=properties, commands=commands)
        return

    @property
    def specializations(self):
        return self._getViewModel(11)

    @staticmethod
    def getSpecializationsType():
        return SpecializationsModel

    def getActiveSpecsMask(self):
        return self._getNumber(12)

    def setActiveSpecsMask(self, value):
        self._setNumber(12, value)
        return

    def getIsIncompatible(self):
        return self._getBool(13)

    def setIsIncompatible(self, value):
        self._setBool(13, value)
        return

    def getLevel(self):
        return self._getNumber(14)

    def setLevel(self, value):
        self._setNumber(14, value)
        return

    def _initialize(self):
        super(OptDeviceAmmunitionSlot, self)._initialize()
        self._addViewModelProperty(b'specializations', SpecializationsModel())
        self._addNumberProperty(b'activeSpecsMask', 0)
        self._addBoolProperty(b'isIncompatible', False)
        self._addNumberProperty(b'level', 0)
        return
