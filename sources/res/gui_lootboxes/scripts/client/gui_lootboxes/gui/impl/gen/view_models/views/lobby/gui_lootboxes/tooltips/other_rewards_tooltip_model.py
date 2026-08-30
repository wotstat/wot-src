from enum import Enum
from frameworks.wulf import ViewModel

class OtherRewardType(Enum):
    ACCOUNTCUSTOMIZATIONS = b'accountCustomizations'
    BOOSTERS = b'boosters'
    CREW = b'crew'
    VEHICLECUSTOMIZATIONS = b'vehicleCustomizations'
    EQUIPMENTS = b'equipments'
    FEATUREITEMS = b'featureItems'
    LOOTBOXES = b'lootboxes'


class OtherRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(OtherRewardsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return OtherRewardType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(OtherRewardsTooltipModel, self)._initialize()
        self._addStringProperty(b'type')
        return
