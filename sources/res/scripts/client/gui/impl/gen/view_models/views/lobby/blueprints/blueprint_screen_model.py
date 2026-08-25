from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_price_content_model import BlueprintPriceContentModel

class BlueprintScreenModel(ViewModel):
    __slots__ = (b'onGoToConversionScreen', b'onClose', b'onResearchVehicle', b'onGoToAllConversion', b'onSubmitUnavailableConfirm', b'onOpenVehicleViewBtnClicked')
    INIT = 0
    UPDATE = 1

    def __init__(self, properties=25, commands=6):
        super(BlueprintScreenModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def conversionMaxCost(self):
        return self._getViewModel(0)

    @staticmethod
    def getConversionMaxCostType():
        return BlueprintPriceContentModel

    def getVehicleName(self):
        return self._getString(1)

    def setVehicleName(self, value):
        self._setString(1, value)
        return

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)
        return

    def getVehicleLevel(self):
        return self._getString(3)

    def setVehicleLevel(self, value):
        self._setString(3, value)
        return

    def getIsElite(self):
        return self._getBool(4)

    def setIsElite(self, value):
        self._setBool(4, value)
        return

    def getSchemeCols(self):
        return self._getNumber(5)

    def setSchemeCols(self, value):
        self._setNumber(5, value)
        return

    def getSchemeRows(self):
        return self._getNumber(6)

    def setSchemeRows(self, value):
        self._setNumber(6, value)
        return

    def getIsUnlocked(self):
        return self._getBool(7)

    def setIsUnlocked(self, value):
        self._setBool(7, value)
        return

    def getIsAvailableForUnlock(self):
        return self._getBool(8)

    def setIsAvailableForUnlock(self, value):
        self._setBool(8, value)
        return

    def getNeedXpToUnlock(self):
        return self._getBool(9)

    def setNeedXpToUnlock(self, value):
        self._setBool(9, value)
        return

    def getConversionAvailable(self):
        return self._getBool(10)

    def setConversionAvailable(self, value):
        self._setBool(10, value)
        return

    def getSchemeItems(self):
        return self._getArray(11)

    def setSchemeItems(self, value):
        self._setArray(11, value)
        return

    def getFilledCount(self):
        return self._getNumber(12)

    def setFilledCount(self, value):
        self._setNumber(12, value)
        return

    def getIsSchemeFullCompleted(self):
        return self._getBool(13)

    def setIsSchemeFullCompleted(self, value):
        self._setBool(13, value)
        return

    def getIsPurchased(self):
        return self._getBool(14)

    def setIsPurchased(self, value):
        self._setBool(14, value)
        return

    def getCost(self):
        return self._getString(15)

    def setCost(self, value):
        self._setString(15, value)
        return

    def getDiscount(self):
        return self._getNumber(16)

    def setDiscount(self, value):
        self._setNumber(16, value)
        return

    def getDiscountAbs(self):
        return self._getString(17)

    def setDiscountAbs(self, value):
        self._setString(17, value)
        return

    def getBackBtnLabel(self):
        return self._getString(18)

    def setBackBtnLabel(self, value):
        self._setString(18, value)
        return

    def getMaxConvertibleFragmentCount(self):
        return self._getNumber(19)

    def setMaxConvertibleFragmentCount(self, value):
        self._setNumber(19, value)
        return

    def getShowUnavailableConfirm(self):
        return self._getBool(20)

    def setShowUnavailableConfirm(self, value):
        self._setBool(20, value)
        return

    def getBlueprintAnimPaused(self):
        return self._getBool(21)

    def setBlueprintAnimPaused(self, value):
        self._setBool(21, value)
        return

    def getCurrentStateView(self):
        return self._getNumber(22)

    def setCurrentStateView(self, value):
        self._setNumber(22, value)
        return

    def getReceivedCount(self):
        return self._getNumber(23)

    def setReceivedCount(self, value):
        self._setNumber(23, value)
        return

    def getShowBlueprintInfotypeIcon(self):
        return self._getBool(24)

    def setShowBlueprintInfotypeIcon(self, value):
        self._setBool(24, value)
        return

    def _initialize(self):
        super(BlueprintScreenModel, self)._initialize()
        self._addViewModelProperty(b'conversionMaxCost', BlueprintPriceContentModel())
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleLevel', b'')
        self._addBoolProperty(b'isElite', False)
        self._addNumberProperty(b'schemeCols', 1)
        self._addNumberProperty(b'schemeRows', 1)
        self._addBoolProperty(b'isUnlocked', False)
        self._addBoolProperty(b'isAvailableForUnlock', False)
        self._addBoolProperty(b'needXpToUnlock', True)
        self._addBoolProperty(b'conversionAvailable', False)
        self._addArrayProperty(b'schemeItems', Array())
        self._addNumberProperty(b'filledCount', 0)
        self._addBoolProperty(b'isSchemeFullCompleted', False)
        self._addBoolProperty(b'isPurchased', False)
        self._addStringProperty(b'cost', b'')
        self._addNumberProperty(b'discount', 0)
        self._addStringProperty(b'discountAbs', b'0')
        self._addStringProperty(b'backBtnLabel', b'')
        self._addNumberProperty(b'maxConvertibleFragmentCount', 0)
        self._addBoolProperty(b'showUnavailableConfirm', False)
        self._addBoolProperty(b'blueprintAnimPaused', False)
        self._addNumberProperty(b'currentStateView', -1)
        self._addNumberProperty(b'receivedCount', 0)
        self._addBoolProperty(b'showBlueprintInfotypeIcon', False)
        self.onGoToConversionScreen = self._addCommand(b'onGoToConversionScreen')
        self.onClose = self._addCommand(b'onClose')
        self.onResearchVehicle = self._addCommand(b'onResearchVehicle')
        self.onGoToAllConversion = self._addCommand(b'onGoToAllConversion')
        self.onSubmitUnavailableConfirm = self._addCommand(b'onSubmitUnavailableConfirm')
        self.onOpenVehicleViewBtnClicked = self._addCommand(b'onOpenVehicleViewBtnClicked')
        return
