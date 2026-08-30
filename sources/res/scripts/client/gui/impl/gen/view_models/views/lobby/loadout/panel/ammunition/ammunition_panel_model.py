from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_group import AmmunitionItemsGroup

class AmmunitionPanelModel(ViewModel):
    __slots__ = (b'onChangeSetupIndex', b'onOpenSlotSpecDialog')
    NO_SLOT_SELECTED = -1

    def __init__(self, properties=6, commands=2):
        super(AmmunitionPanelModel, self).__init__(properties=properties, commands=commands)
        return

    def getGroups(self):
        return self._getArray(0)

    def setGroups(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getGroupsType():
        return AmmunitionItemsGroup

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)
        return

    def getSelectedSlot(self):
        return self._getNumber(2)

    def setSelectedSlot(self, value):
        self._setNumber(2, value)
        return

    def getSelectedSection(self):
        return self._getString(3)

    def setSelectedSection(self, value):
        self._setString(3, value)
        return

    def getVehicleId(self):
        return self._getString(4)

    def setVehicleId(self, value):
        self._setString(4, value)
        return

    def getHasVehSkillTree(self):
        return self._getBool(5)

    def setHasVehSkillTree(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(AmmunitionPanelModel, self)._initialize()
        self._addArrayProperty(b'groups', Array())
        self._addBoolProperty(b'isDisabled', False)
        self._addNumberProperty(b'selectedSlot', -1)
        self._addStringProperty(b'selectedSection', b'')
        self._addStringProperty(b'vehicleId', b'')
        self._addBoolProperty(b'hasVehSkillTree', False)
        self.onChangeSetupIndex = self._addCommand(b'onChangeSetupIndex')
        self.onOpenSlotSpecDialog = self._addCommand(b'onOpenSlotSpecDialog')
        return
