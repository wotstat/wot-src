from enum import Enum
CMD_COLLECT_REWARDS = 31002
CMD_BUY_STEP_TOKENS = 31003
CMD_CLAIM_RARE_REWARD = 31004
DEV_CMD_ADD_PROGRESSION_TOKEN = 31005
DEV_CMD_SET_CYCLE = 31009
DEV_CMD_SET_QUEST = 31010
CMD_BUY_SHOP_PRODUCT = 31014
DEV_CMD_ADD_ARMORY_COIN = 31015
CMD_REROLL_ARMORY_QUEST = 31029
CMD_ACCEPT_REROLL_ARMORY_QUEST = 31030
DAY_BEFORE_END_STYLE_QUEST = 2
MAX_BUNDLE_TOKENS = 99
PDATA_KEY_ARMORY_YARD = b'armoryYard'
ARMORY_YARD_COIN_NAME = b'armory_coin'
FEATURE_NAME_BASE = b'armory_yard'
STAGE_TOKEN_POSTFIX = b'C'
BATTLE_TOKEN_POSTFIX = b'B'
BATTLE_POST_PROGRESSION_TOKEN_POSTFIX = b'Bp'
PROGRESSION_TOKEN_POSTFIX = b'progression'
POST_PROGRESSION_TOKEN_POSTFIX = b'post_progression'
SUBTRAHEND_STAGE_TOKEN_POSTFIX = b'D'
END_TOKEN_POSTFIX = b'end'
PURCHASE_STAGE_ENT_POSTFIX = b'paid'
END_QUEST_POSTFIX = b'end'
CONVERTER_QUEST_POSTFIX = b'converter'
FREE_REROLL_POSTFIX = b'free_reroll'
DAILY_FREE_REROLLED_POSTFIX = b'daily_free_rerolled'
PROGRESSION_LEVEL_PDATA_KEY = b'progressionLevel'
CLAIMED_FINAL_REWARD = b'claimedFinalReward'
CLAIMED_PROGRESSION_REWARD = b'claimedProgressionReward'
CLAIMED_POST_PROGRESSION_REWARD = b'claimedPostProgressionReward'
SHOP_PDATA_KEY = b'shop'
SHOP_LAST_SEASON_COMPLETED = b'isLastSeasonCompleted'
SHOP_PRODUCT_LIMITS = b'limits'
QUEST_CONDITION_OVERRIDE_PDATA_KEY = b'questConditionsOverride'
CURRENT_REROLL_PDATA_KEY = b'currentReroll'
LAST_SUGGESTED_CONDITIONS = b'lastSuggestedConditions'
NEED_CLEAR_REROLL_PROGRESS = b'clearReroll'
POSTBATTLE_QUEST = b'postBattle'
INTRO_VIDEO = None
STYLE_QUEST_POSTFIX = b'style'
VEHICLE_NAME = b'ussr:R75_SU122_54'
POST_PROGRESSION_SHORT_NAME = b'post_prog'

class State(Enum):
    BEFOREPROGRESSION = b'beforeProgression'
    ACTIVE = b'active'
    PURCHASESTAGE = b'purchaseStage'
    COMPLETED = b'completed'
    DISABLED = b'disabled'
    NOTREPLACED = b'notReplaced'


DISABLED_STATES = (
 State.DISABLED, State.BEFOREPROGRESSION)

def getStageToken(cycleID):
    return (b':').join((FEATURE_NAME_BASE, (b'cycle_{}').format(cycleID), STAGE_TOKEN_POSTFIX))


def getSubtrahendStageToken(seasonID):
    return (b':').join((FEATURE_NAME_BASE, (b'season_{}').format(seasonID), SUBTRAHEND_STAGE_TOKEN_POSTFIX))


def getProgressionToken(seasonID):
    return (b':').join((FEATURE_NAME_BASE, (b'season_{}').format(seasonID), PROGRESSION_TOKEN_POSTFIX))


def getPostProgressionToken(seasonID):
    return (b':').join((FEATURE_NAME_BASE, (b'season_{}').format(seasonID), POST_PROGRESSION_TOKEN_POSTFIX))


def getBattleToken(cycleID):
    return (b':').join((FEATURE_NAME_BASE, (b'cycle_{}').format(cycleID), BATTLE_TOKEN_POSTFIX))


