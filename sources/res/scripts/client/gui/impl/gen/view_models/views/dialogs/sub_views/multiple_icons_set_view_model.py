from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_view_model import IconViewModel

class IconPositionLogicEnum(Enum):
    BOTTOMALIGNMENT = b'bottomAlignment'
    CENTREDANDTHROUGHCONTENT = b'centredAndThroughContent'
    MOVECONTENTBELOW = b'moveContentBelow'


class MultipleIconsSetViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MultipleIconsSetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBackgrounds(self):
        return self._getArray(0)

    def setBackgrounds(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getBackgroundsType():
        return IconViewModel

    def getOverlays(self):
        return self._getArray(1)

    def setOverlays(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getOverlaysType():
        return IconViewModel

    def getIcons(self):
        return self._getArray(2)

    def setIcons(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getIconsType():
        return IconViewModel

    def getIconPositionLogic(self):
        return self._getString(3)

    def setIconPositionLogic(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(MultipleIconsSetViewModel, self)._initialize()
        self._addArrayProperty(b'backgrounds', Array())
        self._addArrayProperty(b'overlays', Array())
        self._addArrayProperty(b'icons', Array())
        self._addStringProperty(b'iconPositionLogic', b'centredAndThroughContent')
        return
