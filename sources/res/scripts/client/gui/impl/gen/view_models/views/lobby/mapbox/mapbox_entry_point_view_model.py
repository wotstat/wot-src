from frameworks.wulf import ViewModel

class MapboxEntryPointViewModel(ViewModel):
    __slots__ = (b'onActionClick',)

    def __init__(self, properties=1, commands=1):
        super(MapboxEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEndDate(self):
        return self._getNumber(0)

    def setEndDate(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(MapboxEntryPointViewModel, self)._initialize()
        self._addNumberProperty(b'endDate', -1)
        self.onActionClick = self._addCommand(b'onActionClick')
        return
