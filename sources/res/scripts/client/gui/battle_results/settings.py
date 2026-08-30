class BATTLE_RESULTS_RECORD(object):
    ARENA_UNIQUE_ID = b'arenaUniqueID'
    COMMON = b'common'
    PERSONAL = b'personal'
    PLAYERS = b'players'
    VEHICLES = b'vehicles'
    AVATARS = b'avatars'
    TOP_LEVEL_RECORDS = (
     COMMON, PERSONAL, PLAYERS, VEHICLES, AVATARS)
    PERSONAL_AVATAR = b'avatar'
    COMMON_BOTS = b'bots'


class PREMIUM_STATE(object):
    NONE = 0
    HAS_ALREADY = 1
    BUY_ENABLED = 2
    BOUGHT = 4


class PROGRESS_ACTION(object):
    RESEARCH_UNLOCK_TYPE = b'UNLOCK_LINK_TYPE'
    PURCHASE_UNLOCK_TYPE = b'PURCHASE_LINK_TYPE'
    NEW_SKILL_UNLOCK_TYPE = b'NEW_SKILL_LINK_TYPE'
    NEW_FREE_SKILL_UNLOCK_TYPE = b'NEW_FREE_SKILL_LINK_TYPE'


class PLAYER_TEAM_RESULT(object):
    WIN = b'win'
    DEFEAT = b'lose'
    DRAW = b'tie'
    ENDED = b'ended'


class FACTOR_VALUE(object):
    BASE_CREDITS_FACTOR = 100
    BASE_XP_FACTOR = 100
    BASE_TMEN_XP_FACTOR = 100
    ADDITIONAL_BONUS_ZERO_FACTOR = 0
    ADDITIONAL_BONUS_ONE_FACTOR = 10


class EMBLEM_TYPE(object):
    CLAN = 1


class UI_VISIBILITY(object):
    SHOW_SQUAD = 1
    SHOW_RESOURCES = 2


class CurrenciesConstants(object):
    GOLD = b'gold'
    CREDITS = b'credits'
    CRYSTAL = b'crystal'
    XP_COST = b'xp'
    FREE_XP = b'freeXP'
    MULTY_XP = b'multyXp'
    MULTY_FREE_XP = b'multyFreeXp'
    TMEN_XP = b'tankmenXP'
    COMMON_CURRENCY = b'commonCurrency'
