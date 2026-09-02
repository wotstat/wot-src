from frameworks.wulf import ViewModel
from gui.impl.gen import R

class PersonalMissionModel(ViewModel):
    __slots__ = ()
    STATE_ACTIVE = b'active'
    STATE_IMPROVE = b'improve'
    STATE_COMPLETE = b'complete'
    STATE_WRONG_VEHICLE = b'wrongVehicle'
    STATE_WARNING = b'warning'
    ANIMATION_NONE = b'none'
    ANIMATION_TANK_CHANGE = b'tankChange'
    ANIMATION_NEW_MISSION = b'newMission'

    def __init__(self, properties=10, commands=0):
        super(PersonalMissionModel, self).__init__(properties=properties, commands=commands)
        return

    def getCampaignId(self):
        return self._getNumber(0)

    def setCampaignId(self, value):
        self._setNumber(0, value)
        return

    def getMissionId(self):
        return self._getNumber(1)

    def setMissionId(self, value):
        self._setNumber(1, value)
        return

    def getTitle(self):
        return self._getString(2)

    def setTitle(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)
        return

    def getVehicleIcon(self):
        return self._getResource(4)

    def setVehicleIcon(self, value):
        self._setResource(4, value)
        return

    def getMissionState(self):
        return self._getString(5)

    def setMissionState(self, value):
        self._setString(5, value)
        return

    def getAnimationType(self):
        return self._getString(6)

    def setAnimationType(self, value):
        self._setString(6, value)
        return

    def getWarningMessage(self):
        return self._getString(7)

    def setWarningMessage(self, value):
        self._setString(7, value)
        return

    def getWarningTooltipHeader(self):
        return self._getString(8)

    def setWarningTooltipHeader(self, value):
        self._setString(8, value)
        return

    def getWarningTooltipBody(self):
        return self._getString(9)

    def setWarningTooltipBody(self, value):
        self._setString(9, value)
        return

    def _initialize(self):
        super(PersonalMissionModel, self)._initialize()
        self._addNumberProperty(b'campaignId', 0)
        self._addNumberProperty(b'missionId', 0)
        self._addStringProperty(b'title', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addResourceProperty(b'vehicleIcon', R.invalid())
        self._addStringProperty(b'missionState', b'')
        self._addStringProperty(b'animationType', b'none')
        self._addStringProperty(b'warningMessage', b'')
        self._addStringProperty(b'warningTooltipHeader', b'')
        self._addStringProperty(b'warningTooltipBody', b'')
        return
