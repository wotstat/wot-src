from frameworks.wulf import ViewModel

class BoxInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BoxInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getBoxCategory(self):
        return self._getString(0)

    def setBoxCategory(self, value):
        self._setString(0, value)
        return

    def getBoxesCount(self):
        return self._getNumber(1)

    def setBoxesCount(self, value):
        self._setNumber(1, value)
        return

    def getBoxesCountToGuaranteed(self):
        return self._getNumber(2)

    def setBoxesCountToGuaranteed(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(BoxInfoModel, self)._initialize()
        self._addStringProperty(b'boxCategory', b'')
        self._addNumberProperty(b'boxesCount', 0)
        self._addNumberProperty(b'boxesCountToGuaranteed', 0)
        return
