from __future__ import absolute_import
from collections import namedtuple
from string import Template
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES, CHAT_COMMANDS_THAT_IGNORE_COOLDOWNS, GENERIC_MESSENGER_ARGS
from constants import IS_CLIENT, IS_CHINA
from math_common import decimal_round
_g_id = None

def _makeID(start=None, range=None):
    global _g_id
    id = _g_id = _g_id + 1 if start is None else start
    if range is not None:
        _g_id += range
    return id


_COOLDOWN_OFFSET = 0.0 if IS_CLIENT else -0.1
_INITIAL_DEFAULT_BATTLE_CHAT_COOLDOWN_DURATION = 0.1
_SHORT_BATTLE_CHAT_COOLDOWN_DURATION = 0.0
_TEAM_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 6.0
_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 5.0
_SAME_PRIVATE_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 2.0
_OTHER_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 1.0
_ATTENTION_TO_COMMAND_COOLDOWN_DURATION = 0.2
_SAME_TARGET_PERSONAL_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 3.0
_REACTIONAL_CHAT_CMD_COOLDOWN_DURATION = 0.1
_MAX_ATTENTION_TO_CHAT_COMMANDS_WITHIN_TIMEFRAME = 3
_TIMEFRAME_FOR_ATTENTION_TO_STORAGE = 5
_MAX_ATTENTION_TO_PER_TEAM = 3

def messageArgs(int32Arg1=0, int64Arg1=0, floatArg1=0, strArg1=b'', strArg2=b'', int8Arg1=0):
    return {(GENERIC_MESSENGER_ARGS.INT32_ARG_1.value): int32Arg1, 
       (GENERIC_MESSENGER_ARGS.INT64_ARG_1.value): int64Arg1, 
       (GENERIC_MESSENGER_ARGS.FLOAT_ARG_1.value): floatArg1, 
       (GENERIC_MESSENGER_ARGS.STR_ARG_1.value): strArg1, 
       (GENERIC_MESSENGER_ARGS.STR_ARG_2.value): strArg2, 
       (GENERIC_MESSENGER_ARGS.INT8_ARG_1.value): int8Arg1}


EMPTY_ARGS = messageArgs()

class MESSENGER_ERRORS():
    NO_ERROR = _makeID(start=0)
    GENERIC_ERROR = _makeID()
    NOT_READY = _makeID()
    IN_COOLDOWN = _makeID()
    COMMAND_IN_TEAM_COOLDOWN = _makeID()
    IN_CHAT_BAN = _makeID()
    IS_BUSY = _makeID()
    NOT_ALLOWED = _makeID()
    WRONG_ARGS = _makeID()
    USER_NOT_FOUND = _makeID()
    CANNOT_BAN_ONESELF = _makeID()
    CUSTOM_ERROR_ID = _makeID()

    @staticmethod
    def getErrorName(errorCode):
        name = _MESSENGER_ERROR_NAMES.get(errorCode)
        if name is not None:
            return name
        else:
            return b'ERROR_CODE_' + str(errorCode)


class MESSENGER_LIMITS():
    FIND_USERS_BY_NAME_MAX_RESULT_SIZE = 50
    FIND_USERS_BY_NAME_REQUEST_COOLDOWN_SEC = 5.0 + _COOLDOWN_OFFSET
    BATTLE_CHANNEL_MESSAGE_MAX_SIZE = 140
    UNIT_CHANNEL_MESSAGE_MAX_SIZE = 512
    BATTLE_CHAT_HISTORY_ON_SERVER_MAX_LEN = 10
    UNIT_CHAT_HISTORY_ON_SERVER_MAX_LEN = 20
    BROADCASTS_FROM_CLIENT_COOLDOWN_SEC = (0.5 if not IS_CHINA else 3.0) + _COOLDOWN_OFFSET
    ADMIN_COMMANDS_FROM_CLIENT_COOLDOWN_SEC = 5.0 + _COOLDOWN_OFFSET
    VOIP_CREDENTIALS_REQUEST_COOLDOWN_SEC = 10.0 + _COOLDOWN_OFFSET


