from gui.impl.gen import R
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.specializations_model import SpecializationsModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel

class OptDeviceSlotModel(BaseSlotModel):
    __slots__ = ()

    def __init__(self, properties=31, commands=0):
        super(OptDeviceSlotModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bonuses(self):
        return self._getViewModel(21)

    @staticmethod
    def getBonusesType():
        return BonusesModel

    @property
    def specializations(self):
        return self._getViewModel(22)

    @staticmethod
    def getSpecializationsType():
        return SpecializationsModel

    def getWithDescription(self):
        return self._getBool(23)

    def setWithDescription(self, value):
        self._setBool(23, value)
        return

    def getIsTrophy(self):
        return self._getBool(24)

    def setIsTrophy(self, value):
        self._setBool(24, value)
        return

    def getIsModernized(self):
        return self._getBool(25)

    def setIsModernized(self, value):
        self._setBool(25, value)
        return

    def getIsUpgradable(self):
        return self._getBool(26)

    def setIsUpgradable(self, value):
        self._setBool(26, value)
        return

    def getEffect(self):
        return self._getResource(27)

    def setEffect(self, value):
        self._setResource(27, value)
        return

    def getLevel(self):
        return self._getNumber(28)

    def setLevel(self, value):
        self._setNumber(28, value)
        return

    def getDestroyTooltipBodyPath(self):
        return self._getString(29)

    def setDestroyTooltipBodyPath(self, value):
        self._setString(29, value)
        return

    def getActiveSpecsMask(self):
        return self._getNumber(30)

    def setActiveSpecsMask(self, value):
        self._setNumber(30, value)
        return

    def _initialize(self):
        super(OptDeviceSlotModel, self)._initialize()
        self._addViewModelProperty(b'bonuses', BonusesModel())
        self._addViewModelProperty(b'specializations', SpecializationsModel())
        self._addBoolProperty(b'withDescription', False)
        self._addBoolProperty(b'isTrophy', False)
        self._addBoolProperty(b'isModernized', False)
        self._addBoolProperty(b'isUpgradable', False)
        self._addResourceProperty(b'effect', R.invalid())
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'destroyTooltipBodyPath', b'')
        self._addNumberProperty(b'activeSpecsMask', 0)
        return
