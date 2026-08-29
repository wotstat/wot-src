from gui.impl.gen.view_models.views.lobby.comp7.comp7_bonus_model import Comp7BonusModel

class Comp7StyleBonusModel(Comp7BonusModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(Comp7StyleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getStyleID(self):
        return self._getNumber(11)

    def setStyleID(self, value):
        self._setNumber(11, value)
        return

    def getBranchID(self):
        return self._getNumber(12)

    def setBranchID(self, value):
        self._setNumber(12, value)
        return

    def getProgressLevel(self):
        return self._getNumber(13)

    def setProgressLevel(self, value):
        self._setNumber(13, value)
        return

    def _initialize(self):
        super(Comp7StyleBonusModel, self)._initialize()
        self._addNumberProperty(b'styleID', 0)
        self._addNumberProperty(b'branchID', 0)
        self._addNumberProperty(b'progressLevel', 0)
        return
