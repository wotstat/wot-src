import enum, typing, VOIP
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from comp7_core.gui.battle_control.interfaces import IComp7VOIPController
_HTML_TEMPLATE = b'html_templates:comp7/voiceChat'

@enum.unique
class VoiceChatControlTextStyles(enum.Enum):
    FULL_STATS = b'fullStatsStyle'
    PLAYERS_PANEL = b'playersPanelStyle'


class Comp7VoipHelper(object):
    __slots__ = (b'__component', b'__textStyle', b'__enabled')
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, component, textStyle):
        self.__component = component
        self.__textStyle = textStyle
        self.__enabled = False
        return

    @property
    def _voipController(self):
        return self.__sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.COMP7_VOIP_CTRL)

    @property
    def __isVisible(self):
        voipCtrl = self._voipController
        return self.__enabled and voipCtrl is not None and voipCtrl.isTeamVoipEnabled

    @property
    def __isJoined(self):
        voipCtrl = self._voipController
        return self.__enabled and voipCtrl is not None and voipCtrl.isJoined

    def populate(self):
        component = self.__component
        component.as_setVoiceChatDataS({b'activeText': (self.__makeHtmlString(backport.text(R.strings.comp7_ext.voiceChat.active()))), 
           b'inactiveText': (self.__makeHtmlString(backport.text(R.strings.comp7_ext.voiceChat.inactive())))})
        self.__update()
        self.__subscribe()
        return

    def dispose(self):
        self.__unsubscribe()
        self.__component = None
        return

    def enable(self, enable):
        self.__enabled = enable
        self.__update()
        return

    def onVoiceChatControlClick(self):
        self._voipController.toggleChannelConnection()
        return

    def __subscribe(self):
        voipMgr = VOIP.getVOIPManager()
        if voipMgr is not None:
            voipMgr.onChannelAvailable += self.__update
            voipMgr.onChannelLost += self.__update
            voipMgr.onJoinedChannel += self.__update
            voipMgr.onLeftChannel += self.__update
        return

    def __unsubscribe(self):
        voipMgr = VOIP.getVOIPManager()
        if voipMgr is not None:
            voipMgr.onChannelAvailable -= self.__update
            voipMgr.onChannelLost -= self.__update
            voipMgr.onJoinedChannel -= self.__update
            voipMgr.onLeftChannel -= self.__update
        return

    def __update(self, *_, **__):
        self.__component.as_setVoiceChatControlVisibleS(self.__isVisible)
        self.__component.as_setVoiceChatControlSelectedS(self.__isJoined)
        return

    def __makeHtmlString(self, text):
        return makeHtmlString(_HTML_TEMPLATE, self.__textStyle.value, {b'message': text})
