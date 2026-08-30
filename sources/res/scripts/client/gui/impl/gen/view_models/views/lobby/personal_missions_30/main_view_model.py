from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.missions_state_model import MissionsStateModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.new_operation_banner import NewOperationBanner
from gui.impl.gen.view_models.views.lobby.personal_missions_30.operation_model import OperationModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.operation_status_model import OperationStatusModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.select_operation_model import SelectOperationModel

class MainScreenState(Enum):
    ASSEMBLING = b'assembling'
    MISSIONS = b'missions'
    PROGRESSION = b'progression'


class AnimationState(Enum):
    IDLE = b'idle'
    ANIMATION_STARTED = b'animationStarted'
    ASSEMBLING = b'assembling'
    CONTINUE_DETAIL_INFO = b'continueDetailInfo'
    CONTINUE_CLAIM_DETAIL = b'continueClaimDetail'
    CONTINUE_BACK = b'continueBack'


class MainViewModel(ViewModel):
    __slots__ = (b'onBack', b'onSwitchOperation', b'showOperationVehicleVideo', b'onOperationStatusButtonClick', b'onDetailInfo', b'onClaimDetail', b'onMission', b'onAdditionalMission', b'onVehiclePreview', b'showVehicleInHangar', b'showDetailVideo', b'onMoveSpace', b'onMouseOver3dScene', b'showStylePreview', b'setFreeCamera', b'updateAnimationState')
    OPERATION_ID = b'operationId'
    DETAIL_ID = b'detailId'
    ANIMATION_STATE = b'animationState'

    def __init__(self, properties=11, commands=16):
        super(MainViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return VehicleInfoModel

    @property
    def status(self):
        return self._getViewModel(1)

    @staticmethod
    def getStatusType():
        return OperationStatusModel

    @property
    def missionsModel(self):
        return self._getViewModel(2)

    @staticmethod
    def getMissionsModelType():
        return MissionsStateModel

    @property
    def banner(self):
        return self._getViewModel(3)

    @staticmethod
    def getBannerType():
        return NewOperationBanner

    def getActiveOperationId(self):
        return self._getNumber(4)

    def setActiveOperationId(self, value):
        self._setNumber(4, value)
        return

    def getAnimationState(self):
        return AnimationState(self._getString(5))

    def setAnimationState(self, value):
        self._setString(5, value.value)
        return

    def getCampaignName(self):
        return self._getString(6)

    def setCampaignName(self, value):
        self._setString(6, value)
        return

    def getMenuItems(self):
        return self._getArray(7)

    def setMenuItems(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getMenuItemsType():
        return SelectOperationModel

    def getOperations(self):
        return self._getArray(8)

    def setOperations(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getOperationsType():
        return OperationModel

    def getMainScreenState(self):
        return MainScreenState(self._getString(9))

    def setMainScreenState(self, value):
        self._setString(9, value.value)
        return

    def getCameraFlightInProgress(self):
        return self._getBool(10)

    def setCameraFlightInProgress(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(MainViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicle', VehicleInfoModel())
        self._addViewModelProperty(b'status', OperationStatusModel())
        self._addViewModelProperty(b'missionsModel', MissionsStateModel())
        self._addViewModelProperty(b'banner', NewOperationBanner())
        self._addNumberProperty(b'activeOperationId', 0)
        self._addStringProperty(b'animationState', AnimationState.IDLE.value)
        self._addStringProperty(b'campaignName', b'')
        self._addArrayProperty(b'menuItems', Array())
        self._addArrayProperty(b'operations', Array())
        self._addStringProperty(b'mainScreenState')
        self._addBoolProperty(b'cameraFlightInProgress', False)
        self.onBack = self._addCommand(b'onBack')
        self.onSwitchOperation = self._addCommand(b'onSwitchOperation')
        self.showOperationVehicleVideo = self._addCommand(b'showOperationVehicleVideo')
        self.onOperationStatusButtonClick = self._addCommand(b'onOperationStatusButtonClick')
        self.onDetailInfo = self._addCommand(b'onDetailInfo')
        self.onClaimDetail = self._addCommand(b'onClaimDetail')
        self.onMission = self._addCommand(b'onMission')
        self.onAdditionalMission = self._addCommand(b'onAdditionalMission')
        self.onVehiclePreview = self._addCommand(b'onVehiclePreview')
        self.showVehicleInHangar = self._addCommand(b'showVehicleInHangar')
        self.showDetailVideo = self._addCommand(b'showDetailVideo')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onMouseOver3dScene = self._addCommand(b'onMouseOver3dScene')
        self.showStylePreview = self._addCommand(b'showStylePreview')
        self.setFreeCamera = self._addCommand(b'setFreeCamera')
        self.updateAnimationState = self._addCommand(b'updateAnimationState')
        return