class MESSENGER_ACTION_IDS():
    RESPONSE_SUCCESS = _makeID(start=0)
    RESPONSE_FAILURE = _makeID()
    FIND_USERS_BY_NAME = _makeID()
    GET_VOIP_CREDENTIALS = _makeID()
    LOG_VIVOX_LOGIN = _makeID()
    ENTER_VOIP_CHANNEL = _makeID()
    LEAVE_VOIP_CHANNEL = _makeID()
    _ADMIN_COMMAND_START_ID = _makeID(range=10)
    _BATTLE_ACTION_START_ID = _makeID()
    INIT_BATTLE_CHAT = _makeID()
    REINIT_BATTLE_CHAT = _makeID()
    DEINIT_BATTLE_CHAT = _makeID()
    BROADCAST_BATTLE_MESSAGE = _makeID()
    ON_BATTLE_MESSAGE_BROADCAST = _makeID()
    _BATTLE_CHAT_COMMAND_START_ID = _makeID(range=100)
    _BATTLE_ACTION_END_ID = _makeID()
    _UNIT_ACTION_START_ID = _makeID()
    INIT_UNIT_CHAT = _makeID()
    DEINIT_UNIT_CHAT = _makeID()
    BROADCAST_UNIT_MESSAGE = _makeID()
    ON_UNIT_MESSAGE_BROADCAST = _makeID()
    _UNIT_COMMAND_START_ID = _makeID(range=100)
    _UNIT_ACTION_END_ID = _makeID()
    CUSTOM_ACTION_ID = _makeID()

    @staticmethod
    def getActionName(actionID):
        name = _MESSENGER_ACTION_NAMES.get(actionID)
        if name is not None:
            return name
        else:
            actions = MESSENGER_ACTION_IDS
            cmd = actions.adminChatCommandFromActionID(actionID)
            if cmd is not None:
                return b'command:' + cmd.name
            cmd = actions.battleChatCommandFromActionID(actionID)
            if cmd is not None:
                return b'command:' + cmd.name
            offs = actionID - actions.CUSTOM_ACTION_ID
            if offs >= 0:
                return b'CUSTOM_ACTION_ID+' + str(offs)
            return str(actionID)

    @staticmethod
    def isBattleChatAction(actionID):
        actions = MESSENGER_ACTION_IDS
        return actions._BATTLE_ACTION_START_ID <= actionID <= actions._BATTLE_ACTION_END_ID

    @staticmethod
    def isUnitChatAction(actionID):
        actions = MESSENGER_ACTION_IDS
        return actions._UNIT_ACTION_START_ID <= actionID <= actions._UNIT_ACTION_END_ID

    @staticmethod
    def isRateLimitedBroadcastFromClient(actionID):
        actions = MESSENGER_ACTION_IDS
        if actionID in (actions.BROADCAST_BATTLE_MESSAGE, actions.BROADCAST_UNIT_MESSAGE):
            return True
        battleChatCmdStartID = actions._BATTLE_CHAT_COMMAND_START_ID
        if battleChatCmdStartID <= actionID < battleChatCmdStartID + len(BATTLE_CHAT_COMMANDS):
            cmdName = actions.battleChatCommandFromActionID(actionID).name
            if cmdName == BATTLE_CHAT_COMMAND_NAMES.ATTENTION_TO_POSITION or cmdName in CHAT_COMMANDS_THAT_IGNORE_COOLDOWNS:
                return False
            return True
        return False

    @staticmethod
    def isChatActionSusceptibleToBan(actionID):
        actions = MESSENGER_ACTION_IDS
        if actions.adminChatCommandFromActionID(actionID) is not None:
            return True
        else:
            if actions.isBattleChatAction(actionID):
                return actions.battleChatCommandFromActionID(actionID) is None
            if actions.isUnitChatAction(actionID):
                return True
            return False

    @staticmethod
    def battleChatCommandFromActionID(actionID):
        startID = MESSENGER_ACTION_IDS._BATTLE_CHAT_COMMAND_START_ID
        if startID <= actionID < startID + len(BATTLE_CHAT_COMMANDS):
            return BATTLE_CHAT_COMMANDS[actionID - startID]
        else:
            return

    @staticmethod
    def unitChatCommandFromActionID(actionID):
        startID = MESSENGER_ACTION_IDS._UNIT_COMMAND_START_ID
        if startID <= actionID < startID + len(UNIT_CHAT_COMMANDS):
            return UNIT_CHAT_COMMANDS[actionID - startID]
        else:
            return

    @staticmethod
    def adminChatCommandFromActionID(actionID):
        startID = MESSENGER_ACTION_IDS._ADMIN_COMMAND_START_ID
        if startID <= actionID < startID + len(ADMIN_CHAT_COMMANDS):
            return ADMIN_CHAT_COMMANDS[actionID - startID]
        else:
            return


