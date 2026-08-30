from enum import Enum, unique
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS
from gui.shared.money import Currency
from shared_utils import CONST_CONTAINER

class RankTypes(CONST_CONTAINER):
    ACCOUNT = b'account'
    VEHICLE = b'vehicle'


class YearAwardsNames(CONST_CONTAINER):
    SMALL = RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_SMALL
    MEDIUM = RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_MEDIUM
    BIG = RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_BIG
    LARGE = RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_LARGE


YEAR_AWARDS_ORDER = (
 YearAwardsNames.SMALL,
 YearAwardsNames.MEDIUM,
 YearAwardsNames.BIG,
 YearAwardsNames.LARGE)
ZERO_RANK_ID = 0
ZERO_DIVISION_ID = 0
MAX_GROUPS_IN_DIVISION = 3
AWARDS_ORDER = (
 b'items', Currency.CREDITS, b'premium', b'premium_plus', b'premium_vip',
 Currency.GOLD, b'battleToken', b'tokens', b'entitlements', Currency.CRYSTAL)
YEAR_AWARDS_BONUS_ORDER = (
 Currency.CRYSTAL, b'customizations', b'items', b'selectableBonus', b'vehicles')
DEFAULT_REWARDS_COUNT = 7

class RankedDossierKeys(CONST_CONTAINER):
    ARCHIVE = b'Archive'
    SEASON = b'Season%s'


ARCHIVE_SEASON_ID = 0
STANDARD_POINTS_COUNT = 1
NOT_IN_LEAGUES_QUEST = b'ranked_{}_0_common'
QUALIFICATION_QUEST = b'_qualification_'
FINAL_QUEST_PATTERN = b'ranked_2021_{}_final'
FINAL_LEADER_QUEST = b'ranked_2021_final_leader'
RANKED_QUEST_ID_PREFIX = b'ranked'
YEAR_POINTS_TOKEN = b'rb2021'
YEAR_STRIPE_SERVER_TOKEN = b'ranked_2021_final_top'
YEAR_STRIPE_CLIENT_TOKEN = b'ranked_final_ready'
YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX = b'offer:ranked_battles:deluxe'
ENTITLEMENT_EVENT_TOKEN = b'ranked_entitlement_event'
LOBBY_SUB_LANDING_PARAM = b'?is_landing='
SEASON_RATING_PARAM = b'?spaID={}'

class RankedTokenQuestPostfix(CONST_CONTAINER):
    COMMON = b'common'
    SPRINTER = b'sprinter'
    FINAL = b'final'
    LEADER = b'leader'


class SeasonResultTokenPatterns(CONST_CONTAINER):
    RANKED_OFF_BANNED = b'ranked_{}_banned'
    RANKED_OFF_ROLLED = b'ranked_{}_rolled'
    RANKED_OFF_SPRINTER = b'ranked_{}_sprinter'
    RANKED_OFF_GOLD_LEAGUE_TOKEN = b'ranked_{}_top_1'
    RANKED_OFF_SILVER_LEAGUE_TOKEN = b'ranked_{}_top_2'
    RANKED_OFF_BRONZE_LEAGUE_TOKEN = b'ranked_{}_top_3'


class SeasonGapStates(CONST_CONTAINER):
    WAITING_IN_LEAGUES = 0
    IN_LEAGUES = 1
    BANNED_IN_LEAGUES = 2
    ROLLED_IN_LEAGUES = 3
    WAITING_IN_DIVISIONS = 4
    IN_DIVISIONS = 5
    BANNED_IN_DIVISIONS = 6
    ROLLED_IN_DIVISIONS = 7
    WAITING_NOT_IN_DIVISIONS = 8
    NOT_IN_DIVISIONS = 9
    BANNED_NOT_IN_DIVISIONS = 10
    ROLLED_NOT_IN_DIVISIONS = 11
    WAITING_NOT_IN_SEASON = 12
    NOT_IN_SEASON = 13
    BANNED_NOT_IN_SEASON = 14
    ROLLED_NOT_IN_SEASON = 15


@unique
class AlertTypes(Enum):
    PRIME = b'prime'
    SEASON = b'season'
    VEHICLE = b'vehicle'
