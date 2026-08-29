from frameworks.wulf import ViewModel

class TankmanChangePreviewTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TankmanChangePreviewTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCredits(self):
        return self._getNumber(0)

    def setCredits(self, value):
        self._setNumber(0, value)
        return

    def getRetrainingGold(self):
        return self._getNumber(1)

    def setRetrainingGold(self, value):
        self._setNumber(1, value)
        return

    def getSpecialityGold(self):
        return self._getNumber(2)

    def setSpecialityGold(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(TankmanChangePreviewTooltipModel, self)._initialize()
        self._addNumberProperty(b'credits', 0)
        self._addNumberProperty(b'retrainingGold', 0)
        self._addNumberProperty(b'specialityGold', 0)
        return