RESPONSE_MESSENGER_ACTION_IDS = (
 MESSENGER_ACTION_IDS.RESPONSE_SUCCESS, MESSENGER_ACTION_IDS.RESPONSE_FAILURE)

class CHAT_COMMAND_COOLDOWN_TYPE_IDS():
    TIMEFRAME_DATA_COOLDOWN = _makeID()
    SAME_COMMAND_COOLDOWN = _makeID()
    OTHER_COMMANDS_COOLDOWN = _makeID()
    PRIVATE_COMMANDS_COOLDOWN = _makeID()
    ATTENTION_TO_BLOCKED_COOLDOWN = _makeID()


_MESSENGER_ACTION_NAMES = {_id: _name for _name, _id in MESSENGER_ACTION_IDS.__dict__.items() if isinstance(_id, int) and not _name.startswith(b'_')}
_MESSENGER_ERROR_NAMES = {_id: _name for _name, _id in MESSENGER_ERRORS.__dict__.items() if not _name.startswith(b'_')}
AdminChatCommand = namedtuple(b'AdminChatCommand', (
 b'id',
 b'name',
 b'timeout'))
ADMIN_CHAT_COMMANDS = (
 AdminChatCommand(id=_makeID(start=MESSENGER_ACTION_IDS._ADMIN_COMMAND_START_ID), name=b'USERBAN', timeout=30.0),
 AdminChatCommand(id=_makeID(), name=b'USERUNBAN', timeout=30.0))
ADMIN_CHAT_COMMANDS_BY_NAMES = {v.name: v for v in ADMIN_CHAT_COMMANDS}
BattleChatCommand = namedtuple(b'BattleChatCommand', (
 b'id',
 b'name',
 b'cooldownPeriod',
 b'msgText',
 b'vehMarker',
 b'senderVehMarker',
 b'soundNotification',
 b'msgOnMarker',
 b'soundNotificationReply'))
BattleChatCommand.__new__.__defaults__ = (
 0, None, 0, None, None, None, None, None, None)
UnitChatCommand = namedtuple(b'UnitChatCommand', (
 b'id',
 b'name',
 b'cooldownPeriod',
 b'msgText'))
UNIT_CHAT_COMMANDS = (
 UnitChatCommand(id=_makeID(start=MESSENGER_ACTION_IDS._UNIT_COMMAND_START_ID), name=b'ATTENTIONTOCELL', cooldownPeriod=1.0 + _COOLDOWN_OFFSET, msgText=b'attention_to_cell'),)
