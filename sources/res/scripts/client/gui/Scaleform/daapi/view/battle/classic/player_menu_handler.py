from gui.Scaleform.daapi.view.lobby.user_cm_handlers import USER
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.battle_control.arena_info.settings import INVITATION_DELIVERY_STATUS as _D_STATUS
from gui.shared import events, EVENT_BUS_SCOPE, g_eventBus
from gui.shared.denunciator import DENUNCIATIONS, BattleDenunciator, DENUNCIATIONS_MAP
from helpers import dependency
from helpers import i18n
from constants import IS_CHINA
from messenger.m_constants import PROTO_TYPE, UserEntityScope
from messenger.proto import proto_getter
from messenger.storage import storage_getter
from skeletons.gui.battle_session import IBattleSessionProvider

class DYN_SQUAD_OPTION_ID(object):
    SENT_INVITATION = b'sendInvitationToSquad'
    ACCEPT_INVITATION = b'acceptInvitationToSquad'
    REJECT_INVITATION = b'rejectInvitationToSquad'
    IN_SQUAD = b'inSquad'


class BATTLE_CHAT_OPTION_ID(object):
    ENABLE_COMMUNICATIONS = b'enableCommunications'
    DISABLE_COMMUNICATIONS = b'disableCommunications'


_OPTIONS_HANDLERS = {(USER.ADD_TO_FRIENDS): b'addFriend', 
   (USER.REMOVE_FROM_FRIENDS): b'removeFriend', 
   (USER.ADD_TO_IGNORED): b'setIgnored', 
   (USER.REMOVE_FROM_IGNORED): b'unsetIgnored', 
   (BATTLE_CHAT_OPTION_ID.ENABLE_COMMUNICATIONS): b'enableCommunications', 
   (BATTLE_CHAT_OPTION_ID.DISABLE_COMMUNICATIONS): b'disableCommunications', 
   (DENUNCIATIONS.INCORRECT_BEHAVIOR): b'appealIncorrectBehavior', 
   (DENUNCIATIONS.NOT_FAIR_PLAY): b'appealNotFairPlay', 
   (DENUNCIATIONS.FORBIDDEN_NICK): b'appealForbiddenNick', 
   (DENUNCIATIONS.BOT): b'appealBot', 
   (DYN_SQUAD_OPTION_ID.SENT_INVITATION): b'sendInvitation', 
   (DYN_SQUAD_OPTION_ID.ACCEPT_INVITATION): b'acceptInvitation', 
   (DYN_SQUAD_OPTION_ID.REJECT_INVITATION): b'rejectInvitation'}
if not IS_CHINA:
    _OPTIONS_HANDLERS.update({(USER.SET_MUTED): b'setMuted', 
       (USER.UNSET_MUTED): b'unsetMuted'})
_OPTION_ICONS = {(USER.ADD_TO_FRIENDS): b'addToFriends', 
   (USER.REMOVE_FROM_FRIENDS): b'removeFromFriends', 
   (USER.ADD_TO_IGNORED): b'addToBlacklist', 
   (USER.REMOVE_FROM_IGNORED): b'removeFromBlacklist', 
   (BATTLE_CHAT_OPTION_ID.ENABLE_COMMUNICATIONS): b'enableCommunications', 
   (BATTLE_CHAT_OPTION_ID.DISABLE_COMMUNICATIONS): b'disableCommunications', 
   (DYN_SQUAD_OPTION_ID.SENT_INVITATION): b'addToSquad', 
   (DYN_SQUAD_OPTION_ID.IN_SQUAD): b'inSquad', 
   (DYN_SQUAD_OPTION_ID.ACCEPT_INVITATION): b'acceptInvitation', 
   (DYN_SQUAD_OPTION_ID.REJECT_INVITATION): b'rejectInvitation'}
if not IS_CHINA:
    _OPTION_ICONS.update({(USER.SET_MUTED): b'disableVoice', 
       (USER.UNSET_MUTED): b'enableVoice'})
