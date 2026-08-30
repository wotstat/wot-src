from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_list_model import CrewSkillListModel

class TankmanPreviewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(TankmanPreviewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def skills(self):
        return self._getViewModel(0)

    @staticmethod
    def getSkillsType():
        return CrewSkillListModel

    def getSlotIdx(self):
        return self._getNumber(1)

    def setSlotIdx(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)
        return

    def getRoles(self):
        return self._getArray(4)

    def setRoles(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRolesType():
        return unicode

    def _initialize(self):
        super(TankmanPreviewModel, self)._initialize()
        self._addViewModelProperty(b'skills', CrewSkillListModel())
        self._addNumberProperty(b'slotIdx', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        self._addArrayProperty(b'roles', Array())
        return
