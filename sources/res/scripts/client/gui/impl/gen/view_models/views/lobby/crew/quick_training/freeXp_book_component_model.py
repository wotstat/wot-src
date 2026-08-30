from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel

class FreeXpBookComponentModel(ComponentBaseModel):
    __slots__ = (b'mouseEnter', b'select', b'update', b'manualInput')

    def __init__(self, properties=7, commands=4):
        super(FreeXpBookComponentModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentXpValue(self):
        return self._getNumber(1)

    def setCurrentXpValue(self, value):
        self._setNumber(1, value)
        return

    def getMaxXpValue(self):
        return self._getNumber(2)

    def setMaxXpValue(self, value):
        self._setNumber(2, value)
        return

    def getDiscountSize(self):
        return self._getNumber(3)

    def setDiscountSize(self, value):
        self._setNumber(3, value)
        return

    def getExchangeRate(self):
        return self._getNumber(4)

    def setExchangeRate(self, value):
        self._setNumber(4, value)
        return

    def getIsDisabled(self):
        return self._getBool(5)

    def setIsDisabled(self, value):
        self._setBool(5, value)
        return

    def getHasError(self):
        return self._getBool(6)

    def setHasError(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(FreeXpBookComponentModel, self)._initialize()
        self._addNumberProperty(b'currentXpValue', 0)
        self._addNumberProperty(b'maxXpValue', 0)
        self._addNumberProperty(b'discountSize', 0)
        self._addNumberProperty(b'exchangeRate', 1)
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'hasError', False)
        self.mouseEnter = self._addCommand(b'mouseEnter')
        self.select = self._addCommand(b'select')
        self.update = self._addCommand(b'update')
        self.manualInput = self._addCommand(b'manualInput')
        return
