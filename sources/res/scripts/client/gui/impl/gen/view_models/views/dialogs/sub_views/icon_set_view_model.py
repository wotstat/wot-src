from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_view_model import IconViewModel

class IconPositionLogicEnum(Enum):
    BOTTOMALIGNMENT = b'bottomAlignment'
    CENTREDANDTHROUGHCONTENT = b'centredAndThroughContent'
    MOVECONTENTBELOW = b'moveContentBelow'


class IconSetViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(IconSetViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def icon(self):
        return self._getViewModel(0)

    @staticmethod
    def getIconType():
        return IconViewModel

    def getBackgrounds(self):
        return self._getArray(1)

    def setBackgrounds(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getBackgroundsType():
        return IconViewModel

    def getOverlays(self):
        return self._getArray(2)

    def setOverlays(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getOverlaysType():
        return IconViewModel

    def getIconPositionLogic(self):
        return self._getString(3)

    def setIconPositionLogic(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(IconSetViewModel, self)._initialize()
        self._addViewModelProperty(b'icon', IconViewModel())
        self._addArrayProperty(b'backgrounds', Array())
        self._addArrayProperty(b'overlays', Array())
        self._addStringProperty(b'iconPositionLogic', b'centredAndThroughContent')
        return
