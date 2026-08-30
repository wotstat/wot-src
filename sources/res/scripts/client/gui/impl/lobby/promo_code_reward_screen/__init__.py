from collections import namedtuple
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
REWARD_SCREEN_TOKEN_PREFIX = b'rwscr'
REWARD_SCREEN_TOKEN_DELIMITER = b':'
WAITING_MESSAGE = b'draw_research_items'
WAITING_DATA_TIMEOUT = 10
REWARDS_SOURCE_INVOICE = 0
REWARDS_SOURCE_BATTLE_RESULTS = 1
REWARDS_SOURCE_TOKEN_QUESTS = 2
RewardScreenDescr = namedtuple(b'RewardScreenDescr', b'id, description, title, subtitle,  background, quests, questsDescription, tags')
RewardScreenTokenDescr = namedtuple(b'RewardScreenTokenDescr', b'tag, codeId, uniqIdInChain')

def isPromoCodeToken(token):
    return token.startswith(REWARD_SCREEN_TOKEN_PREFIX + REWARD_SCREEN_TOKEN_DELIMITER)


def parseToken(token):
    if not isPromoCodeToken(token):
        return None
    else:
        tag, codeId, uniqIdInChain = token.split(REWARD_SCREEN_TOKEN_DELIMITER)
        return RewardScreenTokenDescr(tag, codeId, uniqIdInChain)


@dependency.replace_none_kwargs(lobbyCtx=ILobbyContext)
def isPromoCodeRewardScreenEnabled(lobbyCtx=None):
    return lobbyCtx.getServerSettings().isPromoCodeRewardScreenEnabled()


def isLootboxesExtensionAvailable():
    lootBoxRes = R.views.dyn(b'gui_lootboxes').dyn(b'lobby').dyn(b'gui_lootboxes')
    return lootBoxRes.isValid()
