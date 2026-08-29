import logging
from collections import namedtuple
import resource_helper
_logger = logging.getLogger(__name__)
BONUSES_CONFIG_PATH = b'gui_lootboxes/gui/bonuses_gui_config.xml'
BONUSES_CONFIG_PATH_LIST = [BONUSES_CONFIG_PATH]

class BonusesSortTags(object):
    UNSORTABLE = b'unsortable'
    VEHICLE = b'vehicle'
    UNIQUE_CUSTOMIZATION = b'uniqueCustomization'
    RARITY_OPT_DEV = b'rarityOptionalDevice'
    RARITY_CURRENCY = b'rarityCurrency'
    PREMIUM = b'premium'
    UNIQUE_TANKMEN = b'uniqueTankmen'
    TANKMEN = b'tankmen'
    STYLE = b'style'
    LB_STYLE_PROGRESS = b'lbStyleProgress'
    PERSONAL_BOOSTER = b'personalBooster'
    CREW_BOOK = b'crewBook'
    CURRENCY = b'ordinaryCurrency'
    OPT_DEV = b'optionalDevice'
    EQUIPMENT = b'equipment'
    BATTLE_BOOSTER = b'battleBooster'
    CUSTOMIZATION = b'customization'
    SLOT = b'slot'
    BERTH = b'berth'
    BLUEPRINT = b'blueprint'
    NARRATIVE_CLLC_ITEM = b'narrativeCollectionItem'
    CLLC_ITEM_COMP = b'collectionItemCompensation'
    CUSTOM_LOOTBOX = b'customLootBox'
    CUSTOM_LOOTBOXKEY = b'customLootBoxKey'
    CUSTOM_CURRENCY = b'customCurrency'
    RANGE = (
     UNSORTABLE, VEHICLE, UNIQUE_CUSTOMIZATION, RARITY_OPT_DEV, RARITY_CURRENCY, PREMIUM, UNIQUE_TANKMEN,
     TANKMEN, STYLE, LB_STYLE_PROGRESS, PERSONAL_BOOSTER, CREW_BOOK, CURRENCY, CUSTOM_CURRENCY,
     OPT_DEV, EQUIPMENT, BATTLE_BOOSTER, CUSTOMIZATION, SLOT, BERTH, BLUEPRINT, NARRATIVE_CLLC_ITEM,
     CLLC_ITEM_COMP, CUSTOM_LOOTBOX, CUSTOM_LOOTBOXKEY)


BonusesConfig = namedtuple(b'BonusesConfig', [b'orders', b'defaultOrder'])

def readConfig(pathList):
    finalOrders = {}
    defaultOrder = tuple(v for v in BonusesSortTags.RANGE)
    for path in pathList:
        orders, default = _readConfig(path)
        finalOrders.update(orders)
        if default:
            defaultOrder = default

    return BonusesConfig(finalOrders, defaultOrder)


def _readConfig(path):
    orders = {}
    defaultOrder = tuple()
    tags = set()
    ctx, root = resource_helper.getRoot(path)
    if not root:
        _logger.error(b'bonuses gui config not found. Path %s', path)
        return (
         orders, None)
    else:
        for _, tag in resource_helper.getIterator(ctx, root[b'bonusTags']):
            tags.add(tag.name)

        for _, order in resource_helper.getIterator(ctx, root[b'orders']):
            orderTags = _readOrder(ctx, order, tags)
            if order.name == b'default':
                defaultOrder = orderTags
            elif orderTags is not None:
                for category in resource_helper.readStringItem(ctx, order[b'categories']).value.split():
                    orders[category] = orderTags

        return (
         orders, defaultOrder)


def _readOrder(ctx, order, tags):
    res = []
    for _, tag in resource_helper.getIterator(ctx, order):
        if tag.name == b'categories':
            continue
        if tag.name not in tags:
            _logger.error(b'tag %s in order %s not in tags set', tag.name, order.name)
            return None
        res.append(tag.name)

    for tag in BonusesSortTags.RANGE:
        if tag not in res:
            res.append(tag)

    return tuple(res)
