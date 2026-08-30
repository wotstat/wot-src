from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.lootbox_system.base.bonuses_packers import mergeNeededBonuses, processCompensationsWithLootbox
from gui.lootbox_system.base.common import ViewID, Views
from gui.server_events.awards_formatters import AWARDS_SIZES
from helpers import dependency
from skeletons.gui.game_control import ILootBoxSystemController
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.shared import IItemsCache
from web.web_client_api import Field, W2CSchema, WebCommandException, w2c, w2capi
from web.web_client_api.common import ItemPackType, ItemPackTypeGroup, sanitizeResPath

class ViewsIDs(object):
    OVERLAY = b'overlay'
    SHOP = b'shop'
    ALL = (OVERLAY, SHOP)


def _isValidViewID(_, data):
    viewID = data.get(b'view_id')
    if viewID in ViewsIDs.ALL:
        return True
    raise WebCommandException((b'viewID: "{}" is not supported').format(viewID))
    return


class _LootBoxInfo(W2CSchema):
    id = Field(required=True, type=int)
    full_info = Field(type=bool, default=False)


class _ShowViewSchema(W2CSchema):
    id = Field(required=True, type=int)
    view_id = Field(required=False, type=basestring, validator=_isValidViewID)


class _ShowInfoSchema(W2CSchema):
    view_id = Field(required=False, type=basestring, validator=_isValidViewID)
    box_id = Field(required=True, type=int)


@w2capi(name=b'loot_box_system', key=b'action')
class LootBoxSystemWebApi(object):
    __lootBoxes = dependency.descriptor(ILootBoxSystemController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __guiLoader = dependency.descriptor(IGuiLoader)

    @w2c(_LootBoxInfo, b'get_loot_box_info')
    def getLootBoxInfo(self, cmd):
        result = dict()
        lootBox = self.__itemsCache.items.tokens.getLootBoxByID(cmd.id)
        if lootBox is not None:
            guaranteedFrequency = lootBox.getGuaranteedFrequency()
            attemptsAfterReward = self.__itemsCache.items.tokens.getAttemptsAfterGuaranteedRewards(lootBox)
            result[b'guaranteed_bonus_limit'] = guaranteedFrequency
            result[b'max_attempts_to_guaranteed_bonus'] = guaranteedFrequency - attemptsAfterReward
            result[b'category'] = lootBox.getCategory()
            result[b'slots'] = self.__addBonusesInfo(self.__lootBoxes.getBoxInfo(cmd.id).get(b'slots', {}), lootBox.getType(), cmd.full_info)
        return result

    @w2c(_ShowViewSchema, b'show_box')
    def showBox(self, cmd):
        box = self.__itemsCache.items.tokens.getLootBoxByID(cmd.id)
        category = box.getCategory()
        eventName = box.getType()
        if cmd.view_id == ViewsIDs.OVERLAY or cmd.view_id == ViewsIDs.SHOP:
            Views.load(ViewID.MAIN, subViewID=None, category=category, eventName=eventName)
        return

    @w2c(_ShowInfoSchema, b'show_info_page')
    def showInfoPage(self, cmd):
        box = self.__itemsCache.items.tokens.getLootBoxByID(cmd.box_id)
        eventName = box.getType()
        Views.load(ViewID.INFO, eventName=eventName)
        return

    def __addBonusesInfo(self, slotsInfo, eventName, fullInfo):
        result = {}
        for idx, slotData in slotsInfo.iteritems():
            bonuses = mergeNeededBonuses(slotData.get(b'bonuses', []), eventName)
            bonuses = processCompensationsWithLootbox(bonuses, eventName, showLootboxCompensation=False)
            result.update({idx: {b'probability': (int(slotData.get(b'probability', [0])[0] * 10000 + 1e-06) / 100.0), 
                     b'bonuses': []}})
            for bonus in bonuses:
                bonusList = bonus.getWrappedLootBoxesBonusList()
                for bonusEntry in bonusList:
                    if not self.__isExistingBonus(bonusEntry, result[idx][b'bonuses'], fullInfo):
                        bonusEntry[b'icon'] = {size: sanitizeResPath(path) for size, path in bonusEntry[b'icon'].iteritems()}
                        result[idx][b'bonuses'].append(bonusEntry)
                        if bonusEntry.get(b'overlayIcon') is not None:
                            bonusEntry[b'overlayIcon'] = {size: sanitizeResPath(path) for size, path in bonusEntry[b'overlayIcon'].iteritems()}

        return result

    @staticmethod
    def __isExistingBonus(bonusEntry, bonuses, fullInfo):
        if bonusEntry[b'type'] in ItemPackTypeGroup.VEHICLE:
            if fullInfo:
                return bonusEntry[b'id'] in (b[b'id'] for b in bonuses)
            bonusEntry[b'type'] = ItemPackType.VEHICLE
            for size in AWARDS_SIZES.ALL():
                bonusEntry[b'icon'][size] = RES_ICONS.getVehicleAwardIcon(size)

        return bonusEntry[b'type'] in (b[b'type'] for b in bonuses)
