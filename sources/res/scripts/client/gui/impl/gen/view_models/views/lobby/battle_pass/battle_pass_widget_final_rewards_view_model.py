from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.battle_pass.attachments_set_info_model import AttachmentsSetInfoModel
from gui.impl.gen.view_models.views.lobby.battle_pass.character_widget_view_model import CharacterWidgetViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.style_info_model import StyleInfoModel

class BattlePassWidgetFinalRewardsViewModel(ViewModel):
    __slots__ = (b'showTankmen', b'onRewardPreviewClick')

    def __init__(self, properties=5, commands=2):
        super(BattlePassWidgetFinalRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    @property
    def tankmanInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getTankmanInfoType():
        return CharacterWidgetViewModel

    @property
    def styleInfo(self):
        return self._getViewModel(2)

    @staticmethod
    def getStyleInfoType():
        return StyleInfoModel

    @property
    def attachmentsSetInfo(self):
        return self._getViewModel(3)

    @staticmethod
    def getAttachmentsSetInfoType():
        return AttachmentsSetInfoModel

    def getBattleQuest(self):
        return self._getString(4)

    def setBattleQuest(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(BattlePassWidgetFinalRewardsViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addViewModelProperty(b'tankmanInfo', CharacterWidgetViewModel())
        self._addViewModelProperty(b'styleInfo', StyleInfoModel())
        self._addViewModelProperty(b'attachmentsSetInfo', AttachmentsSetInfoModel())
        self._addStringProperty(b'battleQuest', b'')
        self.showTankmen = self._addCommand(b'showTankmen')
        self.onRewardPreviewClick = self._addCommand(b'onRewardPreviewClick')
        return
