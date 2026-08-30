import logging
from constants import PREBATTLE_TYPE_NAMES, PREBATTLE_TYPE, QUEUE_TYPE
from constants import QUEUE_TYPE_NAMES
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.formatters import getPrebattleFullDescription, getPrebattleStartTimeString
from gui.prb_control import prbDispatcherProperty, prbAutoInvitesProperty, prbInvitesProperty
from gui.prb_control.prb_helpers import getModeNameKwargs
from gui.prb_control.settings import PRB_INVITE_STATE
from gui.shared.system_factory import collectPrbInviteHtmlFormatter, registerPrbInvitesHtmlFormatter
from helpers import dependency
from helpers.html import escape as htmlEscape
from messenger.ext import passCensor
from shared_utils import CONST_CONTAINER
from skeletons.gui.game_control import IWinbackController
from skeletons.gui.lobby_context import ILobbyContext
_logger = logging.getLogger(__name__)
QUEUE_LEAVE_PREFIX = b'QUEUE_'
PREBATTLE_LEAVE_PREFIX = b'PREBATTLE_'
_R_INVITES = R.strings.invites.invites

class _PrbInvitePart(CONST_CONTAINER):
    TITLE_CREATOR_NAME = b'inviteTitleCreatorName'
    TITLE = b'inviteTitle'
    WARNING = b'inviteWarning'
    COMMENT = b'inviteComment'
    NOTE = b'inviteNote'
    STATE = b'inviteState'


_PRB_INVITE_PART_KEYS = {(_PrbInvitePart.TITLE_CREATOR_NAME): (b'name',), 
   (_PrbInvitePart.TITLE): (b'title', b'sender'), 
   (_PrbInvitePart.WARNING): (b'warning',), 
   (_PrbInvitePart.COMMENT): (b'comment',), 
   (_PrbInvitePart.NOTE): (b'note',), 
   (_PrbInvitePart.STATE): (b'state',)}

def _formatInvite(inviteType, values, maySkipValue=False, **kwargs):
    if all(values) or maySkipValue:
        return makeHtmlString(path=b'html_templates:lobby/prebattle', key=inviteType, ctx={k: v for k, v in zip(_PRB_INVITE_PART_KEYS[inviteType], values)}, **kwargs)
    return b''


def getPrbName(prbType, lowercase=False):
    try:
        prbName = PREBATTLE_TYPE_NAMES[prbType]
        if lowercase:
            prbName = prbName.lower()
    except KeyError:
        _logger.error(b'Prebattle name not found. %s', prbType)
        prbName = b'N/A'

    return prbName


def getPreQueueName(queueType, lowercase=False):
    try:
        queueName = QUEUE_TYPE_NAMES[queueType]
        if lowercase:
            queueName = queueName.lower()
    except KeyError:
        _logger.error(b'PreQueue name not found. %s', queueType)
        queueName = b'N/A'

    return queueName


