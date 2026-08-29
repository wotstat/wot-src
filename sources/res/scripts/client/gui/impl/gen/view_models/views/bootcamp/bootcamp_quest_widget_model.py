from frameworks.wulf import ViewModel

class BootcampQuestWidgetModel(ViewModel):
    __slots__ = (b'onQuestClick',)

    def __init__(self, properties=3, commands=1):
        super(BootcampQuestWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrent(self):
        return self._getNumber(0)

    def setCurrent(self, value):
        self._setNumber(0, value)
        return

    def getTotal(self):
        return self._getNumber(1)

    def setTotal(self, value):
        self._setNumber(1, value)
        return

    def getTooltipId(self):
        return self._getNumber(2)

    def setTooltipId(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(BootcampQuestWidgetModel, self)._initialize()
        self._addNumberProperty(b'current', 0)
        self._addNumberProperty(b'total', 0)
        self._addNumberProperty(b'tooltipId', 0)
        self.onQuestClick = self._addCommand(b'onQuestClick')
        return
