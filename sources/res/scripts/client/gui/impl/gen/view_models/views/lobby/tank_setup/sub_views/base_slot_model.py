from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.specializations_model import SpecializationsModel

class BaseSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=21, commands=0):
        super(BaseSlotModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceModel

    @property
    def specializations(self):
        return self._getViewModel(1)

    @staticmethod
    def getSpecializationsType():
        return SpecializationsModel

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getIntCD(self):
        return self._getNumber(3)

    def setIntCD(self, value):
        self._setNumber(3, value)
        return

    def getImageName(self):
        return self._getString(4)

    def setImageName(self, value):
        self._setString(4, value)
        return

    def getItemsInStorage(self):
        return self._getNumber(5)

    def setItemsInStorage(self, value):
        self._setNumber(5, value)
        return

    def getItemsInVehicle(self):
        return self._getNumber(6)

    def setItemsInVehicle(self, value):
        self._setNumber(6, value)
        return

    def getItemTypeID(self):
        return self._getNumber(7)

    def setItemTypeID(self, value):
        self._setNumber(7, value)
        return

    def getIsMounted(self):
        return self._getBool(8)

    def setIsMounted(self, value):
        self._setBool(8, value)
        return

    def getIsMountedMoreThanOne(self):
        return self._getBool(9)

    def setIsMountedMoreThanOne(self, value):
        self._setBool(9, value)
        return

    def getIsMountedInOtherSetup(self):
        return self._getBool(10)

    def setIsMountedInOtherSetup(self, value):
        self._setBool(10, value)
        return

    def getIsDisabled(self):
        return self._getBool(11)

    def setIsDisabled(self, value):
        self._setBool(11, value)
        return

    def getIsVisible(self):
        return self._getBool(12)

    def setIsVisible(self, value):
        self._setBool(12, value)
        return

    def getInstalledSlotId(self):
        return self._getNumber(13)

    def setInstalledSlotId(self, value):
        self._setNumber(13, value)
        return

    def getItemInstalledSetupIdx(self):
        return self._getNumber(14)

    def setItemInstalledSetupIdx(self, value):
        self._setNumber(14, value)
        return

    def getItemInstalledSetupSlotIdx(self):
        return self._getNumber(15)

    def setItemInstalledSetupSlotIdx(self, value):
        self._setNumber(15, value)
        return

    def getIsLocked(self):
        return self._getBool(16)

    def setIsLocked(self, value):
        self._setBool(16, value)
        return

    def getIsFreeToDemount(self):
        return self._getBool(17)

    def setIsFreeToDemount(self, value):
        self._setBool(17, value)
        return

    def getLockReason(self):
        return self._getString(18)

    def setLockReason(self, value):
        self._setString(18, value)
        return

    def getOverlayType(self):
        return self._getString(19)

    def setOverlayType(self, value):
        self._setString(19, value)
        return

    def getHighlightType(self):
        return self._getString(20)

    def setHighlightType(self, value):
        self._setString(20, value)
        return

    def _initialize(self):
        super(BaseSlotModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addViewModelProperty(b'specializations', SpecializationsModel())
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'intCD', 0)
        self._addStringProperty(b'imageName', b'')
        self._addNumberProperty(b'itemsInStorage', 0)
        self._addNumberProperty(b'itemsInVehicle', 0)
        self._addNumberProperty(b'itemTypeID', 0)
        self._addBoolProperty(b'isMounted', False)
        self._addBoolProperty(b'isMountedMoreThanOne', False)
        self._addBoolProperty(b'isMountedInOtherSetup', False)
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'isVisible', True)
        self._addNumberProperty(b'installedSlotId', -1)
        self._addNumberProperty(b'itemInstalledSetupIdx', -1)
        self._addNumberProperty(b'itemInstalledSetupSlotIdx', -1)
        self._addBoolProperty(b'isLocked', False)
        self._addBoolProperty(b'isFreeToDemount', False)
        self._addStringProperty(b'lockReason', b'')
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'highlightType', b'')
        return