UNIT_CHAT_COMMANDS_BY_NAMES = {v.name: v for v in UNIT_CHAT_COMMANDS}
BATTLE_CHAT_COMMANDS = [
 BattleChatCommand(id=_makeID(start=MESSENGER_ACTION_IDS._BATTLE_CHAT_COMMAND_START_ID), name=BATTLE_CHAT_COMMAND_NAMES.SOS, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'help_me', vehMarker=b'help_me', senderVehMarker=None, soundNotification=b'ibc_ping_request', soundNotificationReply=b'ibc_ping_help_me_ex_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.POSITIVE, cooldownPeriod=_SAME_PRIVATE_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'positive', vehMarker=b'positive', senderVehMarker=None, soundNotification=b'ibc_ping_affirmative', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.NEGATIVE, cooldownPeriod=_SAME_PRIVATE_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'negative', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.AFFIRMATIVE, cooldownPeriod=_SAME_PRIVATE_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'affirmative', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=b'ATTENTIONTOCELL', cooldownPeriod=_SHORT_BATTLE_CHAT_COOLDOWN_DURATION + _COOLDOWN_OFFSET, msgText=b'attention_to_cell', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.ATTENTION_TO_POSITION, cooldownPeriod=_ATTENTION_TO_COMMAND_COOLDOWN_DURATION, msgText=b'attention_to_position', vehMarker=b'attention_to', senderVehMarker=None, soundNotification=b'ibc_ping_attention', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.REPLY, cooldownPeriod=_REACTIONAL_CHAT_CMD_COOLDOWN_DURATION, msgText=None, vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.CANCEL_REPLY, cooldownPeriod=_REACTIONAL_CHAT_CMD_COOLDOWN_DURATION, msgText=None, vehMarker=None, senderVehMarker=None, soundNotification=b'ibc_ping_cancel', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.ATTACK_OBJECTIVE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attention_to_objective_atk', vehMarker=b'attackObjective', senderVehMarker=None, soundNotification=b'ibc_ping_request', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.ATTACKING_OBJECTIVE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attention_to_objective_atk_autocommit', vehMarker=b'attackingObjective', senderVehMarker=None, soundNotification=b'ibc_ping_action', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.DEFEND_OBJECTIVE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attention_to_objective_def', vehMarker=b'defendObjective', senderVehMarker=None, soundNotification=b'ibc_ping_request', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.DEFENDING_OBJECTIVE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attention_to_objective_def_autocommit', vehMarker=b'defendingObjective', senderVehMarker=None, soundNotification=b'ibc_ping_request', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.ATTACK_BASE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attention_to_base_atk', vehMarker=b'attackBase', senderVehMarker=None, soundNotification=b'ibc_ping_request', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.DEFEND_BASE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attention_to_base_def', vehMarker=b'defendBase', senderVehMarker=None, soundNotification=b'ibc_ping_request', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.SPG_AIM_AREA, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'spg_aim_area', vehMarker=None, senderVehMarker=None, soundNotification=b'ibc_ping_attention', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.ATTACKING_ENEMY_WITH_SPG, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attack_enemy_with_SPG', vehMarker=b'attack', senderVehMarker=b'attackSender', soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.TURNBACK, cooldownPeriod=_SAME_PRIVATE_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'turn_back', vehMarker=b'turn_back', senderVehMarker=None, soundNotification=b'ibc_ping_retreat', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.HELPME, cooldownPeriod=_SAME_PRIVATE_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'help_me_ex', vehMarker=b'help_me_ex', senderVehMarker=None, soundNotification=b'ibc_ping_help_me_ex', soundNotificationReply=b'ibc_ping_help_me_ex_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.ATTACK_ENEMY, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attack_enemy', vehMarker=b'attack', senderVehMarker=b'attackSender', soundNotification=b'ibc_ping_request', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.RELOADINGGUN, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'reloading_gun', vehMarker=b'reloading_gun', senderVehMarker=None, soundNotification=b'ibc_ping_attention', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.THANKS, cooldownPeriod=_SAME_PRIVATE_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'thanks', vehMarker=b'thanks', senderVehMarker=None, soundNotification=b'ibc_ping_thanks', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.RELOADING_CASSETE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'reloading_cassette', vehMarker=b'reloading_gun', senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.RELOADING_READY, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'reloading_ready', vehMarker=None, senderVehMarker=None, soundNotification=b'ibc_ping_attention', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.RELOADING_READY_CASSETE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'reloading_ready_cassette', vehMarker=None, senderVehMarker=None, soundNotification=b'ibc_ping_attention', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.RELOADING_UNAVAILABLE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'reloading_unavailable', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.OVERHEATEDGUN, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'overheated_gun', vehMarker=b'reloading_gun', senderVehMarker=None, soundNotification=b'ibc_ping_attention', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_SAVE_TANKS_ATK, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'global_msg/atk/save_tanks', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.GOING_THERE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'going_there', vehMarker=b'goingTo', senderVehMarker=None, soundNotification=b'ibc_ping_action', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_SAVE_TANKS_DEF, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'global_msg/def/save_tanks', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_TIME_ATK, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'global_msg/atk/time', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_TIME_DEF, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'global_msg/def/time', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_HQ_ATK, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'global_msg/atk/focus_hq', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_HQ_DEF, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'global_msg/def/focus_hq', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_WEST, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'global_msg/lane/west', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_CENTER, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'global_msg/lane/center', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EPIC_GLOBAL_EAST, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'global_msg/lane/east', vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_1, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_1', msgOnMarker=b'event_chat_1'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_2, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_2', msgOnMarker=b'event_chat_2'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_3, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_3', msgOnMarker=b'event_chat_3'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_4, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_4', msgOnMarker=b'event_chat_4'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_5, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_5', msgOnMarker=b'event_chat_5'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_6, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_6', msgOnMarker=b'event_chat_6'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_7, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_7', msgOnMarker=b'event_chat_7'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_1_EX, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_1_ex', msgOnMarker=b'event_chat_1'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_2_EX, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_2_ex', msgOnMarker=b'event_chat_2'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_3_EX, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_3_ex', msgOnMarker=b'event_chat_3'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_4_EX, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_4_ex', msgOnMarker=b'event_chat_4'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_5_EX, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_5_ex', msgOnMarker=b'event_chat_5'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_6_EX, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_6_ex', msgOnMarker=b'event_chat_6'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.EVENT_CHAT_7_EX, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, msgText=b'event_chat_7_ex', msgOnMarker=b'event_chat_7'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.CLEAR_CHAT_COMMANDS, cooldownPeriod=_REACTIONAL_CHAT_CMD_COOLDOWN_DURATION, msgText=None, vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.ATTACKING_ENEMY, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attacking_enemy', vehMarker=b'attack', senderVehMarker=b'attackSender', soundNotification=b'ibc_ping_action', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.SUPPORTING_ALLY, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'supporting_ally', vehMarker=b'supportingAlly', senderVehMarker=None, soundNotification=b'ibc_ping_help_me_ex_reply', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.DEFENDING_BASE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'defending_base', vehMarker=b'defendingBase', senderVehMarker=None, soundNotification=b'ibc_ping_action', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.ATTACKING_BASE, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'attacking_base', vehMarker=b'attackingBase', senderVehMarker=None, soundNotification=b'ibc_ping_action', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.PREBATTLE_WAYPOINT, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'going_there', vehMarker=b'goingTo', senderVehMarker=None, soundNotification=None, soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.CONFIRM, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=None, vehMarker=b'positive', senderVehMarker=None, soundNotification=b'ibc_ping_attention', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.VEHICLE_SPOTPOINT, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=None, vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.SHOOTING_POINT, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=None, vehMarker=None, senderVehMarker=None, soundNotification=b'mt_combat_marker', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.NAVIGATION_POINT, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=None, vehMarker=None, senderVehMarker=None, soundNotification=b'mt_navi_marker', soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.FLAG_POINT, cooldownPeriod=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=None, vehMarker=None, senderVehMarker=None, soundNotification=None, soundNotificationReply=None),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.MOVE_TO_TARGET_POINT, cooldownPeriod=_SAME_TARGET_PERSONAL_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'move_to_target', vehMarker=b'attackObjective', senderVehMarker=None, soundNotification=b'ibc_ping_request', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.MOVING_TO_TARGET_POINT, cooldownPeriod=_SAME_TARGET_PERSONAL_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=b'move_to_target_autocommit', vehMarker=b'attackingObjective', senderVehMarker=None, soundNotification=b'ibc_ping_action', soundNotificationReply=b'ibc_ping_reply'),
 BattleChatCommand(id=_makeID(), name=BATTLE_CHAT_COMMAND_NAMES.COMMENDATION, cooldownPeriod=0.5 + _COOLDOWN_OFFSET, soundNotification=b'ibc_ping_request', soundNotificationReply=b'ibc_ping_reply')]
