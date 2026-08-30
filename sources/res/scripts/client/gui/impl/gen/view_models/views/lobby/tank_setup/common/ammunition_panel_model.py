from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_group import AmmunitionItemsGroup

class AmmunitionPanelModel(ViewModel):
    __slots__ = (b'onSectionSelect', b'onDragDropSwap', b'onSlotClear', b'onSectionResized', b'onChangeSetupIndex', b'onSpecializationSelect')

    def __init__(self, properties=6, commands=6):
        super(AmmunitionPanelModel, self).__init__(properties=properties, commands=commands)
        return

    def getAmmoNotFull(self):
        return self._getBool(0)

    def setAmmoNotFull(self, value):
        self._setBool(0, value)
        return

    def getSelectedSection(self):
        return self._getString(1)

    def setSelectedSection(self, value):
        self._setString(1, value)
        return

    def getSelectedSlot(self):
        return self._getNumber(2)

    def setSelectedSlot(self, value):
        self._setNumber(2, value)
        return

    def getIsSetupSwitchInProgress(self):
        return self._getBool(3)

    def setIsSetupSwitchInProgress(self, value):
        self._setBool(3, value)
        return

    def getSectionGroups(self):
        return self._getArray(4)

    def setSectionGroups(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getSectionGroupsType():
        return AmmunitionItemsGroup

    def getSyncInitiator(self):
        return self._getNumber(5)

    def setSyncInitiator(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(AmmunitionPanelModel, self)._initialize()
        self._addBoolProperty(b'ammoNotFull', False)
        self._addStringProperty(b'selectedSection', b'')
        self._addNumberProperty(b'selectedSlot', -1)
        self._addBoolProperty(b'isSetupSwitchInProgress', False)
        self._addArrayProperty(b'sectionGroups', Array())
        self._addNumberProperty(b'syncInitiator', 0)
        self.onSectionSelect = self._addCommand(b'onSectionSelect')
        self.onDragDropSwap = self._addCommand(b'onDragDropSwap')
        self.onSlotClear = self._addCommand(b'onSlotClear')
        self.onSectionResized = self._addCommand(b'onSectionResized')
        self.onChangeSetupIndex = self._addCommand(b'onChangeSetupIndex')
        self.onSpecializationSelect = self._addCommand(b'onSpecializationSelect')
        return
