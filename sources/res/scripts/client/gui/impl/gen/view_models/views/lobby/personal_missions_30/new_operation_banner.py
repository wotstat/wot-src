from enum import Enum
from frameworks.wulf import ViewModel

class BannerState(Enum):
    DEFAULT = b'default'
    COMPLETED_WITH_HONOR = b'completedWithHonor'
    COMPLETED = b'completed'


class NewOperationBanner(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NewOperationBanner, self).__init__(properties=properties, commands=commands)
        return

    def getOperationId(self):
        return self._getNumber(0)

    def setOperationId(self, value):
        self._setNumber(0, value)
        return

    def getBannerState(self):
        return BannerState(self._getString(1))

    def setBannerState(self, value):
        self._setString(1, value.value)
        return

    def getFirstTimeEntrance(self):
        return self._getBool(2)

    def setFirstTimeEntrance(self, value):
        self._setBool(2, value)
        return

    def getEnabled(self):
        return self._getBool(3)

    def setEnabled(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(NewOperationBanner, self)._initialize()
        self._addNumberProperty(b'operationId', 0)
        self._addStringProperty(b'bannerState', BannerState.DEFAULT.value)
        self._addBoolProperty(b'firstTimeEntrance', True)
        self._addBoolProperty(b'enabled', True)
        return
