from frameworks.wulf import ViewModel

class GfDropDownItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(GfDropDownItem, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getLabel(self):
        return self._getString(1)

    def setLabel(self, value):
        self._setString(1, value)
        return

    def getIsDisabled(self):
        return self._getBool(2)

    def setIsDisabled(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(GfDropDownItem, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'label', b'')
        self._addBoolProperty(b'isDisabled', False)
        return
