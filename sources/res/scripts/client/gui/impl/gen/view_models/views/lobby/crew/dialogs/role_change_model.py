from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.retrain_role_model import RetrainRoleModel

class DisableState(Enum):
    AVAILABLE = b'available'
    FORCED = b'forced'
    CREWLOCK = b'crewLock'
    FREEOPERATION = b'freeOperation'


class RoleChangeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(RoleChangeModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVisible(self):
        return self._getBool(0)

    def setIsVisible(self, value):
        self._setBool(0, value)
        return

    def getIsChecked(self):
        return self._getBool(1)

    def setIsChecked(self, value):
        self._setBool(1, value)
        return

    def getSelectedIdx(self):
        return self._getNumber(2)

    def setSelectedIdx(self, value):
        self._setNumber(2, value)
        return

    def getDisableState(self):
        return DisableState(self._getString(3))

    def setDisableState(self, value):
        self._setString(3, value.value)
        return

    def getRoles(self):
        return self._getArray(4)

    def setRoles(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRolesType():
        return RetrainRoleModel

    def _initialize(self):
        super(RoleChangeModel, self)._initialize()
        self._addBoolProperty(b'isVisible', False)
        self._addBoolProperty(b'isChecked', False)
        self._addNumberProperty(b'selectedIdx', 0)
        self._addStringProperty(b'disableState')
        self._addArrayProperty(b'roles', Array())
        return
