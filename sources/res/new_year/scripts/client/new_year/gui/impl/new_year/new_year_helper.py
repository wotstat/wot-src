import random
from constants import SECONDS_IN_DAY, LOOTBOX_TOKEN_PREFIX
from goodies.goodie_constants import GOODIE_RESOURCE_TYPE
from gui.goodies.goodie_items import _BOOSTER_TYPE_NAMES
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.awards import SupportedTokenTypes
from helpers import dependency
from helpers import time_utils, getLanguageCode, int2roman
from items.components.crew_books_constants import CREW_BOOK_RARITY
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from shared_utils import first
from new_year.gui.impl.new_year.tooltips.ny_discount_reward_tooltip import NyDiscountRewardTooltip
from new_year.ny_constants import NewYearLootBoxes
from new_year_common.items.components.ny_constants import CurrentNYConstants, TOKEN_VARIADIC_DISCOUNT_PREFIX, ToySettings, YEARS, TOKEN_LOOTBOX_FRAGMENT
_ARABIC_NUMBERS_LANGUAGE_CODES = (b'ko', b'no')
IS_ROMAN_NUMBERS_ALLOWED = getLanguageCode() not in _ARABIC_NUMBERS_LANGUAGE_CODES
BONUS_ICONS = {b'xpFactor': (R.images.new_year.gui.maps.icons.newYear.vehicles.icons.icon_battle_exp_main()), 
   b'freeXPFactor': (R.images.new_year.gui.maps.icons.newYear.vehicles.icons.icon_free_exp_main_screen()), 
   b'tankmenXPFactor': (R.images.new_year.gui.maps.icons.newYear.vehicles.icons.icon_crew_exp_main())}
_BONUSES_ORDER = ({b'bonusName': b'tmanToken'}, {b'bonusName': (CurrentNYConstants.FILLERS)}, {b'bonusName': b'battleToken', b'tagStartsWith': LOOTBOX_TOKEN_PREFIX}, {b'bonusName': b'entitlements'}, {b'bonusName': b'crewBooks', b'tag': (CREW_BOOK_RARITY.PERSONAL)}, {b'bonusName': b'dossier', b'tag': b'isPrefixBadge'}, {b'bonusName': b'customizations', b'tag': b'style'}, {b'bonusName': b'customizations'}, {b'bonusName': b'dossier'}, {b'bonusName': b'vehicles'}, {b'bonusName': b'slots'}, {b'bonusNameStartsWith': b'BlueprintNation'}, {b'bonusNameStartsWith': b'Blueprint'}, {b'bonusName': b'goodies'}, {b'bonusName': b'crewBooks'})
_BONUSES_ORDER_GF = (
 TOKEN_LOOTBOX_FRAGMENT,
 CurrentNYConstants.FILLERS,
 b'vehicles',
 b'tmanToken',
 b'variadicDiscount',
 b'newYearSlot',
 b'customizations_style',
 b'customizations',
 b'dossier',
 CREW_BOOK_RARITY.PERSONAL,
 _BOOSTER_TYPE_NAMES[GOODIE_RESOURCE_TYPE.FREE_XP_CREW_XP],
 b'entitlements',
 b'lootBox',
 SupportedTokenTypes.LOOTBOX_TOKEN,
 _BOOSTER_TYPE_NAMES[GOODIE_RESOURCE_TYPE.CREDITS],
 _BOOSTER_TYPE_NAMES[GOODIE_RESOURCE_TYPE.XP],
 b'goodies',
 b'crewBooks',
 b'slots',
 b'newYearAlbumsAccess',
 b'BlueprintNationFragmentCongrats',
 b'BlueprintUniversalFragmentCongrats')
_WEEKLY_LEADERBOARD_ORDER_GF = (
 NewYearLootBoxes.NY_CUR_YEAR_TANKS,
 TOKEN_LOOTBOX_FRAGMENT,
 NewYearLootBoxes.NY_CUR_YEAR_BIG,
 b'customizations_style',
 b'styleProgress',
 b'lbStyleProgress',
 b'vehicles',
 b'hidden_vehicle',
 b'nyStaticDogTag',
 b'dossier',
 NewYearLootBoxes.NY_CUR_YEAR_SMALL,
 SupportedTokenTypes.LOOTBOX_TOKEN)

def __getAdditionalNameBattleToken(bonus):
    if any(t.startswith(LOOTBOX_TOKEN_PREFIX) for t in bonus.getTokens()):
        return b'lootBox'
    if any(t.startswith(TOKEN_VARIADIC_DISCOUNT_PREFIX) for t in bonus.getTokens()):
        return b'variadicDiscount'
    return bonus.getName()


def __getAdditionalNameCustomizations(bonus):
    if bonus.getC11nItem(first(bonus.getCustomizations())).itemTypeName == b'style':
        return b'customizations_style'
    return bonus.getName()


def __getAdditionalNameCrewBooks(bonus):
    if first(bonus.getItems())[0].getBookType() == CREW_BOOK_RARITY.PERSONAL:
        return CREW_BOOK_RARITY.PERSONAL
    return bonus.getName()


def __getAdditionalNameGoodies(bonus):
    booster = first(bonus.getBoosters().keys())
    if booster.boosterType in [GOODIE_RESOURCE_TYPE.CREDITS, GOODIE_RESOURCE_TYPE.XP,
     GOODIE_RESOURCE_TYPE.FREE_XP_CREW_XP]:
        return booster.boosterGuiType
    return bonus.getName()


