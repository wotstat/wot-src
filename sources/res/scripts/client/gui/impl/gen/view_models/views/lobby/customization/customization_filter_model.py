from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class StructureBlockType(Enum):
    GROUPS = b'groups'
    AVAILABILITY = b'availability'
    ONANOTHERVEH = b'onAnotherVeh'
    SPECIAL = b'special'
    HISTORIC = b'historic'
    EDITABLE = b'editable'
    FORMFACTOR = b'formfactor'
    SORTING = b'sorting'
    PROGRESSIONDECALS = b'progressionDecals'


class CustomizationFilterModel(ViewModel):
    __slots__ = (b'openPopoverView', b'clearFilter', b'changeFilter')

    def __init__(self, properties=26, commands=3):
        super(CustomizationFilterModel, self).__init__(properties=properties, commands=commands)
        return

    def getGroups(self):
        return self._getArray(0)

    def setGroups(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getGroupsType():
        return unicode

    def getSelectedGroup(self):
        return self._getNumber(1)

    def setSelectedGroup(self, value):
        self._setNumber(1, value)
        return

    def getAvailability(self):
        return self._getString(2)

    def setAvailability(self, value):
        self._setString(2, value)
        return

    def getOnAnotherVeh(self):
        return self._getBool(3)

    def setOnAnotherVeh(self, value):
        self._setBool(3, value)
        return

    def getIsEnableOnAnotherVeh(self):
        return self._getBool(4)

    def setIsEnableOnAnotherVeh(self, value):
        self._setBool(4, value)
        return

    def getApplied(self):
        return self._getBool(5)

    def setApplied(self, value):
        self._setBool(5, value)
        return

    def getFavorite(self):
        return self._getBool(6)

    def setFavorite(self, value):
        self._setBool(6, value)
        return

    def getHistoric(self):
        return self._getBool(7)

    def setHistoric(self, value):
        self._setBool(7, value)
        return

    def getNonHistoric(self):
        return self._getBool(8)

    def setNonHistoric(self, value):
        self._setBool(8, value)
        return

    def getFantastical(self):
        return self._getBool(9)

    def setFantastical(self, value):
        self._setBool(9, value)
        return

    def getOnlyEditableStyles(self):
        return self._getBool(10)

    def setOnlyEditableStyles(self, value):
        self._setBool(10, value)
        return

    def getOnlyNonEditableStyles(self):
        return self._getBool(11)

    def setOnlyNonEditableStyles(self, value):
        self._setBool(11, value)
        return

    def getOnlyProgressionStyles(self):
        return self._getBool(12)

    def setOnlyProgressionStyles(self, value):
        self._setBool(12, value)
        return

    def getOnlyProgressionDecals(self):
        return self._getBool(13)

    def setOnlyProgressionDecals(self, value):
        self._setBool(13, value)
        return

    def getFormfactor_square(self):
        return self._getBool(14)

    def setFormfactor_square(self, value):
        self._setBool(14, value)
        return

    def getFormfactor_rect1x2(self):
        return self._getBool(15)

    def setFormfactor_rect1x2(self, value):
        self._setBool(15, value)
        return

    def getFormfactor_rect1x3(self):
        return self._getBool(16)

    def setFormfactor_rect1x3(self, value):
        self._setBool(16, value)
        return

    def getFormfactor_rect1x4(self):
        return self._getBool(17)

    def setFormfactor_rect1x4(self, value):
        self._setBool(17, value)
        return

    def getFormfactor_rect1x6(self):
        return self._getBool(18)

    def setFormfactor_rect1x6(self, value):
        self._setBool(18, value)
        return

    def getDisplayGroups(self):
        return self._getArray(19)

    def setDisplayGroups(self, value):
        self._setArray(19, value)
        return

    @staticmethod
    def getDisplayGroupsType():
        return unicode

    def getSelectedDisplayGroup(self):
        return self._getNumber(20)

    def setSelectedDisplayGroup(self, value):
        self._setNumber(20, value)
        return

    def getAllItemsCounter(self):
        return self._getNumber(21)

    def setAllItemsCounter(self, value):
        self._setNumber(21, value)
        return

    def getFilteredItemsCounter(self):
        return self._getNumber(22)

    def setFilteredItemsCounter(self, value):
        self._setNumber(22, value)
        return

    def getNewHiddenItemsCounter(self):
        return self._getNumber(23)

    def setNewHiddenItemsCounter(self, value):
        self._setNumber(23, value)
        return

    def getIsFilteringActive(self):
        return self._getBool(24)

    def setIsFilteringActive(self, value):
        self._setBool(24, value)
        return

    def getStructure(self):
        return self._getArray(25)

    def setStructure(self, value):
        self._setArray(25, value)
        return

    @staticmethod
    def getStructureType():
        return StructureBlockType

    def _initialize(self):
        super(CustomizationFilterModel, self)._initialize()
        self._addArrayProperty(b'groups', Array())
        self._addNumberProperty(b'selectedGroup', 0)
        self._addStringProperty(b'availability', b'')
        self._addBoolProperty(b'onAnotherVeh', False)
        self._addBoolProperty(b'isEnableOnAnotherVeh', False)
        self._addBoolProperty(b'applied', False)
        self._addBoolProperty(b'favorite', False)
        self._addBoolProperty(b'historic', False)
        self._addBoolProperty(b'nonHistoric', False)
        self._addBoolProperty(b'fantastical', False)
        self._addBoolProperty(b'onlyEditableStyles', False)
        self._addBoolProperty(b'onlyNonEditableStyles', False)
        self._addBoolProperty(b'onlyProgressionStyles', False)
        self._addBoolProperty(b'onlyProgressionDecals', False)
        self._addBoolProperty(b'formfactor_square', False)
        self._addBoolProperty(b'formfactor_rect1x2', False)
        self._addBoolProperty(b'formfactor_rect1x3', False)
        self._addBoolProperty(b'formfactor_rect1x4', False)
        self._addBoolProperty(b'formfactor_rect1x6', False)
        self._addArrayProperty(b'displayGroups', Array())
        self._addNumberProperty(b'selectedDisplayGroup', 0)
        self._addNumberProperty(b'allItemsCounter', 0)
        self._addNumberProperty(b'filteredItemsCounter', 0)
        self._addNumberProperty(b'newHiddenItemsCounter', 0)
        self._addBoolProperty(b'isFilteringActive', False)
        self._addArrayProperty(b'structure', Array())
        self.openPopoverView = self._addCommand(b'openPopoverView')
        self.clearFilter = self._addCommand(b'clearFilter')
        self.changeFilter = self._addCommand(b'changeFilter')
        return
