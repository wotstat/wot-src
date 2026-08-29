from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.paragons.common.paragons_vehicle_model import ParagonsVehicleModel
from gui.impl.gen.view_models.views.lobby.paragons.common.request_status_model import RequestStatusModel

class SelectRewardsViewModel(ViewModel):
    __slots__ = (b'onClaim', b'onClose', b'onPreview', b'onCompare')

    def __init__(self, properties=4, commands=4):
        super(SelectRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def requestStatus(self):
        return self._getViewModel(0)

    @staticmethod
    def getRequestStatusType():
        return RequestStatusModel

    def getAvailableToSelect(self):
        return self._getNumber(1)

    def setAvailableToSelect(self, value):
        self._setNumber(1, value)
        return

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)
        return

    def getAvailableRewards(self):
        return self._getArray(3)

    def setAvailableRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getAvailableRewardsType():
        return ParagonsVehicleModel

    def _initialize(self):
        super(SelectRewardsViewModel, self)._initialize()
        self._addViewModelProperty(b'requestStatus', RequestStatusModel())
        self._addNumberProperty(b'availableToSelect', 0)
        self._addNumberProperty(b'level', 0)
        self._addArrayProperty(b'availableRewards', Array())
        self.onClaim = self._addCommand(b'onClaim')
        self.onClose = self._addCommand(b'onClose')
        self.onPreview = self._addCommand(b'onPreview')
        self.onCompare = self._addCommand(b'onCompare')
        return
