import cPickle, time, zlib
from functools import wraps
import constants
from Event import Event
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES
from constants import CHAT_LOG, RESTRICTION_TYPE
from debug_utils import LOG_ERROR
from enumerations import Enumeration, AttributeEnumItem
from messenger_common_chat2 import BATTLE_CHAT_COMMANDS_BY_NAMES
from soft_exception import SoftException
from wotdecorators import noexcept
__all__ = [
 b'CHAT_ACTIONS', b'SYS_MESSAGE_TYPE']
NOTIFICATION_GROUP = Enumeration(b'Group of members for notification', [
 b'All',
 b'NONE',
 b'Originator',
 b'ExceptOriginator'])

def __notifyFilterAll(originatorId, entityId):
    return True


def __notifyFilterNone(originatorId, entityId):
    return False


def __notifyFilterOnlyOriginator(originatorId, entityId):
    return originatorId == entityId


def __notifyFilterExceptOriginator(originatorId, entityId):
    return originatorId != entityId


if constants.IS_BASEAPP:
    CHAT_ACTIONS = Enumeration(b'chatChannelActions', [
     (
      b'enter',
      {b'notifyFilter': __notifyFilterExceptOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.ExceptOriginator), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'broadcast',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.MESSAGES)}),
     (
      b'leave',
      {b'notifyFilter': __notifyFilterExceptOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.ExceptOriginator), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'requestMembers',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'channelDestroyed',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'createChannel',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'requestChannels',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'selfEnter',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'selfLeave',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'requestMessageHistory',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'channelInfoUpdated',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'memberStatusUpdate',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'findUsers',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'requestUsersRoster',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'addIgnored',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'addFriend',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'removeIgnored',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'removeFriend',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'createPrivate',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'friendStatusUpdate',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'userChatCommand',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'sysMessage',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'personalSysMessage',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'chatInitialization',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'userInviteCommand',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'createInvite',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'receiveInvite',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'receiveArchiveInvite',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'receiveMembersCount',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'receiveMembersDelta',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'VOIPSettings',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'VOIPCredentials',
      {b'notifyFilter': __notifyFilterAll, 
         b'notificationGroup': (NOTIFICATION_GROUP.All), 
         b'logLevel': (CHAT_LOG.ACTIONS)}),
     (
      b'setMuted',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'unsetMuted',
      {b'notifyFilter': __notifyFilterOnlyOriginator, 
         b'notificationGroup': (NOTIFICATION_GROUP.Originator), 
         b'logLevel': (CHAT_LOG.NONE)}),
     (
      b'logVivoxLogin',
      {b'notifyFilter': __notifyFilterNone, 
         b'notificationGroup': (NOTIFICATION_GROUP.NONE), 
         b'logLevel': (CHAT_LOG.NONE)})], instance=AttributeEnumItem)
else:
    CHAT_ACTIONS = Enumeration(b'chatActions', [
     (
      b'enter', {}),
     (
      b'broadcast', {}),
     (
      b'leave', {}),
     (
      b'requestMembers', {}),
     (
      b'channelDestroyed', {}),
     (
      b'createChannel', {}),
     (
      b'requestChannels', {}),
     (
      b'selfEnter', {}),
     (
      b'selfLeave', {}),
     (
      b'requestMessageHistory', {}),
     (
      b'channelInfoUpdated', {}),
     (
      b'memberStatusUpdate', {}),
     (
      b'findUsers', {}),
     (
      b'requestUsersRoster', {}),
     (
      b'addIgnored', {}),
     (
      b'addFriend', {}),
     (
      b'removeIgnored', {}),
     (
      b'removeFriend', {}),
     (
      b'createPrivate', {}),
     (
      b'friendStatusUpdate', {}),
     (
      b'userChatCommand', {}),
     (
      b'sysMessage', {}),
     (
      b'personalSysMessage', {}),
     (
      b'chatInitialization', {}),
     (
      b'userInviteCommand', {}),
     (
      b'createInvite', {}),
     (
      b'receiveInvite', {}),
     (
      b'receiveArchiveInvite', {}),
     (
      b'receiveMembersCount', {}),
     (
      b'receiveMembersDelta', {}),
     (
      b'VOIPSettings', {}),
     (
      b'VOIPCredentials', {}),
     (
      b'setMuted', {}),
     (
      b'unsetMuted', {}),
     (
      b'logVivoxLogin', {})], instance=AttributeEnumItem)
