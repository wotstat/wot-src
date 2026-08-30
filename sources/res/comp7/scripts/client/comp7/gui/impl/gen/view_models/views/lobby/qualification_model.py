from frameworks.wulf import ViewModel

class QualificationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(QualificationModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsActive(self):
        return self._getBool(0)

    def setIsActive(self, value):
        self._setBool(0, value)
        return

    def getBattlesCount(self):
        return self._getNumber(1)

    def setBattlesCount(self, value):
        self._setNumber(1, value)
        return

    def getMaxBattlesCount(self):
        return self._getNumber(2)

    def setMaxBattlesCount(self, value):
        self._setNumber(2, value)
        return

    def getIsRatingCalculation(self):
        return self._getBool(3)

    def setIsRatingCalculation(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(QualificationModel, self)._initialize()
        self._addBoolProperty(b'isActive', False)
        self._addNumberProperty(b'battlesCount', 0)
        self._addNumberProperty(b'maxBattlesCount', 0)
        self._addBoolProperty(b'isRatingCalculation', False)
        return
