from __future__ import absolute_import
from gui.clans.clan_helpers import ClanListener
from gui.clans import formatters
from gui.Scaleform.daapi.view.meta.ClanPersonalInvitesWindowMeta import ClanPersonalInvitesWindowMeta
from gui.Scaleform.locale.CLANS import CLANS
from gui.shared.formatters import text_styles
from helpers.i18n import makeString as _ms

class ClanPersonalInvitesWindow(ClanPersonalInvitesWindowMeta, ClanListener):

    def __init__(self, *args, **kwargs):
        super(ClanPersonalInvitesWindow, self).__init__()
        return

    def onClanEnableChanged(self, enabled):
        if not enabled:
            self.onWindowClose()
        return

    def onAccountClanProfileChanged(self, profile):
        if profile.isInClan():
            self.destroy()
        return

    def onAccountInvitesReceived(self, invites):
        self._updateActualInvites()
        return

    def _populate(self):
        super(ClanPersonalInvitesWindow, self)._populate()
        self.startClanListening()
        self._updateActualInvites()
        return

    def _dispose(self):
        super(ClanPersonalInvitesWindow, self)._dispose()
        self.stopClanListening()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(ClanPersonalInvitesWindow, self)._onRegisterFlashComponent(viewPy, alias)
        viewPy.setParentWindow(self)
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _updateActualInvites(self):
        self.as_setActualInvitesTextS(_ms(CLANS.CLANPERSONALINVITESWINDOW_ACTUALINVITES, count=text_styles.stats(formatters.formatInvitesCount(self.webCtrl.getAccountProfile().getInvitesCount()))))
        return