def getPrbInviteStateName(state):
    try:
        stateName = PRB_INVITE_STATE.getKeyByValue(state)
    except KeyError:
        _logger.error(b'State of prebattle invite not found. %s', state)
        stateName = b'N/A'

    return stateName


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getAcceptNotAllowedText(prbType, peripheryID, isInviteActive=True, isAlreadyJoined=False, lobbyContext=None):
    isAnotherPeriphery = lobbyContext is not None and lobbyContext.isAnotherPeriphery(peripheryID)
    text = b''
    if isInviteActive:
        if isAlreadyJoined:
            text = backport.text(_R_INVITES.prebattle.alreadyJoined.dyn(getPrbName(prbType))())
        elif isAnotherPeriphery:
            host = lobbyContext.getPeripheryName(peripheryID)
            if host:
                text = backport.text(_R_INVITES.prebattle.acceptNotAllowed.otherPeriphery(), host=host)
            else:
                text = backport.text(_R_INVITES.prebattle.acceptNotAllowed.undefinedPeriphery())
            text = (b' ').join((text, backport.text(_R_INVITES.note.serverSelectionIsRemembered())))
    return text


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext, winbackController=IWinbackController)
def getLeaveOrChangeText(funcState, invitePrbType, peripheryID, lobbyContext=None, winbackController=None):
    isAnotherPeriphery = lobbyContext is not None and lobbyContext.isAnotherPeriphery(peripheryID)
    text = b''
    if funcState.doLeaveToAcceptInvite(invitePrbType):
        if funcState.isInLegacy() or funcState.isInUnit():
            entityName = PREBATTLE_LEAVE_PREFIX + getPrbName(funcState.entityTypeID)
            kwargs = getModeNameKwargs(funcState.entityTypeID, isQueue=False)
        elif funcState.isInPreQueue() and funcState.entityTypeID:
            entityName = QUEUE_LEAVE_PREFIX + getPreQueueName(funcState.entityTypeID)
            kwargs = getModeNameKwargs(funcState.entityTypeID)
        else:
            _logger.error(b'Can not resolve name of entity. %s', funcState)
            return text
        isInWinback = funcState.isInPreQueue(QUEUE_TYPE.WINBACK)
        isPermanentlyWinbackLeave = winbackController is not None and winbackController.isModeAvailable() and invitePrbType == PREBATTLE_TYPE.SQUAD
        if isAnotherPeriphery:
            if not isInWinback or not isPermanentlyWinbackLeave:
                text = backport.text(_R_INVITES.note.change_and_leave.dyn(entityName)(), host=(lobbyContext.getPeripheryName(peripheryID) or b''), **kwargs)
            if isPermanentlyWinbackLeave:
                if text:
                    text = (b'').join((text, b'\n\n'))
                permanentlyLeaveText = backport.text(_R_INVITES.note.change_and_leave_permanently.QUEUE_WINBACK(), host=lobbyContext.getPeripheryName(peripheryID) or b'')
                text = (b'').join((text, permanentlyLeaveText))
            text = (b' ').join((text, backport.text(_R_INVITES.note.serverSelectionIsRemembered())))
        else:
            if not isInWinback or not isPermanentlyWinbackLeave:
                text = backport.text(_R_INVITES.note.leave.dyn(entityName)(), **kwargs)
            if isPermanentlyWinbackLeave:
                if text:
                    text = (b'').join((text, b'\n\n'))
                text = (b'').join((text, backport.text(_R_INVITES.note.leave_permanently.QUEUE_WINBACK())))
    elif isAnotherPeriphery:
        text = backport.text(_R_INVITES.note.server_change(), host=lobbyContext.getPeripheryName(peripheryID) or b'')
        text = (b' ').join((text, backport.text(_R_INVITES.note.serverSelectionIsRemembered())))
    return text


class InviteFormatter(object):

    def getCtx(self, invite):
        return {b'sender': (invite.senderFullName), 
           b'receiver': (invite.receiverFullName)}

    def getNote(self, invite):
        return b''

    def getText(self, invite):
        return b''


