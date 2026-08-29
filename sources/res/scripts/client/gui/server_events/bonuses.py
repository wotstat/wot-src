import copy, logging
from collections import namedtuple
from functools import partial
from operator import itemgetter
import BigWorld, typing
from adisp import adisp_process
from battle_pass_common import BATTLE_PASS_OFFER_TOKEN_PREFIX, BATTLE_PASS_Q_CHAIN_BONUS_NAME, BATTLE_PASS_Q_CHAIN_TOKEN_PREFIX, BATTLE_PASS_RANDOM_QUEST_BONUS_NAME, BATTLE_PASS_RANDOM_QUEST_TOKEN_PREFIX, BATTLE_PASS_SELECT_BONUS_NAME, BATTLE_PASS_STYLE_PROGRESS_BONUS_NAME, BATTLE_PASS_TOKEN_3D_STYLE, BATTLE_PASS_TOKEN_PREFIX
from blueprints.BlueprintTypes import BlueprintTypes
from blueprints.FragmentTypes import getFragmentType
from comp7_common import COMP7_TOKEN_WEEKLY_REWARD_NAME, COMP7_TOKEN_WEEKLY_REWARD_ID, COMP7_TOKEN_COUPON_REWARD_NAME, COMP7_TOKEN_COUPON_REWARD_ID, COMP7_CUSTOMIZATION_PROGRESS_PREFIX, replaceComp7tokenID
from constants import CURRENCY_TOKEN_PREFIX, DOSSIER_TYPE, EVENT_TYPE as _ET, LOOTBOX_TOKEN_PREFIX, PREMIUM_ENTITLEMENTS, LOOTBOX_KEY_PREFIX, RESOURCE_TOKEN_PREFIX, RentType, CUSTOMIZATION_PROGRESS_PREFIX, WoTPlusBonusType, VERSUS_AI_PROGRESSION_TOKEN_PREFIX, OFFER_TOKEN_PREFIX, LOOTBOX_CUSTOMIZATION_PROGRESS_PREFIX
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR
from dossiers2.custom.records import RECORD_DB_IDS
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK, BADGES_BLOCK
from epic_constants import EPIC_OFFER_TOKEN_PREFIX, EPIC_SELECT_BONUS_NAME
from dog_tags_common.components_config import componentConfigAdapter
from dog_tags_common.config.common import ComponentViewType
from external_strings_utils import strtobool
from frameworks.wulf import WindowLayer
from gui import makeHtmlString
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.genConsts.BOOSTER_CONSTANTS import BOOSTER_CONSTANTS
from gui.Scaleform.genConsts.TEXT_ALIGN import TEXT_ALIGN
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.BADGE import BADGE
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION
from gui.Scaleform.settings import BADGES_ICONS, ICONS_SIZES, getBadgeIconPath
from gui.app_loader.decorators import sf_lobby
from gui.collection.collections_constants import COLLECTION_ITEM_BONUS_NAME, COLLECTION_ITEM_PREFIX_NAME, COLLECTION_ITEM_RES_KEY_TEMPLATE, COLLECTION_RES_PREFIX, COLLECTION_ITEM_TOKEN_PREFIX_NAME, cllcTokenToEntitlement
from gui.game_control.links import URLMacros
from gui.impl import backport
from gui.impl.backport import createTooltipData
from gui.impl.gen import R
from gui.impl.gen_utils import INVALID_RES_ID
from gui.impl.lobby.loot_box.loot_box_helper import getKeyByTokenID
from gui.selectable_reward.constants import FEATURE_TO_PREFIX, SELECTABLE_BONUS_NAME
from gui.server_events.awards_formatters import AWARDS_SIZES, BATTLE_BONUS_X5_TOKEN, CREW_BONUS_X3_TOKEN, TokenBonusFormatter
from gui.server_events.events_helpers import parseC11nProgressToken
from gui.server_events.formatters import parseComplexToken
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.formatters import text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE, GUI_ITEM_TYPE_INDICES
from gui.shared.gui_items.Tankman import Tankman, calculateRoleLevel, getRoleUserName
from gui.shared.gui_items.Vehicle import getIconResourceName, getWotPlusExclusiveVehicleTypeUserName
from gui.shared.gui_items.crew_book import orderCmp
from gui.shared.gui_items.crew_skin import localizedFullName
from gui.shared.gui_items.customization import CustomizationTooltipContext, C11nStyleProgressData
from gui.shared.gui_items.customization.c11n_helpers import getProgressionStyle
from gui.shared.gui_items.dossier.factories import getAchievementFactory
from gui.shared.money import Currency, Money
from gui.shared.system_factory import collectClientBonusMergers
from gui.shared.utils.functions import makeTooltip, stripColorTagDescrTags
from gui.shared.utils.requesters.blueprints_requester import getFragmentNationID, getVehicleCDForIntelligence, getVehicleCDForNational, makeIntelligenceCD, makeNationalCD
from helpers import dependency, getLocalizedData, i18n, time_utils
from helpers.i18n import makeString as _ms
from items import tankmen, vehicles
from items.components import c11n_components as cc
from items.components.crew_skins_constants import NO_CREW_SKIN_ID
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX
from nations import NAMES
from optional_bonuses import BONUS_MERGERS
from paragons_common import getAllParagonsEntitlements
from personal_missions import PM_BRANCH, PM_BRANCH_TO_FREE_TOKEN_NAME
from personal_missions_constants import PM3_OFFER_TOKEN_PREFIX
from preferred_maps import getSlotTypeName
from shared_utils import CONST_CONTAINER, first, makeTupleByDict, findFirst
from skeletons.gui.battle_matters import IBattleMattersController
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.game_control import ICollectionsSystemController, IWotPlusController, ITankAcademyController
from skeletons.gui.game_control import IWinbackController
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.offers import IOffersDataProvider
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from web.web_client_api.common import ItemPackEntry, ItemPackType, ItemPackTypeGroup, getItemPackByGroupAndName
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
if typing.TYPE_CHECKING:
    from typing import List, Tuple, Dict, Callable, Optional, Any
    from account_helpers.offers.events_data import OfferEventData
    from account_helpers.offers.offer_bonuses import ItemsOfferBonus
    from gui.goodies.goodie_items import Booster, _PersonalDiscount, DemountKit, RecertificationForm, GoodieType
    from gui.lobby_context import LobbyContext
    from items.components.crew_skins_components import CrewSkin
    from gui.shared.gui_items.crew_book import CrewBook
DEFAULT_CREW_LVL = 50
_CUSTOMIZATIONS_SCALE = 44.0 / 128
_ZERO_COMPENSATION_MONEY = Money(credits=0, gold=0)
_CUSTOMIZATION_BONUSES = frozenset([
 93, 94, 95, 96, 97, 98])
_META_BONUS_BROWSER_VIEW_TYPE = {b'internal': (VIEW_ALIAS.BROWSER_LOBBY_TOP_SUB), 
   b'overlay': (VIEW_ALIAS.WEB_VIEW_TRANSPARENT)}
_logger = logging.getLogger(__name__)

def _getAchievement(block, record, value):
    if block == ACHIEVEMENT_BLOCK.RARE:
        record = value
        value = 0
    try:
        achieve = getAchievementFactory((block, record)).create(value=value)
        if achieve.isAvailableInQuest():
            return achieve
    except Exception:
        LOG_ERROR(b'There is error while getting bonus dossier record name')
        LOG_CURRENT_EXCEPTION()

    return


def _isAchievement(block):
    return block in ACHIEVEMENT_BLOCK.ALL


def _isBadge(block):
    return block == BADGES_BLOCK


class SimpleBonus(object):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, name, value, isCompensation=False, ctx=None, compensationReason=None):
        self._name = name
        self._value = value
        self._isCompensation = isCompensation
        self._ctx = ctx or {}
        self._compensationReason = compensationReason
        return

    def getName(self):
        return self._name

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value
        return

    def isCompensation(self):
        return self._isCompensation

    def isEqual(self, bonus):
        return bonus.getName() == self._name and self._value == bonus.getValue()

    def getCompensationReason(self):
        return self._compensationReason

    def getContext(self):
        return self._ctx

    def updateContext(self, ctx):
        self._ctx.update(ctx)
        return

    def formatValue(self):
        if self._value:
            return str(self._value)
        else:
            return

    def format(self):
        return self._format(styleSubset=b'bonuses')

    def carouselFormat(self):
        return self._format(styleSubset=b'carouselBonuses')

    def formattedList(self):
        formattedObj = self.format()
        if formattedObj:
            return [formattedObj]
        return []

    def isShowInGUI(self):
        return True

    def getIcon(self):
        return b''

    def getTooltipIcon(self):
        return b''

    def getTooltip(self):
        return _getItemTooltip(self._name)

    def getDescription(self):
        return i18n.makeString(b'#quests:bonuses/%s/description' % self._name, value=self.formatValue())

    def getList(self):
        return

    def getWrappedEpicBonusList(self):
        return self._getWrappedBonusList()

    def getWrappedLootBoxesBonusList(self):
        return self._getWrappedBonusList()

    def _getWrappedBonusList(self):
        awardItem = R.strings.tooltips.awardItem.dyn(self._name)
        return [
         {b'id': 0, 
            b'type': ((b'custom/{}').format(self.getName())), 
            b'value': (self.getValue()), 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
            b'name': (backport.text(awardItem.header()) if awardItem else b''), 
            b'description': (backport.text(awardItem.body()) if awardItem else b'')}]

    def wrapToItemsPack(self, groupID=1):
        return []

    def getIconBySize(self, size):
        iconName = RES_ICONS.getBonusIcon(size, self.getName())
        if iconName is None:
            iconName = RES_ICONS.getBonusIcon(size, b'default')
        return iconName

    def getIconResource(self, size):
        iconR = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(self.getName())
        if iconR:
            return iconR()
        return R.images.gui.maps.icons.quests.bonuses.dyn(size).default()

    def getIconLabel(self):
        return text_styles.hightlight((b'x{}').format(self.getValue()))

    def hasIconFormat(self):
        return False

    def getLightViewModelData(self):
        return (
         self.getName(),)

    def getCount(self):
        return

    def _format(self, styleSubset):
        formattedValue = self.formatValue()
        if self._name is not None and formattedValue is not None:
            text = makeHtmlString((b'html_templates:lobby/quests/{}').format(styleSubset), self._name, {b'value': formattedValue})
            if text != self._name:
                return text
        return formattedValue

    def __getCommonAwardsVOs(self, iconSize=b'small', align=TEXT_ALIGN.CENTER, withCounts=False):
        itemInfo = {b'imgSource': (self.getIconBySize(iconSize)), 
           b'label': (self.getIconLabel()), 
           b'tooltip': (self.getTooltip()), 
           b'align': align}
        if withCounts:
            if isinstance(self._value, int):
                itemInfo[b'count'] = self._value
            else:
                itemInfo[b'count'] = 1
        return itemInfo


class IntegralBonus(SimpleBonus):

    def getCount(self):
        return int(self._value)

    def formatValue(self):
        if self._value:
            return backport.getIntegralFormat(self._value)
        else:
            return


class FloatBonus(SimpleBonus):

    def formatValue(self):
        if self._value:
            return backport.getNiceNumberFormat(self._value)
        else:
            return


class GroupsBonus(SimpleBonus):

    def formatValue(self):
        return


class CountableIntegralBonus(IntegralBonus):

    def wrapToItemsPack(self, groupID=1):
        name = self.getName()
        if name == b'slots':
            name = b'slot'
        type_ = getItemPackByGroupAndName(ItemPackTypeGroup.CUSTOM, name)
        return [
         ItemPackEntry(type=type_, count=self.getCount(), id=0, groupID=groupID)]


class CreditsBonus(IntegralBonus):

    def getIcon(self):
        return backport.image(R.images.gui.maps.icons.library.CreditsIcon_1())

    def getTooltipIcon(self):
        return RES_ICONS.MAPS_ICONS_REFERRAL_AWARD_CREDITS

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (backport.image(R.images.gui.maps.icons.quests.bonuses.small.credits())), 
            b'tooltip': (TOOLTIPS.AWARDITEM_CREDITS)}]

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.credits(self.getValue())

    def wrapToItemsPack(self, groupID=1):
        type_ = getItemPackByGroupAndName(ItemPackTypeGroup.CUSTOM, self.getName())
        return [
         ItemPackEntry(type=type_, count=self.getCount(), id=0, groupID=groupID)]


class GoldBonus(SimpleBonus):

    def getIcon(self):
        return backport.image(R.images.gui.maps.icons.library.GoldIcon_1())

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (backport.image(R.images.gui.maps.icons.quests.bonuses.small.gold())), 
            b'tooltip': (TOOLTIPS.AWARDITEM_GOLD)}]

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.gold(self.getValue())

    def getCount(self):
        return int(self._value)


class CrystalBonus(IntegralBonus):

    def getIcon(self):
        return backport.image(R.images.gui.maps.icons.library.CrystalIconBig())

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (backport.image(R.images.gui.maps.icons.library.CrystalIconBig())), 
            b'tooltip': (TOOLTIPS.AWARDITEM_CRYSTAL)}]

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.crystal(self.getValue())

    def getWrappedEpicBonusList(self):
        awardItem = R.strings.tooltips.awardItem.dyn(self._name)
        return [
         {b'id': 0, 
            b'type': ((b'custom/{}').format(self.getName())), 
            b'value': (self.getValue()), 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
            b'name': (backport.text(awardItem.header()) if awardItem else b''), 
            b'description': (backport.text(awardItem.body()) if awardItem else b'')}]


class EventCoinBonus(IntegralBonus):

    def getIcon(self):
        return backport.image(R.images.gui.maps.icons.library.EventCoinIconBig())

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (backport.image(R.images.gui.maps.icons.library.EventCoinIconBig())), 
            b'tooltip': (TOOLTIPS.AWARDITEM_EVENTCOIN)}]

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.eventCoin(self.getValue())


class BpcoinBonus(IntegralBonus):

    def getIcon(self):
        return backport.image(R.images.gui.maps.icons.library.bpcoinIcon_1())

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (self.getIcon()), 
            b'tooltip': (TOOLTIPS.AWARDITEM_BPCOIN)}]

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.bpcoin(self.getValue())


class EquipCoinBonus(IntegralBonus):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def getIcon(self):
        return backport.image(R.images.gui.maps.icons.library.equipCoin_1())

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (self.getIcon()), 
            b'tooltip': (TOOLTIPS.AWARDITEM_EQUIPCOIN)}]

    def getTooltip(self):
        headerKey, _ = getSimpleTooltipData(self._name)
        header = i18n.makeString(headerKey) if headerKey else None
        isRestorable = self.__lobbyContext.getServerSettings().isOptionalDeviceRestoreEnabled()
        baseDesc = R.strings.tooltips
        body = backport.text(baseDesc.awardItem.equipCoin.body() if isRestorable else baseDesc.header.buttons.equipCoin.description2())
        return makeTooltip(header or None, body or None)

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.equipCoin(self.getValue())


class CurrenciesBonus(IntegralBonus):
    __TEMPLATE_NAME = b'platformCurrency'

    def __init__(self, *args, **kwargs):
        super(CurrenciesBonus, self).__init__(*args, **kwargs)
        self._code = self._value.keys()[0]
        self._value = self._value[self._code][b'count']
        return

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (self.getIconBySize(AWARDS_SIZES.SMALL)), 
            b'tooltip': (self.getTooltip())}]

    def getCode(self):
        return self._code

    def getTooltip(self):
        return _getItemTooltip(self._code)

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.hightlight(self.getValue())

    def getIconBySize(self, size):
        iconName = RES_ICONS.getBonusIcon(size, self._code)
        if iconName is None:
            return super(CurrenciesBonus, self).getIconBySize(size)
        else:
            return iconName

    def getWrappedEpicBonusList(self):
        awardItem = R.strings.tooltips.awardItem.dyn(self._code)
        return [
         {b'id': 0, 
            b'type': ((b'custom/{}').format(self._code)), 
            b'value': (self.getValue()), 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
            b'name': (backport.text(awardItem.header()) if awardItem else b''), 
            b'description': (backport.text(awardItem.body()) if awardItem else b'')}]

    def _format(self, styleSubset):
        if self.__ifPlatformCurrency(self._code):
            formattedValue = self.formatValue()
            if self._name is not None and formattedValue is not None:
                text = makeHtmlString((b'html_templates:lobby/quests/{}').format(styleSubset), self.__TEMPLATE_NAME, {b'value': formattedValue, b'iconName': (self._code)})
                if text != self.__TEMPLATE_NAME:
                    return text
            return formattedValue
        super(CurrenciesBonus, self)._format(styleSubset)
        return

    def __ifPlatformCurrency(self, currencyCode):
        return currencyCode not in Currency.ALL + (CURRENCIES_CONSTANTS.FREE_XP,)


