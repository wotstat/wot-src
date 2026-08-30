from enum import Enum
from frameworks.wulf import ViewModel

class BannerTypeEnum(Enum):
    PM3ENTRYPOINTTEASER = b'PM3EntryPointTeaser'
    PM3ENTRYPOINTOPERATION1 = b'PM3EntryPointOperation1'
    PM3ENTRYPOINTOPERATION2 = b'PM3EntryPointOperation2'
    PM3ENTRYPOINTOPERATION3 = b'PM3EntryPointOperation3'


class Pm3BannerTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(Pm3BannerTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return BannerTypeEnum(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(Pm3BannerTooltipViewModel, self)._initialize()
        self._addStringProperty(b'type', BannerTypeEnum.PM3ENTRYPOINTTEASER.value)
        return
