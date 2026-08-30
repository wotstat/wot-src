from frameworks.wulf import ViewModel

class PetObjectTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PetObjectTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsStorageTooltipVisible(self):
        return self._getBool(0)

    def setIsStorageTooltipVisible(self, value):
        self._setBool(0, value)
        return

    def getIs3dObjectTooltipVisible(self):
        return self._getBool(1)

    def setIs3dObjectTooltipVisible(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(PetObjectTooltipModel, self)._initialize()
        self._addBoolProperty(b'isStorageTooltipVisible', False)
        self._addBoolProperty(b'is3dObjectTooltipVisible', False)
        return
