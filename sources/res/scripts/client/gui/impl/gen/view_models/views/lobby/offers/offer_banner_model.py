from gui.impl.gen import R
from frameworks.wulf import ViewModel

class OfferBannerModel(ViewModel):
    __slots__ = (b'onSelect', b'onClose')

    def __init__(self, properties=4, commands=2):
        super(OfferBannerModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(OfferBannerModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'icon', b'')
        self.onSelect = self._addCommand(b'onSelect')
        self.onClose = self._addCommand(b'onClose')
        return
