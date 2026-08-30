from typing import Dict
from CurrentVehicle import g_currentVehicle
from gui.Scaleform import MENU
from gui.Scaleform.framework.entities.DAAPIDataProvider import DAAPIDataProvider
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.game_control.restore_contoller import getTankmenRestoreInfo
from gui.impl import backport
from gui.server_events import recruit_helper
from gui.shared.formatters import text_styles
from gui.shared.gui_items.Tankman import Tankman, getCrewSkinIconSmall
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.gui_items.crew_skin import localizedFullName
from gui.shared.money import Currency
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData
from gui.shared.tooltips.tankman import getRecoveryStatusText, formatRecoveryLeftValue
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency, i18n
from items.components.crew_skins_constants import NO_CREW_SKIN_ID
from skeletons.gui.game_control import IRestoreController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

def _makeRecoveryPeriodText(restoreInfo):
    price, timeLeft = restoreInfo
    timeStr = formatRecoveryLeftValue(timeLeft)
    if not price.isDefined():
        textStyle = text_styles.main
    elif price.getCurrency() == Currency.GOLD:
        textStyle = text_styles.gold
    else:
        textStyle = text_styles.credits
    return textStyle(timeStr)


def _getTankmanLockMessage(invVehicle):
    if invVehicle.isInBattle:
        return (True, i18n.makeString(b'#menu:tankmen/lockReason/inbattle'))
    if invVehicle.invID == g_currentVehicle.invID and (g_currentVehicle.isInPrebattle() or g_currentVehicle.isInBattle()):
        return (True, i18n.makeString(b'#menu:tankmen/lockReason/prebattle'))
    if invVehicle.isDisabled:
        return (True, i18n.makeString(b'#menu:tankmen/lockReason/disabled'))
    return (False, b'')


@dependency.replace_none_kwargs(itemsCache=IItemsCache, lobbyContext=ILobbyContext)
def _packTankmanData(tankman, itemsCache=None, lobbyContext=None):
    tankmanVehicle = itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)
    if tankman.isInTank:
        vehicle = itemsCache.items.getVehicle(tankman.vehicleInvID)
        vehicleID = vehicle.invID
        slot = tankman.vehicleSlotIdx
        isLocked, msg = _getTankmanLockMessage(vehicle)
        actionBtnEnabled = not isLocked
        isInCurrentTank = g_currentVehicle.isPresent() and tankmanVehicle.invID == g_currentVehicle.invID
        isInSelfVehicle = vehicle.shortUserName == tankmanVehicle.shortUserName
        isInSelfVehicleType = vehicle.type == tankmanVehicle.type
    else:
        isLocked, msg = False, b''
        actionBtnEnabled = True
        isInCurrentTank = False
        vehicleID = None
        slot = None
        isInSelfVehicle = True
        isInSelfVehicleType = True
    data = {b'fullName': (tankman.fullUserName), b'rank': (tankman.rankUserName), 
       b'specializationLevel': (tankman.realRoleLevel.lvl), 
       b'role': (tankman.roleUserName), 
       b'vehicleType': (tankmanVehicle.shortUserName), 
       b'iconFile': (tankman.smallIconPath), 
       b'rankIconFile': (tankman.iconRank), 
       b'contourIconFile': (tankmanVehicle.iconContour), 
       b'tankmanID': (tankman.invID), 
       b'nationID': (tankman.nationID), 
       b'typeID': (tankmanVehicle.innationID), 
       b'roleType': (tankman.descriptor.role), 
       b'tankType': (tankmanVehicle.type), 
       b'inTank': (tankman.isInTank), 
       b'compact': (str(tankman.invID)), 
       b'lastSkillLevel': (tankman.descriptor.lastSkillLevel), 
       b'actionBtnEnabled': actionBtnEnabled, 
       b'inCurrentTank': isInCurrentTank, 
       b'vehicleID': vehicleID, 
       b'slot': slot, 
       b'locked': isLocked, 
       b'lockMessage': msg, 
       b'isInSelfVehicleClass': isInSelfVehicleType, 
       b'isInSelfVehicleType': isInSelfVehicle, 
       b'notRecruited': False, 
       b'hasCommanderFeature': (tankman.role == Tankman.ROLES.COMMANDER), 
       b'roles': (tankman.roles())}
    if tankman.skinID != NO_CREW_SKIN_ID:
        skinItem = itemsCache.items.getCrewSkin(tankman.skinID)
        iconFile = getCrewSkinIconSmall(skinItem.getIconID())
        data[b'iconFile'] = iconFile
        data[b'fullName'] = localizedFullName(skinItem)
    return data


