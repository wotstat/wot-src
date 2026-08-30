from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.box_model import BoxModel

class InfoPageModel(ViewModel):
    __slots__ = (b'onShowVideo', b'onShowShop', b'onClose', b'onShowLootList', b'onPreview', b'onChosenCategory')

    def __init__(self, properties=7, commands=6):
        super(InfoPageModel, self).__init__(properties=properties, commands=commands)
        return

    def getEventName(self):
        return self._getString(0)

    def setEventName(self, value):
        self._setString(0, value)
        return

    def getBoxes(self):
        return self._getArray(1)

    def setBoxes(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getBoxesType():
        return BoxModel

    def getChosenCategory(self):
        return self._getString(2)

    def setChosenCategory(self, value):
        self._setString(2, value)
        return

    def getHasVideoButton(self):
        return self._getBool(3)

    def setHasVideoButton(self, value):
        self._setBool(3, value)
        return

    def getHasShopButton(self):
        return self._getBool(4)

    def setHasShopButton(self, value):
        self._setBool(4, value)
        return

    def getHasLootListLink(self):
        return self._getBool(5)

    def setHasLootListLink(self, value):
        self._setBool(5, value)
        return

    def getEventExpireTime(self):
        return self._getNumber(6)

    def setEventExpireTime(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(InfoPageModel, self)._initialize()
        self._addStringProperty(b'eventName', b'')
        self._addArrayProperty(b'boxes', Array())
        self._addStringProperty(b'chosenCategory', b'')
        self._addBoolProperty(b'hasVideoButton', False)
        self._addBoolProperty(b'hasShopButton', False)
        self._addBoolProperty(b'hasLootListLink', False)
        self._addNumberProperty(b'eventExpireTime', 0)
        self.onShowVideo = self._addCommand(b'onShowVideo')
        self.onShowShop = self._addCommand(b'onShowShop')
        self.onClose = self._addCommand(b'onClose')
        self.onShowLootList = self._addCommand(b'onShowLootList')
        self.onPreview = self._addCommand(b'onPreview')
        self.onChosenCategory = self._addCommand(b'onChosenCategory')
        return
