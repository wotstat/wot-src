from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.bootcamp.bootcamp_nation_model import BootcampNationModel
from gui.impl.gen.view_models.views.bootcamp.preview_model import PreviewModel

class BootcampNationViewModel(ViewModel):
    __slots__ = (b'onNationSelected', b'onNationShow', b'onMoveSpace', b'onEscPressed')

    def __init__(self, properties=8, commands=4):
        super(BootcampNationViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedNation(self):
        return self._getNumber(0)

    def setSelectedNation(self, value):
        self._setNumber(0, value)
        return

    def getNationsList(self):
        return self._getArray(1)

    def setNationsList(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getNationsListType():
        return BootcampNationModel

    def getPromoteNationsList(self):
        return self._getArray(2)

    def setPromoteNationsList(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getPromoteNationsListType():
        return BootcampNationModel

    def getSelectedTitle(self):
        return self._getString(3)

    def setSelectedTitle(self, value):
        self._setString(3, value)
        return

    def getSelectedDescription(self):
        return self._getResource(4)

    def setSelectedDescription(self, value):
        self._setResource(4, value)
        return

    def getIsPromote(self):
        return self._getBool(5)

    def setIsPromote(self, value):
        self._setBool(5, value)
        return

    def getPreviewVehiclesList(self):
        return self._getArray(6)

    def setPreviewVehiclesList(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getPreviewVehiclesListType():
        return PreviewModel

    def getIsPreviewLoading(self):
        return self._getBool(7)

    def setIsPreviewLoading(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(BootcampNationViewModel, self)._initialize()
        self._addNumberProperty(b'selectedNation', 0)
        self._addArrayProperty(b'nationsList', Array())
        self._addArrayProperty(b'promoteNationsList', Array())
        self._addStringProperty(b'selectedTitle', b'')
        self._addResourceProperty(b'selectedDescription', R.invalid())
        self._addBoolProperty(b'isPromote', False)
        self._addArrayProperty(b'previewVehiclesList', Array())
        self._addBoolProperty(b'isPreviewLoading', False)
        self.onNationSelected = self._addCommand(b'onNationSelected')
        self.onNationShow = self._addCommand(b'onNationShow')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onEscPressed = self._addCommand(b'onEscPressed')
        return
