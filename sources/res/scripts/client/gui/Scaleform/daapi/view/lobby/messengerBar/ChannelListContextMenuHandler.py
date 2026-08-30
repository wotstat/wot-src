from __future__ import absolute_import
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import ChannelCarouselEvent

class CHANNEL(object):
    CLOSE_CURRENT = b'closeCurrent'
    MINIMIZE_ALL = b'minimizeAll'
    CLOSE_ALL_EXCEPT_CURRENT = b'closeAllExceptCurrent'


class ChannelListContextMenuHandler(AbstractContextMenuHandler, EventSystemEntity):

    def __init__(self, cmProxy, ctx=None):
        super(ChannelListContextMenuHandler, self).__init__(cmProxy, ctx, {(CHANNEL.MINIMIZE_ALL): b'minimizeAll', 
           (CHANNEL.CLOSE_CURRENT): b'closeCurrent', 
           (CHANNEL.CLOSE_ALL_EXCEPT_CURRENT): b'closeAllExceptCurrent'})
        return

    def closeCurrent(self):
        self.fireEvent(ChannelCarouselEvent(self, ChannelCarouselEvent.CLOSE_BUTTON_CLICK, self._clientID), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def minimizeAll(self):
        self.fireEvent(ChannelCarouselEvent(self, ChannelCarouselEvent.MINIMIZE_ALL_CHANNELS, None), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def closeAllExceptCurrent(self):
        self.fireEvent(ChannelCarouselEvent(self, ChannelCarouselEvent.CLOSE_ALL_EXCEPT_CURRENT, self._clientID), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _initFlashValues(self, ctx):
        self._clientID = int(ctx.clientID)
        self._canClose = bool(ctx.canClose)
        return

    def _clearFlashValues(self):
        self._clientID = None
        self._canClose = None
        return

    def _generateOptions(self, ctx=None):
        return [
         self._makeItem(CHANNEL.MINIMIZE_ALL, MENU.contextmenu(b'messenger/minimizeAll')),
         self._makeSeparator(),
         self._makeItem(CHANNEL.CLOSE_CURRENT, MENU.contextmenu(b'messenger/closeCurrent'), {b'enabled': (self._canClose)}),
         self._makeSeparator(),
         self._makeItem(CHANNEL.CLOSE_ALL_EXCEPT_CURRENT, MENU.contextmenu(b'messenger/closeAllExceptCurrent'))]