def getBattlePostProgressionToken(seasonID):
    return (b':').join((FEATURE_NAME_BASE, (b'season_{}').format(seasonID), BATTLE_POST_PROGRESSION_TOKEN_POSTFIX))


def getFreeRerollToken(groupName):
    return (b':').join((groupName, FREE_REROLL_POSTFIX))


def getDailyUserFreeRerolledToken(groupName):
    return (b':').join((groupName, DAILY_FREE_REROLLED_POSTFIX))


def getEndToken(cycleID):
    return (b':').join((FEATURE_NAME_BASE, (b'cycle_{}').format(cycleID), END_TOKEN_POSTFIX))


def getPurchaseStagePaidEntitlement(seasonID):
    return (b':').join((FEATURE_NAME_BASE, (b'season_{}').format(seasonID), PURCHASE_STAGE_ENT_POSTFIX))


def getGroupName(cycleID):
    return (b'_').join((FEATURE_NAME_BASE, (b'cycle_{}').format(cycleID)))


POST_PROGRESSION_GROUP_PREFIX = FEATURE_NAME_BASE + b'_' + POST_PROGRESSION_SHORT_NAME
_POST_PROGRESSION_GROUP_TEMPLATE = POST_PROGRESSION_GROUP_PREFIX + b'_{}'

def getPostProgressionGroupName(seasonID):
    return _POST_PROGRESSION_GROUP_TEMPLATE.format(seasonID)


def getEndQuestID(cycleID):
    return (b'_').join((FEATURE_NAME_BASE, (b'cycle_{}').format(cycleID), END_QUEST_POSTFIX))


def getBundleBlockToken(seasonID):
    return (b'{}_starter_pack:season_{}').format(FEATURE_NAME_BASE, seasonID)


def getFinalEndQuestID(seasonID):
    return (b'_').join((FEATURE_NAME_BASE, (b'season_{}').format(seasonID), END_QUEST_POSTFIX))


def isArmoryYardToken(tokenID):
    return tokenID.startswith(FEATURE_NAME_BASE)


def isArmoryYardBattleToken(tokenID):
    return tokenID.startswith(FEATURE_NAME_BASE) and tokenID.endswith(BATTLE_TOKEN_POSTFIX)


def isArmoryYardCycleToken(tokenID):
    return tokenID.startswith(FEATURE_NAME_BASE) and tokenID.endswith(STAGE_TOKEN_POSTFIX)


def isArmoryYardStyleQuest(questId):
    return questId.startswith(FEATURE_NAME_BASE) and questId.endswith(STYLE_QUEST_POSTFIX)


def armoryInitialData():
    return {b'currentSeason': None, 
       CLAIMED_PROGRESSION_REWARD: False, 
       CLAIMED_POST_PROGRESSION_REWARD: False, 
       PROGRESSION_LEVEL_PDATA_KEY: 0, 
       SHOP_PDATA_KEY: {b'limits': {}, SHOP_LAST_SEASON_COMPLETED: False}, 
       QUEST_CONDITION_OVERRIDE_PDATA_KEY: {}, LAST_SUGGESTED_CONDITIONS: [], CURRENT_REROLL_PDATA_KEY: {}}


TEMP_TOKENS_LIFETIME_IN_HOURS = 240
COMPLETED_CONDITION_POSTFIX = b'completed'
ARMORY_YARD_QUEST_PREFIX = b'armory_yard_cycle'
CONDITION_PREFIX = b'armory_yard_condition'
NEED_TOKEN_QUEST_COMPLETE_POSTFIX = b'nc'

def getConditionToken(conditionID):
    return (b'armory_yard_condition:{}').format(conditionID)


def getConditionCompletedToken(conditionID):
    return (b'armory_yard_condition:{}:completed').format(conditionID)


def getConditionIDByToken(token):
    return int(token.split(b':')[1])


def getConditionTokenByQuestID(questID):
    return questID.rsplit(b':', 1)[0]


def getConditionIDByQuestID(questID):
    return int(questID.split(b':')[1])


def getQuestCompletedToken(questID):
    return (b'{}:{}').format(questID, NEED_TOKEN_QUEST_COMPLETE_POSTFIX)


ARMORY_YARD_SYS_MSG_PROGRESSION = b'ay_progression'
ARMORY_YARD_SYS_MSG_POST_PROGRESSION = b'ay_post_progression'
TOKEN_EXTRA_TIME_TO_LIVE = 4320