class FreeXpBonus(IntegralBonus):

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (backport.image(R.images.gui.maps.icons.quests.bonuses.small.freeExp())), 
            b'tooltip': (TOOLTIPS.AWARDITEM_FREEXP)}]

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.hightlight(self.getValue())


class _PremiumDaysBonus(IntegralBonus):

    def hasIconFormat(self):
        return True

    def getIconBySize(self, size):
        return RES_ICONS.getBonusIcon(size, (b'{}_{}').format(self.getName(), self.getValue()))

    def getIconResource(self, size):
        iconR = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn((b'{}_{}').format(self.getName(), self.getValue()))
        if iconR:
            return iconR()
        return R.invalid()

    def getIconLabel(self):
        return b''

    def getWrappedLootBoxesBonusList(self):
        result = self._getWrappedBonusList()
        for bonus in result:
            bonus[b'value'] = 1

        return result


class BasicPremiumDaysBonus(_PremiumDaysBonus):

    def getList(self):
        return [
         {b'itemSource': (backport.image(R.images.gui.maps.icons.quests.bonuses.small.premium_1())), 
            b'tooltip': (TOOLTIPS.AWARDITEM_PREMIUM)}]


class PlusPremiumDaysBonus(_PremiumDaysBonus):

    def getList(self):
        return [
         {b'itemSource': (backport.image(R.images.gui.maps.icons.quests.bonuses.small.premium_plus_1())), 
            b'tooltip': (TOOLTIPS.AWARDITEM_PREMIUM)}]

    def wrapToItemsPack(self, groupID=1):
        return [
         ItemPackEntry(type=b'custom/premium_plus', count=self.getCount(), id=0, groupID=groupID)]


class MetaBonus(SimpleBonus):

    def __init__(self, *args, **kwargs):
        super(MetaBonus, self).__init__(*args, **kwargs)
        self.__onLobbyLoadedCallbacks = []
        return

    @sf_lobby
    def __app(self):
        return

    def isShowInGUI(self):
        return False

    def formatValue(self):
        return getLocalizedData({b'value': (self._value)}, b'value')

    def getActions(self):
        return self._value.get(b'actions', {}).iteritems()

    def handleAction(self, action, params):
        if action == b'browse':
            self.__handleBrowseAction(params)
        else:
            NotImplementedError(b'Action "%s" handler is not implemented', action)
        return

    def getWrappedLootBoxesBonusList(self):
        return []

    @adisp_process
    def __handleBrowseAction(self, params):
        from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getClientControlledCloseCtx
        from gui.server_events.events_dispatcher import showMetaBonusOverlayView
        url = params.get(b'url')
        if url is None:
            _logger.warning(b'Browse url is empty')
            return
        else:
            url = yield URLMacros().parse(url)
            target = params.get(b'target')
            if target is None:
                _logger.warning(b'Browse target is empty')
                return
            if target in _META_BONUS_BROWSER_VIEW_TYPE:
                viewType = _META_BONUS_BROWSER_VIEW_TYPE[target]
                kwargs = {}
                if strtobool(params.get(b'isClientCloseControl', b'False')):
                    kwargs.update(getClientControlledCloseCtx())
                if self.__isLobbyLoaded():
                    showMetaBonusOverlayView(url=url, alias=viewType, **kwargs)
                else:
                    self.__app.loaderManager.onViewLoaded += self.__onViewLoaded
                    self.__onLobbyLoadedCallbacks.append(partial(showMetaBonusOverlayView, url, viewType, **kwargs))
            elif target == b'external':
                BigWorld.openWebBrowser(url)
            else:
                _logger.warning(b'Invalid browse target: %s', target)
            return

    def __isLobbyLoaded(self):
        container = self.__app.containerManager.getContainer(WindowLayer.SUB_VIEW)
        return container is not None

    def __onViewLoaded(self, pyView, _):
        if pyView.layer == WindowLayer.SUB_VIEW:
            for callback in self.__onLobbyLoadedCallbacks:
                callback()

            self.__onLobbyLoadedCallbacks = []
            self.__app.loaderManager.onViewLoaded -= self.__onViewLoaded
        return


class TokensBonus(SimpleBonus):
    TOKENS = b'tokens'
    _TOKEN_RECORD = namedtuple(b'_TOKEN_RECORD', [
     b'id',
     b'expires',
     b'count',
     b'limit'])

    def isShowInGUI(self):
        return False

    def formatValue(self):
        return

    def getTokens(self):
        result = {}
        for tID, d in self._value.iteritems():
            expires = d.get(b'expires', {b'at': None}) or {b'at': None}
            result[tID] = self._TOKEN_RECORD(tID, expires.values()[0], d.get(b'count', 0), d.get(b'limit'))

        return result

    def getCount(self):
        return sum(v.get(b'count', 0) for v in self._value.values())


class VersusAIProgressionsTokenBonus(TokensBonus):
    __TEMPLATE_NAME = b'versusAIProgressionsToken'
    _formatter = TokenBonusFormatter()

    def _format(self, styleSubset):
        formatedValue = self.formatValue()
        progressionName = self.getProgressionName()
        preformattedBonus = self._formatter.format(self)[0]
        text = makeHtmlString((b'html_templates:lobby/quests/{}').format(styleSubset), self.__TEMPLATE_NAME, {b'count': formatedValue, b'valueName': (preformattedBonus.userName), b'progressionName': progressionName})
        if text != self.__TEMPLATE_NAME:
            return text
        return formatedValue

    def getProgressionName(self):
        return next(self._value.iterkeys()).split(b':')[1]

    def formatValue(self):
        return str(self.getCount())

    def isShowInGUI(self):
        return True


class ResourceBonus(TokensBonus):

    def __init__(self, name, value, prefix, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__(name, value, isCompensation, ctx)
        self._tokenId = self._value.keys()[0]
        self._resourceName = self._tokenId.replace(prefix, b'')
        return

    def isShowInGUI(self):
        return True

    @property
    def tokenId(self):
        return self._tokenId

    @property
    def resourceName(self):
        return self._resourceName


class BattleTokensBonus(TokensBonus):
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__(name, value, isCompensation, ctx)
        self._name = b'battleToken'
        return

    def isShowInGUI(self):
        return True

    def formatValue(self):
        result = []
        for tokenID, _ in self._value.iteritems():
            complexToken = parseComplexToken(tokenID)
            if complexToken.isDisplayable:
                result.append(self._getUserName(complexToken.styleID))

        if result:
            return (b', ').join(result)
        else:
            return

    def getWrappedLootBoxesBonusList(self):
        return []

    def getWrappedEpicBonusList(self):
        return []

    def _getUserName(self, styleID):
        webCache = self.eventsCache.prefetcher
        return i18n.makeString(webCache.getTokenInfo(styleID))


class BattlePassTokensBonus(TokensBonus):

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(BattlePassTokensBonus, self).__init__(name, value, isCompensation, ctx)
        self._name = b'battlePassToken'
        return

    def isShowInGUI(self):
        return False


class Comp7TokenWeeklyRewardBonus(TokensBonus):

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(Comp7TokenWeeklyRewardBonus, self).__init__(name, value, isCompensation, ctx)
        self._name = COMP7_TOKEN_WEEKLY_REWARD_NAME
        return

    def isShowInGUI(self):
        return True

    def getTooltip(self):
        header = TOOLTIPS.getAwardHeader(self.getName())
        body = TOOLTIPS.getAwardBody(self.getName())
        return makeTooltip(header or None, body or None)


class Comp7TokenCouponBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(Comp7TokenCouponBonus, self).__init__(COMP7_TOKEN_COUPON_REWARD_NAME, value, isCompensation, ctx)
        return

    def isShowInGUI(self):
        return True

    def getTooltip(self):
        header = TOOLTIPS.getAwardHeader(self.getName())
        body = TOOLTIPS.getAwardBody(self.getName())
        return makeTooltip(header or None, body or None)


class BattlePassSelectTokensBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(BattlePassSelectTokensBonus, self).__init__(BATTLE_PASS_SELECT_BONUS_NAME, value, isCompensation, ctx)
        return

    def getType(self):
        tID = self._value.keys()[0]
        bonusType = tID.split(b':')[2]
        return bonusType

    def isShowInGUI(self):
        return True

    def updateContext(self, ctx):
        self._ctx.update(ctx)
        return


class PersonalMissionsSelectTokensBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(PersonalMissionsSelectTokensBonus, self).__init__(SELECTABLE_BONUS_NAME, value, isCompensation, ctx)
        self.__isShowAnimation = False
        return

    def getType(self):
        tID = self._value.keys()[0]
        bonusType = tID.split(b':')[2]
        return bonusType

    def isShowInGUI(self):
        return True

    def updateContext(self, ctx):
        self._ctx.update(ctx)
        return

    def setIsShowAnimation(self, isShowAnimationRewards):
        self.__isShowAnimation = isShowAnimationRewards
        return

    def getIsShowAnimation(self):
        return self.__isShowAnimation


class EpicSelectTokensBonus(TokensBonus):
    __offersProvider = dependency.descriptor(IOffersDataProvider)

    def __init__(self, value, isCompensation=False, ctx=None):
        super(EpicSelectTokensBonus, self).__init__(EPIC_SELECT_BONUS_NAME, value, isCompensation, ctx)
        return

    def getType(self):
        tID = self._value.keys()[0]
        bonusType = tID.split(b':')[2]
        return bonusType

    def getIconBySize(self, size):
        iconName = RES_ICONS.getBonusIcon(size, self.getType())
        if iconName is None:
            iconName = RES_ICONS.getBonusIcon(size, b'default')
        return iconName

    def isShowInGUI(self):
        return True

    def updateContext(self, ctx):
        self._ctx.update(ctx)
        return

    def firstOfferCount(self):
        offer = self.__getBonusOffer()
        if not offer:
            return 0
        gift = offer.getFirstGift()
        firstBonus = first(gift.bonuses)
        return firstBonus.getGiftCount()

    def isEqual(self, bonus):
        if not isinstance(bonus, EpicSelectTokensBonus):
            return False
        return bonus.firstOfferCount() == self.firstOfferCount()

    def isReceived(self):
        offer = self.__getBonusOffer()
        if not offer:
            return True
        return bool(self.__offersProvider.getReceivedGifts(offer.id))

    def canClaim(self):
        return self._ctx.get(b'canClaim', False)

    def getWrappedEpicBonusList(self):
        bonusList = []
        offer = self.__getBonusOffer()
        if offer is not None:
            gift = first(offer.getAllGifts())
            if gift:
                firstBonus = first(gift.bonuses)
                if firstBonus:
                    bonusList = firstBonus.getWrappedEpicBonusList()
                    for bonus in bonusList:
                        bonus.update({b'id': (offer.giftToken), 
                           b'type': ((b'offer/{}').format(bonus[b'type'])), 
                           b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
                           b'isReceived': (self._ctx.get(b'isReceived', False)), 
                           b'name': (backport.text(R.strings.tooltips.epicBattlesOffer.title.dyn(self.getType())()))})

        return bonusList

    def getTooltip(self):
        return createTooltipData(tooltip=None, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.EPIC_BATTLE_INSTRUCTION_TOOLTIP, specialArgs=[
         self.__getGiftTokenName()])

    def __getGiftTokenName(self):
        giftTokenName = first(self.getTokens().keys())
        return giftTokenName

    def __getBonusOffer(self):
        tokenName = self.__getGiftTokenName().replace(b'_gift', b'')
        return self.__offersProvider.getOfferByToken(tokenName)


class BattlePassQuestChainTokensBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(BattlePassQuestChainTokensBonus, self).__init__(BATTLE_PASS_Q_CHAIN_BONUS_NAME, value, isCompensation, ctx)
        return

    @property
    def tokenID(self):
        return first(self._value.keys())

    @property
    def chapterID(self):
        return int(self.__getTokenIDPart(2))

    @property
    def level(self):
        return int(self.__getTokenIDPart(3))

    def getType(self):
        return self.__getTokenIDPart(1)

    def isShowInGUI(self):
        return True

    def __getTokenIDPart(self, index):
        return self.tokenID.split(b':')[index]


class BattlePassRandomQuestTokensBonus(TokensBonus):
    __eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, value, isCompensation=False, ctx=None):
        super(BattlePassRandomQuestTokensBonus, self).__init__(BATTLE_PASS_RANDOM_QUEST_BONUS_NAME, value, isCompensation, ctx)
        return

    @property
    def tokenID(self):
        return first(self._value.keys())

    @property
    def vehicle(self):
        quest = first(self.__eventsCache.getQuestsByTokenRequirement(self.tokenID))
        condition = first(quest.vehicleReqs.getConditions().items)
        if not condition.getVehiclesList():
            _logger.warning(b'Vehicles List is empty because of filter criteria condition!')
        return first(condition.getVehiclesList())

    def isShowInGUI(self):
        return True


class BattlePassStyleProgressTokenBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(BattlePassStyleProgressTokenBonus, self).__init__(BATTLE_PASS_STYLE_PROGRESS_BONUS_NAME, value, isCompensation, ctx)
        return

    def isShowInGUI(self):
        return True

    def getChapter(self):
        tID = self._value.keys()[0]
        chapter = tID.split(b':')[3]
        return int(chapter)

    def getLevel(self):
        tID = self._value.keys()[0]
        level = tID.split(b':')[4]
        return int(level)


class LootBoxTokensBonus(TokensBonus):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, value, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__(b'lootBoxToken', value, isCompensation, ctx)
        return

    def isShowInGUI(self):
        return True

    def format(self):
        return (b', ').join(self.formattedList())

    def formattedList(self):
        result = []
        for tokenID, tokenVal in self._value.iteritems():
            lootBox = self.itemsCache.items.tokens.getLootBoxByTokenID(tokenID)
            if lootBox is not None:
                result.append(makeHtmlString(b'html_templates:lobby/quests/bonuses', b'lootBox', {b'name': (lootBox.getUserName()), 
                   b'count': (tokenVal[b'count'])}))

        return result

    def getWrappedLootBoxesBonusList(self):
        return self._getWrappedBonusList()

    def _getWrappedBonusList(self):
        return [
         {b'id': (self.__getLootBoxTokenID()), 
            b'type': (ItemPackType.CUSTOM_LOOTBOX), 
            b'value': (self.getCount()), 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}}]

    def getIconBySize(self, size):
        iconName = RES_ICONS.getBonusIcon(size, self.__getLootBoxIconName())
        if iconName is None:
            iconName = RES_ICONS.getBonusIcon(size, b'default')
        return iconName

    def __getLootBoxTokenID(self):
        for tokenID in self._value.keys():
            if tokenID.startswith(LOOTBOX_TOKEN_PREFIX):
                return tokenID

        return b''

    def __getLootBoxIconName(self):
        for tokenID in self._value.keys():
            lootBox = self.itemsCache.items.tokens.getLootBoxByTokenID(tokenID)
            if lootBox is not None:
                return lootBox.getIconName()

        return b''


class LootBoxKeyTokensBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__(b'battleToken', value, isCompensation, ctx)
        return

    def isShowInGUI(self):
        return True

    def format(self):
        return (b', ').join(self.formattedList())

    def formattedList(self):
        result = []
        for tokenID, tokenVal in self._value.iteritems():
            lootBoxKey = getKeyByTokenID(tokenID)
            if lootBoxKey is not None:
                text = backport.text(R.strings.lootboxes.userName.dyn(lootBoxKey.userName)())
                result.append(makeHtmlString(b'html_templates:lobby/quests/bonuses', b'lootBoxKey', {b'name': text, 
                   b'count': (int(tokenVal[b'count']))}))

        return result

    def getWrappedLootBoxesBonusList(self):
        return self._getWrappedBonusList()

    def _getWrappedBonusList(self):
        return [
         {b'id': (self.__getLootBoxKeyTokenID()), 
            b'type': (ItemPackType.CUSTOM_LOOTBOXKEY), 
            b'value': 1, 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
            b'count': (self.__getLootBoxKeyCount()), 
            b'expires': (self.__getLootBoxExpires())}]

    def getIconBySize(self, size):
        iconName = RES_ICONS.getBonusIcon(size, self.__getLootBoxKeyIconName())
        if iconName is None:
            iconName = RES_ICONS.getBonusIcon(size, b'default')
        return iconName

    def __getLootBoxKeyTokenID(self):
        for tokenID in self._value.keys():
            if tokenID.startswith(LOOTBOX_KEY_PREFIX):
                return tokenID

        return b''

    def __getLootBoxKeyIconName(self):
        for tokenID in self._value.keys():
            lootBoxKey = getKeyByTokenID(tokenID)
            if lootBoxKey is not None:
                return lootBoxKey.iconName

        return b''

    def __getLootBoxKeyCount(self):
        for token in self._value.values():
            return token.get(b'count', 0)

        return

    def __getLootBoxExpires(self):
        for token in self._value.values():
            return token.get(b'expires')

        return


class TmanTemplateTokensBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__(b'tmanToken', value, isCompensation, ctx)
        return

    def isShowInGUI(self):
        return True

    def _getWrappedBonusList(self):
        result = []
        for tID, tokenRecord in self.getTokens().iteritems():
            recruitInfo = getRecruitInfo(tID)
            if recruitInfo.isFemale():
                bonusImageName = b'tankwoman'
            else:
                bonusImageName = b'tankman'
            result.append({b'id': tID, 
               b'type': (self.getName()), 
               b'value': (tokenRecord.count), 
               b'icon': {(AWARDS_SIZES.SMALL): (backport.image(R.images.gui.maps.icons.quests.bonuses.dyn(AWARDS_SIZES.SMALL).dyn(bonusImageName)())), 
                         (AWARDS_SIZES.BIG): (backport.image(R.images.gui.maps.icons.quests.bonuses.dyn(AWARDS_SIZES.BIG).dyn(bonusImageName)()))}, 
               b'name': (recruitInfo.getFullUserNameByNation(0)), 
               b'description': (recruitInfo.getDescription())})

        return result

    def getWrappedBonusList(self):
        return self._getWrappedBonusList()

    def formattedList(self):
        return [makeHtmlString(b'html_templates:lobby/quests/bonuses', self._name, {b'value': (getRecruitInfo(tID).getFullUserNameByNation(0))}) for tID in self.getTokens()]


class X5BattleTokensBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__(b'tokens', value, isCompensation, ctx)
        return

    def _format(self, styleSubset):
        return makeHtmlString((b'html_templates:lobby/quests/bonuses').format(styleSubset), BATTLE_BONUS_X5_TOKEN, {b'value': (self.formatValue())})

    def formatValue(self):
        return self.getValue()[BATTLE_BONUS_X5_TOKEN][b'count']

    def isShowInGUI(self):
        return True

    def getUserName(self):
        return backport.text(R.strings.quests.bonusName.battle_bonus_x5())

    def getIconBySize(self, size):
        bonusBattleTaskRes = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(BATTLE_BONUS_X5_TOKEN)
        if bonusBattleTaskRes:
            return backport.image(bonusBattleTaskRes())
        else:
            return

    def getIconResource(self, size):
        bonusBattleTaskRes = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(b'bonus_battle_task')
        if bonusBattleTaskRes.isValid():
            return bonusBattleTaskRes()
        return R.invalid()

    def getWrappedLootBoxesBonusList(self):
        result = []
        for _, tokenRecord in self.getTokens().iteritems():
            result.append({b'id': 0, 
               b'type': (ItemPackType.CUSTOM_X5_BATTLE_BONUS), 
               b'value': (tokenRecord.count), 
               b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), 
                         (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
               b'name': (self.getUserName()), 
               b'description': b''})

        return result


class X3CrewTokensBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__(b'tokens', value, isCompensation, ctx)
        return

    def _format(self, styleSubset):
        return makeHtmlString(b'html_templates:lobby/quests/bonuses', CREW_BONUS_X3_TOKEN, {b'value': (self.formatValue())})

    def formatValue(self):
        return self.getValue()[CREW_BONUS_X3_TOKEN][b'count']

    def isShowInGUI(self):
        return True

    def getUserName(self):
        return backport.text(R.strings.quests.bonusName.crew_bonus_x3())

    def getIconBySize(self, size):
        crewBattleTaskRes = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(CREW_BONUS_X3_TOKEN)
        if crewBattleTaskRes:
            return backport.image(crewBattleTaskRes())
        else:
            return

    def getIconResource(self, size):
        crewBattleTaskRes = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(CREW_BONUS_X3_TOKEN)
        if crewBattleTaskRes.isValid():
            return crewBattleTaskRes()
        return R.invalid()

    def getWrappedEventLootBoxesBonusList(self):
        result = []
        for _, tokenRecord in self.getTokens().iteritems():
            result.append({b'id': 0, 
               b'type': (ItemPackType.CUSTOM_X3_CREW_BONUS), 
               b'value': (tokenRecord.count), 
               b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), 
                         (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
               b'name': (self.getUserName()), 
               b'description': b''})

        return result


class SelectableBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None, name=SELECTABLE_BONUS_NAME):
        super(SelectableBonus, self).__init__(name, value, isCompensation, ctx)
        return

    def isShowInGUI(self):
        return True

    def getType(self):
        return first(self._value.keys()).split(b':')[2]

    def formatValue(self):
        if self._value:
            return str(self._value)
        else:
            return

    def getLightViewModelData(self):
        return (
         self.getType(),)


class EntitlementBonus(SimpleBonus):
    _ENTITLEMENT_RECORD = namedtuple(b'_ENTITLEMENT_RECORD', [b'id', b'amount'])
    _FORMATTED_AMOUNT = [b'ranked_202203_access']
    _FORMATTED_AMOUNT.extend(getAllParagonsEntitlements())

    @staticmethod
    def hasConfiguredName(entitlementID):
        return R.strings.quests.bonusName.entitlements.dyn(entitlementID).exists()

    @staticmethod
    def hasConfiguredResources(entitlementID):
        if not R.strings.quests.bonusName.entitlements.dyn(entitlementID):
            return False
        for size in AWARDS_SIZES.ALL():
            if not R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(entitlementID):
                return False

        return True

    @classmethod
    def isFormattedAmount(cls, entitlementID):
        return entitlementID in cls._FORMATTED_AMOUNT

    @classmethod
    def getUserName(cls, entitlementID):
        if cls.hasConfiguredName(entitlementID):
            return backport.text(R.strings.quests.bonusName.entitlements.dyn(entitlementID)())
        return b''

    @classmethod
    def getUserNameWithCount(cls, entitlementID, count):
        if cls.hasConfiguredName(entitlementID) and count > 0:
            if cls.isFormattedAmount(entitlementID):
                res = R.strings.messenger.serviceChannelMessages.battleResults.quests.entitlements.fmtMultiplier()
                formattedCountStr = backport.text(res, count=backport.getIntegralFormat(count)) if count > 1 else b''
            else:
                countRes = R.strings.messenger.serviceChannelMessages.battleResults.quests.entitlements.multiplier()
                formattedCountStr = backport.text(countRes, count=backport.getIntegralFormat(count))
            return text_styles.concatStylesToSingleLine(cls.getUserName(entitlementID), formattedCountStr)
        return b''

    @classmethod
    def extendFormattedAmount(cls, entitlementIDs):
        cls._FORMATTED_AMOUNT.extend(entitlementIDs)
        return

    def isShowInGUI(self):
        value = self.getValue()
        return value.amount > 0 and self.hasConfiguredName(value.id)

    def getIconBySize(self, size):
        value = self.getValue()
        if self.hasConfiguredResources(value.id):
            return backport.image(R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(value.id)())
        return b''

    def getIconResource(self, size):
        value = self.getValue()
        if self.hasConfiguredResources(value.id):
            return R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(value.id)()
        return R.invalid()

    def getTooltip(self):
        return _getItemTooltip(self.getValue().id)

    def getValue(self):
        return self._ENTITLEMENT_RECORD(*self._value)

    def getCount(self):
        return self.getValue().amount

    def _getWrappedBonusList(self):
        value = self.getValue()
        descriptionRes = R.strings.tooltips.awardItem.dyn(value.id)
        return [
         {b'id': (value.id), 
            b'value': (value.amount), 
            b'type': ((b'custom/{}').format(self.getName())), 
            b'name': (self.getUserName(value.id)), 
            b'description': (backport.text(descriptionRes.body()) if descriptionRes else b''), 
            b'icon': {(AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG)), 
                      (AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL))}}]

    def formatValue(self):
        value = self.getValue()
        formattedValue = self.getUserNameWithCount(value.id, value.amount)
        if formattedValue:
            return formattedValue
        else:
            return


class ICollectionItemBonus(object):

    def getItem(self):
        raise NotImplementedError
        return

    def getType(self):
        raise NotImplementedError
        return

    def getCollectionId(self):
        raise NotImplementedError
        return

    def getItemId(self):
        raise NotImplementedError
        return


class CollectionTokenBonus(TokensBonus, ICollectionItemBonus):
    __collectionsSystem = dependency.descriptor(ICollectionsSystemController)

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(CollectionTokenBonus, self).__init__(name, value, isCompensation, ctx)
        tokenID = first(self.getTokens().keys())
        itemData = tokenID.split(b':') if tokenID is not None else None
        if itemData and len(itemData) == 4:
            _, _, collectionId, itemId = itemData
            self.__collectionId = int(collectionId)
            self.__itemId = int(itemId)
        else:
            _logger.error(b'CollectionTokenBonus has wrong format tokenID= %s', tokenID)
            self.__collectionId = None
            self.__itemId = None
        return

    def isShowInGUI(self):
        return True

    def getItem(self):
        collection = self.__getCollection()
        if collection:
            return collection.items[self.__itemId]
        else:
            return

    def getType(self):
        item = self.getItem()
        if item is not None:
            return item.type
        else:
            return

    def getCollectionId(self):
        return self.__collectionId

    def getItemId(self):
        return self.__itemId

    def getIconBySize(self, size):
        if self.__getCollection() is None:
            return
        else:
            if size == AWARDS_SIZES.SMALL:
                return backport.image(R.images.gui.maps.icons.collectionItems.c_48x48.dyn(COLLECTION_ITEM_RES_KEY_TEMPLATE.format(self.getType(), self.__collectionId, self.__itemId))())
            return backport.image(R.images.gui.maps.icons.collectionItems.c_80x80.dyn(COLLECTION_ITEM_RES_KEY_TEMPLATE.format(self.getType(), self.__collectionId, self.__itemId))())

    def _getWrappedBonusList(self):
        return [
         {b'id': (cllcTokenToEntitlement(first(self.getTokens().keys(), b''))), 
            b'value': 1, 
            b'type': ((b'custom/{}').format(self.getName())), 
            b'name': b'', 
            b'description': b'', 
            b'icon': {(AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG)), 
                      (AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL))}}]

    def __getCollection(self):
        if self.__collectionId is not None and self.__itemId is not None:
            return self.__collectionsSystem.getCollection(self.__collectionId)
        else:
            return


class CollectionEntitlementBonus(EntitlementBonus, ICollectionItemBonus):
    __collectionsSystem = dependency.descriptor(ICollectionsSystemController)

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(CollectionEntitlementBonus, self).__init__(name, value, isCompensation, ctx)
        value = self.getValue()
        _, _, collectionId, itemId = value.id.split(b'_')
        self.__collectionId = int(collectionId)
        self.__itemId = int(itemId)
        return

    def isShowInGUI(self):
        return True

    def getItem(self):
        return self.__collectionsSystem.getCollection(self.__collectionId).items[self.__itemId]

    def getType(self):
        return self.getItem().type

    def getCollectionId(self):
        return self.__collectionId

    def getItemId(self):
        return self.__itemId

    def getIconBySize(self, size):
        if size == AWARDS_SIZES.SMALL:
            return backport.image(R.images.gui.maps.icons.collectionItems.c_48x48.dyn(COLLECTION_ITEM_RES_KEY_TEMPLATE.format(self.getType(), self.__collectionId, self.__itemId))())
        return backport.image(R.images.gui.maps.icons.collectionItems.c_80x80.dyn(COLLECTION_ITEM_RES_KEY_TEMPLATE.format(self.getType(), self.__collectionId, self.__itemId))())


class AnyCollectionItemBonus(SimpleBonus):
    __collectionsSystem = dependency.descriptor(ICollectionsSystemController)

    def isShowInGUI(self):
        return True

    def getCollectionId(self):
        return int(self.getValue())

    def getIconBySize(self, size):
        if size == AWARDS_SIZES.SMALL:
            return backport.image(R.images.gui.maps.icons.collectionItems.c_48x48.dyn((b'any_{}').format(self.getCollectionId()))())
        return backport.image(R.images.gui.maps.icons.collectionItems.c_80x80.dyn((b'any_{}').format(self.getCollectionId()))())

    def _getWrappedBonusList(self):
        collRes = R.strings.dyn(COLLECTION_RES_PREFIX + self.__collectionsSystem.getCollection(self.getCollectionId()).name)
        return [
         {b'id': (self.getCollectionId()), 
            b'type': (ItemPackType.CUSTOM_ANY_COLLECTION_ITEM), 
            b'value': 1, 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
            b'name': (backport.text(collRes.anyCollectionItem.tooltip.header())), 
            b'description': (backport.text(collRes.anyCollectionItem.tooltip.body()))}]


