from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.tooltips.tankman_tooltip_view_icon_model import TankmanTooltipViewIconModel

class TankmanTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(TankmanTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def icons(self):
        return self._getViewModel(0)

    @staticmethod
    def getIconsType():
        return TankmanTooltipViewIconModel

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getSubtitle(self):
        return self._getString(2)

    def setSubtitle(self, value):
        self._setString(2, value)
        return

    def getMainIcon(self):
        return self._getString(3)

    def setMainIcon(self, value):
        self._setString(3, value)
        return

    def getDescription(self):
        return self._getString(4)

    def setDescription(self, value):
        self._setString(4, value)
        return

    def getIconsTitle(self):
        return self._getString(5)

    def setIconsTitle(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(TankmanTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'icons', UserListModel())
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'subtitle', b'')
        self._addStringProperty(b'mainIcon', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'iconsTitle', b'')
        return
