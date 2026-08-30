from frameworks.wulf import ViewModel

class RoleSkillSlotModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=5, commands=1):
        super(RoleSkillSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getRoleSkill(self):
        return self._getString(0)

    def setRoleSkill(self, value):
        self._setString(0, value)
        return

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)
        return

    def getRoleName(self):
        return self._getString(2)

    def setRoleName(self, value):
        self._setString(2, value)
        return

    def getCanSwitch(self):
        return self._getBool(3)

    def setCanSwitch(self, value):
        self._setBool(3, value)
        return

    def getIsPopoverOpen(self):
        return self._getBool(4)

    def setIsPopoverOpen(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(RoleSkillSlotModel, self)._initialize()
        self._addStringProperty(b'roleSkill', b'')
        self._addNumberProperty(b'intCD', 0)
        self._addStringProperty(b'roleName', b'')
        self._addBoolProperty(b'canSwitch', True)
        self._addBoolProperty(b'isPopoverOpen', False)
        self.onClick = self._addCommand(b'onClick')
        return
