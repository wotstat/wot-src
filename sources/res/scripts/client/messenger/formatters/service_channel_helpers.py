import typing, logging
from collections import namedtuple
from gui.collection.collections_constants import COLLECTION_ITEM_PREFIX_NAME
from gui.server_events.bonuses import BattleTokensBonus
from items import makeIntCompactDescrByID
from optional_bonuses import BONUS_MERGERS
from skeletons.gui.shared import IItemsCache
from items.components.c11n_constants import CustomizationNamesToTypes
from helpers import dependency
from messenger import g_settings
_logger = logging.getLogger(__name__)
EOL = b'\n'
DEFAULT_MESSAGE = b'defaultMessage'
if typing.TYPE_CHECKING:
    from messenger.proto.bw.wrappers import ServiceChannelMessage
MessageData = namedtuple(b'MessageData', b'data, settings')

def getRewardsForBoxes(message, boxIDs):
    data = message.data or {}
    resultRewards = {}
    for boxID in boxIDs:
        mergeRewards(resultRewards, data[boxID][b'rewards'])

    return resultRewards


def getRewardsForQuests(message, questIDs):
    data = message.data or {}
    detailRewards = data.get(b'detailedRewards', {})
    resultRewards = {}
    for questID, rewards in detailRewards.items():
        if questID in questIDs:
            mergeRewards(resultRewards, rewards)

    return resultRewards


def mergeRewards(resultRewards, rewards):
    for bonusName, bonusValue in rewards.items():
        if bonusName in BONUS_MERGERS:
            BONUS_MERGERS[bonusName](resultRewards, bonusName, bonusValue, False, 1, None)
        elif bonusName == b'selectableCrewbook':
            _mergeSelectableCrewbook(resultRewards, bonusName, bonusValue)
        else:
            _logger.warning(b'BONUS_MERGERS has not bonus %s', bonusName)

    return


def _mergeSelectableCrewbook(resultRewards, bonusName, bonusValue):
    selectablesTotal = resultRewards.setdefault(bonusName, {})
    for item in bonusValue:
        selectablesTotal[item[b'itemName']] = item[b'count']

    return


def getCustomizationItem(itemId, customizationName):
    itemsCache = dependency.instance(IItemsCache)
    customizationType = CustomizationNamesToTypes.get(customizationName.upper())
    if customizationType is None:
        _logger.warning(b'Wrong customization name: %s', customizationName)
    compactDescr = makeIntCompactDescrByID(b'customizationItem', customizationType, itemId)
    return itemsCache.items.getItemByCD(compactDescr)


def getCustomizationItemData(itemId, customizationName):
    item = getCustomizationItem(itemId, customizationName)
    itemName = item.userName
    itemTypeName = item.itemFullTypeName
    return _CustomizationItemData(itemTypeName, itemName)


_CustomizationItemData = namedtuple(b'_CustomizationItemData', (b'guiItemType', b'userName'))

def getDefaultMessage(normal=b'', bold=b''):
    return g_settings.msgTemplates.format(DEFAULT_MESSAGE, {b'normal': normal, b'bold': bold})


def popCollectionEntitlements(rewards):
    entitlements = {name: data for name, data in rewards[b'entitlements'].iteritems() if name.startswith(COLLECTION_ITEM_PREFIX_NAME)} if b'entitlements' in rewards else {}
    for eName in entitlements.iterkeys():
        rewards[b'entitlements'].pop(eName)

    return entitlements


def parseTokenBonusCount(bonus, tokenName):
    if isinstance(bonus, BattleTokensBonus):
        return bonus.getValue().get(tokenName, {}).get(b'count', 0)
    return 0
