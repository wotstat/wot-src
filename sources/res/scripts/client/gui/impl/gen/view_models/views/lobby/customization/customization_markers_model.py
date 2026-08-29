from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.customization_marker_edit_mode_model import CustomizationMarkerEditModeModel
from gui.impl.gen.view_models.views.lobby.customization.customization_marker_model import CustomizationMarkerModel
from gui.impl.gen.view_models.views.lobby.customization.customization_types_model import CustomizationTypesModel

class CustomizationMarkersModel(ViewModel):
    __slots__ = (b'onSelectAnchor', b'onHoverAnchor', b'onDragAnchor', b'onRemoveChar', b'onAddChar', b'onDeleteAllChars', b'onEnterInput')

    def __init__(self, properties=3, commands=7):
        super(CustomizationMarkersModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def editModeData(self):
        return self._getViewModel(0)

    @staticmethod
    def getEditModeDataType():
        return CustomizationMarkerEditModeModel

    @property
    def customizationTypes(self):
        return self._getViewModel(1)

    @staticmethod
    def getCustomizationTypesType():
        return CustomizationTypesModel

    def getMarkersList(self):
        return self._getArray(2)

    def setMarkersList(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getMarkersListType():
        return CustomizationMarkerModel

    def _initialize(self):
        super(CustomizationMarkersModel, self)._initialize()
        self._addViewModelProperty(b'editModeData', CustomizationMarkerEditModeModel())
        self._addViewModelProperty(b'customizationTypes', CustomizationTypesModel())
        self._addArrayProperty(b'markersList', Array())
        self.onSelectAnchor = self._addCommand(b'onSelectAnchor')
        self.onHoverAnchor = self._addCommand(b'onHoverAnchor')
        self.onDragAnchor = self._addCommand(b'onDragAnchor')
        self.onRemoveChar = self._addCommand(b'onRemoveChar')
        self.onAddChar = self._addCommand(b'onAddChar')
        self.onDeleteAllChars = self._addCommand(b'onDeleteAllChars')
        self.onEnterInput = self._addCommand(b'onEnterInput')
        return
