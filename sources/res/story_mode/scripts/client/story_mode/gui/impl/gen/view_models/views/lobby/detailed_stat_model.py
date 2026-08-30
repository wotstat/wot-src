from frameworks.wulf import ViewModel

class DetailedStatModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DetailedStatModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)
        return

    def getText(self):
        return self._getString(1)

    def setText(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(DetailedStatModel, self)._initialize()
        self._addNumberProperty(b'value', 0)
        self._addStringProperty(b'text', b'')
        return
