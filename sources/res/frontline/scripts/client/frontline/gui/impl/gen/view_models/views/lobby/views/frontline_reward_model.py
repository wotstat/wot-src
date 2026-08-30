from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class ClaimState(Enum):
    STATIC = b'static'
    CLAIMABLE = b'claimable'


class FrontlineRewardModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(FrontlineRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(9)

    def setId(self, value):
        self._setString(9, value)
        return

    def getClaimState(self):
        return ClaimState(self._getString(10))

    def setClaimState(self, value):
        self._setString(10, value.value)
        return

    def getType(self):
        return self._getString(11)

    def setType(self, value):
        self._setString(11, value)
        return

    def getOverlayType(self):
        return self._getString(12)

    def setOverlayType(self, value):
        self._setString(12, value)
        return

    def _initialize(self):
        super(FrontlineRewardModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'claimState')
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'overlayType', b'')
        return
