from frameworks.wulf import ViewModel

class CustomizationCarouselArrowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CustomizationCarouselArrowModel, self).__init__(properties=properties, commands=commands)
        return

    def getArrowIndex(self):
        return self._getNumber(0)

    def setArrowIndex(self, value):
        self._setNumber(0, value)
        return

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(CustomizationCarouselArrowModel, self)._initialize()
        self._addNumberProperty(b'arrowIndex', 0)
        self._addBoolProperty(b'isEnabled', False)
        return
