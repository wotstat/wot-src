import enum
ROLE_EQUIPMENT_TAG = b'roleEquipment'
COMP7_CURRENT_SEASON = 4
COMP7_MASKOT_ID = b'5'
SEASONS_IN_YEAR = 4
COMP7_QUEST_PREFIX = (b'comp7_{maskot}_{season}').format(maskot=COMP7_MASKOT_ID, season=COMP7_CURRENT_SEASON)
COMP7_TOKEN_PREFIX = (b'comp7_{maskot}_{season}').format(maskot=COMP7_MASKOT_ID, season=COMP7_CURRENT_SEASON)
COMP7_QUEST_DELIMITER = b'_'
COMP7_TOKEN_WEEKLY_REWARD_ID = (b'comp7_{maskot}_{season}_weekly_rewards_token').format(maskot=COMP7_MASKOT_ID, season=COMP7_CURRENT_SEASON)
COMP7_TOKEN_WEEKLY_REWARD_NAME = b'comp7TokenWeeklyReward'
COMP7_TOKEN_COUPON_REWARD_ID = b'comp7:coupon'
COMP7_TOKEN_COUPON_REWARD_NAME = b'comp7TokenCouponReward'
COMP7_CUSTOMIZATION_PROGRESS_PREFIX = b'comp7_cust_progress_'
COMP7_QUALIFICATION_QUEST_ID = (b'comp7_{maskot}_{season}_ranks_65').format(maskot=COMP7_MASKOT_ID, season=COMP7_CURRENT_SEASON)
COMP7_SEASON_POINTS_ENTITLEMENT_TMPL = b'comp7_season_points'

def seasonPointsCodeBySeasonNumber(seasonNumber):
    return (b':').join((COMP7_SEASON_POINTS_ENTITLEMENT_TMPL, COMP7_MASKOT_ID, str(seasonNumber)))


def replaceComp7tokenID(tID, targetTokenPrefix):
    return tID.replace(COMP7_CUSTOMIZATION_PROGRESS_PREFIX, targetTokenPrefix)


SEASON_POINTS_ENTITLEMENTS = [seasonPointsCodeBySeasonNumber(n + 1) for n in range(SEASONS_IN_YEAR)]

@enum.unique
class Comp7QuestType(enum.Enum):
    RANKS = b'ranks'
    TOKENS = b'token'
    PERIODIC = b'period'
    ACTIVITY = b'activity'
    WEEKLY = b'weekly'


CLIENT_VISIBLE_QUESTS_TYPE = (
 Comp7QuestType.TOKENS,
 Comp7QuestType.RANKS,
 Comp7QuestType.PERIODIC,
 Comp7QuestType.WEEKLY)

class BattleStatuses(object):
    STARTED = 0
    WIN = 1
    LOSE = 2
    DESERTER = 3
    FINISHED_WITH_ERROR = 4
    STARTED_RANGE = (
     STARTED, WIN, LOSE, DESERTER)
    FINISHED_RANGE = (WIN, LOSE, DESERTER)


class Comp7QualificationState(object):
    NOT_STARTED = b'not_started'
    IN_PROGRESS = b'in_progress'
    WAITING_BATTLE_RESULTS = b'wait_battle_results'
    FINALIZING = b'finalizing'
    COMPLETED = b'completed'
    states = (
     NOT_STARTED, IN_PROGRESS, WAITING_BATTLE_RESULTS, FINALIZING, COMPLETED)

    @classmethod
    def isBattleAllowed(cls, state):
        return state in (cls.IN_PROGRESS, cls.COMPLETED)

    @classmethod
    def isUnitAllowed(cls, state):
        return state == cls.COMPLETED

    @classmethod
    def isQualificationActive(cls, state):
        return state != cls.COMPLETED

    @classmethod
    def isResultsProcessing(cls, state):
        return state in (cls.WAITING_BATTLE_RESULTS, cls.FINALIZING)

    @classmethod
    def isCalculationQualificationRating(cls, state):
        return state in (Comp7QualificationState.NOT_STARTED,)
