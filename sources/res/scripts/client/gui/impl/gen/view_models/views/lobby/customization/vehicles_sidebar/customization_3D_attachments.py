from frameworks.wulf import ViewModel

class Customization3DAttachments(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(Customization3DAttachments, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(Customization3DAttachments, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'amount', 0)
        return
