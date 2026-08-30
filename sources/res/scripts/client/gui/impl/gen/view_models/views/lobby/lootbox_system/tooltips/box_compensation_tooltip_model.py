from frameworks.wulf import ViewModel

class BoxCompensationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BoxCompensationTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getEventName(self):
        return self._getString(0)

    def setEventName(self, value):
        self._setString(0, value)
        return

    def getBoxesCountToGuaranteed(self):
        return self._getNumber(1)

    def setBoxesCountToGuaranteed(self, value):
        self._setNumber(1, value)
        return

    def getBoxCategory(self):
        return self._getString(2)

    def setBoxCategory(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(BoxCompensationTooltipModel, self)._initialize()
        self._addStringProperty(b'eventName', b'')
        self._addNumberProperty(b'boxesCountToGuaranteed', 0)
        self._addStringProperty(b'boxCategory', b'')
        return
