from __future__ import absolute_import
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.clans import formatters as clans_fmts
from gui.shared import event_dispatcher, utils
from shared_utils import CONST_CONTAINER

class CLAN_CM_OPTIONS(CONST_CONTAINER):
    CLAN_PROFILE = b'clanProfile'
    COPY_TO_CB = b'copyToClipboard'


class BaseClanCMHandler(AbstractContextMenuHandler, EventSystemEntity):

    def __init__(self, cmProxy, ctx=None):
        super(BaseClanCMHandler, self).__init__(cmProxy, ctx, {(CLAN_CM_OPTIONS.CLAN_PROFILE): b'showClanProfile', 
           (CLAN_CM_OPTIONS.COPY_TO_CB): b'copyToClipboard'})
        self.__clanDbID = int(ctx.dbID)
        self.__clanName = ctx.clanName
        self.__clanAbbrev = ctx.clanAbbrev
        return

    def showClanProfile(self):
        event_dispatcher.showClanProfileWindow(self.__clanDbID, self.__clanAbbrev)
        return

    def copyToClipboard(self):
        utils.copyToClipboard(clans_fmts.getClanFullName(self.__clanName, self.__clanAbbrev))
        return

    def _generateOptions(self, ctx=None):
        return [
         self._makeItem(CLAN_CM_OPTIONS.CLAN_PROFILE, MENU.contextmenu(b'viewClanProfile')),
         self._makeItem(CLAN_CM_OPTIONS.COPY_TO_CB, MENU.contextmenu(b'copyClanName'))]