class PrbInviteHtmlTextFormatter(InviteFormatter):

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @prbInvitesProperty
    def prbInvites(self):
        return

    def canAcceptInvite(self, invite):
        return self.prbInvites.canAcceptInvite(invite)

    def getIconName(self, invite):
        return (b'{0:>s}InviteIcon').format(getPrbName(invite.type, True))

    def getIconPath(self, invite, pathMaker=None):
        return pathMaker(self.getIconName(invite))

    def getTitle(self, invite):
        creatorName = _formatInvite(_PrbInvitePart.TITLE_CREATOR_NAME, (invite.senderFullName,))
        return _formatInvite(_PrbInvitePart.TITLE, (self._getTitle(invite), creatorName), True)

    def getWarning(self, invite):
        warning = backport.text(_R_INVITES.warning.dyn(invite.warning)()) if invite.warning else b''
        return _formatInvite(_PrbInvitePart.WARNING, (warning,))

    def getComment(self, invite):
        comment = passCensor(invite.comment)
        comment = backport.text(_R_INVITES.comment(), comment=htmlEscape(comment)) if comment else b''
        return _formatInvite(_PrbInvitePart.COMMENT, (comment,))

    def getNote(self, invite):
        if self.canAcceptInvite(invite):
            note = getLeaveOrChangeText(self.prbDispatcher.getFunctionalState(), invite.type, invite.peripheryID) if self.prbDispatcher else b''
        else:
            note = getAcceptNotAllowedText(invite.type, invite.peripheryID, invite.isActive(), invite.alreadyJoined)
        return _formatInvite(_PrbInvitePart.NOTE, (note,))

    def getState(self, invite):
        inviteState = invite.getState()
        state = backport.text(_R_INVITES.state.dyn(getPrbInviteStateName(inviteState))()) if inviteState else b''
        return _formatInvite(_PrbInvitePart.STATE, (state,))

    def getText(self, invite):
        result = []
        text = self.getTitle(invite)
        if text:
            result.append(text)
        text = self.getWarning(invite)
        if text:
            result.append(text)
        text = self.getComment(invite)
        if text:
            result.append(text)
        text = self.getNote(invite)
        if text:
            result.append(text)
        text = self.getState(invite)
        if text:
            result.append(text)
        return (b'').join(result)

    def updateTooltips(self, invite, canAccept, message):
        return message

    def _getTitle(self, invite):
        kwargs = getModeNameKwargs(invite.type, isQueue=False)
        return backport.text(R.strings.invites.invites.text.dyn(getPrbName(invite.type))(), **kwargs)


class PrbExternalBattleInviteHtmlTextFormatter(PrbInviteHtmlTextFormatter):

    def getComment(self, invite):
        comment = passCensor(invite.comment)
        return _formatInvite(_PrbInvitePart.COMMENT, (htmlEscape(comment),))


class PrbInviteTitleFormatter(InviteFormatter):

    def getText(self, _):
        return backport.text(R.strings.invites.gui.titles.invite())


class AutoInviteTextFormatter(InviteFormatter):

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @prbAutoInvitesProperty
    def prbAutoInvites(self):
        return

    def getNote(self, invite):
        note = b''
        if self.prbAutoInvites.canAcceptInvite(invite):
            if self.prbAutoInvites:
                note = getLeaveOrChangeText(self.prbDispatcher.getFunctionalState(), invite.prbType, invite.peripheryID)
        else:
            note = getAcceptNotAllowedText(invite.prbType, invite.peripheryID)
        return note

    def getText(self, invite):
        startTimeStr = (u'{} {}').format(backport.text(R.strings.prebattle.title.battleSession.startTime()), getPrebattleStartTimeString(invite.startTime))
        return (u'{}, {}').format(getPrebattleFullDescription(invite.description), startTimeStr)


class _PrbInviteInfo(object):

    def as_dict(self):
        raise NotImplementedError
        return


class PrbAutoInviteInfo(_PrbInviteInfo):

    def __init__(self, prbID):
        self.__prbID = prbID
        return

    @prbAutoInvitesProperty
    def prbAutoInvites(self):
        return

    def getID(self):
        return self.__prbID

    def getTitle(self):
        return PrbInviteTitleFormatter().getText(None)

    def as_dict(self):
        invite = self.prbAutoInvites.getInvite(self.__prbID)
        canAccept = self.prbAutoInvites.canAcceptInvite(invite)
        formatter = AutoInviteTextFormatter()
        result = {b'id': (self.__prbID), 
           b'text': (formatter.getText(invite)), 
           b'comment': b'', 
           b'note': (formatter.getNote(invite)), 
           b'canAccept': canAccept, 
           b'canDecline': True, 
           b'isAcceptVisible': True, 
           b'isDeclineVisible': False}
        return result


registerPrbInvitesHtmlFormatter(PREBATTLE_TYPE.EXTERNAL_PREBATTLES, PrbExternalBattleInviteHtmlTextFormatter)

def getPrbInviteHtmlFormatter(invite):
    formatter = collectPrbInviteHtmlFormatter(invite.type)
    return formatter or PrbInviteHtmlTextFormatter()
