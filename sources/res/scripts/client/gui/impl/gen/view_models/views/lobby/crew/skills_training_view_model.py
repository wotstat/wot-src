from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.crew.skills_list_model import SkillsListModel
from gui.impl.gen.view_models.views.lobby.crew.sort_dropdown_item_model import SortDropdownItemModel

class SkillsTrainingViewModel(ViewModel):
    __slots__ = (b'onClose', b'onSortingSelectionChange')

    def __init__(self, properties=14, commands=2):
        super(SkillsTrainingViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    @property
    def skillsList(self):
        return self._getViewModel(1)

    @staticmethod
    def getSkillsListType():
        return SkillsListModel

    def getIsFemale(self):
        return self._getBool(2)

    def setIsFemale(self, value):
        self._setBool(2, value)
        return

    def getIsMajorQualification(self):
        return self._getBool(3)

    def setIsMajorQualification(self, value):
        self._setBool(3, value)
        return

    def getRole(self):
        return self._getString(4)

    def setRole(self, value):
        self._setString(4, value)
        return

    def getCurrentSkillsAmount(self):
        return self._getNumber(5)

    def setCurrentSkillsAmount(self, value):
        self._setNumber(5, value)
        return

    def getTotalSkillsAmount(self):
        return self._getNumber(6)

    def setTotalSkillsAmount(self, value):
        self._setNumber(6, value)
        return

    def getAvailableSkillsAmount(self):
        return self._getNumber(7)

    def setAvailableSkillsAmount(self, value):
        self._setNumber(7, value)
        return

    def getAreAllSkillsLearned(self):
        return self._getBool(8)

    def setAreAllSkillsLearned(self, value):
        self._setBool(8, value)
        return

    def getSkillsEfficiency(self):
        return self._getReal(9)

    def setSkillsEfficiency(self, value):
        self._setReal(9, value)
        return

    def getIsAnySkillSelected(self):
        return self._getBool(10)

    def setIsAnySkillSelected(self, value):
        self._setBool(10, value)
        return

    def getIsTankmanInVehicle(self):
        return self._getBool(11)

    def setIsTankmanInVehicle(self, value):
        self._setBool(11, value)
        return

    def getSortingDropDownItems(self):
        return self._getArray(12)

    def setSortingDropDownItems(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getSortingDropDownItemsType():
        return SortDropdownItemModel

    def getShowSortingSelectionWarning(self):
        return self._getBool(13)

    def setShowSortingSelectionWarning(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(SkillsTrainingViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addViewModelProperty(b'skillsList', SkillsListModel())
        self._addBoolProperty(b'isFemale', False)
        self._addBoolProperty(b'isMajorQualification', False)
        self._addStringProperty(b'role', b'')
        self._addNumberProperty(b'currentSkillsAmount', 0)
        self._addNumberProperty(b'totalSkillsAmount', 0)
        self._addNumberProperty(b'availableSkillsAmount', 0)
        self._addBoolProperty(b'areAllSkillsLearned', False)
        self._addRealProperty(b'skillsEfficiency', 0.0)
        self._addBoolProperty(b'isAnySkillSelected', False)
        self._addBoolProperty(b'isTankmanInVehicle', False)
        self._addArrayProperty(b'sortingDropDownItems', Array())
        self._addBoolProperty(b'showSortingSelectionWarning', False)
        self.onClose = self._addCommand(b'onClose')
        self.onSortingSelectionChange = self._addCommand(b'onSortingSelectionChange')
        return