def _packNotRecruitedTankman(recruitInfo):
    expiryTime = recruitInfo.getExpiryTime()
    recruitBeforeStr = i18n.makeString(MENU.BARRACKS_NOTRECRUITEDACTIVATEBEFORE, date=expiryTime) if expiryTime else b''
    availableRoles = recruitInfo.getRoles()
    roleType = availableRoles[0] if len(availableRoles) == 1 else b''
    result = {b'rank': recruitBeforeStr, 
       b'specializationLevel': (recruitInfo.getRoleLevel()), 
       b'role': (text_styles.counter(recruitInfo.getLabel())), 
       b'vehicleType': b'', 
       b'iconFile': (recruitInfo.getSmallIconPath()), 
       b'rankIconFile': b'', 
       b'contourIconFile': b'', 
       b'tankmanID': (-1), 
       b'nationID': (-1), 
       b'typeID': (-1), 
       b'roleType': roleType, 
       b'tankType': b'', 
       b'inTank': False, 
       b'compact': b'', 
       b'lastSkillLevel': (recruitInfo.getLastSkillLevel()), 
       b'actionBtnEnabled': True, 
       b'inCurrentTank': False, 
       b'vehicleID': None, 
       b'slot': None, 
       b'locked': False, 
       b'lockMessage': b'', 
       b'isInSelfVehicleClass': True, 
       b'isInSelfVehicleType': True, 
       b'notRecruited': True, 
       b'isRankNameVisible': True, 
       b'recoveryPeriodText': None, 
       b'roles': (availableRoles if len(availableRoles) == 1 else []), 
       b'actionBtnLabel': (MENU.BARRACKS_BTNRECRUITNOTRECRUITED), 
       b'actionBtnTooltip': (TOOLTIPS.BARRACKS_TANKMEN_RECRUIT), 
       b'skills': [], b'isSkillsVisible': False, 
       b'recruitID': (str(recruitInfo.getRecruitID()))}
    return result


def _packDismissedTankman(tankman):
    skillsList = []
    for skill in tankman.skills:
        skillsList.append({b'tankmanID': (tankman.invID), 
           b'id': (str(tankman.skills.index(skill))), 
           b'name': (skill.userName), 
           b'desc': (skill.description), 
           b'icon': (skill.icon), 
           b'level': (skill.level), 
           b'active': (skill.isEnable)})

    newSkillsCount, lastNewSkillLvl = tankman.newSkillCount
    if newSkillsCount > 0:
        skillsList.append({b'buy': True, 
           b'buyCount': (newSkillsCount - 1), 
           b'tankmanID': (tankman.invID), 
           b'level': lastNewSkillLvl})
    restoreInfo = getTankmenRestoreInfo(tankman)
    actionBtnTooltip = makeTooltip(TOOLTIPS.BARRACKS_TANKMEN_RECOVERYBTN_HEADER, getRecoveryStatusText(restoreInfo))
    tankmanData = _packTankmanData(tankman)
    tankmanData.update({b'isRankNameVisible': False, 
       b'recoveryPeriodText': (_makeRecoveryPeriodText(restoreInfo)), 
       b'actionBtnLabel': (MENU.BARRACKS_BTNRECOVERY), 
       b'actionBtnTooltip': actionBtnTooltip, 
       b'skills': skillsList, 
       b'isSkillsVisible': True})
    return tankmanData


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def _packBuyBerthsSlot(itemsCache=None):
    berths = itemsCache.items.stats.tankmenBerthsCount
    berthPrice, berthCount = itemsCache.items.shop.getTankmanBerthPrice(berths)
    defaultBerthPrice, _ = itemsCache.items.shop.defaults.getTankmanBerthPrice(berths)
    action = None
    if berthPrice != defaultBerthPrice:
        action = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, b'berthsPrices', True, berthPrice, defaultBerthPrice)
    return {b'buy': True, 
       b'price': (backport.getGoldFormat(berthPrice.getSignValue(Currency.GOLD))), 
       b'actionPriceData': action, 
       b'count': berthCount}


