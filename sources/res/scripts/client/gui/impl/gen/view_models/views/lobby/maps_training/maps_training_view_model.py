from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.hangar.menu_item_model import MenuItemModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_group_model import MapsTrainingGroupModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_map_model import MapsTrainingMapModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_selected_map_model import MapsTrainingSelectedMapModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_vehicle_marker_model import MapsTrainingVehicleMarkerModel

class MapsTrainingViewModel(ViewModel):
    __slots__ = (b'onBack', b'onSelect', b'onScenarioSelect', b'onFilteringChange', b'onBlurRectUpdated', b'onMoveSpace', b'onMouseOver3dScene', b'onInfoClicked', b'onClose', b'onNavigate')

    def __init__(self, properties=11, commands=10):
        super(MapsTrainingViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def selectedMapModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getSelectedMapModelType():
        return MapsTrainingSelectedMapModel

    @property
    def vehicleMarker(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleMarkerType():
        return MapsTrainingVehicleMarkerModel

    def getIsMapSelected(self):
        return self._getBool(2)

    def setIsMapSelected(self, value):
        self._setBool(2, value)
        return

    def getIncompleteFilter(self):
        return self._getBool(3)

    def setIncompleteFilter(self, value):
        self._setBool(3, value)
        return

    def getTitleFilter(self):
        return self._getString(4)

    def setTitleFilter(self, value):
        self._setString(4, value)
        return

    def getIsDataLoaded(self):
        return self._getBool(5)

    def setIsDataLoaded(self, value):
        self._setBool(5, value)
        return

    def getMaps(self):
        return self._getArray(6)

    def setMaps(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getMapsType():
        return MapsTrainingMapModel

    def getGroups(self):
        return self._getArray(7)

    def setGroups(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getGroupsType():
        return MapsTrainingGroupModel

    def getMenuItems(self):
        return self._getArray(8)

    def setMenuItems(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getMenuItemsType():
        return MenuItemModel

    def getModeName(self):
        return self._getString(9)

    def setModeName(self, value):
        self._setString(9, value)
        return

    def getModeId(self):
        return self._getString(10)

    def setModeId(self, value):
        self._setString(10, value)
        return

    def _initialize(self):
        super(MapsTrainingViewModel, self)._initialize()
        self._addViewModelProperty(b'selectedMapModel', MapsTrainingSelectedMapModel())
        self._addViewModelProperty(b'vehicleMarker', MapsTrainingVehicleMarkerModel())
        self._addBoolProperty(b'isMapSelected', False)
        self._addBoolProperty(b'incompleteFilter', False)
        self._addStringProperty(b'titleFilter', b'')
        self._addBoolProperty(b'isDataLoaded', False)
        self._addArrayProperty(b'maps', Array())
        self._addArrayProperty(b'groups', Array())
        self._addArrayProperty(b'menuItems', Array())
        self._addStringProperty(b'modeName', b'')
        self._addStringProperty(b'modeId', b'')
        self.onBack = self._addCommand(b'onBack')
        self.onSelect = self._addCommand(b'onSelect')
        self.onScenarioSelect = self._addCommand(b'onScenarioSelect')
        self.onFilteringChange = self._addCommand(b'onFilteringChange')
        self.onBlurRectUpdated = self._addCommand(b'onBlurRectUpdated')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onMouseOver3dScene = self._addCommand(b'onMouseOver3dScene')
        self.onInfoClicked = self._addCommand(b'onInfoClicked')
        self.onClose = self._addCommand(b'onClose')
        self.onNavigate = self._addCommand(b'onNavigate')
        return