BATTLE_CHAT_COMMANDS_BY_NAMES = {v.name: v for v in BATTLE_CHAT_COMMANDS}
ExtBattleChatCommand = namedtuple(b'ExtBattleChatCommand', (
 b'name',
 b'markerType',
 b'cooldownPeriod',
 b'processorType',
 b'msgText',
 b'vehMarker',
 b'senderVehMarker',
 b'soundNotification',
 b'msgOnMarker',
 b'soundNotificationReply'))
ExtBattleChatCommand.__new__.__defaults__ = (
 None, None, 0, 0, None, None, None, None, None, None)

def addBattleChatCommand(extCommand):
    command = BattleChatCommand(id=_makeID(start=MESSENGER_ACTION_IDS._BATTLE_CHAT_COMMAND_START_ID + len(BATTLE_CHAT_COMMANDS)), name=extCommand.name, cooldownPeriod=extCommand.cooldownPeriod if extCommand.cooldownPeriod > 0 else _SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, msgText=extCommand.msgText, vehMarker=extCommand.vehMarker, senderVehMarker=extCommand.senderVehMarker, soundNotification=extCommand.soundNotification, msgOnMarker=extCommand.msgOnMarker, soundNotificationReply=extCommand.soundNotificationReply)
    BATTLE_CHAT_COMMANDS.append(command)
    BATTLE_CHAT_COMMANDS_BY_NAMES[extCommand.name] = command
    return