CHAT_RESPONSES = Enumeration(b'chatActionResponses', (b'success', b'internalError', b'channelAlreadyExists', b'channelDestroyed', b'passwordRequired', b'incorrectPassword', b'channelNotExists', b'memberBanned', b'memberDisconnecting', b'notAllowed', b'connectTimeout', b'initializationFailure', b'userNotExists', b'usersRosterLimitReached', b'activeChannelsLimitReached', b'sqlError', b'incorrectCharacter', b'addFriendError', b'addIgnoredError', b'userIgnoredError', b'chatCommandError', b'memberAlreadyBanned', b'memberAlreadyModerator', b'memberNotModerator', b'commandInCooldown', b'createPrivateError', b'actionInCooldown', b'chatBanned', b'inviteCommandError', b'unknownCommand', b'inviteCreateError', b'membersLimitReached', b'notSupported', b'inviteCreationNotAllowed', b'incorrectCommandArgument', b'invalidChannelName', b'setMutedError', b'unsetMutedError'))
__DEFAULT_COOLDOWN = 0.5
__BATTLE_COMMANDS_DEFAULT_COOLDOWN = __DEFAULT_COOLDOWN
__CHINA_USER_MESSAGE_COOLDOWN = 3.0
__COOLDOWN_CHECK_CLIENT = 1
__COOLDOWN_CHECK_BASE = 2
__COOLDOWN_CHECK_ALL = __COOLDOWN_CHECK_CLIENT | __COOLDOWN_CHECK_BASE
CHAT_COMMANDS = Enumeration(b'chatCommands', [
 (
  b'initAck', {b'chnlCmd': 0}),
 (
  b'updateMemeberStatus', {b'chnlCmd': 0}),
 (
  b'findUser',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'addFriend',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'addIgnored',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'removeFriend',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'removeIgnored',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'createPrivate',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'joinPrivate', {b'chnlCmd': 0}),
 (
  b'requestUsersRoster', {b'chnlCmd': 0}),
 (
  b'requestFriendStatus', {b'chnlCmd': 0}),
 (
  b'friendStatusChange', {b'chnlCmd': 0}),
 (
  b'addAdmirer', {b'chnlCmd': 0}),
 (
  b'addAdmirerAck', {b'chnlCmd': 0}),
 (
  b'removeAdmirer', {b'chnlCmd': 0}),
 (
  b'onAddToIgnored', {b'chnlCmd': 0}),
 (
  b'CHGCHNLNAME',
  {b'chnlCmd': 1, 
     b'argsCnt': 1, b'cooldown': {b'period': 30.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'GREETING',
  {b'chnlCmd': 1, 
     b'argsCnt': 1, b'cooldown': {b'period': 30.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'BAN',
  {b'chnlCmd': 1, 
     b'argsCnt': 3, b'cooldown': {b'period': 10.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'UNBAN',
  {b'chnlCmd': 1, 
     b'argsCnt': 1, b'cooldown': {b'period': 10.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'ADDMODERATOR',
  {b'chnlCmd': 1, 
     b'argsCnt': 1, b'cooldown': {b'period': 10.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'DELMODERATOR',
  {b'chnlCmd': 1, 
     b'argsCnt': 1, b'cooldown': {b'period': 10.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'requestLastSysMessages', {b'chnlCmd': 0}),
 (
  b'chatAckInitialization', {b'chnlCmd': 0}),
 (
  b'createInvite',
  {b'inviteCmd': 1, 
     b'cooldown': {b'period': 0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'inviteReceived', {b'inviteCmd': 1}),
 (
  b'acceptInvite',
  {b'inviteCmd': 1, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'rejectInvite',
  {b'inviteCmd': 1, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'getActiveInvites',
  {b'inviteCmd': 1, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'getArchiveInvites',
  {b'inviteCmd': 1, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'getMembersCount',
  {b'chnlCmd': 1, 
     b'cooldown': {b'period': __DEFAULT_COOLDOWN, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'requestSystemChatChannels',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': __DEFAULT_COOLDOWN, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'findChatChannels',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'getChannelInfoById', {b'chnlCmd': 0}),
 (
  b'createChatChannel',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 10.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'destroyChatChannel', {b'chnlCmd': 0}),
 (
  b'requestChatChannelMembers',
  {b'chnlCmd': 1, 
     b'skipBanCheck': 1, b'cooldown': {b'period': 2.0, b'side': 0}}),
 (
  b'enterChatChannel',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': __DEFAULT_COOLDOWN, b'side': 0}}),
 (
  b'leaveChatChannel',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': __DEFAULT_COOLDOWN, 
                   b'side': 0}}),
 (
  b'broadcast',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': (__DEFAULT_COOLDOWN if not constants.IS_CHINA else __CHINA_USER_MESSAGE_COOLDOWN), 
                   b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'USERBAN',
  {b'userCmd': 1, 
     b'argsCnt': 4, b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'USERUNBAN',
  {b'userCmd': 1, 
     b'argsCnt': 2, b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'requestVOIPSettings',
  {b'chnlCmd': 1, 
     b'skipBanCheck': 1, b'cooldown': {b'period': __DEFAULT_COOLDOWN, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'requestVOIPCredentials',
  {b'chnlCmd': 0, 
     b'skipBanCheck': 1}),
 (
  b'setMuted',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'unsetMuted',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': 5.0, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  b'logVivoxLogin',
  {b'chnlCmd': 0, 
     b'cooldown': {b'period': __DEFAULT_COOLDOWN, b'side': __COOLDOWN_CHECK_ALL}}),
 (
  BATTLE_CHAT_COMMAND_NAMES.SOS,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.POSITIVE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTENTION_TO_POSITION,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.REPLY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.CANCEL_REPLY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTACK_OBJECTIVE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.DEFEND_OBJECTIVE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTACK_BASE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.DEFEND_BASE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.SPG_AIM_AREA,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTACKING_ENEMY_WITH_SPG,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.TURNBACK,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.HELPME,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTACK_ENEMY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.RELOADINGGUN,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.THANKS,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.RELOADING_CASSETE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.RELOADING_READY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.RELOADING_READY_CASSETE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.RELOADING_UNAVAILABLE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_SAVE_TANKS_ATK,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.GOING_THERE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_SAVE_TANKS_DEF,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_TIME_ATK,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_TIME_DEF,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_HQ_ATK,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_HQ_DEF,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_WEST,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_CENTER,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_EAST,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_1,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_2,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_3,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_4,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_5,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_6,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_7,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_1_EX,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_2_EX,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_3_EX,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_4_EX,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_5_EX,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_6_EX,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_7_EX,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.CLEAR_CHAT_COMMANDS,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTACKING_ENEMY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.SUPPORTING_ALLY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.DEFENDING_BASE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTACKING_BASE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.PREBATTLE_WAYPOINT,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.CONFIRM,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTACKING_OBJECTIVE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.DEFENDING_OBJECTIVE,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.VEHICLE_SPOTPOINT,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.SHOOTING_POINT,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.NAVIGATION_POINT,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.FLAG_POINT,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.OVERHEAT_CANT_SHOOT,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTACK_SUPPLY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.ATTACKING_SUPPLY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.DEFEND_SUPPLY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.DEFENDING_SUPPLY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.SELF_REPAIR_SUPPLY,
  {b'battleCmd': 1}),
 (
  BATTLE_CHAT_COMMAND_NAMES.FOCUS_SUPPLY,
  {b'battleCmd': 1})], instance=AttributeEnumItem)
CHAT_MEMBER_STATUSES = Enumeration(b'chatMemberStatuses', [
 b'available',
 b'inBattle'])
CHAT_MEMBER_BAN_TYPE = Enumeration(b'chatMemberBanType', [
 b'none',
 b'readonly',
 b'full'])
CHAT_MEMBER_ROLE = Enumeration(b'chatMemberRole', [
 b'member',
 b'visitor',
 b'moderator'])
CHAT_MEMBER_GROUP = Enumeration(b'chatMemberRole', [
 b'member',
 b'channelOwner',
 b'channelModerator',
 b'chatAdmin'])
CHAT_CHANNEL_BATTLE_TEAM = 1
CHAT_CHANNEL_BATTLE = 2
CHAT_CHANNEL_PREBATTLE = 4
CHAT_CHANNEL_PRIVATE = 8
CHAT_CHANNEL_DESTROYING = 16
CHAT_CHANNEL_TRAINING = 32
CHAT_CHANNEL_SQUAD = 64
CHAT_CHANNEL_TEAM = 128
CHAT_CHANNEL_VOICE = 256
CHAT_CHANNEL_CLAN = 512
CHAT_CHANNEL_PREBATTLE_CLAN = 1024
CHAT_CHANNEL_TOURNAMENT = 2048
CHAT_CHANNEL_UNIT = 4096
CHAT_CHANNEL_NOTIFY_MEMBERS_MASK = 3
CHAT_CHANNEL_NOTIFY_MEMBERS_IN_OUT = 0
CHAT_CHANNEL_NOT_NOTIFY_MEMBERS_IN_OUT = 1
CHAT_CHANNEL_NOTIFY_MEMBERS_COUNT = 2
CHAT_CHANNEL_NOTIFY_MEMBERS_DELTA = 3

def boundActionResponseFilter(response):

    def wrap(func):

        @wraps(func)
        def wrapper(obj, actionData, *args, **kwArgs):
            if CHAT_RESPONSES[actionData[b'actionResponse']] == response:
                func(obj, actionData, *args, **kwArgs)
            return

        return wrapper

    return wrap


def buildChatActionData(action, channelId=None, **kwArgs):
    data = {}
    data[b'requestID'] = kwArgs.get(b'requestID', -1)
    data[b'action'] = action.index()
    data[b'channel'] = channelId if channelId is not None else 0
    data[b'actionResponse'] = kwArgs.get(b'actionResponse', CHAT_RESPONSES.success).index()
    data[b'originator'] = kwArgs.get(b'originator', -1)
    data[b'originatorNickName'] = kwArgs.get(b'originatorNickName', b'')
    data[b'group'] = kwArgs.get(b'group', CHAT_MEMBER_GROUP.member).index()
    data[b'data'] = kwArgs.get(b'data')
    data[b'time'] = time.time()
    data[b'sentTime'] = data[b'time']
    data[b'flags'] = kwArgs.get(b'flags', 0)
    return data


ChatChannelKeyPrefix = b'chatChannel_'

def buildChannelsKey(id):
    return b'%s%d' % (ChatChannelKeyPrefix, id)


@noexcept
def getChannelsIDFromKey(key):
    if key.startswith(ChatChannelKeyPrefix):
        strID = key.replace(ChatChannelKeyPrefix, b'')
        return int(strID)
    return 0


def isChannelSecured(channelInfo):
    return channelInfo is not None and channelInfo.get(b'isReadOnly', False)


def _testChannelFlag(channelInfo, testedFlag, resultForNone=True):
    if channelInfo is None:
        return resultForNone
    else:
        flags = channelInfo.get(b'flags', 0)
        return _testFlags(flags, testedFlag)


def _testFlags(flags, testedFlag):
    return flags & testedFlag == testedFlag


def isChannelDestroying(channelInfo):
    return _testChannelFlag(channelInfo, CHAT_CHANNEL_DESTROYING)


def isChannelDestroyingFlags(flags):
    return _testFlags(flags, CHAT_CHANNEL_DESTROYING)


def isPrivateChannel(channelInfo):
    return _testChannelFlag(channelInfo, CHAT_CHANNEL_PRIVATE)


def isTrainingChannel(channelInfo):
    return _testChannelFlag(channelInfo, CHAT_CHANNEL_TRAINING)


def isPrebattleChannel(channelInfo):
    return _testChannelFlag(channelInfo, CHAT_CHANNEL_PREBATTLE)


def isPrebattleChannelFlags(flags):
    return _testFlags(flags, CHAT_CHANNEL_PREBATTLE)


def isSquadChannel(channelInfo):
    return _testChannelFlag(channelInfo, CHAT_CHANNEL_SQUAD)


def isTeamChannel(channelInfo):
    return _testChannelFlag(channelInfo, CHAT_CHANNEL_TEAM)


def isBattleTeamFlags(flags):
    return _testFlags(flags, CHAT_CHANNEL_BATTLE)


def isArenaBattleTeamFlags(flags):
    return _testFlags(flags, CHAT_CHANNEL_BATTLE_TEAM)


def isChannelHasVoice(channelInfo):
    return _testChannelFlag(channelInfo, CHAT_CHANNEL_VOICE)


def isChannelHasVoiceFlags(flags):
    return _testFlags(flags, CHAT_CHANNEL_VOICE)


def isClanChannel(channelInfo):
    return _testChannelFlag(channelInfo, CHAT_CHANNEL_CLAN, False)


def isClanChannelFlags(flags):
    return _testFlags(flags, CHAT_CHANNEL_CLAN)


def isTournamentChannelFlags(flags):
    return _testFlags(flags, CHAT_CHANNEL_TOURNAMENT)


def isPrebattleClanChannelFlags(flags):
    return _testFlags(flags, CHAT_CHANNEL_PREBATTLE_CLAN)


def isRegularChannel(channelInfo):
    if channelInfo is None:
        return False
    else:
        return isRegularChannelFlags(channelInfo.get(b'flags', 0))


def isRegularChannelFlags(flags):
    return flags == 0


def isBanAppliedToChannel(banType, channelInfo):
    if banType == constants.NOVICE_RESTRICTIONS_BAN_TYPE:
        return isRegularChannelFlags(channelInfo.get(b'flags', 0)) or isPrivateChannel(channelInfo)
    return True


class BaseChatCommandProcessor(object):

    def __init__(self, comand):
        self._command = comand
        return

    def parseRawData(self, rawData, verifyData=True):
        if verifyData:
            self.__verifyRawData(rawData)
        parsedData = self._makeTuple(rawData)
        if verifyData:
            self._verifyTupledData(parsedData)
        return self._adjustTupleDataTypes(parsedData)

    def verifyParsedData(self, int64Arg=0, int16arg=0, stringArg1=b'', stringArg2=b''):
        return True

    def _verifyTupledData(self, dataAsTuple):
        return self.verifyParsedData(dataAsTuple[1], dataAsTuple[2], dataAsTuple[3], dataAsTuple[4])

    def __verifyRawData(self, rawData):
        argsCnt = self._command.argsCnt
        if len(rawData) != argsCnt:
            raise ChatCommandError(error=b'#chat:errors/toosmallargs' if len(rawData) < argsCnt else b'#chat:errors/toomanyargs')
        return True

    def _makeTuple(self, rawData):
        return (
         self._command, 0, 0, b'', b'')

    def _adjustTupleDataTypes(self, rawTuple):
        return (
         self._command, long(rawTuple[1]), int(rawTuple[2]), rawTuple[3], rawTuple[4])

    def set_command(self, newValue):
        self.__command = newValue
        return

    _command = property((lambda self: self.__command), set_command)


class OneStringArgCommandProcessor(BaseChatCommandProcessor):

    def __init__(self, command):
        BaseChatCommandProcessor.__init__(self, command)
        return

    def _makeTuple(self, rawData):
        return (self._command, 0, 0, rawData[0], b'')


class NoArgsCommandProcessor(BaseChatCommandProcessor):

    def __init__(self, command):
        BaseChatCommandProcessor.__init__(self, command)
        return


class BanCommandProcessor(BaseChatCommandProcessor):

    def __init__(self):
        BaseChatCommandProcessor.__init__(self, CHAT_COMMANDS.BAN)
        return

    def _makeTuple(self, rawData):
        return (self._command, 0, -1 if isPermanentBan(rawData[1]) else rawData[1], rawData[0], rawData[2])

    def verifyParsedData(self, int64Arg=0, int16arg=0, stringArg1=b'', stringArg2=b''):
        errorMessage = b'#chat:errors/timeincorrect'
        timeArg = int16arg
        if isinstance(timeArg, basestring) and timeArg.isdigit() or isinstance(timeArg, (int, long)):
            time = int(timeArg)
            if time == -1:
                pass
            elif time < 1 or time > 1440:
                raise ChatCommandError(error=errorMessage)
        else:
            raise ChatCommandError(error=errorMessage)
        return True


class UserCommandProcessor(BaseChatCommandProcessor):
    _USER_BAN_TYPES = Enumeration(b'UserCommandBanTypes', {(RESTRICTION_TYPE.BAN): b'game', 
       (RESTRICTION_TYPE.CHAT_BAN): b'chat'})

    def __init__(self, command):
        BaseChatCommandProcessor.__init__(self, command)
        return


class UserBanCommandProcessor(UserCommandProcessor):
    import re
    __BAN_TIME_RE = re.compile(b'([-|+]?)([0-9]*)([hdwmy]?)')

    def __init__(self):
        UserCommandProcessor.__init__(self, CHAT_COMMANDS.USERBAN)
        return

    def _makeTuple(self, rawData):
        if isinstance(rawData[0], basestring):
            banType = rawData[0].lower()
            if banType not in UserCommandProcessor._USER_BAN_TYPES:
                raise IncorrectCommandArgumentError(rawData[0])
        else:
            raise IncorrectCommandArgumentError(rawData[0])
        banTypeIdx = getattr(UserCommandProcessor._USER_BAN_TYPES, banType).index()
        banPeriod = None
        if isinstance(rawData[2], basestring):
            res = self.__BAN_TIME_RE.match(rawData[2])
            multiplier = 1
            if res:
                sign, amount, timeSpec = res.groups()
                if not amount:
                    raise IncorrectCommandArgumentError(rawData[2])
                if b'h' == timeSpec:
                    multiplier = 60
                elif b'd' == timeSpec:
                    multiplier = 1440
                elif b'w' == timeSpec:
                    multiplier = 10080
                elif b'm' == timeSpec:
                    multiplier = 43200
                elif b'y' == timeSpec:
                    multiplier = 43200
                if b'-' == sign:
                    multiplier *= -1
                banPeriod = long(amount) * multiplier
        elif isinstance(rawData[2], long):
            banPeriod = rawData[2]
        else:
            raise IncorrectCommandArgumentError(rawData[2])
        words = rawData[3].split()
        if words and b'kick' == words[0].lower():
            banTypeIdx *= -1
            rawData[3] = (b' ').join(words[1:])
        return (self._command, banPeriod, banTypeIdx, rawData[1], rawData[3])

    def verifyParsedData(self, banPeriod=0, banTypeIdx=0, username=b'', reason=b''):
        if not (isinstance(banPeriod, basestring) and banPeriod.isdigit() or isinstance(banPeriod, (int, long))):
            raise IncorrectCommandArgumentError(banPeriod)
        try:
            _ = UserCommandProcessor._USER_BAN_TYPES[banTypeIdx]
        except:
            raise IncorrectCommandArgumentError(banTypeIdx)

        return True


class UserUnbanCommandProcessor(UserCommandProcessor):

    def __init__(self):
        UserCommandProcessor.__init__(self, CHAT_COMMANDS.USERUNBAN)
        return

    def _makeTuple(self, rawData):
        if isinstance(rawData[0], basestring):
            banType = rawData[0].lower()
            if banType not in UserCommandProcessor._USER_BAN_TYPES:
                raise IncorrectCommandArgumentError(rawData[0])
        else:
            raise IncorrectCommandArgumentError(rawData[0])
        banTypeIdx = getattr(UserCommandProcessor._USER_BAN_TYPES, banType).index()
        return (
         self._command, 0, banTypeIdx, rawData[1], b'')

    def verifyParsedData(self, banPeriod=0, banTypeIdx=0, username=b'', reason=b''):
        try:
            _ = UserCommandProcessor._USER_BAN_TYPES[banTypeIdx]
        except:
            raise IncorrectCommandArgumentError(banTypeIdx)

        return True


_g_chatCommandProcessors = {(CHAT_COMMANDS.BAN): (BanCommandProcessor()), 
   (CHAT_COMMANDS.CHGCHNLNAME): (OneStringArgCommandProcessor(CHAT_COMMANDS.CHGCHNLNAME)), 
   (CHAT_COMMANDS.GREETING): (OneStringArgCommandProcessor(CHAT_COMMANDS.GREETING)), 
   (CHAT_COMMANDS.UNBAN): (OneStringArgCommandProcessor(CHAT_COMMANDS.UNBAN)), 
   (CHAT_COMMANDS.ADDMODERATOR): (OneStringArgCommandProcessor(CHAT_COMMANDS.ADDMODERATOR)), 
   (CHAT_COMMANDS.DELMODERATOR): (OneStringArgCommandProcessor(CHAT_COMMANDS.DELMODERATOR)), 
   (CHAT_COMMANDS.USERBAN): (UserBanCommandProcessor()), 
   (CHAT_COMMANDS.USERUNBAN): (UserUnbanCommandProcessor())}

def initChatCooldownData():
    cooldDownData = {}
    for command in CHAT_COMMANDS.all():
        coolDownConfig = getattr(command, b'cooldown') if hasattr(command, b'cooldown') else {}
        coolDownPeriod = coolDownConfig.get(b'period', -1)
        if coolDownPeriod > 0:
            cooldDownData[command.index()] = {b'cooldown': coolDownPeriod, b'side': (coolDownConfig.get(b'side', 0)), 
               b'last': (time.time() - coolDownPeriod)}

    return cooldDownData


if constants.IS_CLIENT or constants.IS_BOT:
    g_chatCooldownData = initChatCooldownData()

def __isOperationInCooldown(cooldownDataInfo, operation, update=True):
    cooldDownData = cooldownDataInfo.get(operation.index(), None)
    if cooldDownData:
        checkSide = __COOLDOWN_CHECK_CLIENT if constants.IS_CLIENT else __COOLDOWN_CHECK_BASE
        commandTime = time.time()
        lastCommandTime = cooldDownData.get(b'last', commandTime)
        coolDownPeriod = cooldDownData.get(b'cooldown', -1)
        cooldownCheckSide = cooldDownData.get(b'side', 0)
        if cooldownCheckSide & checkSide == checkSide:
            if lastCommandTime + coolDownPeriod >= commandTime:
                return True
            if update:
                cooldDownData[b'last'] = commandTime
                cooldownDataInfo[operation.index()] = cooldDownData
    return False


def isOperationInCooldown(cooldownData, operation, update=True):
    return __isOperationInCooldown(cooldownData, operation, update=update)


def getOperationCooldownPeriod(operation):
    coolDownConfig = getattr(operation, b'cooldown') if hasattr(operation, b'cooldown') else {}
    return coolDownConfig.get(b'period', -1)


_g_chatadmins = [
 b'redfox',
 b'ars',
 b'snake']

def isChatAdmin(username):
    return username in _g_chatadmins


def __isCommandFromCategory(category, cmdName=None, cmdIdx=None):
    try:
        if cmdIdx is None:
            cmdItem = CHAT_COMMANDS.lookup(cmdName)
        else:
            cmdItem = CHAT_COMMANDS[cmdIdx]
    except:
        cmdItem = None

    return cmdItem is not None and hasattr(cmdItem, category) and getattr(cmdItem, category) == 1


def isInviteCommand(cmdName):
    return __isCommandFromCategory(b'inviteCmd', cmdName=cmdName)


def isInviteCommandIdx(cmdIdx):
    return __isCommandFromCategory(b'inviteCmd', cmdIdx=cmdIdx)


def isChannelChatCommand(cmdName):
    return __isCommandFromCategory(b'chnlCmd', cmdName=cmdName)


def isChannelChatCommandIdx(cmdIdx):
    return __isCommandFromCategory(b'chnlCmd', cmdIdx=cmdIdx)


def isUserCommand(cmdName):
    return __isCommandFromCategory(b'userCmd', cmdName=cmdName)


def isUserCommandIdx(cmdIdx):
    return __isCommandFromCategory(b'userCmd', cmdIdx=cmdIdx)


def isBattleChatCommand(cmdName):
    return cmdName in BATTLE_CHAT_COMMANDS_BY_NAMES


def isBattleChatCommandIdx(cmdIdx):
    return __isCommandFromCategory(b'battleCmd', cmdIdx=cmdIdx)


def isSkipBanCheckForChatCommand(cmdName):
    return __isCommandFromCategory(b'skipBanCheck', cmdName=cmdName)


def isSkipBanCheckForCommandIdx(cmdIdx):
    return __isCommandFromCategory(b'skipBanCheck', cmdIdx=cmdIdx)


def isCommandMessage(message):
    if message.startswith(b'/'):
        words = message[1:].split()
        if len(words) > 0:
            return isChannelChatCommand(words[0]) or isBattleChatCommand(words[0]) or isUserCommand(words[0])
    return False


def parseCommandMessage(message, verifyArgs=True):
    LOG_ERROR(b'parseCommandMessage:', message)
    if isCommandMessage(message):
        data = message[1:].split(None, 1)
        cmd = CHAT_COMMANDS.lookup(data[0])
        argsCnt = cmd.argsCnt - 1
        rawData = data[1].split(None, argsCnt) if len(data) > 1 else []
        cmdProcessor = _g_chatCommandProcessors.get(cmd, None)
        if cmdProcessor is None:
            LOG_ERROR(b'Can`t process arguments: command %s hasn`t argument processor. command ignored' % (cmd,))
            return (0, 0, b'', b'')
        return cmdProcessor.parseRawData(rawData, verifyArgs)
    return


def verifyCommandData(command, int64Arg=0, int16arg=0, stringArg1=b'', stringArg2=b''):
    cmdProcessor = _g_chatCommandProcessors.get(command, None)
    if cmdProcessor is None:
        LOG_ERROR(b'Can`t process arguments: command %s hasn`t argument processor. command ignored' % (command,))
        return False
    else:
        return cmdProcessor.verifyParsedData(int64Arg, int16arg, stringArg1, stringArg2)
        return


def isPermanentBan(banTime):
    return b'permanent' == banTime


class ChatActionHandlers(object):

    def __init__(self):
        self.__actionHandlers = None
        self._onEntityInit()
        return

    def _onEntityInit(self):
        if hasattr(self, b'__actionHandlers'):
            self._clear()
        self.__actionHandlers = {}
        return

    def _onEntityRestore(self):
        self._onEntityInit()
        return

    def _onEntityDestroy(self):
        self._clear()
        return

    def _clear(self):
        for handlers in self.__actionHandlers.values():
            handlers.clear()

        self.__actionHandlers.clear()
        self.__actionHandlers = None
        return

    def _getActionHandlers(self, actionId):
        if actionId not in self.__actionHandlers:
            handlers = self.__actionHandlers[actionId] = Event()
        else:
            handlers = self.__actionHandlers[actionId]
        return handlers

    def _subscribeActionHandler(self, actionId, handler):
        handlers = self._getActionHandlers(actionId)
        handlers += handler
        return

    def _unsubscribeActionHandler(self, actionId, handler):
        handlers = self._getActionHandlers(actionId)
        handlers -= handler
        return


class ChatError(SoftException):

    def __init__(self, response=None, auxMessage=None, messageArgs=None):
        SoftException.__init__(self)
        self.__response = CHAT_RESPONSES.internalError if response is None else response
        self.__auxMessage = auxMessage
        self._messageArgs = messageArgs
        return

    response = property((lambda self: self.__response))

    def _getMessage(self):
        return b'Internal error occurred' + (b':' + self.__auxMessage if self.__auxMessage is not None else b'')

    def __get_message(self):
        return self._getMessage()

    message = property(__get_message)
    messageArgs = property((lambda self: self._messageArgs))


class UserBannedError(ChatError):

    def __init__(self, banOwnerNick, banReason, banEndTime):
        ChatError.__init__(self, CHAT_RESPONSES.memberBanned)
        self.__banOwnerNick = banOwnerNick
        self.__banReason = banReason
        self.__banEndTime = banEndTime
        self._messageArgs = {b'banOwnerNick': (self.__banOwnerNick), 
           b'banReason': (self.__banReason), 
           b'banEndTime': (self.__banEndTime)}
        return

    def _getMessage(self):
        if self.__banEndTime is not None:
            return b'You are banned by user %s till %s. Reason: %s.' % (
             self.__banOwnerNick, self.__banEndTime, self.__banReason)
        else:
            return b'You are banned by user %s till %s. Reason: %s.' % (
             self.__banOwnerNick, self.__banEndTime, self.__banReason)
            return


class ChatBannedError(ChatError):

    def __init__(self, banReason, banEndTime, banType=None):
        ChatError.__init__(self, CHAT_RESPONSES.chatBanned)
        self.__banReason = banReason
        self.__banEndTime = banEndTime
        self.__banType = banType
        self._messageArgs = {b'banReason': (self.__banReason), 
           b'banEndTime': (self.__banEndTime), 
           b'banType': (self.__banType)}
        return

    def _getMessage(self):
        if self.__banEndTime is not None:
            return b'You are banned till %s. Reason: %s.' % (self.__banEndTime, self.__banReason)
        else:
            return b'You are banned. Reason: %s.' % self.__banReason
            return


class ChatSQLError(ChatError):

    def __init__(self, error=None):
        ChatError.__init__(self, CHAT_RESPONSES.sqlError)
        self.__error = error
        self._messageArgs = {b'error': error}
        return

    def _getMessage(self):
        return b'SQL error occurred: %s' % (self.__error,)


class IncorrectCharacter(ChatError):

    def __init__(self):
        ChatError.__init__(self, CHAT_RESPONSES.incorrectCharacter)
        return

    def _getMessage(self):
        return b'String contains incorrect character(s)'


class AddFriendError(ChatError):

    def __init__(self, reason):
        ChatError.__init__(self, CHAT_RESPONSES.addFriendError)
        self.__reason = reason
        self._messageArgs = {b'reason': reason}
        return

    def _getMessage(self):
        return b'Can`t add user to friends: %s' % self.__reason


class AddIgnoredError(ChatError):

    def __init__(self, reason):
        ChatError.__init__(self, CHAT_RESPONSES.addIgnoredError)
        self.__reason = reason
        self._messageArgs = {b'reason': reason}
        return

    def _getMessage(self):
        return b'Can`t add user to ignored users list: %s' % self.__reason


class SetMutedError(ChatError):

    def __init__(self, reason):
        ChatError.__init__(self, CHAT_RESPONSES.setMutedError)
        self.__reason = reason
        self._messageArgs = {b'reason': reason}
        return

    def _getMessage(self):
        return b'Can`t add user to muted users list: %s' % self.__reason


class UnsetMutedError(ChatError):

    def __init__(self, reason):
        ChatError.__init__(self, CHAT_RESPONSES.unsetMutedError)
        self.__reason = reason
        self._messageArgs = {b'reason': reason}
        return

    def _getMessage(self):
        return b'Can`t remove user from muted users list: %s' % self.__reason


class UserIgnoredError(ChatError):

    def __init__(self, ignorerName):
        ChatError.__init__(self, CHAT_RESPONSES.userIgnoredError)
        self.__ignorerName = ignorerName
        self._messageArgs = {b'ignorer': ignorerName}
        return

    def _getMessage(self):
        return b'You are in the ignored users list of user %s' % self.__ignorerName


class CreatePrivateError(ChatError):

    def __init__(self, reason):
        ChatError.__init__(self, CHAT_RESPONSES.createPrivateError)
        self.__reason = reason
        self._messageArgs = {b'reason': reason}
        return

    def _getMessage(self):
        return b'Can`t create private channel: %s' % self.__reason


class ActiveChannelsLimitReached(ChatError):

    def __init__(self, limit):
        ChatError.__init__(self, CHAT_RESPONSES.activeChannelsLimitReached)
        self.__limit = limit
        self._messageArgs = {b'limit': limit}
        return

    def _getMessage(self):
        return b'You have reached limit in %d opened channels' % self.__limit


class UsersRosterLimitReached(ChatError):

    def __init__(self, limit):
        ChatError.__init__(self, CHAT_RESPONSES.usersRosterLimitReached)
        self.__limit = limit
        self._messageArgs = {b'limit': limit}
        return

    def _getMessage(self):
        return b'You already have maximum number of users (friends and ignored) allowed: %d' % self.__limit


class ChatCommandError(ChatError):

    def __init__(self, response=None, error=None):
        ChatError.__init__(self, CHAT_RESPONSES.chatCommandError if response is None else response)
        self.__error = error
        if error is not None:
            self._messageArgs = {b'error': error}
        return

    def _getMessage(self):
        return b'Chat command error occurred: %s' % (self.__error,)


class InviteCommandError(ChatError):

    def __init__(self, inviteID, response=None, error=None):
        ChatError.__init__(self, CHAT_RESPONSES.inviteCommandError if response is None else response)
        self.__error = error
        self.__inviteID = inviteID
        self._messageArgs = {b'inviteID': inviteID}
        if error is not None:
            self._messageArgs[b'error'] = error
        return

    def _getMessage(self):
        return b'Invite command error occurred: %s during processing invite wit ID: %s' % (
         self.__error, self.__inviteID)


class InviteCreateError(InviteCommandError):

    def __init__(self, response=None, error=None):
        InviteCommandError.__init__(self, None, response=CHAT_RESPONSES.inviteCreateError if response is None else response, error=error)
        return


class InviteCreationNotAllowed(InviteCreateError):

    def __init__(self, response=None, error=None):
        InviteCreateError.__init__(self, response=CHAT_RESPONSES.inviteCreationNotAllowed if response is None else response, error=error)
        return


class ChatCommandInCooldown(ChatCommandError):

    def __init__(self, command):
        ChatCommandError.__init__(self, CHAT_RESPONSES.commandInCooldown)
        coolDownConfig = getattr(command, b'cooldown') if hasattr(command, b'cooldown') else {}
        coolDownPeriod = coolDownConfig.get(b'period', None)
        self._messageArgs = {b'command': (command.name()), 
           b'cooldownPeriod': coolDownPeriod}
        return


class ChatCommandNotAllowedError(ChatCommandError):

    def __init__(self):
        ChatCommandError.__init__(self, CHAT_RESPONSES.notAllowed, b'operation not allowed to user')
        return


class MemberAlreadyBanned(ChatCommandError):

    def __init__(self, member):
        ChatCommandError.__init__(self, CHAT_RESPONSES.memberAlreadyBanned)
        self._messageArgs = {b'user': member}
        return


class MemberAlreadyModerator(ChatCommandError):

    def __init__(self, member):
        ChatCommandError.__init__(self, CHAT_RESPONSES.memberAlreadyModerator)
        self._messageArgs = {b'user': member}
        return


class MemberNotModerator(ChatCommandError):

    def __init__(self, member):
        ChatCommandError.__init__(self, CHAT_RESPONSES.memberNotModerator)
        self._messageArgs = {b'user': member}
        return


class IncorrectCommandArgumentError(ChatCommandError):

    def __init__(self, arg):
        ChatCommandError.__init__(self, CHAT_RESPONSES.incorrectCommandArgument)
        self._messageArgs = {b'arg': arg}
        return


class ChatException(ChatError, Exception):

    def __init__(self, response=None):
        ChatError.__init__(self, response)
        return


class ChannelNotExists(ChatException):

    def __init__(self, id):
        ChatException.__init__(self, CHAT_RESPONSES.channelNotExists)
        self.__channelId = id
        return

    def _getMessage(self):
        return b'Channel with id: %s not exists' % self.__channelId


class UserNotExists(ChatException):

    def __init__(self, nickname):
        ChatException.__init__(self, CHAT_RESPONSES.userNotExists)
        self.__nickname = nickname
        self._messageArgs = {b'user': nickname}
        return

    def _getMessage(self):
        return b'User with nickname: %s not exists' % self.__nickname


SYS_MESSAGE_TYPE = Enumeration(b'systemMessageType', [
 302, 
 303, 
 304, 
 305, 
 306, 
 307, 
 308, 
 309, 
 310, 
 311, 
 312, 
 313, 
 314, 
 315, 
 316, 
 317, 
 318, 
 319, 
 320, 
 321, 
 322, 
 323, 
 324, 
 325, 
 326, 
 327, 
 328, 
 329, 
 330, 
 331, 
 332, 
 333, 
 334, 
 335, 
 336, 
 337, 
 338, 
 339, 
 340, 
 341, 
 342, 
 343, 
 344, 
 345, 
 346, 
 347, 
 348, 
 349, 
 350, 
 351, 
 352, 
 353, 
 354, 
 355, 
 356, 
 357, 
 358, 
 359, 
 360, 
 361, 
 362, 
 363, 
 364, 
 365, 
 366, 
 367, 
 368, 
 369, 
 370, 
 371, 
 372, 
 373, 
 374, 
 375, 
 376, 
 377, 
 378, 
 379, 
 380, 
 381, 
 382, 
 383, 
 384, 
 385, 
 386, 
 387, 
 388, 
 389, 
 390, 
 391, 
 392, 
 393, 
 394, 
 395, 
 396, 
 397, 
 398, 
 399, 
 400, 
 401, 
 402, 
 403, 
 404, 
 405, 
 406, 
 407, 
 408, 
 409, 
 410, 
 411, 
 412, 
 413, 
 414, 
 415, 
 416, 
 417, 
 418, 
 419, 
 420, 
 421, 
 422, 
 423, 
 424, 
 425, 
 426, 
 427, 
 428, 
 429, 
 430, 
 431, 
 432, 
 433, 
 434, 
 435, 
 436, 
 437, 
 438, 
 439, 
 440, 
 441])
SYS_MESSAGE_IMPORTANCE = Enumeration(b'systemMessageImportance', [
 b'normal',
 b'high'])
SM_REQUEST_PERSONAL_MESSAGES_FLAG = 1
SM_REQUEST_SYSTEM_MESSAGES_FLAG = 2
SM_REQUEST_INTERNAL_SYS_MESSAGES_FLAG = 4

class MapRemovedFromBLReason(object):
    MAP_DISABLED = 1
    SLOT_DISABLED = 2


def isMembersListSupported(channelInfo):
    if channelInfo is None:
        return False
    else:
        return isMembersListSupportedByFlags(channelInfo.get(b'notifyFlags', 0))
        return


def isMembersListSupportedByFlags(channelNotifyFlags):
    return getMembersListMode(channelNotifyFlags) in (
     CHAT_CHANNEL_NOTIFY_MEMBERS_DELTA, CHAT_CHANNEL_NOTIFY_MEMBERS_IN_OUT)


def getMembersListMode(channelNotifyFlags):
    return channelNotifyFlags & CHAT_CHANNEL_NOTIFY_MEMBERS_MASK


def setMembersListMode(channelNotifyFlags, newMode):
    oldMode = channelNotifyFlags & CHAT_CHANNEL_NOTIFY_MEMBERS_MASK
    channelNotifyFlags -= oldMode
    channelNotifyFlags += newMode
    return channelNotifyFlags


USERS_ROSTER_FRIEND = 1
USERS_ROSTER_IGNORED = 2
USERS_ROSTER_VOICE_MUTED = 4

def isFromFriendRoster(rosterData):
    return _checkRosterAccessBitmask(rosterData, USERS_ROSTER_FRIEND)


def isFromIgnoreRoster(rosterData):
    return _checkRosterAccessBitmask(rosterData, USERS_ROSTER_IGNORED)


def isVoiceMuted(rosterData):
    return _checkRosterAccessBitmask(rosterData, USERS_ROSTER_VOICE_MUTED)


def _checkRosterAccessBitmask(rosterData, bitmask):
    accessFlags = rosterData.get(b'accessFlags', 0) if rosterData is not None else 0
    return accessFlags & bitmask == bitmask


class MESSAGE_FILTER_TYPE(object):
    EXCLUDE = 1
    INCLUDE = 2


def compressSysMessage(message):
    if isinstance(message, dict):
        message = zlib.compress(cPickle.dumps(message, -1), 1)
    return message


def decompressSysMessage(message):
    try:
        message = cPickle.loads(zlib.decompress(message))
    except:
        pass

    return message
