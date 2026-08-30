from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.clan_supply.clan_supply_vehicle_model import ClanSupplyVehicleModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.stage_model import StageModel
from gui.impl.gen.view_models.views.lobby.clan_supply.stage_info_model import StageInfoModel

class ScreenStatus(IntEnum):
    PENDING = 0
    ERROR = 1
    LOADED = 2


class ProgressionModel(ViewModel):
    __slots__ = (b'onPreviewClick', b'onBuyStage', b'onSelectStage', b'onRefresh')

    def __init__(self, properties=7, commands=4):
        super(ProgressionModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def stageInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getStageInfoType():
        return StageInfoModel

    @property
    def vehicleInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleInfoType():
        return ClanSupplyVehicleModel

    def getStatus(self):
        return ScreenStatus(self._getNumber(2))

    def setStatus(self, value):
        self._setNumber(2, value.value)
        return

    def getSelectedStageID(self):
        return self._getNumber(3)

    def setSelectedStageID(self, value):
        self._setNumber(3, value)
        return

    def getIsCompleted(self):
        return self._getBool(4)

    def setIsCompleted(self, value):
        self._setBool(4, value)
        return

    def getIsMainRewardAvailable(self):
        return self._getBool(5)

    def setIsMainRewardAvailable(self, value):
        self._setBool(5, value)
        return

    def getStages(self):
        return self._getArray(6)

    def setStages(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getStagesType():
        return StageModel

    def _initialize(self):
        super(ProgressionModel, self)._initialize()
        self._addViewModelProperty(b'stageInfo', StageInfoModel())
        self._addViewModelProperty(b'vehicleInfo', ClanSupplyVehicleModel())
        self._addNumberProperty(b'status')
        self._addNumberProperty(b'selectedStageID', 0)
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isMainRewardAvailable', False)
        self._addArrayProperty(b'stages', Array())
        self.onPreviewClick = self._addCommand(b'onPreviewClick')
        self.onBuyStage = self._addCommand(b'onBuyStage')
        self.onSelectStage = self._addCommand(b'onSelectStage')
        self.onRefresh = self._addCommand(b'onRefresh')
        return