def personalMissionsTokensFactory(name, value, isCompensation=False, ctx=None):
    from gui.server_events.finders import PERSONAL_MISSION_TOKEN
    completionTokenID = PERSONAL_MISSION_TOKEN % (ctx[b'campaignID'], ctx[b'operationID'])
    result = []
    for tID, tValue in value.iteritems():
        if tID in PM_BRANCH_TO_FREE_TOKEN_NAME.values():
            result.append(FreeTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID == completionTokenID:
            result.append(CompletionTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(PM3_OFFER_TOKEN_PREFIX):
            result.append(PersonalMissionsSelectTokensBonus({tID: tValue}, isCompensation, ctx))
        else:
            result.append(TokensBonus(name, {tID: tValue}, isCompensation, ctx))

    return result


def createBonusFromTokens(result, prefix, bonusId, value):
    bonus = getNonQuestBonuses(bonusId.replace(prefix, b''), value.get(b'count'))
    if bonus:
        result.append(bonus[0])
    return


def tokensFactory(name, value, isCompensation=False, ctx=None):
    result = []
    for tID, tValue in value.iteritems():
        if tID.startswith(LOOTBOX_TOKEN_PREFIX):
            result.append(LootBoxTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(LOOTBOX_KEY_PREFIX):
            result.append(LootBoxKeyTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
            result.append(TmanTemplateTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(BATTLE_BONUS_X5_TOKEN):
            result.append(X5BattleTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(CREW_BONUS_X3_TOKEN):
            result.append(X3CrewTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(BATTLE_PASS_TOKEN_3D_STYLE):
            result.append(BattlePassStyleProgressTokenBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(BATTLE_PASS_OFFER_TOKEN_PREFIX):
            result.append(BattlePassSelectTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(PM3_OFFER_TOKEN_PREFIX):
            result.append(PersonalMissionsSelectTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(EPIC_OFFER_TOKEN_PREFIX):
            result.append(EpicSelectTokensBonus({tID: tValue}, isCompensation, ctx))
        elif _isSelectableBonusID(tID):
            result.append(SelectableBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(BATTLE_PASS_Q_CHAIN_TOKEN_PREFIX):
            result.append(BattlePassQuestChainTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(BATTLE_PASS_RANDOM_QUEST_TOKEN_PREFIX):
            result.append(BattlePassRandomQuestTokensBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(BATTLE_PASS_TOKEN_PREFIX):
            result.append(BattlePassTokensBonus(name, {tID: tValue}, isCompensation, ctx))
        elif tID.startswith(CURRENCY_TOKEN_PREFIX):
            createBonusFromTokens(result, CURRENCY_TOKEN_PREFIX, tID, tValue)
        elif tID.startswith(RESOURCE_TOKEN_PREFIX):
            result.append(ResourceBonus(name, {tID: tValue}, RESOURCE_TOKEN_PREFIX, isCompensation, ctx))
        elif tID.startswith(CUSTOMIZATION_PROGRESS_PREFIX):
            result.append(C11nProgressTokenBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(COMP7_CUSTOMIZATION_PROGRESS_PREFIX):
            result.append(C11nProgressTokenBonus({(replaceComp7tokenID(tID, CUSTOMIZATION_PROGRESS_PREFIX)): tValue}, isCompensation, ctx))
        elif tID.startswith(COMP7_TOKEN_WEEKLY_REWARD_ID):
            result.append(Comp7TokenWeeklyRewardBonus(name, {tID: tValue}, isCompensation, ctx))
        elif tID.startswith(COMP7_TOKEN_COUPON_REWARD_ID):
            result.append(Comp7TokenCouponBonus({tID: tValue}, isCompensation, ctx))
        elif tID.startswith(COLLECTION_ITEM_TOKEN_PREFIX_NAME):
            result.append(CollectionTokenBonus(COLLECTION_ITEM_BONUS_NAME, {tID: tValue}, isCompensation, ctx))
        elif tID.startswith(VERSUS_AI_PROGRESSION_TOKEN_PREFIX):
            result.append(VersusAIProgressionsTokenBonus(name, {tID: tValue}, isCompensation, ctx))
        elif tID.startswith(LOOTBOX_CUSTOMIZATION_PROGRESS_PREFIX):
            result.append(LbC11nProgressTokenBonus({tID: tValue}, isCompensation, ctx))
        else:
            result.append(BattleTokensBonus(name, {tID: tValue}, isCompensation, ctx))

    return result


def currenciesFactory(name, value, isCompensation=False, ctx=None):
    result = []
    for tID, tValue in value.iteritems():
        result.append(CurrenciesBonus(name, {tID: tValue}))

    return result


def entitlementsFactory(name, value, isCompensation=False, ctx=None):
    result = []
    for eID, eValue in value.iteritems():
        if eID.startswith(COLLECTION_ITEM_PREFIX_NAME):
            result.append(CollectionEntitlementBonus(COLLECTION_ITEM_BONUS_NAME, (eID, eValue.get(b'count', 0)), isCompensation, ctx))
        else:
            result.append(EntitlementBonus(name, (eID, eValue.get(b'count', 0)), isCompensation, ctx))

    return result


class FreeTokensBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None, hasPawned=False):
        super(FreeTokensBonus, self).__init__(b'freeTokens', value, isCompensation, ctx)
        self.__hasPawnedTokens = hasPawned
        return

    def isShowInGUI(self):
        return self.getCount() > 0

    def formatValue(self):
        return str(self.getCount())

    def format(self):
        return makeHtmlString(b'html_templates:lobby/quests/bonuses', self._name, {b'value': (self.formatValue())})

    def areTokensPawned(self):
        return self.__hasPawnedTokens

    def getImageFileName(self):
        return (b'_').join((self.getName(), str(self.__determineBranchID())))

    def __determineBranchID(self):
        result = PM_BRANCH.REGULAR
        for branch, token in PM_BRANCH_TO_FREE_TOKEN_NAME.iteritems():
            if token in self._value:
                result = branch

        return result


class CompletionTokensBonus(TokensBonus):

    def __init__(self, value, isCompensation=False, ctx=None):
        super(CompletionTokensBonus, self).__init__(b'completionTokens', value, isCompensation, ctx)
        return

    def isShowInGUI(self):
        return self.getCount() > 0

    def formatValue(self):
        return str(self.getCount())

    def format(self):
        return makeHtmlString(b'html_templates:lobby/quests/bonuses', self._name, {b'value': (self.formatValue())})


class C11nProgressTokenBonus(TokensBonus):
    BONUS_NAME = b'styleProgress'

    def __init__(self, value, isCompensation=False, ctx=None):
        super(C11nProgressTokenBonus, self).__init__(self.BONUS_NAME, value, isCompensation, ctx)
        token = first(self.getTokens().values())
        self.__tokenID = token.id
        self.__progressData = self._parseC11nProgressToken(token)
        return

    @staticmethod
    def _parseC11nProgressToken(token):
        return parseC11nProgressToken(token)

    def isShowInGUI(self):
        return True

    def getTokenID(self):
        return self.__tokenID

    def getStyleID(self):
        return self.__progressData.styleID

    def getBranchID(self):
        return self.__progressData.branch

    def getProgressLevel(self):
        return self.__progressData.level

    def _format(self, **_):
        styleID = self.getStyleID()
        branchID = self.getBranchID()
        progressLevel = self.getProgressLevel()
        style = getProgressionStyle(styleID, branchID, progressLevel)
        return backport.text(R.strings.quests.bonusName.styleProgress(), name=style.userName, progress=progressLevel)


class LbC11nProgressTokenBonus(C11nProgressTokenBonus):
    BONUS_NAME = b'lbStyleProgress'

    @staticmethod
    def _parseC11nProgressToken(token):
        try:
            _, style, progressLevel = token.id.split(b':')
            styleID, branchID = style.split(b'_')
            return C11nStyleProgressData(int(styleID), int(branchID), int(progressLevel))
        except ValueError:
            return C11nStyleProgressData(None, None, None)

        return


class ItemsBonus(SimpleBonus):

    def getItems(self):
        if self._value is not None:
            _getItem = self.itemsCache.items.getItemByCD
            return dict((_getItem(intCD), count) for intCD, count in self._value.iteritems())
        else:
            return {}

    def format(self):
        result = []
        for item, count in self.getItems().iteritems():
            if item is not None and count:
                result.append(i18n.makeString(b'#quests:bonuses/items/name', name=item.userName, count=count))

        if result:
            return (b', ').join(result)
        else:
            return

    def getList(self):
        result = []
        for item, count in self.getItems().iteritems():
            if item is not None and count:
                description = item.fullDescription
                if item.itemTypeID in (GUI_ITEM_TYPE.OPTIONALDEVICE, GUI_ITEM_TYPE.EQUIPMENT):
                    description = stripColorTagDescrTags(description)
                tooltip = makeTooltip(header=item.userName, body=description)
                result.append({b'value': (backport.getIntegralFormat(count)), 
                   b'itemSource': (item.icon), 
                   b'tooltip': tooltip})

        return result

    def _getWrappedBonusList(self):
        result = []
        for item, count in self.getItems().iteritems():
            if item is not None and count:
                typeName = item.itemTypeName
                if item.itemTypeID in (GUI_ITEM_TYPE.BATTLE_BOOSTER, GUI_ITEM_TYPE.EQUIPMENT,
                 GUI_ITEM_TYPE.VEHICLE_MODULES):
                    typeName = b'equipment'
                result.append({b'id': (item.intCD), 
                   b'type': ((b'item/{}').format(typeName)), 
                   b'value': count, 
                   b'icon': {(AWARDS_SIZES.SMALL): (item.getBonusIcon(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (item.getBonusIcon(AWARDS_SIZES.BIG))}, 
                   b'name': (item.userName), 
                   b'description': (item.shortDescriptionSpecial.format(colorTagOpen=b'', colorTagClose=b''))})

        return result

    def hasIconFormat(self):
        return True

    def wrapToItemsPack(self, groupID=1):
        pack = []
        for data, count in self.getItems().iteritems():
            type_ = getItemPackByGroupAndName(ItemPackTypeGroup.ITEM, data.itemTypeName, ItemPackType.ITEM_EQUIPMENT)
            pack.append(ItemPackEntry(type=type_, count=count, id=data.intCDO.intCompactDescr, groupID=groupID))

        return pack

    def getLightViewModelData(self):
        return (
         first(self.getItems().iterkeys()).name,)

    def __getCommonAwardsVOs(self, item, count, iconSize=b'small', align=TEXT_ALIGN.RIGHT, withCounts=False):
        itemInfo = {b'imgSource': (item.getBonusIcon(iconSize)), 
           b'label': (text_styles.stats((b'x{}').format(count))), 
           b'tooltip': (self.makeItemTooltip(item)), 
           b'align': align}
        if withCounts:
            itemInfo[b'count'] = count
        return itemInfo

    @staticmethod
    def makeItemTooltip(item):
        description = item.fullDescription
        if item.itemTypeID in (GUI_ITEM_TYPE.OPTIONALDEVICE, GUI_ITEM_TYPE.EQUIPMENT):
            description = stripColorTagDescrTags(description)
        return makeTooltip(header=item.userName, body=description)

    def getCount(self):
        return sum(v for v in self._value.values())


class GoodiesBonus(SimpleBonus):
    GOODIES = b'goodies'
    goodiesCache = dependency.descriptor(IGoodiesCache)

    def getBoosters(self):
        return self._getGoodies(self.goodiesCache.getBooster)

    def getDiscounts(self):
        return self._getGoodies(self.goodiesCache.getDiscount)

    def getDemountKits(self):
        return self._getGoodies(self.goodiesCache.getDemountKit)

    def getRecertificationForms(self):
        return self._getGoodies(self.goodiesCache.getRecertificationForm)

    def _getGoodies(self, goodieGetter):
        goodies = {}
        if self._value is not None:
            for boosterID, info in self._value.iteritems():
                goodie = goodieGetter(int(boosterID))
                if goodie is not None and goodie.enabled:
                    goodies[goodie] = info.get(b'count', 1)

        return goodies

    def format(self):
        return (b', ').join(self.formattedList())

    @staticmethod
    def __makeBoosterVO(booster):
        return {b'icon': (booster.icon), 
           b'showCount': False, 
           b'qualityIconSrc': (booster.getQualityIcon()), 
           b'slotLinkage': (BOOSTER_CONSTANTS.SLOT_UI), 
           b'showLeftTime': False, 
           b'boosterId': (booster.boosterID)}

    def hasIconFormat(self):
        return True

    def getList(self):
        result = []
        for booster, count in sorted(self.getBoosters().iteritems(), key=(lambda (booster, count): booster.boosterType)):
            if booster is not None:
                result.append({b'value': (backport.getIntegralFormat(count)), 
                   b'tooltip': (TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO), 
                   b'boosterVO': (self.__makeBoosterVO(booster))})

        for discount, count in sorted(self.getDiscounts().iteritems()):
            if discount is not None:
                tooltip = makeTooltip(header=discount.userName, body=discount.description)
                result.append({b'value': (discount.getFormattedValue()), 
                   b'itemSource': (discount.icon), 
                   b'tooltip': tooltip})

        return result

    def _getWrappedBonusList(self):
        result = []
        for booster, count in self.getBoosters().iteritems():
            if booster is not None:
                result.append({b'id': (booster.boosterID), 
                   b'type': ((b'goodie/{}').format(booster.getTypeAsString())), 
                   b'value': count, 
                   b'icon': {(AWARDS_SIZES.SMALL): (RES_ICONS.getBonusIcon(AWARDS_SIZES.SMALL, booster.getFullNameForResource())), 
                             (AWARDS_SIZES.BIG): (RES_ICONS.getBonusIcon(AWARDS_SIZES.BIG, booster.getFullNameForResource()))}, 
                   b'name': (booster.userName), 
                   b'description': (booster.getBonusDescription())})

        for discount, count in self.getDiscounts().iteritems():
            if discount is not None:
                result.append({b'id': (discount.discountID), 
                   b'type': ((b'discount/{}').format(discount.targetType)), 
                   b'value': (discount.getFormattedValue()), 
                   b'icon': {(AWARDS_SIZES.SMALL): (discount.icon), (AWARDS_SIZES.BIG): (discount.bigIcon)}, 
                   b'name': (discount.userName), 
                   b'description': (discount.getBonusDescription())})

        for form, count in self.getRecertificationForms().iteritems():
            if form is not None:
                result.append({b'id': (form.intCD), 
                   b'type': ((b'goodie/{}').format(form.itemTypeName)), 
                   b'value': count, 
                   b'icon': {(AWARDS_SIZES.SMALL): (form.iconInfo), (AWARDS_SIZES.BIG): (form.bigIcon)}, 
                   b'name': (form.userName), 
                   b'description': (form.shortDescription)})

        return result

    def getWrappedLootBoxesBonusList(self):
        result = []
        for demountKit, count in self.getDemountKits().iteritems():
            if demountKit is not None:
                result.append({b'id': (demountKit.intCD), 
                   b'type': ((b'demountKit/{}').format(demountKit.demountKitGuiType)), 
                   b'value': count, 
                   b'icon': {(AWARDS_SIZES.SMALL): (demountKit.getIcon(ICONS_SIZES.X48)), (AWARDS_SIZES.BIG): (demountKit.getIcon(ICONS_SIZES.X80))}, 
                   b'name': (demountKit.userName), 
                   b'description': (demountKit.shortDescription)})

        result.extend(self._getWrappedBonusList())
        return result

    def formattedList(self):
        result = []
        for booster, count in self.getBoosters().iteritems():
            if booster is not None:
                result.append(i18n.makeString(b'#quests:bonuses/boosters/name', name=booster.userName, count=count))

        for discount, count in self.getDiscounts().iteritems():
            if discount is not None:
                result.append(i18n.makeString(b'#quests:bonuses/discount/name', name=discount.userName, targetName=discount.targetName, effectValue=discount.getFormattedValue(), count=count))

        for demountKit, count in self.getDemountKits().iteritems():
            result.append(backport.text(R.strings.quests.bonuses.items.name(), name=demountKit.userName, count=count))

        for recertificationForm, count in self.getRecertificationForms().iteritems():
            result.append(backport.text(R.strings.quests.bonuses.items.name(), name=recertificationForm.userName, count=count))

        return result

    def wrapToItemsPack(self, groupID=1):
        pack = []
        for goodie in self.getWrappedEpicBonusList():
            pack.append(ItemPackEntry(type=goodie[b'type'], count=goodie[b'value'], id=goodie[b'id'], groupID=groupID))

        return pack

    def getCount(self):
        return sum(v.get(b'count', 0) for v in self._value.values())

    def __getCommonAwardsVOs(self, item, count, iconSize=b'small', align=TEXT_ALIGN.RIGHT, withCounts=False):
        itemData = {b'imgSource': (RES_ICONS.getBonusIcon(iconSize, item.boosterGuiType)), 
           b'label': (text_styles.hightlight((b'x{}').format(count))), 
           b'align': align}
        itemData.update(self.__itemTooltip(item))
        if withCounts:
            itemData[b'count'] = count
        return itemData

    @staticmethod
    def __itemTooltip(booster):
        return {b'isSpecial': True, 
           b'specialAlias': (TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO), 
           b'specialArgs': [
                          booster.boosterID]}


class VehiclesBonus(SimpleBonus):
    VEHICLES_BONUS = b'vehicles'

    @classmethod
    def isNonZeroCompensation(cls, vehInfo):
        compensatedNumber = vehInfo.get(b'compensatedNumber', 0)
        compensation = vehInfo.get(b'customCompensation')
        if compensatedNumber and compensation is not None:
            money = Money(*compensation)
            if money == _ZERO_COMPENSATION_MONEY:
                return False
        return True

    def formatValue(self):
        result = []
        for item, _ in self.getVehicles():
            result.append(item.shortUserName)

        return (b', ').join(result)

    def format(self):
        return (b', ').join(self.formattedList())

    def formattedList(self):
        result = []
        for item, vehInfo in self.getVehicles():
            tmanRoleLevel = self.getTmanRoleLevel(vehInfo)
            rentDays = self.getRentDays(vehInfo)
            vInfoLabels = []
            if rentDays is not None:
                rentDaysStr = makeHtmlString(b'html_templates:lobby/quests/bonuses', b'rentDays', {b'value': (str(rentDays))})
                vInfoLabels.append(rentDaysStr)
            if tmanRoleLevel is not None:
                crewLvl = i18n.makeString(b'#quests:bonuses/vehicles/crewLvl', tmanRoleLevel)
                vInfoLabels.append(crewLvl)
            if vInfoLabels:
                result.append(text_styles.standard(i18n.makeString(b'#quests:bonuses/vehicles/name', name=text_styles.main(item.userName), vehInfo=(b'; ').join(vInfoLabels))))
            else:
                result.append(text_styles.main(item.userName))

        return result

    def getCount(self):
        return len(self.getVehicles())

    def _getWrappedBonusList(self):
        result = []
        for item, vehInfo in self.getVehicles():
            icons = dict()
            if self.isRentVehicle(vehInfo):
                for size in AWARDS_SIZES.ALL():
                    icons[size] = RES_ICONS.getRentVehicleAwardIcon(size)

            else:
                icons = {(AWARDS_SIZES.SMALL): (item.iconSmall), 
                   (AWARDS_SIZES.BIG): (item.icon)}
            result.append({b'id': (item.intCD), 
               b'type': ((b'vehicle/{}').format(item.type)), 
               b'value': 1, 
               b'icon': icons})

        return result

    def getIcon(self):
        return backport.image(R.images.gui.maps.icons.library.tank())

    def getTooltipIcon(self):
        vehicle, _ = self.getVehicles()[0]
        return vehicle.icon

    def getVehicles(self):
        result = []
        if self._value is not None:
            if isinstance(self._value, dict):
                for intCD, vehInfo in self._value.iteritems():
                    item = self.itemsCache.items.getItemByCD(intCD)
                    if item is not None and not item.isOnlyForBattleRoyaleBattles:
                        result.append((item, vehInfo))

            elif isinstance(self._value, list):
                for subDict in self._value:
                    for intCD, vehInfo in subDict.iteritems():
                        item = self.itemsCache.items.getItemByCD(intCD)
                        if item is not None and not item.isOnlyForBattleRoyaleBattles:
                            result.append((item, vehInfo))

        return result

    def isRentVehicle(self, vehInfo):
        if self.getRentBattles(vehInfo) or self.getRentDays(vehInfo) or self.getRentWins(vehInfo) or self.getRentSeason(vehInfo) or self.getRentCycle(vehInfo):
            return True
        return False

    def compensation(self, vehicle, bonus):
        bonuses = []
        for curVehicle, vehInfo in self.getVehicles():
            compensatedNumber = vehInfo.get(b'compensatedNumber', 0)
            compensation = vehInfo.get(b'customCompensation')
            if compensatedNumber and compensation is not None and curVehicle == vehicle:
                money = Money(*compensation)
                while compensatedNumber > 0:
                    for currency, value in money.iteritems():
                        if value:
                            cls = _BONUSES.get(currency)
                            bonuses.append(cls(currency, value, isCompensation=True, compensationReason=bonus))

                    compensatedNumber -= 1

        return bonuses

    def getPossibleCompensationBonuses(self, vehicle, bonus):
        bonuses = []
        for curVehicle, vehInfo in self.getVehicles():
            compensation = vehInfo.get(b'customCompensation')
            if compensation is not None and curVehicle == vehicle:
                money = Money(*compensation)
                for currency, value in money.iteritems():
                    if value:
                        cls = _BONUSES.get(currency)
                        bonuses.append(cls(currency, value, isCompensation=True, compensationReason=bonus))

        return bonuses

    def checkIsCompensatedVehicle(self, vehicle):
        for curVehicle, vehInfo in self.getVehicles():
            compensation = vehInfo.get(b'customCompensation')
            return curVehicle == vehicle and compensation

        return False

    def getIconLabel(self):
        return b'x1'

    def wrapToItemsPack(self, groupID=1):
        pack = []
        for vehicle, vehInfo in self.getVehicles():
            type_ = getItemPackByGroupAndName(ItemPackTypeGroup.VEHICLE, vehicle.itemTypeName)
            pack.append(ItemPackEntry(type=type_, count=1, id=vehicle.intCDO.intCompactDescr, groupID=groupID))
            tmanPack = []
            for tman in vehInfo.get(b'tankmen', []):
                tankmanDescr = tankmen.TankmanDescr(tman)
                tmanPack.append({b'isPremium': (tankmanDescr.isPremium), 
                   b'freeXP': (tankmanDescr.freeXP), 
                   b'skills': [], b'gId': (tankmanDescr.gid), 
                   b'role': (tankmanDescr.role), 
                   b'nationID': (tankmanDescr.nationID), 
                   b'roleLevel': (tankmanDescr.roleLevel), 
                   b'vehicleTypeID': (tankmanDescr.vehicleTypeID), 
                   b'freeSkills': (tankmanDescr.freeSkills)})

            crew = ItemPackEntry(type=ItemPackType.CREW_CUSTOM, count=1, id=1, groupID=groupID, extra={b'tankmen': tmanPack})
            pack.append(crew)

        return pack

    def isOneOf(self):
        vehiclesInBonus = self.getVehicles()
        if vehiclesInBonus:
            _, vehicleData = vehiclesInBonus[0]
            return vehicleData.get(b'oneof', False)
        return False

    def __getCommonAwardsVOs(self, vehicle, vehInfo, iconSize=b'small', align=TEXT_ALIGN.RIGHT, withCounts=False):
        vehicleVO = self.__getVehicleVO(vehicle, vehInfo, partial(RES_ICONS.getBonusIcon, iconSize))
        vehicleVO.update({b'label': (self.getIconLabel())})
        vehicleVO[b'align'] = align
        if withCounts:
            vehicleVO[b'count'] = 1
        return vehicleVO

    @classmethod
    def getTmanRoleLevel(cls, vehInfo):
        if b'noCrew' not in vehInfo:
            if b'crewLvl' in vehInfo:
                return calculateRoleLevel(vehInfo.get(b'crewLvl', DEFAULT_CREW_LVL), vehInfo.get(b'crewFreeXP', 0))
            if b'tankmen' in vehInfo:
                for tman in vehInfo[b'tankmen']:
                    if isinstance(tman, str):
                        tankmanDecsr = tankmen.TankmanDescr(compactDescr=tman)
                        if tankmanDecsr.role == Tankman.ROLES.COMMANDER:
                            return calculateRoleLevel(tankmanDecsr.roleLevel, tankmanDecsr.freeXP)
                    elif tman[b'role'] == Tankman.ROLES.COMMANDER:
                        return calculateRoleLevel(tman.get(b'roleLevel', DEFAULT_CREW_LVL), tman.get(b'freeXP', 0))

        return

    @staticmethod
    def getRentDays(vehInfo):
        if b'rent' not in vehInfo:
            return
        else:
            time = vehInfo.get(b'rent', {}).get(b'time')
            if time:
                if time == float(b'inf'):
                    return
                if time <= time_utils.DAYS_IN_YEAR:
                    return int(time)
                rentDaysLeft = time_utils.getDaysLeftDueDate(time)
                if rentDaysLeft >= 0:
                    return int(rentDaysLeft)
                return
            return

    @staticmethod
    def getRentBattles(vehInfo):
        return vehInfo.get(b'rent', {}).get(b'battles')

    @staticmethod
    def getRentWins(vehInfo):
        return vehInfo.get(b'rent', {}).get(b'wins')

    @staticmethod
    def getRentSeason(vehInfo):
        return vehInfo.get(b'rent', {}).get(b'season')

    @staticmethod
    def getRentCycle(vehInfo):
        return vehInfo.get(b'rent', {}).get(b'cycle')

    def getRentInfo(self, vehInfo):
        if self.isRentVehicle(vehInfo):
            for rentType, getter in ((RentType.TIME_RENT, self.getRentDays),
             (
              RentType.BATTLES_RENT, self.getRentBattles),
             (
              RentType.WINS_RENT, self.getRentWins)):
                rentValue = getter(vehInfo)
                if rentValue:
                    return (rentType, rentValue)

        return (
         RentType.NO_RENT, 0)

    def __getVehicleVO(self, vehicle, vehicleInfo, iconGetter):
        tmanRoleLevel = self.getTmanRoleLevel(vehicleInfo)
        rentDays = self.getRentDays(vehicleInfo)
        if rentDays:
            iconName = b'vehicles_rent'
            rentExpiryTime = time_utils.getCurrentTimestamp() + rentDays * time_utils.ONE_DAY
        else:
            iconName = b'vehicles'
            rentExpiryTime = 0
        return {b'imgSource': (iconGetter(iconName)), 
           b'isSpecial': True, 
           b'specialAlias': (TOOLTIPS_CONSTANTS.AWARD_VEHICLE), 
           b'specialArgs': [
                          vehicle.intCD, tmanRoleLevel, rentExpiryTime]}


class ParagonsUnlocksBonus(SimpleBonus):

    def getParagonsUnlocks(self):
        return self._value.get(b'ids')

    def formatValue(self):
        return b''


class BadgesGroupBonus(SimpleBonus):

    def getBadges(self):
        groupID = self._value
        badges = self.itemsCache.items.getBadges()
        return [badge for badge in badges.itervalues() if groupID == badge.group]


class DossierBonus(SimpleBonus):

    def getRecords(self):
        records = {}
        if self._value is not None:
            for dossierType in self._value:
                if dossierType != DOSSIER_TYPE.CLAN:
                    popUpRecords = {}
                    if self._ctx and b'popUpRecords' in self._ctx:
                        popUpRecords = dict(self._ctx[b'popUpRecords'])
                    for name, data in self._value[dossierType].iteritems():
                        block = name[0]
                        if block == BADGES_BLOCK:
                            blid = int(name[1])
                        else:
                            blid = RECORD_DB_IDS.get(name, 0)
                        val = popUpRecords.get(blid)
                        if val is None:
                            val = data.get(b'value', 0)
                        records[name] = val

        return records

    def getAchievements(self):
        return self.__getItems(_isAchievement)

    def getAchievementsFromDossier(self, statsBlock):
        result = []
        for record in self.getRecords().iterkeys():
            achievement = statsBlock.getAchievement(record)
            if achievement is not None:
                result.append(achievement)

        return result

    def getBadges(self):
        result = []
        badges = None
        for (block, record), _ in self.getRecords().iteritems():
            if _isBadge(block):
                badgeID = int(record)
                if badges is None:
                    badges = self.itemsCache.items.getBadges()
                if badgeID in badges:
                    result.append(badges[badgeID])

        return result

    def format(self):
        return (b', ').join(self.formattedList())

    def formattedList(self):
        return [achievement.getUserName() for achievement in self.getAchievements()]

    def getCount(self):
        return sum(v for v in self.getRecords().values())

    def _getWrappedBonusList(self):
        result = []
        for block, record in self.getRecords().iterkeys():
            if block == b'singleAchievements':
                blockID = RECORD_DB_IDS[block, record]
            else:
                blockID = record
            icons = self.__getEpicBonusImages(block, record)
            if not icons[b'small'] and not icons[b'big']:
                icons = self.__getAchievementImages(record)
            result.append({b'id': blockID, 
               b'name': record, 
               b'type': block, 
               b'value': 1, 
               b'icon': icons})

        return result

    def __getEpicBonusImages(self, block, record):
        if block == b'playerBadges':
            return {(AWARDS_SIZES.SMALL): (getBadgeIconPath(BADGES_ICONS.X48, record)), 
               (AWARDS_SIZES.BIG): (getBadgeIconPath(BADGES_ICONS.X80, record))}
        if block == b'singleAchievements':
            return {(AWARDS_SIZES.SMALL): (RES_ICONS.getEpicAchievementIcon(ICONS_SIZES.X48, record)), 
               (AWARDS_SIZES.BIG): (RES_ICONS.getEpicAchievementIcon(ICONS_SIZES.X80, record))}
        return {}

    def __getAchievementImages(self, record):
        return {(AWARDS_SIZES.SMALL): (backport.image(R.images.gui.maps.icons.achievement.num(ICONS_SIZES.X48).dyn(record)())), 
           (AWARDS_SIZES.BIG): (backport.image(R.images.gui.maps.icons.achievement.num(ICONS_SIZES.X80).dyn(record)()))}

    def __getCommonAwardsVOs(self, block, record, iconSize=b'small', withCounts=False):
        badgesIconSizes = {b'big': (BADGES_ICONS.X80), b'small': (BADGES_ICONS.X48)}
        if _isBadge(block):
            header = i18n.makeString(BADGE.badgeName(record))
            body = i18n.makeString(BADGE.badgeDescriptor(record))
            note = i18n.makeString(BADGE.BADGE_NOTE)
            badgeVO = {b'imgSource': (getBadgeIconPath(badgesIconSizes[iconSize], record)), 
               b'label': b'', 
               b'tooltip': (makeTooltip(header, body, note))}
            if withCounts:
                badgeVO[b'count'] = 1
            return badgeVO
        return

    def __getItems(self, filterFunc):
        result = []
        for (block, record), value in self.getRecords().iteritems():
            if filterFunc(block):
                achieve = _getAchievement(block, record, value)
                if achieve is not None:
                    result.append(achieve)

        return result


class PersonalMissionDossierBonus(DossierBonus):

    def isShowInGUI(self):
        return bool(self.getBadges())


class TankmenBonus(SimpleBonus):
    _TankmanInfoRecord = namedtuple(b'_TankmanInfoRecord', [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15])

    def formatValue(self):
        result = []
        for group in self.getTankmenGroups().itervalues():
            if group[b'skills']:
                labelI18nKey = b'#quests:bonuses/item/tankmen/with_skills'
            else:
                labelI18nKey = b'#quests:bonuses/item/tankmen/no_skills'
            result.append(i18n.makeString(labelI18nKey, **group))

        return (b' ').join(result)

    def getTankmenData(self):
        result = []
        if self._value is not None:
            for tankmanData in self._value:
                if isinstance(tankmanData, str):
                    result.append(self._makeTmanInfoByDescr(tankmen.TankmanDescr(compactDescr=tankmanData)))
                else:
                    result.append(makeTupleByDict(self._TankmanInfoRecord, tankmanData))

        return result

    def getTankmenGroups(self):
        groups = {}
        for tmanInfo in self.getTankmenData():
            roleLevel = calculateRoleLevel(tmanInfo.roleLevel, tmanInfo.freeXP, typeID=(tmanInfo.nationID, tmanInfo.vehicleTypeID))
            if tmanInfo.vehicleTypeID not in groups:
                vehIntCD = vehicles.makeIntCompactDescrByID(b'vehicle', tmanInfo.nationID, tmanInfo.vehicleTypeID)
                groups[tmanInfo.vehicleTypeID] = {b'vehName': (self.itemsCache.items.getItemByCD(vehIntCD).shortUserName), 
                   b'skills': (len(tmanInfo.skills)), 
                   b'roleLevel': roleLevel}
            else:
                group = groups[tmanInfo.vehicleTypeID]
                group[b'skills'] += len(tmanInfo.skills)
                group[b'roleLevel'] = min(group[b'roleLevel'], roleLevel)

        return groups

    def getTankmenDescriptors(self):
        result = []
        if self._value is not None:
            for tankmanData in self._value:
                if isinstance(tankmanData, str):
                    result.append(tankmen.TankmanDescr(compactDescr=tankmanData))
                else:
                    result.append(tankmen.generateCompactDescr(tankmen.generatePassport(tankmanData[b'nationID'], tankmanData.get(b'isPremium', False)), tankmanData[b'vehicleTypeID'], tankmanData[b'role'], tankmanData[b'roleLevel'], tankmanData[b'skills']))

            return result
        return

    def getIcon(self):
        return backport.image(R.images.gui.maps.icons.library.tankman())

    def getTooltipIcon(self):
        for tmanInfo in self.getTankmenData():
            if tmanInfo.isFemale:
                return RES_ICONS.MAPS_ICONS_QUESTS_TANKMANFEMALEGRAY

        return RES_ICONS.MAPS_ICONS_REFERRAL_REFSYS_MEN_BW

    def getCount(self):
        if self._value is not None:
            return len(self._value)
        else:
            return 0

    @classmethod
    def _makeTmanInfoByDescr(cls, td):
        return cls._TankmanInfoRecord(td.nationID, td.role, td.vehicleTypeID, td.firstNameID, -1, td.lastNameID, -1, td.iconID, -1, td.isPremium, td.roleLevel, td.freeXP, td.skills, td.isFemale, [])

    @classmethod
    def getTankmenDataForCrew(cls, vehCD, roleLevel):
        vehicle = cls.itemsCache.items.getItemByCD(vehCD)
        nation, vehicleTypeID = vehicle.typeDescr.id
        result = {b'nationID': nation, 
           b'vehicleTypeID': vehicleTypeID, 
           b'roleLevel': roleLevel, 
           b'freeXP': 0, 
           b'skills': []}
        for field in cls._TankmanInfoRecord._fields:
            if field not in result:
                result[field] = None

        return result


class TankwomanBonus(TankmenBonus):

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(TankwomanBonus, self).__init__(name, value, isCompensation)
        self._name = b'tankwomanBonus'
        return

    def formatValue(self):
        result = []
        for tmanInfo in self.getTankmenData():
            if tmanInfo.isFemale:
                result.append(i18n.makeString(QUESTS.BONUSES_ITEM_TANKWOMAN))
            else:
                result.append(i18n.makeString(QUESTS.BONUSES_TANKMEN_DESCRIPTION, value=getRoleUserName(tmanInfo.role)))

        return (b', ').join(result)


class CustomizationsBonus(SimpleBonus):
    c11n = dependency.descriptor(ICustomizationService)

    def getList(self):
        result = []
        separator = b''
        customizations = self.getCustomizations()
        customizationsCountMax = len(customizations) - 1
        if customizationsCountMax > 0:
            separator = b', '
        for count, itemData in enumerate(customizations):
            boundVehicle = itemData.get(b'vehTypeCompDescr')
            boundToCurrentVehicle = itemData.get(b'boundToCurrentVehicle', False)
            item = self.getC11nItem(itemData)
            value = itemData.get(b'value', 0)
            valueStr = None
            if value > 1:
                valueStr = text_styles.main(i18n.makeString(QUESTS.BONUSES_CUSTOMIZATION_VALUE, count=value))
            key = VEHICLE_CUSTOMIZATION.getElementBonusDesc(item.itemFullTypeName)
            bonusDesc = b''
            if key is not None:
                bonusDesc = _ms(key, value=item.userName)
                if value > 0:
                    bonusDesc = bonusDesc + b' ' + _ms(VEHICLE_CUSTOMIZATION.ELEMENTBONUS_FACTOR, count=value)
                if count < customizationsCountMax:
                    bonusDesc = bonusDesc + separator
            result.append({b'intCD': (item.intCD), 
               b'texture': (item.icon), 
               b'value': value, 
               b'valueStr': valueStr, 
               b'boundVehicle': boundVehicle, 
               b'boundToCurrentVehicle': boundToCurrentVehicle, 
               b'showPrice': False, 
               b'description': bonusDesc})

        return result

    def getCount(self):
        return sum(v.get(b'value', 1) for v in self.getCustomizations())

    @staticmethod
    def getItemTypeID(itemTypeName):
        if itemTypeName == b'projection_decal':
            itemTypeID = GUI_ITEM_TYPE.PROJECTION_DECAL
        elif itemTypeName == b'personal_number':
            itemTypeID = GUI_ITEM_TYPE.PERSONAL_NUMBER
        else:
            itemTypeID = GUI_ITEM_TYPE_INDICES.get(itemTypeName)
        return itemTypeID

    def _getWrappedBonusList(self):
        result = []
        for itemData in self.getCustomizations():
            itemType = itemData.get(b'custType')
            itemTypeID = self.getItemTypeID(itemType)
            item = self.c11n.getItemByID(itemTypeID, itemData.get(b'id'))
            smallIcon = item.getBonusIcon(AWARDS_SIZES.SMALL)
            bigIcon = item.getBonusIcon(AWARDS_SIZES.BIG)
            typeStr = self.__getItemTypeStr(itemType)
            if itemType == b'style':
                smallIcon = RES_ICONS.getBonusIcon(AWARDS_SIZES.SMALL, itemType)
                bigIcon = RES_ICONS.getBonusIcon(AWARDS_SIZES.BIG, itemType)
            result.append({b'id': (itemData.get(b'id')), 
               b'type': typeStr, 
               b'value': (itemData.get(b'value', 0)), 
               b'icon': {(AWARDS_SIZES.SMALL): smallIcon, 
                         (AWARDS_SIZES.BIG): bigIcon}, 
               b'name': (item.longUserName), 
               b'description': (item.longDescriptionSpecial)})

        return result

    def getWrappedBonus(self):
        result = []
        for itemData in self.getCustomizations():
            itemType = itemData.get(b'custType')
            itemTypeID = self.getItemTypeID(itemType)
            item = self.c11n.getItemByID(itemTypeID, itemData.get(b'id'))
            typeStr = self.__getItemTypeStr(itemType)
            result.append({b'id': (item.intCD), 
               b'type': typeStr, 
               b'value': (itemData.get(b'value', 0))})

        return result

    def getCustomizations(self):
        return self._value or []

    def compensation(self):
        bonuses = []
        substitutes = []
        cache = vehicles.g_cache.customization20()
        for customizationItem in self._value:
            c11nItem = self.getC11nItem(customizationItem)
            itemType, itemId = cc.splitIntDescr(c11nItem.intCD)
            c11nComponent = cache.itemTypes[itemType][itemId]
            count = customizationItem.get(b'value')
            inventoryCount = c11nItem.inventoryCount
            maxNumber = c11nComponent.maxNumber
            compensationCount = count - max(0, maxNumber - inventoryCount)
            if compensationCount > 0 and maxNumber != 0:
                realCount = count - compensationCount
                if realCount > 0:
                    substituteItem = copy.deepcopy(customizationItem)
                    substituteItem[b'value'] = realCount
                    substitutes.append(substituteItem)
                compensation = customizationItem.get(b'customCompensation')
                money = Money.makeMoney(compensation)
                if money is not None:
                    for currency, value in money.iteritems():
                        if value:
                            cls = _BONUSES.get(currency)
                            bonuses.append(cls(currency, value * compensationCount, isCompensation=True))

            else:
                substitutes.append(copy.deepcopy(customizationItem))

        bonuses.insert(0, CustomizationsBonus(b'customizations', substitutes))
        return bonuses

    def getC11nItem(self, item):
        itemTypeName = item.get(b'custType')
        itemID = item.get(b'id')
        itemTypeID = self.getItemTypeID(itemTypeName)
        c11nItem = self.c11n.getItemByID(itemTypeID, itemID)
        return c11nItem

    def wrapToItemsPack(self, groupID=1):
        pack = []
        for customization in self.getWrappedBonus():
            pack.append(ItemPackEntry(type=customization[b'type'], count=customization[b'value'], id=customization[b'id'], groupID=groupID))

        return pack

    def hasAnyCustomCompensations(self):
        for customizationItem in self._value:
            if customizationItem.get(b'customCompensation'):
                return True

        return False

    def __getItemTypeStr(self, itemType):
        typeStr = itemType
        if itemType == b'decal':
            typeStr = b'decal/1'
        elif itemType in _CUSTOMIZATION_BONUSES:
            typeStr = (b'').join([typeStr, b'/all'])
        return typeStr

    def __getCommonAwardsVOs(self, item, data, iconSize=b'small', align=TEXT_ALIGN.RIGHT, withCounts=False):
        c11nItem = self.getC11nItem(item)
        count = item.get(b'value', 1)
        itemData = {b'imgSource': (RES_ICONS.getBonusIcon(iconSize, c11nItem.itemTypeName)), 
           b'label': (text_styles.hightlight((b'x{}').format(count))), 
           b'align': align}
        itemData.update(self.__itemTooltip(data))
        if withCounts:
            itemData[b'count'] = count
        return itemData

    def __itemTooltip(self, data):
        return {b'isSpecial': True, 
           b'specialAlias': (TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM), 
           b'specialArgs': (CustomizationTooltipContext(itemCD=data[b'intCD'], showInventoryBlock=data[b'showPrice']))}


class BoxBonus(SimpleBonus):

    class HandlerNames(object):
        pass

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(BoxBonus, self).__init__(name, value, isCompensation)
        self.__iconsHandlerData = (b'', None)
        self.__tooltipType = None
        self.__iconHandlers = {}
        return

    def setupIconHandler(self, handlerData, handlerParams):
        self.__iconsHandlerData = (handlerData, handlerParams)
        return

    def setTooltipType(self, tooltipType):
        self.__tooltipType = tooltipType
        return

    def getIconBySize(self, size):
        handlerName, params = self.__iconsHandlerData
        handler = self.__iconHandlers.get(handlerName)
        if handler:
            return handler(params, size)
        else:
            return

    def getIconLabel(self):
        return b''

    def getTooltip(self):
        name = self._name
        if self.__tooltipType is not None:
            name = (b'/').join([name, self.__tooltipType])
        return _getItemTooltip(name)


class UniversalCrewbook(SimpleBonus):
    __ITEM = namedtuple(b'__ITEM', (b'name', b'count', b'options'))

    def getItems(self):
        return [self.__ITEM(item[b'itemName'], item[b'count'], self.__getOptionsBonus(item[b'options'])) for item in self._value]

    def __getOptionsBonus(self, options):
        bonusCls = _BONUSES.get(options.get(b'name'))
        return first(bonusCls(options.get(b'name'), options.get(b'value')))


def subscriptionBonusFactory(name, value, isCompensation=False, ctx=None):
    subsBonus = {(WoTPlusBonusType.GOLD_BANK): GoldBank, 
       (WoTPlusBonusType.IDLE_CREW_XP): IdleCrewXP, 
       (WoTPlusBonusType.EXCLUDED_MAP): ExcludedMap, 
       (WoTPlusBonusType.FREE_EQUIPMENT_DEMOUNTING): FreeEquipmentDemounting, 
       (WoTPlusBonusType.EXCLUSIVE_VEHICLE): WoTPlusExclusiveVehicle, 
       (WoTPlusBonusType.ATTENDANCE_REWARD): AttendanceReward, 
       (WoTPlusBonusType.TEAM_CREDITS_BONUS): TeamCreditsBonus, 
       (WoTPlusBonusType.DAILY_QUESTS_REWARDS): DailyQuestsRewards}
    return subsBonus.get(value)()


class WoTPlusBonus(SimpleBonus):

    def __init__(self, name):
        super(WoTPlusBonus, self).__init__(name, None)
        return


class GoldBank(WoTPlusBonus):
    _lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        super(GoldBank, self).__init__(WoTPlusBonusType.GOLD_BANK)
        return

    def getTooltip(self):
        goldReserveCapacity = self._lobbyContext.getServerSettings().getRenewableSubMaxGoldReserveCapacity()
        headerData, bodyData = getSimpleTooltipData(self._name)
        header = i18n.makeString(headerData)
        body = i18n.makeString(bodyData, goldReserveCapacity=goldReserveCapacity)
        return makeTooltip(header, body)


class AttendanceReward(WoTPlusBonus):

    def __init__(self):
        super(AttendanceReward, self).__init__(WoTPlusBonusType.ATTENDANCE_REWARD)
        return


class IdleCrewXP(WoTPlusBonus):

    def __init__(self):
        super(IdleCrewXP, self).__init__(WoTPlusBonusType.IDLE_CREW_XP)
        return


class ExcludedMap(WoTPlusBonus):

    def __init__(self):
        super(ExcludedMap, self).__init__(WoTPlusBonusType.EXCLUDED_MAP)
        return


class FreeEquipmentDemounting(WoTPlusBonus):

    def __init__(self):
        super(FreeEquipmentDemounting, self).__init__(WoTPlusBonusType.FREE_EQUIPMENT_DEMOUNTING)
        return


class TeamCreditsBonus(WoTPlusBonus):

    def __init__(self):
        super(TeamCreditsBonus, self).__init__(WoTPlusBonusType.TEAM_CREDITS_BONUS)
        return


class DailyQuestsRewards(WoTPlusBonus):

    def __init__(self):
        super(DailyQuestsRewards, self).__init__(WoTPlusBonusType.DAILY_QUESTS_REWARDS)
        return


class WoTPlusExclusiveVehicle(WoTPlusBonus):
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)

    def __init__(self):
        super(WoTPlusExclusiveVehicle, self).__init__(WoTPlusBonusType.EXCLUSIVE_VEHICLE)
        return

    def getTooltip(self):
        vehicle = self._wotPlusCtrl.getActiveExclusiveVehicle()
        vehicleName = self._wotPlusCtrl.getActiveExclusiveVehicleName()
        header = b''
        body = b''
        if vehicle is not None:
            headerData, bodyData = getSimpleTooltipData(self._name)
            header = i18n.makeString(headerData)
            body = i18n.makeString(bodyData, vehicleName=vehicleName, vehicleType=getWotPlusExclusiveVehicleTypeUserName(vehicle.classTag))
        return makeTooltip(header, body)


def randomBlueprintBonusFactory(name, value, isCompensation=False, ctx=None):
    blueprintBonuses = []
    for params, fragmentCount in value.iteritems():
        blueprintBonuses.append(RandomBlueprintBonus(name, (params, fragmentCount), isCompensation, ctx))

    return blueprintBonuses


def blueprintBonusFactory(name, value, isCompensation=False, ctx=None):
    blueprintBonuses = []
    for fragmentCD, fragmentCount in sorted(value.iteritems(), key=itemgetter(0)):
        fragmentType = getFragmentType(fragmentCD)
        if fragmentType == BlueprintTypes.VEHICLE:
            blueprintBonuses.append(VehicleBlueprintBonus(name, (fragmentCD, fragmentCount), isCompensation, ctx))
        elif fragmentType == BlueprintTypes.INTELLIGENCE_DATA:
            vehicleCD = getVehicleCDForIntelligence(fragmentCD)
            blueprintBonuses.append(IntelligenceBlueprintBonus(name, (vehicleCD, fragmentCount), isCompensation, ctx))
        elif fragmentType == BlueprintTypes.NATIONAL:
            vehicleCD = getVehicleCDForNational(fragmentCD)
            blueprintBonuses.append(NationalBlueprintBonus(name, (vehicleCD, fragmentCount), isCompensation, ctx))

    return blueprintBonuses


class BlueprintsBonusSubtypes(CONST_CONTAINER):
    FINAL_FRAGMENT = b'BlueprintFinalFragmentCongrats'
    UNIVERSAL_FRAGMENT = b'BlueprintUniversalFragmentCongrats'
    NATION_FRAGMENT = b'BlueprintNationFragmentCongrats'
    VEHICLE_FRAGMENT = b'BlueprintVehicleFragmentCongrats'
    RANDOM_FRAGMENT = b'BlueprintRandomFragmentCongrats'
    RANDOM_NATIONAL_FRAGMENT = b'BlueprintRandomNationalFragmentCongrats'
    USE_CONGRATS = (
     FINAL_FRAGMENT,
     VEHICLE_FRAGMENT)


class RandomBlueprintBonus(SimpleBonus):
    _HTML_TEMPLATE = b'anyBlueprints'
    _HTML_TEMPLATE_NATIONAL = b'anyNationalBlueprints'

    def getBlueprintName(self):
        if self._getBlueprintType() == BlueprintTypes.NATIONAL:
            return BlueprintsBonusSubtypes.RANDOM_NATIONAL_FRAGMENT
        return BlueprintsBonusSubtypes.RANDOM_FRAGMENT

    def getBlueprintTooltipName(self):
        if self._getBlueprintType() == BlueprintTypes.NATIONAL:
            return backport.text(R.strings.tooltips.blueprint.BlueprintFragmentTooltip.randomNational.header())
        return backport.text(R.strings.tooltips.blueprint.BlueprintFragmentTooltip.random.header())

    def getBlueprintSpecialAlias(self):
        if self._getBlueprintType() == BlueprintTypes.NATIONAL:
            return TOOLTIPS_CONSTANTS.BLUEPRINT_RANDOM_NATIONAL_INFO
        return TOOLTIPS_CONSTANTS.BLUEPRINT_RANDOM_INFO

    def getBlueprintSpecialArgs(self):
        return

    def formatBlueprintValue(self):
        return b''

    def getImageCategory(self):
        if self._getBlueprintType() == BlueprintTypes.NATIONAL:
            return b'randomNational'
        return b'random'

    def getImage(self, size=b'big'):
        return RES_ICONS.getBlueprintFragment(size, self.getImageCategory())

    def getIconResource(self, size):
        iconR = R.images.gui.maps.icons.blueprints.fragment.dyn(size).dyn(self.getImageCategory())
        if iconR:
            return iconR()
        return R.images.gui.maps.icons.quests.bonuses.dyn(size).default()

    def getCount(self):
        return self._value[1]

    def getTooltip(self):
        return b''

    def canPacked(self):
        return False

    def getWrappedLootBoxesBonusList(self):
        return [
         {b'id': 0, 
            b'type': (ItemPackType.BLUEPRINT_ANY), 
            b'value': (self.getCount()), 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getImage(size=b'small')), (AWARDS_SIZES.BIG): (self.getImage())}, 
            b'name': (self.getBlueprintTooltipName()), 
            b'description': (backport.text(R.strings.tooltips.blueprint.BlueprintFragmentTooltip.random.description()))}]

    def _getFormattedMessage(self, styleSubset, formattedValue):
        return makeHtmlString((b'html_templates:lobby/quests/{}').format(styleSubset), self._getHtmlTemplate(), {b'value': formattedValue})

    def _format(self, styleSubset):
        formattedValue = str(self.getValue()[1])
        text = b''
        if formattedValue is not None:
            text = self._getFormattedMessage(styleSubset, formattedValue)
        return text

    def _getBlueprintType(self):
        return self._value[0]

    def _getHtmlTemplate(self):
        if self._getBlueprintType() == BlueprintTypes.NATIONAL:
            return self._HTML_TEMPLATE_NATIONAL
        return self._HTML_TEMPLATE


class VehicleBlueprintBonus(SimpleBonus):
    _HTML_TEMPLATE = b'vehicleBlueprints'

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(VehicleBlueprintBonus, self).__init__(name, value, isCompensation, ctx)
        if self._isFinalFragment():
            self._name = b'finalBlueprints'
        return

    def getBlueprintName(self):
        if self._isFinalFragment():
            return BlueprintsBonusSubtypes.FINAL_FRAGMENT
        return BlueprintsBonusSubtypes.VEHICLE_FRAGMENT

    def getBlueprintSpecialAlias(self):
        if self._isFinalFragment():
            return TOOLTIPS_CONSTANTS.BLUEPRINT_INFO
        return TOOLTIPS_CONSTANTS.BLUEPRINT_FRAGMENT_INFO

    def getBlueprintSpecialArgs(self):
        return self._getFragmentCD()

    def formatBlueprintValue(self):
        return text_styles.neutral(self.itemsCache.items.getItemByCD(self._getFragmentCD()).shortUserName)

    def getImageCategory(self):
        if self._isFinalFragment():
            return b'vehicle_complete'
        return b'vehicle'

    def getImage(self, size=b'big'):
        return RES_ICONS.getBlueprintFragment(size, self.getImageCategory())

    def getIconResource(self, size):
        iconR = R.images.gui.maps.icons.blueprints.fragment.dyn(size).dyn(self.getImageCategory())
        if iconR:
            return iconR()
        return R.images.gui.maps.icons.quests.bonuses.dyn(size).default()

    def getCount(self):
        return self._value[1]

    def getTooltip(self):
        return b''

    def getWrappedLootBoxesBonusList(self):
        return [
         {b'id': (self.getBlueprintSpecialArgs()), 
            b'type': (self._getWrapperType()), 
            b'value': (self.getCount()), 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getImage(size=b'small')), (AWARDS_SIZES.BIG): (self.getImage())}, 
            b'name': (self.getBlueprintTooltipName()), 
            b'description': (self._getDescription())}]

    def _getWrappedBonusList(self):
        result = []
        result.append({b'id': (self._getFragmentCD()), 
           b'type': ((b'custom/{}').format(self.getName())), 
           b'value': (self.getCount()), 
           b'icon': {(AWARDS_SIZES.SMALL): (self.getImage()), (AWARDS_SIZES.BIG): (self.getImage())}, 
           b'name': (self.getBlueprintTooltipName()), 
           b'description': (self._getDescription())})
        return result

    def canPacked(self):
        return False

    def getBlueprintTooltipName(self):
        return backport.text(R.strings.tooltips.blueprint.VehicleBlueprintTooltip.header())

    def _getDescription(self):
        return backport.text(R.strings.tooltips.blueprint.VehicleBlueprintTooltip.descriptionFirst())

    def _getFragmentCD(self):
        return self._value[0]

    def _getFormattedMessage(self, styleSubset, formattedValue):
        vehicleName = self.itemsCache.items.getItemByCD(self._getFragmentCD()).shortUserName
        return makeHtmlString((b'html_templates:lobby/quests/{}').format(styleSubset), self._HTML_TEMPLATE, {b'vehicleName': vehicleName, b'value': formattedValue})

    def _format(self, styleSubset):
        formattedValue = str(self.getValue()[1])
        text = b''
        if formattedValue is not None:
            text = self._getFormattedMessage(styleSubset, formattedValue)
        return text

    def _isFinalFragment(self):
        level = self.itemsCache.items.getItemByCD(self._getFragmentCD()).level
        filledCount, totalCount = self.itemsCache.items.blueprints.getBlueprintCount(self._getFragmentCD(), level)
        if filledCount == totalCount:
            return True
        return False

    def _getWrapperType(self):
        return ItemPackType.BLUEPRINT


class IntelligenceBlueprintBonus(VehicleBlueprintBonus):
    _HTML_TEMPLATE = b'universalBlueprints'

    def getBlueprintName(self):
        return BlueprintsBonusSubtypes.UNIVERSAL_FRAGMENT

    def getBlueprintSpecialArgs(self):
        return int(makeIntelligenceCD(self._getFragmentCD()))

    def getImageCategory(self):
        return b'intelligence'

    def getBlueprintSpecialAlias(self):
        return TOOLTIPS_CONSTANTS.BLUEPRINT_FRAGMENT_INFO

    def formatBlueprintValue(self):
        return b''

    def canPacked(self):
        return self._ctx.get(b'isPacked', False) and self.getCount() > 1

    def getBlueprintTooltipName(self):
        return backport.text(R.strings.tooltips.blueprint.BlueprintFragmentTooltip.intelFragment())

    def _getDescription(self):
        return backport.text(R.strings.tooltips.blueprint.BlueprintFragmentTooltip.intelDescription())

    def _getFormattedMessage(self, styleSubset, formattedValue):
        return makeHtmlString((b'html_templates:lobby/quests/{}').format(styleSubset), self._HTML_TEMPLATE, {b'value': formattedValue})

    def _isFinalFragment(self):
        return False

    def _getWrapperType(self):
        return ItemPackType.BLUEPRINT_INTELEGENCE_DATA


class NationalBlueprintBonus(VehicleBlueprintBonus):
    _HTML_TEMPLATE = b'nationBlueprints'

    def getBlueprintName(self):
        return BlueprintsBonusSubtypes.NATION_FRAGMENT

    def getBlueprintSpecialArgs(self):
        return int(makeNationalCD(self._getFragmentCD()))

    def getImageCategory(self):
        import nations
        return nations.NAMES[self.__getNationID()]

    def getBlueprintSpecialAlias(self):
        return TOOLTIPS_CONSTANTS.BLUEPRINT_FRAGMENT_INFO

    def formatBlueprintValue(self):
        return b''

    def canPacked(self):
        return self._ctx.get(b'isPacked', False) and self.getCount() > 1

    def getBlueprintTooltipName(self):
        return i18n.makeString(TOOLTIPS.BLUEPRINT_BLUEPRINTFRAGMENTTOOLTIP_NATIONALFRAGMENT)

    def getLightViewModelData(self):
        return (
         self.getName() + b'_' + self.getImageCategory(),)

    def _getDescription(self):
        return i18n.makeString(TOOLTIPS.BLUEPRINT_BLUEPRINTFRAGMENTTOOLTIP_NATIONALDESCRIPTION, nation=self._localizedNationName())

    def _localizedNationName(self):
        nationID = self.__getNationID()
        return backport.text(R.strings.nations.dyn(NAMES[nationID]).genetiveCase())

    def _getFormattedMessage(self, styleSubset, formattedValue):
        return makeHtmlString((b'html_templates:lobby/quests/{}').format(styleSubset), self._HTML_TEMPLATE, {b'nationName': (self._localizedNationName()), b'value': formattedValue})

    def _isFinalFragment(self):
        return False

    def __getNationID(self):
        return getFragmentNationID(self._getFragmentCD())

    def _getWrapperType(self):
        return ItemPackType.BLUEPRINT_NATIONAL


class CrewSkinsBonus(SimpleBonus):

    def getItems(self):
        if self._value is None:
            return []
        else:
            getItem = self.itemsCache.items.getCrewSkin
            result = []
            crewSkinID = self._value.get(b'id', NO_CREW_SKIN_ID)
            count = self._value.get(b'count', 0)
            customCompensation = self._value.get(b'customCompensation', None)
            compensatedNumber = self._value.get(b'compensatedNumber', None)
            if crewSkinID != NO_CREW_SKIN_ID and (count > 0 or customCompensation is not None):
                crewSkinItem = getItem(crewSkinID)
                if crewSkinItem is not None:
                    if customCompensation is not None and compensatedNumber is not None:
                        customCompensation = (
                         customCompensation,)
                    if compensatedNumber > 0:
                        result.append((
                         crewSkinItem,
                         0,
                         customCompensation,
                         compensatedNumber))
                    if count > 0:
                        result.append((
                         crewSkinItem,
                         count,
                         None,
                         0))
            return result

    def getCount(self):
        return sum(v[1] for v in self.getItems())

    def format(self):
        return (b', ').join(self.formattedList())

    def formattedList(self):
        sortedByRarity = {}
        for item, count, _, _ in self.getItems():
            if count:
                rarity = item.getRarity()
                totalCount = sortedByRarity.setdefault(rarity, 0)
                sortedByRarity[rarity] = totalCount + count

        result = []
        for rarity, count in sortedByRarity.iteritems():
            result.append(makeHtmlString(b'html_templates:lobby/quests/bonuses', b'crewSkin', {b'value': count, b'rarity': (str(rarity))}))

        return result

    def _getWrappedBonusList(self):
        result = []
        for item, count, _, _ in self.getItems():
            if item is not None:
                resourceID = str(item.itemTypeName + str(item.getRarity()))
                result.append({b'id': (item.intCD), 
                   b'name': (localizedFullName(item)), 
                   b'description': (item.getDescription()), 
                   b'type': ((b'item/{}').format(item.itemTypeName)), 
                   b'value': count, 
                   b'icon': {(AWARDS_SIZES.SMALL): (backport.image(R.images.gui.maps.icons.quests.bonuses.small.dyn(resourceID)())), 
                             (AWARDS_SIZES.BIG): (backport.image(R.images.gui.maps.icons.quests.bonuses.big.dyn(resourceID)()))}})

        return result

    def compensation(self, compensatedNumber, customCompensation, bonus):
        bonuses = []
        if compensatedNumber > 0 and customCompensation is not None:
            money = Money(*customCompensation)
            currencies = money.getSetCurrencies(byWeight=True)
            for currency in currencies:
                cls = _BONUSES.get(currency)
                bonuses.append(cls(currency, money.get(currency=currency), isCompensation=True, compensationReason=bonus))

        return bonuses

    def __getCommonAwardsVOs(self, item, count, iconSize=b'small', align=TEXT_ALIGN.RIGHT, withCounts=False):
        itemInfo = {b'imgSource': (item.getBonusIcon(iconSize)), 
           b'label': (text_styles.stats((b'x{}').format(count))), 
           b'align': align, 
           b'isSpecial': True, 
           b'specialArgs': [
                          item.id], 
           b'specialAlias': (TOOLTIPS_CONSTANTS.CREW_SKIN)}
        if withCounts:
            itemInfo[b'count'] = count
        return itemInfo


class CrewBooksBonus(SimpleBonus):

    def getItems(self):
        if self._value is None:
            return []
        else:
            getItem = self.itemsCache.items.getItemByCD
            result = []
            for crewBookCD, count in self._value.iteritems():
                crewBookItem = getItem(crewBookCD)
                if crewBookItem is not None:
                    result.append((
                     crewBookItem,
                     count))

            return sorted(result, (lambda x, y: orderCmp(x[0], y[0])))

    def format(self):
        return (b', ').join(self.formattedList())

    def formattedList(self):
        result = []
        for item, count in self.getItems():
            result.append(makeHtmlString(b'html_templates:lobby/quests/bonuses', b'crewBook', {b'type': (item.getBookType()), b'nation': (item.getNation()), b'value': count, b'name': (item.userName)}))

        return result

    def getCount(self):
        return sum(v[1] for v in self.getItems())

    def _getWrappedBonusList(self):
        result = []
        for item, count in self.getItems():
            if item is not None:
                result.append({b'id': (item.intCD), 
                   b'type': ((b'crew_book/{}').format(item.getBookType())), 
                   b'value': count, 
                   b'icon': {(AWARDS_SIZES.SMALL): (item.getShopIcon(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (item.getShopIcon(AWARDS_SIZES.BIG))}, 
                   b'name': (item.userName), 
                   b'description': (item.fullDescription)})

        return result

    def wrapToItemsPack(self, groupID=1):
        pack = []
        for crewbook, count in self.getItems():
            type_ = getItemPackByGroupAndName(ItemPackTypeGroup.CREW_BOOKS, crewbook.getBookType())
            pack.append(ItemPackEntry(type=type_, count=count, id=crewbook.intCDO.intCompactDescr, groupID=groupID))

        return pack

    def getLightViewModelData(self):
        return (
         self.getItems()[0][0].icon,)

    def getWrappedLootBoxesBonusList(self):
        result = []
        icons = R.images.gui.maps.icons.crewBooks.books
        for item, count in self.getItems():
            if item is not None:
                if item.isCommon():
                    iconSmall = icons.big.brochure_random()
                    iconBig = icons.s600x450.brochure_random()
                else:
                    resName = getIconResourceName(item.icon)
                    iconSmall = icons.small.dyn(resName)()
                    iconBig = icons.s600x450.dyn(resName)()
                result.append({b'id': (item.intCD), 
                   b'type': ((b'crew_book/{}').format(item.getBookType())), 
                   b'value': count, 
                   b'icon': {(AWARDS_SIZES.SMALL): (backport.image(iconSmall) if iconSmall != INVALID_RES_ID else b''), 
                             (AWARDS_SIZES.BIG): (backport.image(iconBig) if iconBig != INVALID_RES_ID else b'')}, 
                   b'name': (item.userName), 
                   b'description': (item.fullDescription)})

        return result

    def __getCommonAwardsVOs(self, item, count, iconSize=b'small', align=TEXT_ALIGN.RIGHT, withCounts=False):
        itemInfo = {b'imgSource': (item.getBonusIcon(iconSize)), 
           b'label': (text_styles.stats((b'x{}').format(count))), 
           b'align': align, 
           b'isSpecial': True, 
           b'specialArgs': [
                          item.id], 
           b'specialAlias': None}
        if withCounts:
            itemInfo[b'count'] = count
        return itemInfo


class BattlePassPointsBonus(SimpleBonus):

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (self.getIconBySize(AWARDS_SIZES.SMALL))}]

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.hightlight(self.__getValueSum())

    def getCount(self):
        return self.__getValueSum()

    def formatValue(self):
        if self.__getValueSum():
            return backport.getIntegralFormat(self.__getValueSum())
        else:
            return

    def getIconBySize(self, size):
        res = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(self.getName())
        if res.exists():
            return backport.image(res())
        else:
            return

    def getWrappedEpicBonusList(self):
        awardItem = R.strings.tooltips.awardItem.dyn(self._name)
        return [
         {b'id': 0, 
            b'type': ((b'custom/{}').format(self.getName())), 
            b'value': (self.__getValueSum()), 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
            b'name': (backport.text(awardItem.header()) if awardItem else b''), 
            b'description': (backport.text(awardItem.body()) if awardItem else b'')}]

    def __getCommonAwardsVOs(self, iconSize=b'small', align=TEXT_ALIGN.CENTER, withCounts=False):
        itemInfo = {b'imgSource': (self.getIconBySize(iconSize)), 
           b'label': (self.getIconLabel()), 
           b'align': align, 
           b'isSpecial': True, 
           b'specialAlias': (TOOLTIPS_CONSTANTS.BATTLE_PASS_POINTS), 
           b'specialArgs': None}
        if withCounts:
            itemInfo[b'count'] = self.__getValueSum()
        return itemInfo

    def __getValueSum(self):
        vehiclePoints = self._value.get(b'vehicles')
        if vehiclePoints is not None:
            return sum(points for points in vehiclePoints.itervalues())
        else:
            return 0


class EpicAbilityPtsBonus(IntegralBonus):
    pass


class ItemsBonusFactory(object):
    CREW_BOOKS_BONUS_CLASS = CrewBooksBonus
    ITEMS_BONUS_CLASS = ItemsBonus

    def __call__(self, name, value, isCompensation=False, ctx=None):
        itemBonusesDict = {}
        crewBooksBonusesDict = {}
        itemBonuses = []
        for intCD, count in value.iteritems():
            itemTypeID, _, _ = vehicles.parseIntCompactDescr(intCD)
            bonusesDict = crewBooksBonusesDict if itemTypeID == GUI_ITEM_TYPE.CREW_BOOKS else itemBonusesDict
            bonusesDict[intCD] = count

        if crewBooksBonusesDict:
            itemBonuses.append(self.CREW_BOOKS_BONUS_CLASS(b'crewBooks', crewBooksBonusesDict, isCompensation, ctx))
        if itemBonusesDict:
            itemBonuses.append(self.ITEMS_BONUS_CLASS(name, itemBonusesDict, isCompensation, ctx))
        return itemBonuses


class CrewSkinsBonusFactory(object):
    CREW_SKINS_BONUS_CLASS = CrewSkinsBonus

    def __call__(self, name, value, isCompensation=False, ctx=None):
        bonuses = []
        for crewSkinData in value:
            bonuses.append(self.CREW_SKINS_BONUS_CLASS(name=name, value=crewSkinData, isCompensation=isCompensation, ctx=ctx))

        return bonuses


class DogTagComponentBonus(SimpleBonus):
    _DogTagComponentRecord = namedtuple(b'_DogTagComponentRecord', [
     b'componentId', b'unlock', b'value', b'grade'])

    def getDogTagComponents(self):
        if self._value is not None:
            return [self.makeComponentRecord(dogTagInfo) for dogTagInfo in self._value]
        else:
            return []

    def getUnlockedComponents(self):
        if self._value is not None:
            return [self.makeComponentRecord(dogTagInfo) for dogTagInfo in self._value if dogTagInfo.get(b'unlock')]
        else:
            return []

    @classmethod
    def makeComponentRecord(cls, dogTagInfo):
        return cls._DogTagComponentRecord(componentId=dogTagInfo[b'id'], unlock=dogTagInfo.get(b'unlock'), grade=dogTagInfo.get(b'grade', 0), value=dogTagInfo.get(b'value'))

    def getCount(self):
        if self._value is not None:
            return len(self._value)
        else:
            return 0

    def getUnlockedBackgrounds(self):
        if self._value is not None:
            return [self.makeComponentRecord(dogTagInfo) for dogTagInfo in self._value if dogTagInfo.get(b'unlock') and self._checkDogTagType(dogTagInfo[b'id'], ComponentViewType.BACKGROUND)]
        else:
            return []

    def getUnlockedEngravings(self):
        if self._value is not None:
            return [self.makeComponentRecord(dogTagInfo) for dogTagInfo in self._value if dogTagInfo.get(b'unlock') and self._checkDogTagType(dogTagInfo[b'id'], ComponentViewType.ENGRAVING)]
        else:
            return []

    @staticmethod
    def _checkDogTagType(dogTagId, checkType):
        return componentConfigAdapter.getComponentById(dogTagId).viewType == checkType


def _getPreferredMapSlotAwardTexts(slotName):
    awardItem = R.strings.tooltips.awardItem.dyn(slotName)
    if not awardItem:
        return (b'', b'')
    name = backport.text(awardItem.header()) if hasattr(awardItem, b'header') else b''
    if hasattr(awardItem, b'body'):
        description = backport.text(awardItem.body())
    elif hasattr(awardItem, b'body1'):
        description = backport.text(awardItem.body1())
    else:
        description = b''
    return (name, description)


class PreferredMapSlotsBonus(IntegralBonus):

    def __init__(self, *args, **kwargs):
        super(PreferredMapSlotsBonus, self).__init__(*args, **kwargs)
        slotID, day = first(self._value.items())
        self._slotName = getSlotTypeName(slotID).value
        self._value = day
        return

    def getList(self):
        return [
         {b'value': (self.formatValue()), 
            b'itemSource': (self.getIconBySize(AWARDS_SIZES.SMALL)), 
            b'tooltip': (self.getTooltip())}]

    def getSlotName(self):
        return self._slotName

    def getTooltip(self):
        return _getItemTooltip(self._slotName)

    def hasIconFormat(self):
        return True

    def getIconLabel(self):
        return text_styles.hightlight(self.getValue())

    def getIconBySize(self, size):
        iconName = RES_ICONS.getBonusIcon(size, self._slotName)
        if iconName is None:
            return super(PreferredMapSlotsBonus, self).getIconBySize(size)
        else:
            return iconName

    def getWrappedEpicBonusList(self):
        return self.getWrappedLootBoxesBonusList()

    def getWrappedLootBoxesBonusList(self):
        name, description = _getPreferredMapSlotAwardTexts(self._slotName)
        return [
         {b'id': 0, 
            b'type': ((b'custom/{}').format(self._slotName)), 
            b'value': (self.getValue()), 
            b'icon': {(AWARDS_SIZES.SMALL): (self.getIconBySize(AWARDS_SIZES.SMALL)), (AWARDS_SIZES.BIG): (self.getIconBySize(AWARDS_SIZES.BIG))}, 
            b'name': name, 
            b'description': description}]


_BONUSES = {(Currency.CREDITS): CreditsBonus, 
   (Currency.GOLD): GoldBonus, 
   (Currency.CRYSTAL): CrystalBonus, 
   (Currency.EVENT_COIN): EventCoinBonus, 
   (Currency.BPCOIN): BpcoinBonus, 
   (Currency.EQUIP_COIN): EquipCoinBonus, 
   b'strBonus': SimpleBonus, 
   b'groups': GroupsBonus, 
   b'xp': IntegralBonus, 
   b'freeXP': FreeXpBonus, 
   b'tankmenXP': IntegralBonus, 
   b'xpFactor': FloatBonus, 
   b'creditsFactor': FloatBonus, 
   b'freeXPFactor': FloatBonus, 
   b'tankmenXPFactor': FloatBonus, 
   b'dailyXPFactor': FloatBonus, 
   b'slots': CountableIntegralBonus, 
   b'berths': CountableIntegralBonus, 
   (PREMIUM_ENTITLEMENTS.BASIC): BasicPremiumDaysBonus, 
   (PREMIUM_ENTITLEMENTS.PLUS): PlusPremiumDaysBonus, 
   (VehiclesBonus.VEHICLES_BONUS): VehiclesBonus, 
   b'meta': MetaBonus, 
   b'tokens': {b'default': tokensFactory, 
               (_ET.BATTLE_QUEST): tokensFactory, 
               (_ET.TOKEN_QUEST): tokensFactory, 
               (_ET.PERSONAL_QUEST): tokensFactory, 
               (_ET.PERSONAL_MISSION): personalMissionsTokensFactory, 
               (_ET.ELEN_QUEST): tokensFactory}, 
   b'dossier': {b'default': DossierBonus, 
                (_ET.PERSONAL_MISSION): PersonalMissionDossierBonus}, 
   b'tankmen': {b'default': TankmenBonus, 
                (_ET.PERSONAL_MISSION): TankwomanBonus}, 
   b'customizations': CustomizationsBonus, 
   b'goodies': GoodiesBonus, 
   b'items': (ItemsBonusFactory()), 
   b'oneof': BoxBonus, 
   b'badgesGroup': BadgesGroupBonus, 
   b'blueprints': blueprintBonusFactory, 
   b'blueprintsAny': randomBlueprintBonusFactory, 
   b'crewSkins': (CrewSkinsBonusFactory()), 
   b'entitlements': entitlementsFactory, 
   b'rankedDailyBattles': CountableIntegralBonus, 
   b'rankedBonusBattles': CountableIntegralBonus, 
   b'battlePassPoints': BattlePassPointsBonus, 
   b'dogTagComponents': DogTagComponentBonus, 
   b'selectableCrewbook': UniversalCrewbook, 
   b'randomCrewbook': UniversalCrewbook, 
   b'currencies': {b'default': currenciesFactory}, 
   b'subscriptionBonus': subscriptionBonusFactory, 
   b'paragonsUnlocks': ParagonsUnlocksBonus, 
   b'vehicleSelector': SimpleBonus, 
   b'preferredMapSlots': PreferredMapSlotsBonus}
HIDDEN_BONUSES = (
 MetaBonus,)
_BONUSES_PRIORITY = (
 b'tokens',
 b'oneof')
_BONUSES_ORDER = dict((n, idx) for idx, n in enumerate(_BONUSES_PRIORITY))

def compareBonuses(bonusName1, bonusName2):
    if bonusName1 not in _BONUSES_ORDER and bonusName2 not in _BONUSES_ORDER:
        return cmp(bonusName1, bonusName2)
    if bonusName1 not in _BONUSES_ORDER:
        return 1
    if bonusName2 not in _BONUSES_ORDER:
        return -1
    return _BONUSES_ORDER[bonusName1] - _BONUSES_ORDER[bonusName2]


def _getFromTree(tree, path):
    if not tree or not path:
        return
    key = path[0]
    subTree = None
    if key in tree:
        subTree = tree[key]
    elif b'default' in tree:
        subTree = tree[b'default']
    if isinstance(subTree, dict):
        return _getFromTree(subTree, path[1:])
    else:
        return subTree


def _initFromTree(key, name, value, isCompensation=False, ctx=None):
    factory = _getFromTree(_BONUSES, key)
    if factory is not None:
        result = factory(name, value, isCompensation, ctx)
        if result is not None:
            if not isinstance(result, list):
                return [result]
            return result
    return []


def getBonuses(quest, name, value, isCompensation=False, ctx=None):
    questType = quest.getType()
    key = [name, questType]
    ctx = ctx or {}
    if questType in (_ET.BATTLE_QUEST, _ET.TOKEN_QUEST, _ET.PERSONAL_QUEST) and name == b'tokens':
        parentsName = quest.getParentsName()
        for n, v in value.iteritems():
            if n in parentsName:
                questNames = parentsName[n]
                if questNames:
                    v.update({b'questNames': questNames})

    elif questType == _ET.PERSONAL_MISSION:
        ctx.update({b'operationID': (quest.getOperationID()), 
           b'chainID': (quest.getChainID()), 
           b'campaignID': (quest.getCampaignID()), 
           b'areTokensPawned': False})
    return _initFromTree(key, name, value, isCompensation, ctx=ctx)


def getServiceBonuses(name, value, isCompensation=False):
    return _initFromTree((name, b'default'), name, value, isCompensation)


def getTutorialBonuses(name, value):
    if name == b'dossier':
        key = (
         name, b'default')
    else:
        key = (
         name,)
    return _initFromTree(key, name, value)


def getEventBoardsBonusObj(name, value):
    return _initFromTree((name, _ET.ELEN_QUEST), name, value)


def getNonQuestBonuses(name, value, ctx=None):
    if name == b'preferredMapSlots' and isinstance(value, dict) and len(value) > 1:
        bonuses = []
        for slotID, slotDurationDays in value.iteritems():
            bonuses.extend(_initFromTree((name, b'default'), name, {slotID: slotDurationDays}, ctx=ctx))

        return bonuses
    return _initFromTree((name, b'default'), name, value, ctx=ctx)


def getOfferBonuses(name, value, ctx=None):
    from account_helpers.offers.offer_bonuses import OfferBonusAdapter, OFFER_BONUSES
    offerBonuses = []
    isCompensation = False
    offerBonusFactory = _getFromTree(OFFER_BONUSES, (name, b'default'))
    if offerBonusFactory is not None:
        result = offerBonusFactory(name, value, isCompensation, ctx)
        if result is not None:
            offerBonuses = result if isinstance(result, list) else [result]
    else:
        bonuses = getNonQuestBonuses(name, value)
        offerBonuses = [OfferBonusAdapter(bonus) for bonus in bonuses]
    return offerBonuses


def getSimpleTooltipData(name):
    return (
     TOOLTIPS.getAwardHeader(name), TOOLTIPS.getAwardBody(name))


def _getItemTooltip(name):
    data = getSimpleTooltipData(name)
    header = i18n.makeString(data[0])
    body = i18n.makeString(data[1])
    if header or body:
        return makeTooltip(header or None, body or None)
    return b''


def mergeBonuses(bonuses):
    merged = copy.deepcopy(bonuses)
    if len(merged) > 1:
        i = 0
        while i < len(merged) - 1:
            j = i + 1
            while j < len(merged):
                mergFunc = getMergeBonusFunction(merged[i], merged[j])
                if mergFunc and merged[i].getName() == merged[j].getName():
                    merged[i], needPop = mergFunc(merged[i], merged[j])
                    if needPop:
                        merged.pop(j)
                    else:
                        j += 1
                else:
                    j += 1

            i += 1

    return merged


def getMergeBonusFunction(lhv, rhv):

    def hasOneBaseClass(l, r, cls):
        return isinstance(l, cls) and isinstance(r, cls)

    def ofSameClassWithBase(l, r, cls):
        return hasOneBaseClass(l, r, cls) and type(l) is type(r)

    if ofSameClassWithBase(lhv, rhv, CrewSkinsBonus) or ofSameClassWithBase(lhv, rhv, CollectionTokenBonus):
        return
    if hasOneBaseClass(lhv, rhv, ItemsBonus):
        return mergeItemsBonuses
    else:
        if hasOneBaseClass(lhv, rhv, CurrenciesBonus):
            return mergeCurrenciesBonus
        if hasOneBaseClass(lhv, rhv, IntegralBonus) or hasOneBaseClass(lhv, rhv, GoldBonus):
            return mergeIntegralBonuses
        if hasOneBaseClass(lhv, rhv, CustomizationsBonus):
            return mergeCustomizationBonuses
        if hasOneBaseClass(lhv, rhv, C11nProgressTokenBonus):
            return
        for predicate, merger in collectClientBonusMergers():
            if predicate(lhv, rhv):
                return merger

        if ofSameClassWithBase(lhv, lhv, SimpleBonus):
            return mergeSimpleBonuses
        return


def mergeItemsBonuses(lhv, rhv):
    merged = copy.deepcopy(lhv)
    for key in merged.getValue():
        if key in rhv.getValue():
            merged.getValue()[key] += rhv.getValue()[key]

    for key, value in rhv.getValue().iteritems():
        if key not in merged.getValue():
            merged.getValue()[key] = value

    return (
     merged, True)


def mergeIntegralBonuses(lhv, rhv):
    merged = copy.deepcopy(lhv)
    merged.setValue(merged.getValue() + rhv.getValue())
    return (merged, True)


def mergeCustomizationBonuses(lhv, rhv):
    merged = copy.deepcopy(lhv)
    mergedValue = merged.getValue()
    for rhvItem in rhv.getValue():
        mergedItem = findFirst((lambda i, ri=rhvItem: i[b'id'] == ri[b'id'] and i[b'custType'] == ri[b'custType']), mergedValue)
        if mergedItem is not None:
            mergedItem[b'value'] += rhvItem[b'value']
        else:
            mergedValue.append(rhvItem)
        merged.setValue(mergedValue)

    return (merged, True)


def mergeCurrenciesBonus(lhv, rhv):
    merged = copy.deepcopy(lhv)
    mergedValue = merged.getValue()
    needPop = False
    if merged.getCode() == rhv.getCode():
        merged.setValue(mergedValue + rhv.getValue())
        needPop = True
    return (merged, needPop)


def mergeSimpleBonuses(lhv, rhv):
    merged = copy.deepcopy(lhv)
    value = merged.getValue()
    needPop = False
    if isinstance(value, tuple):
        lKey, lValue = value
        rKey, rValue = rhv.getValue()
        if lKey == rKey:
            merged.setValue((lKey, lValue + rValue))
            needPop = True
    elif isinstance(value, dict):
        merged.setValue(__mergeDicts(value, rhv.getValue()))
        needPop = True
    return (merged, needPop)


def __mergeDicts(lhv, rhv):
    merged = copy.deepcopy(lhv)
    for key in merged.keys():
        if key in rhv:
            if isinstance(merged[key], dict):
                merged[key] = __mergeDicts(merged[key], rhv[key])
            else:
                merged[key] = merged[key] + rhv[key]

    for key in rhv.keys():
        if key not in merged:
            merged[key] = rhv[key]

    return merged


def getMergedBonusesFromDicts(bonusesList):
    result = {}
    for bonuses in bonusesList:
        for bonusName, bonusValue in bonuses.iteritems():
            if bonusName in BONUS_MERGERS:
                BONUS_MERGERS[bonusName](result, bonusName, bonusValue, False, 1, None)
            else:
                _logger.warning(b'BONUS_MERGERS has not bonus %s', bonusName)

    return result


def splitBonuses(bonuses):
    split = []
    for bonus in bonuses:
        splitFunc = getSplitBonusFunction(bonus)
        if splitFunc:
            split.extend(splitFunc(bonus))
        else:
            split.append(bonus)

    return split


def getSplitBonusFunction(bonus):
    if isinstance(bonus, CrewSkinsBonus):
        return
    else:
        if isinstance(bonus, CustomizationsBonus):
            return splitCustomizationsBonus
        if isinstance(bonus, (IntegralBonus, GoldBonus)):
            return splitIntegralBonuses
        if isinstance(bonus, SimpleBonus):
            return splitSimpleBonuses
        return


def splitIntegralBonuses(bonus):
    return [
     bonus]


def splitSimpleBonuses(bonus):
    split = []
    value = bonus.getValue()
    if isinstance(value, dict):
        for key, sub in value.iteritems():
            item = copy.deepcopy(bonus)
            item.setValue({key: sub})
            split.append(item)

    elif isinstance(value, list):
        for sub in value:
            item = copy.deepcopy(bonus)
            item.setValue([sub])
            split.append(item)

    else:
        split.append(bonus)
    return split


def splitCustomizationsBonus(bonus):
    split = []
    value = bonus.getValue()
    camoItem = None
    for sub in value:
        if sub.get(b'custType', b'') == b'camouflage':
            if camoItem is None:
                camoItem = copy.deepcopy(bonus)
                camoItem.setValue([])
            oldValue = camoItem.getValue()
            oldValue.append(sub)
            camoItem.setValue(oldValue)
        else:
            item = copy.deepcopy(bonus)
            item.setValue([sub])
            split.append(item)

    if camoItem is not None:
        split.append(camoItem)
    return split


def getVehicleCrewReward(vehiclesReward):
    if not vehiclesReward:
        return None
    else:
        _, vehicleInfo = vehiclesReward.getVehicles()[0]
        tmen = [tman for tman in vehicleInfo.get(b'tankmen', [])]
        tmenBonus = TankmenBonus(b'tankmen', tmen)
        return tmenBonus


@dependency.replace_none_kwargs(bmController=IBattleMattersController, taController=ITankAcademyController, winbackController=IWinbackController)
def isDynamicOfferToken(bonusID, bmController=None, taController=None, winbackController=None):
    return bmController.isDelayedRewardToken(bonusID) or taController.isDelayedRewardToken(bonusID) or winbackController.isWinbackOfferToken(bonusID)


def formatBlueprint(bonus, count=None):
    blueprintType = bonus.getBlueprintName()
    if blueprintType == BlueprintsBonusSubtypes.FINAL_FRAGMENT:
        blueprintString = backport.text(R.strings.quests.bonusName.blueprints.any())
    elif blueprintType == BlueprintsBonusSubtypes.UNIVERSAL_FRAGMENT:
        blueprintString = backport.text(R.strings.quests.bonusName.blueprints.universal())
    elif blueprintType == BlueprintsBonusSubtypes.NATION_FRAGMENT:
        nation = backport.text(R.strings.nations.dyn(bonus.getImageCategory(), b'')())
        blueprintString = backport.text(R.strings.quests.bonusName.blueprints.nation(), nationName=nation)
    elif blueprintType == BlueprintsBonusSubtypes.VEHICLE_FRAGMENT:
        blueprintString = backport.text(R.strings.quests.bonusName.blueprints.vehicle.any())
    elif blueprintType == BlueprintsBonusSubtypes.RANDOM_FRAGMENT:
        blueprintString = backport.text(R.strings.quests.bonusName.blueprints.any())
    elif blueprintType == BlueprintsBonusSubtypes.RANDOM_NATIONAL_FRAGMENT:
        blueprintString = backport.text(R.strings.quests.bonusName.blueprints.nation.any())
    else:
        blueprintString = b''
    if count is not None:
        return (b' ').join([blueprintString, str(count)])
    else:
        return blueprintString


def _isSelectableBonusID(bonusID):
    return bonusID.startswith(OFFER_TOKEN_PREFIX) and (any(bonusID.startswith(prefix) for prefix in FEATURE_TO_PREFIX.itervalues()) or isDynamicOfferToken(bonusID))
