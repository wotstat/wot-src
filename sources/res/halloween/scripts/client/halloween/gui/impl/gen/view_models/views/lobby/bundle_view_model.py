from enum import Enum
from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.bundle_model import BundleModel

class WindowType(Enum):
    KEYWIDGET = b'keyWidget'
    DECRYPT = b'decrypt'
    SKIP = b'skip'


class TitleStates(Enum):
    DEFAULT = b'default'
    ONLYSHOPBUNDLE = b'onlyShopBundle'
    ONLYKEYSBUNDLE = b'onlyKeysBundle'


class BundleViewModel(ViewModel):
    __slots__ = (b'onClose', b'onPurchase')

    def __init__(self, properties=6, commands=2):
        super(BundleViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLackOfKeys(self):
        return self._getNumber(0)

    def setLackOfKeys(self, value):
        self._setNumber(0, value)
        return

    def getSlide(self):
        return self._getNumber(1)

    def setSlide(self, value):
        self._setNumber(1, value)
        return

    def getWindowType(self):
        return WindowType(self._getString(2))

    def setWindowType(self, value):
        self._setString(2, value.value)
        return

    def getTitleState(self):
        return TitleStates(self._getString(3))

    def setTitleState(self, value):
        self._setString(3, value.value)
        return

    def getBundles(self):
        return self._getArray(4)

    def setBundles(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getBundlesType():
        return BundleModel

    def getGoldCount(self):
        return self._getNumber(5)

    def setGoldCount(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(BundleViewModel, self)._initialize()
        self._addNumberProperty(b'lackOfKeys', 0)
        self._addNumberProperty(b'slide', 0)
        self._addStringProperty(b'windowType')
        self._addStringProperty(b'titleState')
        self._addArrayProperty(b'bundles', Array())
        self._addNumberProperty(b'goldCount', 0)
        self.onClose = self._addCommand(b'onClose')
        self.onPurchase = self._addCommand(b'onPurchase')
        return
