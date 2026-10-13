from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.reward_path_item_view_model import RewardPathItemViewModel
from halloween.gui.impl.gen.view_models.views.lobby.vehicle_title_view_model import VehicleTitleViewModel

class RewardPathViewModel(ViewModel):
    __slots__ = (b'onClose', b'onPreview', b'onViewLoaded', b'goToMission', b'goToCrewSelect')

    def __init__(self, properties=5, commands=5):
        super(RewardPathViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def mainGiftVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getMainGiftVehicleType():
        return VehicleTitleViewModel

    def getArtefacts(self):
        return self._getArray(1)

    def setArtefacts(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getArtefactsType():
        return RewardPathItemViewModel

    def getIsCompleted(self):
        return self._getBool(2)

    def setIsCompleted(self, value):
        self._setBool(2, value)
        return

    def getProgress(self):
        return self._getNumber(3)

    def setProgress(self, value):
        self._setNumber(3, value)
        return

    def getSelectedArtefactID(self):
        return self._getString(4)

    def setSelectedArtefactID(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(RewardPathViewModel, self)._initialize()
        self._addViewModelProperty(b'mainGiftVehicle', VehicleTitleViewModel())
        self._addArrayProperty(b'artefacts', Array())
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'progress', 0)
        self._addStringProperty(b'selectedArtefactID', b'')
        self.onClose = self._addCommand(b'onClose')
        self.onPreview = self._addCommand(b'onPreview')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.goToMission = self._addCommand(b'goToMission')
        self.goToCrewSelect = self._addCommand(b'goToCrewSelect')
        return