def _packActiveTankman(tankman):
    if isinstance(tankman, Tankman):
        tankmanData = _packTankmanData(tankman)
        if tankman.isInTank:
            actionBtnLabel = MENU.BARRACKS_BTNUNLOAD
            actionBtnTooltip = TOOLTIPS.BARRACKS_TANKMEN_UNLOAD
        else:
            actionBtnLabel = MENU.BARRACKS_BTNDISSMISS
            actionBtnTooltip = TOOLTIPS.BARRACKS_TANKMEN_DISMISS
        tankmanData.update({b'isRankNameVisible': True, 
           b'recoveryPeriodText': None, 
           b'actionBtnLabel': actionBtnLabel, 
           b'actionBtnTooltip': actionBtnTooltip, 
           b'skills': None, 
           b'isSkillsVisible': False})
        return tankmanData
    else:
        return tankman


class BarracksDataProvider(DAAPIDataProvider):
    restore = dependency.descriptor(IRestoreController)
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        super(BarracksDataProvider, self).__init__()
        self.__list = []
        self.__totalCount = 0
        self.__filteredCount = 0
        self.__placeCount = 0
        return

    def buildList(self, items):
        self.__list = items
        self.refresh()
        return

    def emptyItem(self):
        return

    @property
    def collection(self):
        return self.__list

    def clear(self):
        self.__list = []
        return

    @property
    def totalCount(self):
        return self.__totalCount

    @property
    def filteredCount(self):
        return self.__filteredCount

    @property
    def placeCount(self):
        return self.__placeCount

    def showDismissedTankmen(self, criteria):
        allTankmen = self.restore.getDismissedTankmen()
        filteredList = filter(criteria, allTankmen)
        self.__totalCount = len(allTankmen)
        self.__filteredCount = len(filteredList)
        self.__placeCount = self.restore.getMaxTankmenBufferLength()
        self.setItemWrapper(_packDismissedTankman)
        self.buildList(filteredList)
        return

    def showNotRecruitedTankmen(self):
        notRecruitedList = recruit_helper.getAllRecruitsInfo(sortByExpireTime=True)
        self.__totalCount = self.__filteredCount = len(notRecruitedList)
        self.__placeCount = 0
        self.setItemWrapper(_packNotRecruitedTankman)
        self.buildList(notRecruitedList)
        return

    def showActiveTankmen(self, criteria):
        removeTankmanCriteria = ~REQ_CRITERIA.VEHICLE.IS_CREW_HIDDEN
        removeTankmanCriteria |= ~REQ_CRITERIA.VEHICLE.BATTLE_ROYALE
        removeTankmanCriteria |= ~REQ_CRITERIA.VEHICLE.HIDDEN_IN_HANGAR
        allTankmen = self.itemsCache.items.removeUnsuitableTankmen(self.itemsCache.items.getTankmen().values(), removeTankmanCriteria)
        self.__totalCount = len(allTankmen)
        tankmenInBarracks = 0
        tankmenList = [_packBuyBerthsSlot()]
        for tankman in allTankmen:
            if not tankman.isInTank:
                tankmenInBarracks += 1
            if criteria(tankman):
                tankmenList.append(tankman)

        self.__filteredCount = len(tankmenList) - 1
        slots = self.itemsCache.items.stats.tankmenBerthsCount
        if tankmenInBarracks < slots:
            tankmenList.insert(1, {b'empty': True, b'freePlaces': (slots - tankmenInBarracks)})
        self.__placeCount = max(slots - tankmenInBarracks, 0)
        self.setItemWrapper(_packActiveTankman)
        self.buildList(tankmenList)
        return
