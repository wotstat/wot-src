from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.campaign_model import CampaignModel

class CampaignSelectorViewState(Enum):
    FIRST_TWO = b'firstTwo'
    THIRD = b'third'
    COMPLETED_WITH_HONOR = b'completedWithHonor'
    LOCKED = b'locked'


class CampaignSelectorModel(ViewModel):
    __slots__ = (b'onOperation', b'onMoreInfo', b'switchCampaign', b'onClose')
    OPERATION_ID = b'operationId'
    CAMPAIGNS_STATE = b'campaignsState'
    FIRST_ACTIVATE = b'firstActivate'

    def __init__(self, properties=4, commands=4):
        super(CampaignSelectorModel, self).__init__(properties=properties, commands=commands)
        return

    def getCampaigns(self):
        return self._getArray(0)

    def setCampaigns(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getCampaignsType():
        return CampaignModel

    def getBlockedByVehicle(self):
        return self._getBool(1)

    def setBlockedByVehicle(self, value):
        self._setBool(1, value)
        return

    def getFirstTimeEntrance(self):
        return self._getBool(2)

    def setFirstTimeEntrance(self, value):
        self._setBool(2, value)
        return

    def getCampaignSelectorViewState(self):
        return CampaignSelectorViewState(self._getString(3))

    def setCampaignSelectorViewState(self, value):
        self._setString(3, value.value)
        return

    def _initialize(self):
        super(CampaignSelectorModel, self)._initialize()
        self._addArrayProperty(b'campaigns', Array())
        self._addBoolProperty(b'blockedByVehicle', False)
        self._addBoolProperty(b'firstTimeEntrance', False)
        self._addStringProperty(b'campaignSelectorViewState')
        self.onOperation = self._addCommand(b'onOperation')
        self.onMoreInfo = self._addCommand(b'onMoreInfo')
        self.switchCampaign = self._addCommand(b'switchCampaign')
        self.onClose = self._addCommand(b'onClose')
        return
