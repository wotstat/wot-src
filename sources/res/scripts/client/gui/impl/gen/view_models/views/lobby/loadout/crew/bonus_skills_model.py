from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.perk_model import PerkModel

class BonusSkillsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BonusSkillsModel, self).__init__(properties=properties, commands=commands)
        return

    def getRole(self):
        return self._getString(0)

    def setRole(self, value):
        self._setString(0, value)
        return

    def getNewCount(self):
        return self._getNumber(1)

    def setNewCount(self, value):
        self._setNumber(1, value)
        return

    def getTrainingProgress(self):
        return self._getNumber(2)

    def setTrainingProgress(self, value):
        self._setNumber(2, value)
        return

    def getSkills(self):
        return self._getArray(3)

    def setSkills(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getSkillsType():
        return PerkModel

    def _initialize(self):
        super(BonusSkillsModel, self)._initialize()
        self._addStringProperty(b'role', b'')
        self._addNumberProperty(b'newCount', 0)
        self._addNumberProperty(b'trainingProgress', -1)
        self._addArrayProperty(b'skills', Array())
        return
