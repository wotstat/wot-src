from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_preview.tabs.tankman_preview_model import TankmanPreviewModel
from gui.impl.gen.view_models.views.lobby.vehicle_preview.tabs.title_model import TitleModel

class CrewTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CrewTabModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def headerModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getHeaderModelType():
        return TitleModel

    def getIsLockedCrew(self):
        return self._getBool(1)

    def setIsLockedCrew(self, value):
        self._setBool(1, value)
        return

    def getHasDog(self):
        return self._getBool(2)

    def setHasDog(self, value):
        self._setBool(2, value)
        return

    def getNation(self):
        return self._getString(3)

    def setNation(self, value):
        self._setString(3, value)
        return

    def getTankmen(self):
        return self._getArray(4)

    def setTankmen(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getTankmenType():
        return TankmanPreviewModel

    def _initialize(self):
        super(CrewTabModel, self)._initialize()
        self._addViewModelProperty(b'headerModel', TitleModel())
        self._addBoolProperty(b'isLockedCrew', False)
        self._addBoolProperty(b'hasDog', False)
        self._addStringProperty(b'nation', b'')
        self._addArrayProperty(b'tankmen', Array())
        return
