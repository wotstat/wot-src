from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class ProgressStyleBonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(ProgressStyleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getStyleID(self):
        return self._getNumber(8)

    def setStyleID(self, value):
        self._setNumber(8, value)
        return

    def getBranchID(self):
        return self._getNumber(9)

    def setBranchID(self, value):
        self._setNumber(9, value)
        return

    def getProgressLevel(self):
        return self._getNumber(10)

    def setProgressLevel(self, value):
        self._setNumber(10, value)
        return

    def getProgressLevelsCount(self):
        return self._getNumber(11)

    def setProgressLevelsCount(self, value):
        self._setNumber(11, value)
        return

    def getIsGranted(self):
        return self._getBool(12)

    def setIsGranted(self, value):
        self._setBool(12, value)
        return

    def _initialize(self):
        super(ProgressStyleBonusModel, self)._initialize()
        self._addNumberProperty(b'styleID', 0)
        self._addNumberProperty(b'branchID', 0)
        self._addNumberProperty(b'progressLevel', 0)
        self._addNumberProperty(b'progressLevelsCount', 0)
        self._addBoolProperty(b'isGranted', False)
        return