class MUC_SERVICE_TYPE(object):
    STANDARD = 1
    USER = 2
    CLAN = 3


MUC_SERVICE_TYPES = frozenset((MUC_SERVICE_TYPE.CLAN, MUC_SERVICE_TYPE.STANDARD, MUC_SERVICE_TYPE.USER))

def resolveMucRoomsOfService(service):
    t = Template(service[b'format'])
    return t.substitute(service)


def canResolveMucRoomsOfService(service):
    canResolve = False
    try:
        Template(service[b'format']).substitute(service)
        canResolve = True
    except:
        pass

    return canResolve


ChatCommandBlockedData = namedtuple(b'ChatCommandBlockedData', (
 b'reqID',
 b'cmdID',
 b'cooldownType',
 b'cooldownEnd',
 b'targetID'))
COOLDOWN_SETTING_NAMES = (
 b'teamChatCmdCooldown',
 b'sameChatCmdCooldown',
 b'sameTargetChatCmdCooldown',
 b'otherChatCmdCooldown',
 b'attentionToTeamLimit',
 b'attentionToTimeframeLimit',
 b'timeframeToAttentionCmds')
BattleChatCmdGameModeCoolDownData = namedtuple(b'BattleChatCmdGameModeCoolDownData', COOLDOWN_SETTING_NAMES)
DEFAULT_SPAM_PROTECTION_SETTING = BattleChatCmdGameModeCoolDownData(teamChatCmdCooldown=_TEAM_BATTLE_CHAT_CMD_COOLDOWN_DURATION, sameChatCmdCooldown=_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION, sameTargetChatCmdCooldown=_SAME_TARGET_PERSONAL_BATTLE_CHAT_CMD_COOLDOWN_DURATION, otherChatCmdCooldown=_OTHER_BATTLE_CHAT_CMD_COOLDOWN_DURATION, attentionToTeamLimit=_MAX_ATTENTION_TO_PER_TEAM, attentionToTimeframeLimit=_MAX_ATTENTION_TO_CHAT_COMMANDS_WITHIN_TIMEFRAME, timeframeToAttentionCmds=_TIMEFRAME_FOR_ATTENTION_TO_STORAGE)
BATTLE_CMD_COOLDOWN_ALLOWED_MARGIN = 0.1

