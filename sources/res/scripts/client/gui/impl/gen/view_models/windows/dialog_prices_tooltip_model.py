from gui.impl.gen import R
from frameworks.wulf import ViewModel

class DialogPricesTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(DialogPricesTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getValueMainCost(self):
        return self._getString(0)

    def setValueMainCost(self, value):
        self._setString(0, value)
        return

    def getIconMainCost(self):
        return self._getResource(1)

    def setIconMainCost(self, value):
        self._setResource(1, value)
        return

    def getLabelMainCost(self):
        return self._getResource(2)

    def setLabelMainCost(self, value):
        self._setResource(2, value)
        return

    def getValueAdditionalCost(self):
        return self._getString(3)

    def setValueAdditionalCost(self, value):
        self._setString(3, value)
        return

    def getIconAdditionalCost(self):
        return self._getResource(4)

    def setIconAdditionalCost(self, value):
        self._setResource(4, value)
        return

    def getLabelAdditionalCost(self):
        return self._getResource(5)

    def setLabelAdditionalCost(self, value):
        self._setResource(5, value)
        return

    def getTotalCost(self):
        return self._getString(6)

    def setTotalCost(self, value):
        self._setString(6, value)
        return

    def getLabelTotalCost(self):
        return self._getResource(7)

    def setLabelTotalCost(self, value):
        self._setResource(7, value)
        return

    def _initialize(self):
        super(DialogPricesTooltipModel, self)._initialize()
        self._addStringProperty(b'valueMainCost', b'0')
        self._addResourceProperty(b'iconMainCost', R.invalid())
        self._addResourceProperty(b'labelMainCost', R.invalid())
        self._addStringProperty(b'valueAdditionalCost', b'0')
        self._addResourceProperty(b'iconAdditionalCost', R.invalid())
        self._addResourceProperty(b'labelAdditionalCost', R.invalid())
        self._addStringProperty(b'totalCost', b'0')
        self._addResourceProperty(b'labelTotalCost', R.invalid())
        return
