from gui.impl.gen import R
from frameworks.wulf import ViewModel

class FragmentItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FragmentItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def getFragmentCD(self):
        return self._getNumber(2)

    def setFragmentCD(self, value):
        self._setNumber(2, value)
        return

    def getSpecialIcon(self):
        return self._getResource(3)

    def setSpecialIcon(self, value):
        self._setResource(3, value)
        return

    def _initialize(self):
        super(FragmentItemModel, self)._initialize()
        self._addStringProperty(b'value', b'--')
        self._addResourceProperty(b'icon', R.invalid())
        self._addNumberProperty(b'fragmentCD', 0)
        self._addResourceProperty(b'specialIcon', R.invalid())
        return