def areSenderCooldownsActive(currTime, listOfCoolDownTimeData, cmdIDToSend, targetIDToSend):
    if listOfCoolDownTimeData is None:
        return listOfCoolDownTimeData
    else:
        removeDataList = []
        blockReasonData = None
        for cmdBlockedData in listOfCoolDownTimeData:
            if decimal_round(cmdBlockedData.cooldownEnd - currTime, 2) <= BATTLE_CMD_COOLDOWN_ALLOWED_MARGIN:
                removeDataList.append(cmdBlockedData)
            else:
                validBlockData = None
                if cmdBlockedData.cooldownType == CHAT_COMMAND_COOLDOWN_TYPE_IDS.SAME_COMMAND_COOLDOWN and cmdBlockedData.cmdID == cmdIDToSend:
                    validBlockData = cmdBlockedData
                elif cmdBlockedData.cooldownType == CHAT_COMMAND_COOLDOWN_TYPE_IDS.OTHER_COMMANDS_COOLDOWN and cmdBlockedData.cmdID != cmdIDToSend:
                    validBlockData = cmdBlockedData
                elif cmdBlockedData.cooldownType == CHAT_COMMAND_COOLDOWN_TYPE_IDS.PRIVATE_COMMANDS_COOLDOWN and cmdBlockedData.targetID == targetIDToSend:
                    validBlockData = cmdBlockedData
                elif cmdBlockedData.cooldownType == CHAT_COMMAND_COOLDOWN_TYPE_IDS.ATTENTION_TO_BLOCKED_COOLDOWN and cmdBlockedData.cmdID == cmdIDToSend:
                    validBlockData = cmdBlockedData
                if cmdBlockedData.cooldownType != CHAT_COMMAND_COOLDOWN_TYPE_IDS.TIMEFRAME_DATA_COOLDOWN and validBlockData is not None:
                    blockReasonData = validBlockData

        if removeDataList:
            for cdData in removeDataList:
                if cdData in listOfCoolDownTimeData:
                    listOfCoolDownTimeData.remove(cdData)

        return blockReasonData


def addCoolDowns(currTime, listOfCoolDownTimeData, cmdID, cmdName, cmdCooldownTime, cmdTargetID, reqID, cooldownConf):
    listOfCoolDownTimeData.append(ChatCommandBlockedData(reqID=reqID, cmdID=cmdID, cooldownType=CHAT_COMMAND_COOLDOWN_TYPE_IDS.SAME_COMMAND_COOLDOWN, cooldownEnd=currTime + cmdCooldownTime, targetID=cmdTargetID))
    listOfCoolDownTimeData.append(ChatCommandBlockedData(reqID=reqID, cmdID=cmdID, cooldownType=CHAT_COMMAND_COOLDOWN_TYPE_IDS.OTHER_COMMANDS_COOLDOWN, cooldownEnd=currTime + cooldownConf.otherChatCmdCooldown, targetID=cmdTargetID))
    if cmdName in (BATTLE_CHAT_COMMAND_NAMES.HELPME, BATTLE_CHAT_COMMAND_NAMES.THANKS,
     BATTLE_CHAT_COMMAND_NAMES.TURNBACK):
        listOfCoolDownTimeData.append(ChatCommandBlockedData(reqID=reqID, cmdID=cmdID, cooldownType=CHAT_COMMAND_COOLDOWN_TYPE_IDS.PRIVATE_COMMANDS_COOLDOWN, cooldownEnd=currTime + cooldownConf.sameTargetChatCmdCooldown, targetID=cmdTargetID))
    if cmdName == BATTLE_CHAT_COMMAND_NAMES.ATTENTION_TO_POSITION:
        activeOldAttComands = [blockData for blockData in listOfCoolDownTimeData if blockData.cmdID == cmdID and blockData.cooldownType == CHAT_COMMAND_COOLDOWN_TYPE_IDS.TIMEFRAME_DATA_COOLDOWN]
        if activeOldAttComands and len(activeOldAttComands) >= cooldownConf.attentionToTimeframeLimit - 1:
            data = ChatCommandBlockedData(reqID=reqID, cmdID=cmdID, cooldownType=CHAT_COMMAND_COOLDOWN_TYPE_IDS.ATTENTION_TO_BLOCKED_COOLDOWN, cooldownEnd=currTime + cooldownConf.sameChatCmdCooldown, targetID=cmdTargetID)
        else:
            data = ChatCommandBlockedData(reqID=reqID, cmdID=cmdID, cooldownType=CHAT_COMMAND_COOLDOWN_TYPE_IDS.TIMEFRAME_DATA_COOLDOWN, cooldownEnd=currTime + cooldownConf.timeframeToAttentionCmds, targetID=cmdTargetID)
        listOfCoolDownTimeData.append(data)
    return
