from PlayerEvents import g_playerEvents
from adisp import adisp_process
from gui import DialogsInterface
from gui.Scaleform.daapi.view.meta.ReceivedInviteWindowMeta import ReceivedInviteWindowMeta
from gui.prb_control import prbPeripheriesHandlerProperty, prbAutoInvitesProperty
from gui.prb_control.formatters.invites import PrbAutoInviteInfo
from gui.prb_control.entities.battle_session.legacy.ctx import JoinBattleSessionCtx
from gui.prb_control.entities.listener import IGlobalListener
from gui.prb_control.prb_getters import getPrebattleAutoInvites
from gui.shared import actions
from messenger.ext import channel_num_gen
from messenger.gui import events_dispatcher
from messenger.m_constants import LAZY_CHANNEL
from predefined_hosts import g_preDefinedHosts
__author__ = b'd_savitski'

class _DisableNotify(actions.Action):

    def __init__(self, clientID):
        super(_DisableNotify, self).__init__()
        self.__clientID = clientID
        return

    def invoke(self):
        events_dispatcher.notifyCarousel(self.__clientID, notify=False)
        self._completed = True
        return


class _InviteWindow(IGlobalListener, ReceivedInviteWindowMeta):

    def __init__(self, inviteInfo):
        super(_InviteWindow, self).__init__()
        self._inviteInfo = inviteInfo
        return

    def onPrbEntitySwitched(self):
        self._updateReceivedInfo()
        return

    def onTeamStatesReceived(self, entity, team1State, team2State):
        self._updateReceivedInfo()
        return

    def onUnitFlagsChanged(self, flags, timeLeft):
        self._updateReceivedInfo()
        return

    def cancelInvite(self):
        self.onWindowClose()
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _populate(self):
        super(_InviteWindow, self)._populate()
        self.startGlobalListening()
        self.as_setTitleS(self._inviteInfo.getTitle())
        self._updateReceivedInfo()
        return

    def _dispose(self):
        self._inviteInfo = None
        self.stopGlobalListening()
        super(_InviteWindow, self)._dispose()
        return

    def _updateReceivedInfo(self):
        self.as_setReceivedInviteInfoS(self._inviteInfo.as_dict())
        return


class AutoInviteWindow(_InviteWindow):

    def __init__(self, ctx):
        super(AutoInviteWindow, self).__init__(PrbAutoInviteInfo(ctx.get(b'prbID')))
        return

    @prbPeripheriesHandlerProperty
    def prbPeripheriesHandler(self):
        return

    @prbAutoInvitesProperty
    def prbAutoInvites(self):
        return

    @adisp_process
    def acceptInvite(self):
        yield lambda callback: callback(None)
        prbID = self._inviteInfo.getID()
        invite = self.prbAutoInvites.getInvite(prbID)
        postActions = [
         actions.LeavePrbModalEntity()]
        finishActions = [
         _DisableNotify(channel_num_gen.getClientID4LazyChannel(LAZY_CHANNEL.SPECIAL_BATTLES))]
        if g_preDefinedHosts.isRoamingPeriphery(invite.peripheryID):
            success = yield DialogsInterface.showI18nConfirmDialog(b'changeRoamingPeriphery')
            if not success:
                return
        self.prbPeripheriesHandler.join(invite.peripheryID, JoinBattleSessionCtx(prbID, invite.prbType, b'prebattle/join'), postActions, finishActions)
        return

    def declineInvite(self):
        self.onWindowClose()
        return

    def _populate(self):
        super(AutoInviteWindow, self)._populate()
        g_playerEvents.onPrebattleAutoInvitesChanged += self.__onPrbAutoInvitesChanged
        return

    def _dispose(self):
        g_playerEvents.onPrebattleAutoInvitesChanged -= self.__onPrbAutoInvitesChanged
        super(AutoInviteWindow, self)._dispose()
        return

    def __onPrbAutoInvitesChanged(self):
        if self._inviteInfo.getID() not in getPrebattleAutoInvites():
            self.destroy()
        return
