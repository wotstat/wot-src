import weakref, constants
from debug_utils import LOG_DEBUG
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.daapi.view.meta.ChannelComponentMeta import ChannelComponentMeta
from gui.impl.gen import R
from helpers import dependency
from messenger.gui import events_dispatcher
from messenger.proto.bw_chat2.wrappers import UnitDataFactory
from skeletons.gui.app_loader import IAppLoader
_R_SQUAD = R.strings.messenger.dialogs.squadChannel

class ChannelComponent(ChannelComponentMeta):
    __appLoader = dependency.descriptor(IAppLoader)

    def __init__(self):
        super(ChannelComponent, self).__init__()
        self._controller = lambda : None
        return

    def __del__(self):
        LOG_DEBUG(b'ChannelComponent deleted', self)
        return

    def setController(self, controller):
        controller.activate()
        events_dispatcher.notifyCarousel(controller.getChannel().getClientID(), notify=False)
        self._controller = weakref.ref(controller)
        if self.flashObject:
            self.as_setJoinedS(controller.isJoined())
        if self.flashObject:
            self.as_setLastUnsentMessageS(controller.getMemInputText())
        return

    def removeController(self):
        if self.flashObject and self._controller():
            self._controller().setMemInputText(self.as_getLastUnsentMessageS())
        self._controller = lambda : None
        if self.flashObject:
            self.as_setJoinedS(False)
        return

    def close(self):
        ctrl = self._controller()
        if ctrl:
            ctrl.exit()
        return

    def minimize(self):
        ctrl = self._controller()
        if ctrl:
            if self.flashObject:
                ctrl.setMemInputText(self.as_getLastUnsentMessageS())
            ctrl.deactivate()
        return

    def getMessageMaxLength(self):
        return round(constants.CHAT_MESSAGE_MAX_LENGTH / 2, 0)

    def onLinkClick(self, data):
        contextMenuMgr = self.__appLoader.getApp().contextMenuManager
        if contextMenuMgr is not None:
            databaseID, userName = data.split(b':')
            ctx = {b'dbID': databaseID, 
               b'userName': userName}
            contextMenuMgr.show(CONTEXT_MENU_HANDLER_TYPE.BASE_USER_APPEAL, ctx)
        return

    def isJoined(self):
        isJoined = False
        if self._controller():
            isJoined = self._controller().isJoined()
        return isJoined

    def sendMessage(self, message):
        result = False
        if self._controller():
            result = self._controller().sendMessage(message)
        return result

    def getHistory(self):
        result = b''
        if self._controller():
            result = (b'\n').join(self._controller().getHistory())
        return result

    def addNotification(self, text):
        factory = UnitDataFactory()
        message = factory.messageVO(factory.broadcastArgs(text))
        self._controller().addMessage(message, False)
        return

    def getLastUnsentMessage(self):
        result = b''
        return result

    def setLastUnsentMessage(self, message):
        LOG_DEBUG(b'ChannelComponent setLastUnsentMessage ', message, self)
        return

    def addMessage(self, message):
        self.as_addMessageS(message)
        return

    def addCommand(self, cmd):
        return
