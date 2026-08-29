from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.universal_flag.details.universal_flag_background import UniversalFlagBackground

class VisibilityState(Enum):
    HIDDEN = b'hidden'
    SHOWN = b'shown'
    MAINTENANCE = b'maintenance'


class UniversalFlagEntryPointModel(ViewModel):
    __slots__ = (b'openEvent',)

    def __init__(self, properties=3, commands=1):
        super(UniversalFlagEntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def background(self):
        return self._getViewModel(0)

    @staticmethod
    def getBackgroundType():
        return UniversalFlagBackground

    def getVisibilityState(self):
        return VisibilityState(self._getString(1))

    def setVisibilityState(self, value):
        self._setString(1, value.value)
        return

    def getPrevState(self):
        return VisibilityState(self._getString(2))

    def setPrevState(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(UniversalFlagEntryPointModel, self)._initialize()
        self._addViewModelProperty(b'background', UniversalFlagBackground())
        self._addStringProperty(b'visibilityState')
        self._addStringProperty(b'prevState')
        self.openEvent = self._addCommand(b'openEvent')
        return
