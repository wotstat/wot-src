from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.skill_select_item_model import SkillSelectItemModel

class SkillSelectRowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(SkillSelectRowModel, self).__init__(properties=properties, commands=commands)
        return

    def getSkills(self):
        return self._getArray(0)

    def setSkills(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getSkillsType():
        return SkillSelectItemModel

    def getCommonSkills(self):
        return self._getArray(1)

    def setCommonSkills(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getCommonSkillsType():
        return SkillSelectItemModel

    def getRole(self):
        return self._getString(2)

    def setRole(self, value):
        self._setString(2, value)
        return

    def getPossibleMaxSelected(self):
        return self._getNumber(3)

    def setPossibleMaxSelected(self, value):
        self._setNumber(3, value)
        return

    def getSelectedAmount(self):
        return self._getNumber(4)

    def setSelectedAmount(self, value):
        self._setNumber(4, value)
        return

    def getTankmanIdx(self):
        return self._getNumber(5)

    def setTankmanIdx(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(SkillSelectRowModel, self)._initialize()
        self._addArrayProperty(b'skills', Array())
        self._addArrayProperty(b'commonSkills', Array())
        self._addStringProperty(b'role', b'')
        self._addNumberProperty(b'possibleMaxSelected', 0)
        self._addNumberProperty(b'selectedAmount', 0)
        self._addNumberProperty(b'tankmanIdx', -1)
        return
