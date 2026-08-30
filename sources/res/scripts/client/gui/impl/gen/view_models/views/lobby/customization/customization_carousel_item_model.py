from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class CustomizationCarouselItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=46, commands=0):
        super(CustomizationCarouselItemModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def buyPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getBuyPriceType():
        return PriceModel

    def getIsFilled(self):
        return self._getBool(1)

    def setIsFilled(self, value):
        self._setBool(1, value)
        return

    def getTypeId(self):
        return self._getNumber(2)

    def setTypeId(self, value):
        self._setNumber(2, value)
        return

    def getImageCached(self):
        return self._getBool(3)

    def setImageCached(self, value):
        self._setBool(3, value)
        return

    def getAutoRentEnabled(self):
        return self._getBool(4)

    def setAutoRentEnabled(self, value):
        self._setBool(4, value)
        return

    def getCustomizationDisplayType(self):
        return self._getNumber(5)

    def setCustomizationDisplayType(self, value):
        self._setNumber(5, value)
        return

    def getDefaultIconAlpha(self):
        return self._getReal(6)

    def setDefaultIconAlpha(self, value):
        self._setReal(6, value)
        return

    def getShowAlert(self):
        return self._getBool(7)

    def setShowAlert(self, value):
        self._setBool(7, value)
        return

    def getRentalInfoText(self):
        return self._getString(8)

    def setRentalInfoText(self, value):
        self._setString(8, value)
        return

    def getEditBtnEnabled(self):
        return self._getBool(9)

    def setEditBtnEnabled(self, value):
        self._setBool(9, value)
        return

    def getShowDetailItems(self):
        return self._getBool(10)

    def setShowDetailItems(self, value):
        self._setBool(10, value)
        return

    def getIsNew(self):
        return self._getBool(11)

    def setIsNew(self, value):
        self._setBool(11, value)
        return

    def getIsLinked(self):
        return self._getBool(12)

    def setIsLinked(self, value):
        self._setBool(12, value)
        return

    def getIsDarked(self):
        return self._getBool(13)

    def setIsDarked(self, value):
        self._setBool(13, value)
        return

    def getLockText(self):
        return self._getString(14)

    def setLockText(self, value):
        self._setString(14, value)
        return

    def getEditableIcon(self):
        return self._getString(15)

    def setEditableIcon(self, value):
        self._setString(15, value)
        return

    def getScale(self):
        return self._getNumber(16)

    def setScale(self, value):
        self._setNumber(16, value)
        return

    def getBuyOperationAllowed(self):
        return self._getBool(17)

    def setBuyOperationAllowed(self, value):
        self._setBool(17, value)
        return

    def getIsUnsuitable(self):
        return self._getBool(18)

    def setIsUnsuitable(self, value):
        self._setBool(18, value)
        return

    def getIsSpecial(self):
        return self._getBool(19)

    def setIsSpecial(self, value):
        self._setBool(19, value)
        return

    def getIsInProgress(self):
        return self._getBool(20)

    def setIsInProgress(self, value):
        self._setBool(20, value)
        return

    def getIsWide(self):
        return self._getBool(21)

    def setIsWide(self, value):
        self._setBool(21, value)
        return

    def getIsEquipped(self):
        return self._getBool(22)

    def setIsEquipped(self, value):
        self._setBool(22, value)
        return

    def getIcon(self):
        return self._getString(23)

    def setIcon(self, value):
        self._setString(23, value)
        return

    def getShowEditableHint(self):
        return self._getBool(24)

    def setShowEditableHint(self, value):
        self._setBool(24, value)
        return

    def getFormFactor(self):
        return self._getNumber(25)

    def setFormFactor(self, value):
        self._setNumber(25, value)
        return

    def getIsChained(self):
        return self._getBool(26)

    def setIsChained(self, value):
        self._setBool(26, value)
        return

    def getNoveltyCounter(self):
        return self._getNumber(27)

    def setNoveltyCounter(self, value):
        self._setNumber(27, value)
        return

    def getLocked(self):
        return self._getBool(28)

    def setLocked(self, value):
        self._setBool(28, value)
        return

    def getIsWithSerialNumber(self):
        return self._getBool(29)

    def setIsWithSerialNumber(self, value):
        self._setBool(29, value)
        return

    def getIntCD(self):
        return self._getNumber(30)

    def setIntCD(self, value):
        self._setNumber(30, value)
        return

    def getIsRental(self):
        return self._getBool(31)

    def setIsRental(self, value):
        self._setBool(31, value)
        return

    def getTooltip(self):
        return self._getString(32)

    def setTooltip(self, value):
        self._setString(32, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(33)

    def setProgressionLevel(self, value):
        self._setNumber(33, value)
        return

    def getShowRareIcon(self):
        return self._getBool(34)

    def setShowRareIcon(self, value):
        self._setBool(34, value)
        return

    def getIsAllSeasons(self):
        return self._getBool(35)

    def setIsAllSeasons(self, value):
        self._setBool(35, value)
        return

    def getEditNoveltyCounter(self):
        return self._getNumber(36)

    def setEditNoveltyCounter(self, value):
        self._setNumber(36, value)
        return

    def getShowEditBtnHint(self):
        return self._getBool(37)

    def setShowEditBtnHint(self, value):
        self._setBool(37, value)
        return

    def getIsAlreadyUsed(self):
        return self._getBool(38)

    def setIsAlreadyUsed(self, value):
        self._setBool(38, value)
        return

    def getIsDim(self):
        return self._getBool(39)

    def setIsDim(self, value):
        self._setBool(39, value)
        return

    def getFormIconSource(self):
        return self._getString(40)

    def setFormIconSource(self, value):
        self._setString(40, value)
        return

    def getIsProgressionRewindEnabled(self):
        return self._getBool(41)

    def setIsProgressionRewindEnabled(self, value):
        self._setBool(41, value)
        return

    def getIsMainType(self):
        return self._getBool(42)

    def setIsMainType(self, value):
        self._setBool(42, value)
        return

    def getQuantity(self):
        return self._getNumber(43)

    def setQuantity(self, value):
        self._setNumber(43, value)
        return

    def getExtraName(self):
        return self._getString(44)

    def setExtraName(self, value):
        self._setString(44, value)
        return

    def getIsSelected(self):
        return self._getBool(45)

    def setIsSelected(self, value):
        self._setBool(45, value)
        return

    def _initialize(self):
        super(CustomizationCarouselItemModel, self)._initialize()
        self._addViewModelProperty(b'buyPrice', PriceModel())
        self._addBoolProperty(b'isFilled', False)
        self._addNumberProperty(b'typeId', 0)
        self._addBoolProperty(b'imageCached', False)
        self._addBoolProperty(b'autoRentEnabled', False)
        self._addNumberProperty(b'customizationDisplayType', 0)
        self._addRealProperty(b'defaultIconAlpha', 0.0)
        self._addBoolProperty(b'showAlert', False)
        self._addStringProperty(b'rentalInfoText', b'')
        self._addBoolProperty(b'editBtnEnabled', False)
        self._addBoolProperty(b'showDetailItems', False)
        self._addBoolProperty(b'isNew', False)
        self._addBoolProperty(b'isLinked', False)
        self._addBoolProperty(b'isDarked', False)
        self._addStringProperty(b'lockText', b'')
        self._addStringProperty(b'editableIcon', b'')
        self._addNumberProperty(b'scale', 0)
        self._addBoolProperty(b'buyOperationAllowed', False)
        self._addBoolProperty(b'isUnsuitable', False)
        self._addBoolProperty(b'isSpecial', False)
        self._addBoolProperty(b'isInProgress', False)
        self._addBoolProperty(b'isWide', False)
        self._addBoolProperty(b'isEquipped', False)
        self._addStringProperty(b'icon', b'')
        self._addBoolProperty(b'showEditableHint', False)
        self._addNumberProperty(b'formFactor', 0)
        self._addBoolProperty(b'isChained', False)
        self._addNumberProperty(b'noveltyCounter', 0)
        self._addBoolProperty(b'locked', False)
        self._addBoolProperty(b'isWithSerialNumber', False)
        self._addNumberProperty(b'intCD', 0)
        self._addBoolProperty(b'isRental', False)
        self._addStringProperty(b'tooltip', b'')
        self._addNumberProperty(b'progressionLevel', 0)
        self._addBoolProperty(b'showRareIcon', False)
        self._addBoolProperty(b'isAllSeasons', False)
        self._addNumberProperty(b'editNoveltyCounter', 0)
        self._addBoolProperty(b'showEditBtnHint', False)
        self._addBoolProperty(b'isAlreadyUsed', False)
        self._addBoolProperty(b'isDim', False)
        self._addStringProperty(b'formIconSource', b'')
        self._addBoolProperty(b'isProgressionRewindEnabled', False)
        self._addBoolProperty(b'isMainType', False)
        self._addNumberProperty(b'quantity', 0)
        self._addStringProperty(b'extraName', b'')
        self._addBoolProperty(b'isSelected', False)
        return
