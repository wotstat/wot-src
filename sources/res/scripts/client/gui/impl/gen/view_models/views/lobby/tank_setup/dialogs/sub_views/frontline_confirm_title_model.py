from frameworks.wulf import ViewModel

class FrontlineConfirmTitleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(FrontlineConfirmTitleModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(FrontlineConfirmTitleModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        return
