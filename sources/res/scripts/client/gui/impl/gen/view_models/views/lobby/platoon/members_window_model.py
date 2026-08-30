from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.platoon.button_find_players_cancel_search_model import ButtonFindPlayersCancelSearchModel
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel
from gui.impl.gen.view_models.views.lobby.platoon.button_switch_ready_model import ButtonSwitchReadyModel
from gui.impl.gen.view_models.views.lobby.platoon.slot_model import SlotModel
from gui.impl.gen.view_models.views.lobby.platoon.window_header_model import WindowHeaderModel
from gui.impl.gen.view_models.windows.window_model import WindowModel

class PrebattleTypes(Enum):
    SQUAD = b'squad'
    EVENT = b'event'
    EPIC = b'epic'
    BATTLEROYAL = b'battle_royal'
    MAPBOX = b'mapbox'
    COMP7 = b'comp7'
    COMP7LIGHT = b'comp7_light'
    FUNRANDOM = b'funRandom'


class MembersWindowModel(WindowModel):
    __slots__ = (b'onFocusChange',)

    def __init__(self, properties=17, commands=3):
        super(MembersWindowModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def btnInviteFriends(self):
        return self._getViewModel(3)

    @staticmethod
    def getBtnInviteFriendsType():
        return ButtonModel

    @property
    def btnSwitchReady(self):
        return self._getViewModel(4)

    @staticmethod
    def getBtnSwitchReadyType():
        return ButtonSwitchReadyModel

    @property
    def btnFindPlayers(self):
        return self._getViewModel(5)

    @staticmethod
    def getBtnFindPlayersType():
        return ButtonFindPlayersCancelSearchModel

    @property
    def header(self):
        return self._getViewModel(6)

    @staticmethod
    def getHeaderType():
        return WindowHeaderModel

    def getSlots(self):
        return self._getArray(7)

    def setSlots(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getSlotsType():
        return SlotModel

    def getIsHorizontal(self):
        return self._getBool(8)

    def setIsHorizontal(self, value):
        self._setBool(8, value)
        return

    def getIsShort(self):
        return self._getBool(9)

    def setIsShort(self, value):
        self._setBool(9, value)
        return

    def getWindowTooltipHeader(self):
        return self._getString(10)

    def setWindowTooltipHeader(self, value):
        self._setString(10, value)
        return

    def getWindowTooltipBody(self):
        return self._getString(11)

    def setWindowTooltipBody(self, value):
        self._setString(11, value)
        return

    def getIsCommander(self):
        return self._getBool(12)

    def setIsCommander(self, value):
        self._setBool(12, value)
        return

    def getShouldShowFindPlayersButton(self):
        return self._getBool(13)

    def setShouldShowFindPlayersButton(self, value):
        self._setBool(13, value)
        return

    def getFooterMessage(self):
        return self._getString(14)

    def setFooterMessage(self, value):
        self._setString(14, value)
        return

    def getIsFooterMessageGrey(self):
        return self._getBool(15)

    def setIsFooterMessageGrey(self, value):
        self._setBool(15, value)
        return

    def getPrebattleType(self):
        return PrebattleTypes(self._getString(16))

    def setPrebattleType(self, value):
        self._setString(16, value.value)
        return

    def _initialize(self):
        super(MembersWindowModel, self)._initialize()
        self._addViewModelProperty(b'btnInviteFriends', ButtonModel())
        self._addViewModelProperty(b'btnSwitchReady', ButtonSwitchReadyModel())
        self._addViewModelProperty(b'btnFindPlayers', ButtonFindPlayersCancelSearchModel())
        self._addViewModelProperty(b'header', WindowHeaderModel())
        self._addArrayProperty(b'slots', Array())
        self._addBoolProperty(b'isHorizontal', False)
        self._addBoolProperty(b'isShort', False)
        self._addStringProperty(b'windowTooltipHeader', b'')
        self._addStringProperty(b'windowTooltipBody', b'')
        self._addBoolProperty(b'isCommander', False)
        self._addBoolProperty(b'shouldShowFindPlayersButton', True)
        self._addStringProperty(b'footerMessage', b'')
        self._addBoolProperty(b'isFooterMessageGrey', False)
        self._addStringProperty(b'prebattleType')
        self.onFocusChange = self._addCommand(b'onFocusChange')
        return