ADDITIONAL_BONUS_NAME_GETTERS = {b'battleToken': __getAdditionalNameBattleToken, 
   b'blueprints': (lambda b: b.getBlueprintName()), 
   b'customizations': __getAdditionalNameCustomizations, 
   b'crewBooks': __getAdditionalNameCrewBooks, 
   b'goodies': __getAdditionalNameGoodies}
_BONUSES_ORDER_CACHE = {}

def nyBonusSortOrder(preformattedBonus):
    bonusName, tags = preformattedBonus.bonusName, preformattedBonus.postProcessTags
    if isinstance(tags, tuple):
        tags = b'' if not tags else tags[0]
    primaryKey = (bonusName, tags)
    if primaryKey in _BONUSES_ORDER_CACHE:
        return _BONUSES_ORDER_CACHE[primaryKey]
    result = len(_BONUSES_ORDER)
    for index, criteria in enumerate(_BONUSES_ORDER):
        if b'bonusName' in criteria and bonusName != criteria[b'bonusName']:
            continue
        if b'bonusNameStartsWith' in criteria and not bonusName.startswith(criteria[b'bonusNameStartsWith']):
            continue
        if b'tag' in criteria and criteria[b'tag'] not in tags:
            continue
        if b'tagStartsWith' in criteria and not tags.startswith(criteria[b'tagStartsWith']):
            continue
        result = index
        break

    _BONUSES_ORDER_CACHE[primaryKey] = result
    return result


def nyBonusGFSortOrder(bonus):
    bonusName = bonus.getName()
    getAdditionalName = ADDITIONAL_BONUS_NAME_GETTERS.get(bonusName)
    if getAdditionalName is not None:
        bonusName = getAdditionalName(bonus)
    if bonusName in _BONUSES_ORDER_GF:
        return _BONUSES_ORDER_GF.index(bonusName)
    else:
        return len(_BONUSES_ORDER_GF)


def __getLootBoxSortKey(bonus):
    tokenID = first(bonus.getTokens())
    if not tokenID:
        return SupportedTokenTypes.LOOTBOX_TOKEN
    else:
        lootBox = dependency.instance(IItemsCache).items.tokens.getLootBoxByTokenID(tokenID)
        lbType = lootBox.getType() if lootBox is not None else None
        if lbType in _WEEKLY_LEADERBOARD_ORDER_GF:
            return lbType
        return SupportedTokenTypes.LOOTBOX_TOKEN


def nyWeeklyLeaderboardGFSortOrder(bonus):
    bonusName = bonus.getName()
    if bonusName == SupportedTokenTypes.LOOTBOX_TOKEN:
        bonusName = __getLootBoxSortKey(bonus)
    if bonusName in _WEEKLY_LEADERBOARD_ORDER_GF:
        return _WEEKLY_LEADERBOARD_ORDER_GF.index(bonusName)
    return len(_WEEKLY_LEADERBOARD_ORDER_GF)


def nyCreateToolTipContentDecorator(func):

    def wrapper(self, event, contentID):
        if contentID == R.views.new_year.lobby.new_year.tooltips.NyDiscountRewardTooltip():
            variadicID, discount = event.getArgument(b'variadicID'), event.getArgument(b'discount')
            return NyDiscountRewardTooltip(variadicID, discount)
        return func(self, event, contentID)

    return wrapper


def backportTooltipDecorator(tooltipItemsName=b'_tooltips'):

    def decorator(func):

        def wrapper(self, event):
            if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
                tooltipData = _getTooltipDataByEvent(event, getattr(self, tooltipItemsName, {}))
                if tooltipData is None:
                    return
                window = backport.BackportTooltipWindow(tooltipData, self.getParentWindow())
                window.load()
                return window
            else:
                return func(self, event)

        return wrapper

    return decorator


def _getTooltipDataByEvent(event, tooltipItems):
    tooltipId = event.getArgument(b'tooltipId')
    if tooltipId is None:
        return
    else:
        return tooltipItems.get(tooltipId, None)


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getNextGameTime(lobbyContext=None):
    gameDayStartingTime = lobbyContext.getServerSettings().regionals.getGameDayStartingTime()
    currentTime = time_utils.getCurrentTimestamp()
    newGameDayStartTime = (int((currentTime - gameDayStartingTime) // SECONDS_IN_DAY) + 1) * SECONDS_IN_DAY
    return newGameDayStartTime + gameDayStartingTime


def formatRomanNumber(number):
    if IS_ROMAN_NUMBERS_ALLOWED:
        return int2roman(number)
    return str(number)


def getGiftSystemCongratulationText(messageID):
    return backport.text(R.strings.ny.giftSystem.messages.num(messageID, default=R.strings.ny.giftSystem.messages.default)())


def getGiftSystemCongratulationResource(messageID):
    resource = R.strings.ny.giftSystem.messages.num(messageID)
    if resource.exists():
        return resource
    return R.strings.ny.giftSystem.messages.default


def getGiftSystemRandomCongratulationID(excludeID=0):
    congratIDs = set(xrange(1, R.strings.ny.giftSystem.messages.length())) - {excludeID}
    return random.choice(list(congratIDs))


def collectionRewardQuestsFilterFunc(q):
    return any(x.lower() in q.getID() for x in ToySettings.CURRENT_USUAL) and YEARS.getYearStrFromYearNum(YEARS.ALL[-1]) in q.getID()
