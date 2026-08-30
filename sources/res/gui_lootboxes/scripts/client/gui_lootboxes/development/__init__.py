from account_helpers.AccountSettings import LOOT_BOXES_INTRO_SHOWN
from gui.impl.gen import R
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui_lootboxes.development.dev_stat_fetcher import devStat
from gui_lootboxes.gui.shared.event_dispatcher import showRewardScreenWindow
from gui_lootboxes.skeletons.statistic_lootbox_controller import IStatisticLootBoxController
from helpers import dependency
from shared_utils import first
from skeletons.gui.game_control import IGuiLootBoxesController
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.shared import IItemsCache

def _getLootBoxBonusesExample():
    return {b'blueprints': {65523: 10}, b'freeXP': 100000, 
       b'crewSkins': [{b'count': 1, b'id': 2}], b'gold': 100000, 
       b'crystal': 100000, 
       b'dossier': {1: {(b'playerBadges', 105): {b'unique': False, b'type': b'append', b'value': 1}}}, b'items': {27643: 1, 38905: 1, 2590: 1, 14073: 1, 16633: 1, 11769: 1, 507: 10, 15390: 1}, b'vehicles': {59985: {b'noCrew': True, b'customCompensation': (0, 9000), b'compensatedNumber': 1}, 60209: {b'noCrew': True, b'rent': {b'battles': 10}}, 32001: {b'noCrew': True}}, b'customizations': [{b'custType': b'camouflage', b'id': 15400, b'value': 1}, {b'custType': b'decal', b'id': 15574, b'value': 1}, {b'custType': b'paint', b'id': 128, b'value': 1}, {b'custType': b'projection_decal', b'id': 564, b'value': 1}, {b'custType': b'style', b'id': 62, b'value': 1}, {b'custType': b'style', b'id': 434, b'value': 1}, {b'custType': b'decal', b'id': 14580, b'value': 1}], b'dogTagComponents': [{b'unlock': True, b'id': 600, b'value': 0.0}], b'premium_plus': 1, 
       b'tokens': {b'tman_template:::men1::::brotherhood::base:': {b'count': 1, b'expires': {b'at': 4104777660L}}, b'battle_bonus_x5': {b'count': 1, b'expires': {b'at': 2524608000L}}}, b'credits': 100000, b'slots': 5, b'goodies': {121001: {b'count': 3}, 12852: {b'count': 5}, 13461: {b'count': 1}}}


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def printAllLootBoxes(itemsCache=None):
    import pprint
    pprint.pprint(sorted(itemsCache.items.tokens.getLootBoxes().values()))
    return


@dependency.replace_none_kwargs(guiLoader=IGuiLoader)
def getStorageViewInstance(guiLoader=None):
    return first(guiLoader.windowsManager.findViews((lambda v: v.layoutID == R.views.gui_lootboxes.lobby.gui_lootboxes.StorageView())))


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def devShowRewardScreenWindow(bonuses=None, itemsCache=None, mainReward=b'vehicle'):
    if bonuses == b'example':
        bonuses = _getLootBoxBonusesExample()
    elif bonuses == b'example2':
        bonuses = {b'tokens': {b'lb_comp:credits:1000:cllc:31001': {b'count': 1, b'expires': {b'at': 0}, b'limit': 0}}, b'preferredMapSlots': {3: 3}, b'vehicles': [
                       {(itemsCache.items.getItem(GUI_ITEM_TYPE.VEHICLE, 0, 144).intCD): {b'customCompensation': (0, 10550), 
                                                                                            b'compensatedNumber': 1}}]}
    elif bonuses is None:
        bonuses = {b'premium_plus': 2, b'gold': 750, 
           b'credits': 100000, 
           b'crystal': 500, 
           b'freeXP': 5000, 
           b'items': {27131: 20, 12025: 1, 27643: 10, 22009: 1, 27387: 10}, b'dossier': {1: {(b'singleAchievements', b'hw2019Medal'): {b'value': 1, 
                                                                      b'unique': True, 
                                                                      b'type': b'set'}}}, 
           b'tokens': {b'lb_comp:credits:1000:cllc:31001': {b'count': 1, b'expires': {b'at': 0}, b'limit': 0}}, b'entitlements': {b'cllc_item_31001_1': {b'count': 1, b'expires': 0}}, b'vehicles': [
                       {(itemsCache.items.getItem(GUI_ITEM_TYPE.VEHICLE, 0, 144).intCD): {b'customCompensation': (0, 10550), 
                                                                                            b'compensatedNumber': 1}}]}
        if mainReward == b'vehicle':
            bonuses[b'vehicles'] = [{(itemsCache.items.getItem(GUI_ITEM_TYPE.VEHICLE, 0, 144).intCD): {}}]
        elif mainReward == b'customization':
            bonuses[b'customizations'] = [{b'custType': b'style', b'id': 31013, b'value': 1}]
        elif mainReward == b'cllc':
            bonuses[b'entitlements'] = {b'cllc_item_31001_1': {b'count': 1, b'expires': 0}}
        if mainReward == b'tankmen':
            bonuses[b'tokens'] = {b'tman_template:::tankmen_bp10_3:210060:::brotherhood!commander_sixthSense::tankmen_bp10_3:commander': {b'count': 1, 
                                                                                                                       b'expires': {b'at': 0}, b'limit': 0}}
        elif mainReward == b'vehicleCompensation':
            bonuses[b'vehicles'] = [
             {(itemsCache.items.getItem(GUI_ITEM_TYPE.VEHICLE, 0, 144).intCD): {b'customCompensation': (0, 10550), 
                                                                                  b'compensatedNumber': 1}}]
            bonuses[b'gold'] += 10550
        elif mainReward == b'customizationCompensation':
            bonuses[b'customizations'] = [{b'custType': b'style', b'id': 31013, b'value': 1, b'customCompensation': (0, 10550)}]
            bonuses[b'gold'] += 10550
    lootbox = first(itemsCache.items.tokens.getLootBoxes().values())
    showRewardScreenWindow([bonuses], lootbox)
    return


@dependency.replace_none_kwargs(guiLootBoxesCtrl=IGuiLootBoxesController)
def getGuiLootBoxesCtr(guiLootBoxesCtrl=None):
    return guiLootBoxesCtrl


@dependency.replace_none_kwargs(guiLootBoxesCtrl=IGuiLootBoxesController)
def devResetLootBoxesIntro(guiLootBoxesCtrl=None):
    guiLootBoxesCtrl.setSetting(LOOT_BOXES_INTRO_SHOWN, False)
    return


@dependency.replace_none_kwargs(statLootBoxCtrl=IStatisticLootBoxController)
def getStatisticCtrl(statLootBoxCtrl=None):
    return statLootBoxCtrl


def initDevStat():
    devStat()
    return
