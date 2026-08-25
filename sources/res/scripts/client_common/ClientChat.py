from __future__ import absolute_import
import zlib, time
from collections import deque
from future.moves import pickle
import BigWorld, Event, chat_shared, helpers.time_utils as tm
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR, LOG_DEBUG
from chat_shared import CHAT_RESPONSES, CHAT_ACTIONS, CHAT_COMMANDS, parseCommandMessage, ChatCommandError, isCommandMessage, buildChatActionData, ChatError, ChatCommandInCooldown, SYS_MESSAGE_TYPE
from ids_generators import SequenceIDGenerator
from invites import INVITE_TYPES
from messenger import MessengerEntry
from constants import USER_SEARCH_MODE, IS_CLIENT

class ClientChat(object):
    __dataProcessors = [
     b'_ClientChat__dataTimeProcessor',
     b'_ClientChat__inviteDataTimeProcessor',
     b'_ClientChat__systemMessageTimeProcessor']
    __actionHandlers = {(CHAT_ACTIONS.receiveInvite.index()): b'_ClientChat__onReceiveInvite'}

    def __init__(self):
        self.__chatActionCallbacks = {}
        self._idGen = SequenceIDGenerator()
        return

    def acquireRequestID(self):
        return next(self._idGen)

    def requestSystemChatChannels(self):
        self.__baseChatCommand(CHAT_COMMANDS.requestSystemChatChannels)
        return

    def findChatChannels(self, sample, requestID=None):
        if requestID is None:
            requestID = self.acquireRequestID()
        try:
            self.__baseChatCommand(CHAT_COMMANDS.findChatChannels, stringArg1=sample, ignoreCooldown=False, requestID=requestID)
        except ChatError as ex:
            self._processChatError(CHAT_ACTIONS.requestChannels, 0, ex, requestID=requestID)

        return

    def getChannelInfoById(self, channelId):
        self.__baseChatCommand(CHAT_COMMANDS.getChannelInfoById, int64Arg=channelId)
        return

    def requestChatChannelMembers(self, channelId):
        self.__baseChannelChatCommand(channelId, CHAT_COMMANDS.requestChatChannelMembers)
        return

    def requestChatChannelMembersCount(self, channelId):
        self.__baseChannelChatCommand(channelId, CHAT_COMMANDS.getMembersCount)
        return

    def createChatChannel(self, channelName, password=None):
        try:
            self.__baseChatCommand(CHAT_COMMANDS.createChatChannel, stringArg1=channelName, stringArg2=password if password is not None else b'', ignoreCooldown=False)
        except ChatError as ex:
            self._processChatError(CHAT_COMMANDS.createChatChannel, 0, ex)

        return

    def destroyChatChannel(self, channelId):
        self.__baseChannelChatCommand(channelId, CHAT_COMMANDS.destroyChatChannel)
        return

    def enterChat(self, channelId, password=None):
        self.__baseChannelChatCommand(channelId, CHAT_COMMANDS.enterChatChannel, stringArg1=password if password is not None else b'')
        return

    def broadcast(self, channelId, message):
        if not message or message.isspace():
            return
        message = message.rstrip()
        if not isCommandMessage(message):
            try:
                self.__baseChannelChatCommand(channelId, CHAT_COMMANDS.broadcast, stringArg1=message, ignoreCooldown=False)
            except ChatError as ex:
                self._processChatError(CHAT_ACTIONS.broadcast, channelId, ex)

        else:
            try:
                command, int64Arg, int16Arg, stringArg1, stringArg2 = parseCommandMessage(message)
                self.__baseChannelChatCommand(channelId, command, int64Arg, int16Arg, stringArg1, stringArg2, ignoreCooldown=False)
            except ChatCommandError as ex:
                self._processChatError(CHAT_ACTIONS.userChatCommand, channelId, ex)

        return

    def leaveChat(self, channelId):
        self.__baseChannelChatCommand(channelId, CHAT_COMMANDS.leaveChatChannel)
        return

    def onChatActionFailure(self, actionData):
        MessengerEntry.g_instance.protos.BW.onChatActionFailure(actionData)
        return

    def onChatAction(self, chatActionData):
        if IS_CLIENT:
            LOG_DEBUG(b'onChatAction:%s' % (dict(chatActionData),))
        for processor in self.__dataProcessors:
            getattr(self, processor)(chatActionData)

        if CHAT_RESPONSES[chatActionData[b'actionResponse']] != CHAT_RESPONSES.success:
            self.onChatActionFailure(chatActionData)
        else:
            handlerName = self.__actionHandlers.get(chatActionData[b'action'], None)
            if handlerName:
                getattr(self, handlerName)(chatActionData)
            chId = chatActionData[b'channel']
            commonCallbacks = self.__getChatActionCallbacks(CHAT_ACTIONS[chatActionData[b'action']], 0)
            commonCallbacks(chatActionData)
            if chId != 0:
                channelCallbacks = self.__getChatActionCallbacks(CHAT_ACTIONS[chatActionData[b'action']], chId)
                channelCallbacks(chatActionData)
        return

    def requestLastSysMessages(self):
        self.__baseChatCommand(CHAT_COMMANDS.requestLastSysMessages)
        return

    def findUsers(self, userNamePattern, onlineMode=None, requestID=None):
        if onlineMode is None:
            searchMode = USER_SEARCH_MODE.ALL
        elif onlineMode:
            searchMode = USER_SEARCH_MODE.ONLINE
        else:
            searchMode = USER_SEARCH_MODE.OFFLINE
        self.__baseChatCommand(CHAT_COMMANDS.findUser, int16Arg=searchMode, stringArg1=userNamePattern, requestID=requestID)
        return

    def requestUsersRoster(self, flags=0):
        self.__baseChatCommand(CHAT_COMMANDS.requestUsersRoster, int16Arg=flags)
        return

    def logVivoxLogin(self):
        self.__baseChatCommand(CHAT_COMMANDS.logVivoxLogin)
        return

    def requestFriendStatus(self, friendID=-1):
        self.__baseChatCommand(CHAT_COMMANDS.requestFriendStatus, int64Arg=friendID)
        return

    def addFriend(self, friendID, friendName):
        self.__baseChatCommand(CHAT_COMMANDS.addFriend, int64Arg=friendID, stringArg1=friendName)
        return

    def createPrivate(self, friendID, friendName):
        self.__baseChatCommand(CHAT_COMMANDS.createPrivate, int64Arg=friendID, stringArg1=friendName)
        return

    def removeFriend(self, friendID):
        self.__baseChatCommand(CHAT_COMMANDS.removeFriend, int64Arg=friendID)
        return

    def addIgnored(self, ignoredID, ignoredName):
        self.__baseChatCommand(CHAT_COMMANDS.addIgnored, int64Arg=ignoredID, stringArg1=ignoredName)
        return

    def removeIgnored(self, ignoredID):
        self.__baseChatCommand(CHAT_COMMANDS.removeIgnored, int64Arg=ignoredID)
        return

    def createPrebattleInvite(self, receiverName, auxText, prebattleID, prebattleType, requestID=None):
        self.__baseInviteCommand(CHAT_COMMANDS.createInvite, INVITE_TYPES.PREBATTLE, receiverName, prebattleID, prebattleType, stringArg2=auxText, requestID=requestID)
        return

    def createBarterInvite(self, receiverName, auxText, itemID, requestID=None):
        self.__baseInviteCommand(CHAT_COMMANDS.createInvite, INVITE_TYPES.BARTER, receiverName, itemID, stringArg2=auxText, requestID=requestID)
        return

    def acceptPrebattleInvite(self, inviteID, requestID=None):
        if requestID is None:
            requestID = self.acquireRequestID()
        self.base.ackCommand(requestID, CHAT_COMMANDS.acceptInvite.index(), time.time(), inviteID, -1)
        return

    def rejectInvite(self, inviteID, requestID=None):
        if requestID is None:
            requestID = self.acquireRequestID()
        self.base.ackCommand(requestID, CHAT_COMMANDS.rejectInvite.index(), time.time(), inviteID, -1)
        return

    def getActiveInvites(self):
        self.__baseInviteCommand(CHAT_COMMANDS.getActiveInvites)
        return

    def getArchiveInvites(self):
        self.__baseInviteCommand(CHAT_COMMANDS.getArchiveInvites)
        return

    def requestVOIPCredentials(self, changePwd=0):
        self.__baseChatCommand(CHAT_COMMANDS.requestVOIPCredentials, int16Arg=changePwd)
        return

    def subscribeChatAction(self, callback, action, channelId=None):
        cbs = self.__getChatActionCallbacks(action, channelId)
        cbs += callback
        return

    def unsubscribeChatAction(self, callback, action, channelId=None):
        cbs = self.__getChatActionCallbacks(action, channelId)
        cbs -= callback
        return

    def setChatActionsCallbacks(self, callbacks):
        self.__chatActionCallbacks = callbacks
        return

    def sendChannelChatCommand(self, channelID, command, int64Arg=0, int16Arg=0, stringArg1=b'', stringArg2=b''):
        self.__baseChannelChatCommand(channelID, command, int64Arg, int16Arg, stringArg1, stringArg2)
        return

    def _processChatError(self, action, channelId, chatError, requestID=-1):
        if isinstance(chatError, ChatError):
            actionData = chatError.messageArgs if chatError.messageArgs is not None else chatError.message
        else:
            actionData = b''
        chatAction = buildChatActionData(action=action, requestID=requestID, channelId=channelId, originatorNickName=self.name, data=actionData, actionResponse=chatError.response if isinstance(chatError, ChatError) else CHAT_RESPONSES.internalError)
        self.onChatAction(chatAction)
        return

    def __getChatActionCallbacks(self, action, channelId):
        channelId = channelId if channelId is not None else 0
        key = (action, channelId)
        if key not in self.__chatActionCallbacks:
            handlers = self.__chatActionCallbacks[key] = Event.Event()
        else:
            handlers = self.__chatActionCallbacks[key]
        return handlers

    def __receiveStreamedData(self, streamID, data):
        failed = False
        try:
            data = zlib.decompress(data)
            chatMessages = pickle.loads(data)
        except Exception:
            LOG_CURRENT_EXCEPTION()
            failed = True

        if not failed:
            chIds = sorted(chatMessages.keys(), key=abs)
            for chId in chIds:
                channelQueue = chatMessages.get(chId, deque())
                while True:
                    try:
                        actionData = channelQueue.popleft()
                        self.onChatAction(actionData)
                    except IndexError:
                        break

        self.__baseChatCommand(CHAT_COMMANDS.initAck, int64Arg=streamID, int16Arg=failed)
        return

    def __baseChannelChatCommand(self, channelID, command, int64Arg=0, int16Arg=0, stringArg1=b'', stringArg2=b'', ignoreCooldown=True):
        if channelID == 0:
            LOG_ERROR(b'Can`t execute chat channel command for channelId: %s' % (channelID,))
        elif chat_shared.isOperationInCooldown(chat_shared.g_chatCooldownData, command):
            if ignoreCooldown:
                return
            raise ChatCommandInCooldown(command)
        self.__baseChatCommand(command, channelID, int64Arg, int16Arg, stringArg1, stringArg2)
        return

    def __baseChatCommand(self, command, channelID=0, int64Arg=0, int16Arg=0, stringArg1=b'', stringArg2=b'', ignoreCooldown=True, requestID=None):
        if requestID is None:
            requestID = self.acquireRequestID()
        if chat_shared.isOperationInCooldown(chat_shared.g_chatCooldownData, command):
            if not ignoreCooldown:
                raise ChatCommandInCooldown(command)
        self.base.chatCommandFromClient(requestID, command.index(), channelID, int64Arg, int16Arg, stringArg1, stringArg2)
        return

    def __baseInviteCommand(self, command, inviteType=None, receiverName=b'', int64Arg=0, int16Arg=0, stringArg1=b'', stringArg2=b'', requestID=None):
        if requestID is None:
            requestID = self.acquireRequestID()
        self.base.inviteCommand(requestID, command.index(), inviteType.index() if inviteType is not None else -1, receiverName, int64Arg, int16Arg, stringArg1, stringArg2)
        return

    def __onReceiveInvite(self, chatActionData):
        inviteID = chatActionData[b'data'].get(b'id', None)
        receivedAt = chatActionData[b'data'].get(b'received_at', None)
        if inviteID is not None and receivedAt is None:
            requestID = self.acquireRequestID()
            self.base.ackCommand(requestID, CHAT_COMMANDS.inviteReceived.index(), time.time(), inviteID, -1)
        return

    def __dataTimeProcessor(self, actionData):
        actionData[b'time'] = tm.makeLocalServerTime(actionData[b'time'])
        actionData[b'sentTime'] = tm.makeLocalServerTime(actionData[b'sentTime'])
        return

    def __inviteDataTimeProcessor(self, actionData):
        isInviteAction = CHAT_ACTIONS[actionData[b'action']] in (
         CHAT_ACTIONS.createInvite, CHAT_ACTIONS.receiveInvite,
         CHAT_ACTIONS.receiveArchiveInvite)
        if isInviteAction:
            if actionData.has_key(b'data'):
                inviteData = actionData[b'data']
                if b'sent_at' in inviteData:
                    inviteData[b'sent_at'] = tm.utcToLocalDatetime(tm.makeLocalServerDatetime(inviteData[b'sent_at']))
                if b'received_at' in inviteData:
                    inviteData[b'received_at'] = tm.utcToLocalDatetime(tm.makeLocalServerDatetime(inviteData[b'received_at']))
                if b'processed_at' in inviteData:
                    inviteData[b'processed_at'] = tm.utcToLocalDatetime(tm.makeLocalServerDatetime(inviteData[b'processed_at']))
        return

    def __systemMessageTimeProcessor(self, actionData):
        isSystemMessage = CHAT_ACTIONS[actionData[b'action']] in (
         CHAT_ACTIONS.personalSysMessage, CHAT_ACTIONS.sysMessage)
        if isSystemMessage:
            if actionData.has_key(b'data'):
                messageData = actionData[b'data']
                messageType = messageData[b'type']
                if b'created_at' in messageData:
                    messageData[b'created_at'] = tm.makeLocalServerDatetime(messageData[b'created_at'])
                if b'finished_at' in messageData:
                    messageData[b'finished_at'] = tm.makeLocalServerDatetime(messageData[b'finished_at'])
                if b'started_at' in messageData:
                    messageData[b'started_at'] = tm.makeLocalServerDatetime(messageData[b'started_at'])
                if messageType == SYS_MESSAGE_TYPE.serverReboot.index():
                    messageData[b'data'] = tm.makeLocalServerDatetime(messageData[b'data'])
                elif messageType == SYS_MESSAGE_TYPE.battleResults.index():
                    if b'arenaCreateTime' in messageData[b'data']:
                        messageData[b'data'][b'arenaCreateTime'] = tm.makeLocalServerTime(messageData[b'data'][b'arenaCreateTime'])
                elif messageType == SYS_MESSAGE_TYPE.currencyUpdate.index():
                    messageData[b'data'][b'date'] = tm.makeLocalServerTime(messageData[b'data'][b'date'])
                elif messageType in (
                 SYS_MESSAGE_TYPE.accountTypeChanged.index(),
                 SYS_MESSAGE_TYPE.premiumBought.index(),
                 SYS_MESSAGE_TYPE.premiumExtended.index(),
                 SYS_MESSAGE_TYPE.premiumExpired.index()):
                    if b'expiryTime' in messageData[b'data']:
                        messageData[b'data'][b'expiryTime'] = tm.makeLocalServerTime(messageData[b'data'][b'expiryTime'])
        return
