from gui.impl.gen.view_models.views.lobby.crew.common.button_model import ButtonModel

class CrewBooksButtonModel(ButtonModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CrewBooksButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getTotalAmount(self):
        return self._getNumber(1)

    def setTotalAmount(self, value):
        self._setNumber(1, value)
        return

    def getNewAmount(self):
        return self._getString(2)

    def setNewAmount(self, value):
        self._setString(2, value)
        return

    def getHasDiscount(self):
        return self._getBool(3)

    def setHasDiscount(self, value):
        self._setBool(3, value)
        return

    def getIsDisabled(self):
        return self._getBool(4)

    def setIsDisabled(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(CrewBooksButtonModel, self)._initialize()
        self._addNumberProperty(b'totalAmount', 0)
        self._addStringProperty(b'newAmount', b'')
        self._addBoolProperty(b'hasDiscount', False)
        self._addBoolProperty(b'isDisabled', False)
        return