_BOT_NO_ACTIONS_OPTION_ID = b'botNoActions'

class PlayerContextMenuInfo(object):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __slots__ = (b'avatarSessionID', b'isBot', b'isFriend', b'isIgnored', b'isTemporaryIgnored', b'isMuted', b'userName', b'isAlly', b'battleUser')

    def __init__(self, avatarSessionID, userName):
        super(PlayerContextMenuInfo, self).__init__()
        self.avatarSessionID = avatarSessionID
        self.isBot = not avatarSessionID
        self.isFriend = False
        self.isIgnored = False
        self.isTemporaryIgnored = False
        self.isMuted = False
        self.userName = userName
        self.isAlly = self.sessionProvider.getCtx().isAlly(avatarSessionID=avatarSessionID)
        self.battleUser = self.usersStorage.getUser(avatarSessionID, scope=UserEntityScope.BATTLE)
        if self.battleUser is not None:
            self.isFriend = self.battleUser.isFriend()
            self.isIgnored = self.battleUser.isIgnored()
            self.isTemporaryIgnored = self.battleUser.isTemporaryIgnored()
            self.isMuted = self.battleUser.isMuted()
        return

    @storage_getter(b'users')
    def usersStorage(self):
        return


class PlayerMenuHandler(AbstractContextMenuHandler):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, cmProxy, ctx=None):
        self.__denunciator = BattleDenunciator()
        self.__arenaUniqueID = BattleDenunciator.getArenaUniqueID()
        g_eventBus.addListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(PlayerMenuHandler, self).__init__(cmProxy, ctx=ctx, handlers=_OPTIONS_HANDLERS)
        return

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return

    @property
    def arenaVisitor(self):
        return self.sessionProvider.arenaVisitor

    def fini(self):
        g_eventBus.removeListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.__denunciator = None
        super(PlayerMenuHandler, self).fini()
        return

    def addFriend(self):
        self.sessionProvider.shared.anonymizerFakesCtrl.addBattleFriend(self.__userInfo.avatarSessionID)
        return

    def removeFriend(self):
        self.sessionProvider.shared.anonymizerFakesCtrl.removeBattleFriend(self.__userInfo.avatarSessionID)
        return

    def setIgnored(self):
        self.sessionProvider.shared.anonymizerFakesCtrl.addBattleIgnored(self.__userInfo.avatarSessionID)
        return

    def unsetIgnored(self):
        self.sessionProvider.shared.anonymizerFakesCtrl.removeBattleIgnored(self.__userInfo.avatarSessionID)
        return

    def disableCommunications(self):
        self.sessionProvider.shared.anonymizerFakesCtrl.addTmpIgnored(self.__userInfo.avatarSessionID, self.__userInfo.userName)
        return

    def enableCommunications(self):
        self.sessionProvider.shared.anonymizerFakesCtrl.removeTmpIgnored(self.__userInfo.avatarSessionID)
        return

    def setMuted(self):
        self.sessionProvider.shared.anonymizerFakesCtrl.mute(self.__userInfo.avatarSessionID, self.__userInfo.userName)
        return

    def unsetMuted(self):
        self.sessionProvider.shared.anonymizerFakesCtrl.unmute(self.__userInfo.avatarSessionID)
        return

    def appealIncorrectBehavior(self):
        self.__denunciator.makeAppeal(self.__vInfo.vehicleID, self.__userInfo.userName, DENUNCIATIONS.INCORRECT_BEHAVIOR, self.__arenaUniqueID)
        return

    def appealNotFairPlay(self):
        self.__denunciator.makeAppeal(self.__vInfo.vehicleID, self.__userInfo.userName, DENUNCIATIONS.NOT_FAIR_PLAY, self.__arenaUniqueID)
        return

    def appealForbiddenNick(self):
        self.__denunciator.makeAppeal(self.__vInfo.vehicleID, self.__userInfo.userName, DENUNCIATIONS.FORBIDDEN_NICK, self.__arenaUniqueID)
        return

    def appealBot(self):
        self.__denunciator.makeAppeal(self.__vInfo.vehicleID, self.__userInfo.userName, DENUNCIATIONS.BOT, self.__arenaUniqueID)
        return

    def sendInvitation(self):
        self.sessionProvider.invitations.send(self.__userInfo.avatarSessionID)
        return

    def acceptInvitation(self):
        self.sessionProvider.invitations.accept(self.__userInfo.avatarSessionID)
        return

    def rejectInvitation(self):
        self.sessionProvider.invitations.reject(self.__userInfo.avatarSessionID)
        return

    def _initFlashValues(self, ctx):
        self.__vInfo = self.sessionProvider.getArenaDP().getVehicleInfo(ctx.vehicleID)
        player = self.__vInfo.player
        self.__userInfo = PlayerContextMenuInfo(player.avatarSessionID, player.name)
        return

    def _clearFlashValues(self):
        self.__userInfo = None
        self.__vInfo = None
        return

    def _generateOptions(self, ctx=None):
        options = []
        if self.sessionProvider.isReplayPlaying:
            return options
        if not self.__userInfo.isBot:
            options = self.__addDynSquadInfo(options)
            options = self.__addFriendshipInfo(options)
            options = self.__addIgnoreInfo(options)
            options = self.__addCommunicationInfo(options)
            if not IS_CHINA:
                options = self.__addMutedInfo(options)
            options = self.__addDenunciationsInfo(options)
        else:
            options = self.__addBotInfo(options)
        return options

    @classmethod
    def _getOptionIcon(cls, optionID):
        return _OPTION_ICONS.get(optionID, b'')

    @classmethod
    def _getOptionInitData(cls, optionID, isEnabled=True):
        return {b'enabled': isEnabled, 
           b'iconType': (cls._getOptionIcon(optionID))}

    def __addDynSquadInfo(self, options):
        make = self._makeItem
        ctx = self.sessionProvider.getCtx()
        if not self.arenaVisitor.hasDynSquads():
            return options
        else:
            if not ctx.isInvitationEnabled() or ctx.hasSquadRestrictions():
                return options
            if not self.__userInfo.isAlly:
                return options
            isIgnored = self.__userInfo.isIgnored
            status = self.__vInfo.invitationDeliveryStatus
            if status & _D_STATUS.FORBIDDEN_BY_RECEIVER > 0 or status & _D_STATUS.RECEIVED_FROM > 0 and not status & _D_STATUS.RECEIVED_INACTIVE or status & _D_STATUS.SENT_TO > 0 and not status & _D_STATUS.SENT_INACTIVE:
                optionID = DYN_SQUAD_OPTION_ID.SENT_INVITATION
                isEnabled = False
            elif self.__vInfo.isSquadMan():
                optionID = DYN_SQUAD_OPTION_ID.IN_SQUAD
                isEnabled = False
            else:
                optionID = DYN_SQUAD_OPTION_ID.SENT_INVITATION
                isEnabled = not isIgnored
            if optionID is not None:
                options.append(self._makeItem(optionID, MENU.contextmenu(optionID), optInitData=self._getOptionInitData(optionID, isEnabled)))
            if status & _D_STATUS.RECEIVED_FROM > 0 and not status & _D_STATUS.RECEIVED_INACTIVE:
                options.append(make(DYN_SQUAD_OPTION_ID.ACCEPT_INVITATION, MENU.contextmenu(DYN_SQUAD_OPTION_ID.ACCEPT_INVITATION), optInitData=self._getOptionInitData(DYN_SQUAD_OPTION_ID.ACCEPT_INVITATION, not isIgnored)))
                options.append(make(DYN_SQUAD_OPTION_ID.REJECT_INVITATION, MENU.contextmenu(DYN_SQUAD_OPTION_ID.REJECT_INVITATION), optInitData=self._getOptionInitData(DYN_SQUAD_OPTION_ID.REJECT_INVITATION, not isIgnored)))
            return options

    def __addFriendshipInfo(self, options):
        isEnabled = True
        if self.__userInfo.isFriend:
            optionID = USER.REMOVE_FROM_FRIENDS
        else:
            optionID = USER.ADD_TO_FRIENDS
        options.append(self._makeItem(optionID, MENU.contextmenu(optionID), optInitData=self._getOptionInitData(optionID, isEnabled)))
        return options

    def __addIgnoreInfo(self, options):
        isEnabled = True
        if self.__userInfo.isTemporaryIgnored:
            optionID = USER.ADD_TO_IGNORED
            isEnabled = False
        elif self.__userInfo.isIgnored:
            optionID = USER.REMOVE_FROM_IGNORED
        else:
            optionID = USER.ADD_TO_IGNORED
        options.append(self._makeItem(optionID, MENU.contextmenu(optionID), optInitData=self._getOptionInitData(optionID, isEnabled)))
        return options

    def __addCommunicationInfo(self, options):
        isForbiddenBattleType = self.arenaVisitor.gui.isTrainingBattle()
        if not isForbiddenBattleType:
            isEnabled = True
            if self.__userInfo.isTemporaryIgnored:
                optionID = BATTLE_CHAT_OPTION_ID.ENABLE_COMMUNICATIONS
            elif not self.__userInfo.isIgnored:
                optionID = BATTLE_CHAT_OPTION_ID.DISABLE_COMMUNICATIONS
            else:
                optionID = BATTLE_CHAT_OPTION_ID.DISABLE_COMMUNICATIONS
                isEnabled = False
            options.append(self._makeItem(optionID, MENU.contextmenu(optionID), optInitData=self._getOptionInitData(optionID, isEnabled)))
        return options

    def __addMutedInfo(self, options):
        isVisible = self.bwProto.voipController.isVOIPEnabled() and (self.__userInfo.isAlly or self.arenaVisitor.gui.isTrainingBattle())
        isEnabled = not self.__userInfo.isIgnored or self.__userInfo.isTemporaryIgnored
        if self.__userInfo.isMuted:
            optionID = USER.UNSET_MUTED
        else:
            optionID = USER.SET_MUTED
        if isVisible:
            options.append(self._makeItem(optionID, MENU.contextmenu(optionID), optInitData=self._getOptionInitData(optionID, isEnabled)))
        return options

    def __isAppealsForTopicEnabled(self, topic):
        topicID = DENUNCIATIONS_MAP[topic]
        return self.__denunciator.isAppealsForTopicEnabled(self.__vInfo.vehicleID, topicID, self.__arenaUniqueID)

    def __addDenunciationsInfo(self, options):
        make = self._makeItem
        if self.__userInfo.isAlly or self.arenaVisitor.gui.isTrainingBattle():
            order = DENUNCIATIONS.ORDER
        else:
            order = DENUNCIATIONS.ENEMY_ORDER
        sub = [make(denunciation, MENU.contextmenu(denunciation), optInitData={b'enabled': (self.__isAppealsForTopicEnabled(denunciation))}) for denunciation in order]
        label = (b'{} {}/{}').format(i18n.makeString(MENU.CONTEXTMENU_APPEAL), self.__denunciator.getDenunciationsLeft(), self.__denunciator.getDenunciationsPerDay())
        options.append(make(DENUNCIATIONS.APPEAL, label, optInitData={b'enabled': (self.__denunciator.isAppealsEnabled())}, optSubMenu=sub))
        return options

    def __addBotInfo(self, options):
        options.append(self._makeItem(_BOT_NO_ACTIONS_OPTION_ID, MENU.contextmenu(_BOT_NO_ACTIONS_OPTION_ID), optInitData=self._getOptionInitData(_BOT_NO_ACTIONS_OPTION_ID, False)))
        return options

    def __handleHideCursor(self, _):
        self.onContextMenuHide()
        return
