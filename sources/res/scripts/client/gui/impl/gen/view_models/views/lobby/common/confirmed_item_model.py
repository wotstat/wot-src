from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class ConfirmedItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ConfirmedItemModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def demountPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getDemountPriceType():
        return PriceModel

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getImageSource(self):
        return self._getResource(2)

    def setImageSource(self, value):
        self._setResource(2, value)
        return

    def getOverlayType(self):
        return self._getString(3)

    def setOverlayType(self, value):
        self._setString(3, value)
        return

    def getHighlightType(self):
        return self._getString(4)

    def setHighlightType(self, value):
        self._setString(4, value)
        return

    def getOptItemDescKey(self):
        return self._getString(5)

    def setOptItemDescKey(self, value):
        self._setString(5, value)
        return

    def getLevel(self):
        return self._getNumber(6)

    def setLevel(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(ConfirmedItemModel, self)._initialize()
        self._addViewModelProperty(b'demountPrice', PriceModel())
        self._addStringProperty(b'name', b'')
        self._addResourceProperty(b'imageSource', R.invalid())
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'highlightType', b'')
        self._addStringProperty(b'optItemDescKey', b'')
        self._addNumberProperty(b'level', 0)
        return
