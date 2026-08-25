from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.cyberSport import PLAYER_GUI_STATUS
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeSlotsVOs, MAX_PLAYER_COUNT_ALL, makeTotalLevelLabel, makeUnitStateLabel, makeVehicleVO
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS
from gui.clans.clan_cache import g_clanCache
from gui.clans.stronghold_event_requester import FrozenVehiclesConstants
from gui.prb_control import settings
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME
from helpers import i18n
from shared_utils import BitmaskHelper

class FILTER_STATE(BitmaskHelper):
    ALL = 0
    LIGHT_TANK = 1
    MEDIUM_TANK = 2
    HEAVY_TANK = 4
    SPG = 8
    AT_SPG = 16
    VEHICLE_TYPES = (
     (
      LIGHT_TANK, VEHICLE_CLASS_NAME.LIGHT_TANK),
     (
      MEDIUM_TANK, VEHICLE_CLASS_NAME.MEDIUM_TANK),
     (
      HEAVY_TANK, VEHICLE_CLASS_NAME.HEAVY_TANK),
     (
      AT_SPG, VEHICLE_CLASS_NAME.AT_SPG),
     (
      SPG, VEHICLE_CLASS_NAME.SPG))


def _convertVehClassNamesToState(vehClassNames):
    state = FILTER_STATE.ALL
    for bType, vType in FILTER_STATE.VEHICLE_TYPES:
        if vType in vehClassNames:
            state |= bType

    return state


def makeStrongholdsSlotsVOs(unitEntity, unitMgrID=None, maxPlayerCount=MAX_PLAYER_COUNT_ALL):
    isRosterSet, slots = makeSlotsVOs(unitEntity, unitMgrID, maxPlayerCount)
    isCommander = unitEntity.isCommander()
    fullData = unitEntity.getUnitFullData(unitMgrID=unitMgrID)
    isPlayersMatchingAvailable = unitEntity.isPlayersMatchingAvailable()
    slotFilters = unitEntity.getSlotFilters().items()
    vehTypesInSlotFilters = {slotId: _convertVehClassNamesToState(item.get(b'vehicle_types', [])) for slotId, item in slotFilters}
    vehiclesInSlotFilters = {slotId: item.get(b'vehicle_cds', []) for slotId, item in slotFilters}
    canSetupPlayersMatching = isPlayersMatchingAvailable and isCommander
    canUnfreezeVehicles = g_clanCache.strongholdEventProvider.canUnfreezeVehicles()
    rosterSettings = unitEntity.getRosterSettings()
    legionariesMaxCount = rosterSettings.getLegionariesMaxCount()
    legionariesInRoster = fullData.stats.legionariesInRoster
    playersMatchingSlotsCount = fullData.stats.playersMatchingSlotsCount
    maxLegionariesNotReached = legionariesMaxCount > legionariesInRoster + playersMatchingSlotsCount
    slotsInPlayersMatching = unitEntity.getSlotsInPlayersMatching()
    unitInPlayersMatchingMode = unitEntity.inPlayersMatchingMode()
    for idx, slot in enumerate(slots):
        if slot[b'isLocked']:
            break
        vehTypesInSlot = vehTypesInSlotFilters.get(idx, 0)
        vehiclesInSlot = vehiclesInSlotFilters.get(idx, ())
        slot[b'isMatchingEnabled'] = canSetupPlayersMatching
        slot[b'isFiltersEnabled'] = maxLegionariesNotReached
        if slot[b'player'] is not None:
            slot[b'filterState'] = 0
            slot[b'vehicles'] = ()
            slot[b'isRemoveAvailable'] = unitEntity.getPermissions().canAssignToSlot(slot[b'player'][b'dbID'])
            frozenVehicles = unitEntity.getEventFrozenVehicles(slot[b'player'][b'dbID'])
            if frozenVehicles is not None and slot[b'selectedVehicle'] is not None:
                slot[b'hasFrozenVehicle'] = _updateStrongholdEventVehicleVO(slot[b'selectedVehicle'], frozenVehicles)
                slot[b'canUnfrozeVehicles'] = canUnfreezeVehicles and slot[b'hasFrozenVehicle']
                slot[b'unfrozeVehiclesBtnEnabled'] = frozenVehicles != FrozenVehiclesConstants.ALL_VEHICLES_FROZEN
            continue
        slot[b'filterState'] = vehTypesInSlot
        slot[b'vehicles'] = vehiclesInSlot
        if idx in slotsInPlayersMatching or unitInPlayersMatchingMode:
            if isCommander:
                slotLabel = i18n.makeString(FORTIFICATIONS.SORTIE_MEMBER_SLOT_FOR_LEGIONARY)
            else:
                slotLabel = i18n.makeString(FORTIFICATIONS.SORTIE_MEMBER_SLOT_FOR_LEGIONARY_SEARCH)
            slot.update({b'canBeTaken': False, 
               b'isLegionaries': True, 
               b'slotLabel': slotLabel, 
               b'playerStatus': (PLAYER_GUI_STATUS.READY), 
               b'isFiltersEnabled': True})
        if slot[b'isLegionaries'] and slot[b'selectedVehicle'] and not slot[b'isFreezed'] and not slot[b'isCommanderState']:
            slot[b'selectedVehicle'][b'isReadyToFight'] = True

    return (
     isRosterSet, slots)


def makeSortieVO(unitEntity, isCommander, unitMgrID=None, canInvite=True, maxPlayerCount=MAX_PLAYER_COUNT_ALL):
    fullData = unitEntity.getUnitFullData(unitMgrID=unitMgrID)
    levelsValidation = unitEntity.validateLevels()
    canDoAction, restriction = levelsValidation.isValid, levelsValidation.restriction
    sumLevelsStr = makeTotalLevelLabel(fullData.stats, restriction)
    _, slots = makeStrongholdsSlotsVOs(unitEntity, unitMgrID, maxPlayerCount)
    if fullData.playerInfo.isInSlot:
        disableCanBeTakenButtonInSlots(slots)
    if fullData.flags.isLocked() or unitEntity.isStrongholdUnitFreezed() or unitEntity.inPlayersMatchingMode():
        setFreezedInSlots(slots)
        canAssignToSlot = False
    else:
        canAssignToSlot = canInvite
    return {b'canInvite': canInvite, 
       b'isCommander': isCommander, 
       b'isFreezed': (fullData.flags.isLocked()), 
       b'canAssignToSlot': canAssignToSlot, 
       b'hasRestrictions': (fullData.unit.isRosterSet(ignored=settings.CREATOR_ROSTER_SLOT_INDEXES)), 
       b'statusLbl': (makeUnitStateLabel(fullData.flags)), 
       b'statusValue': (fullData.flags.isOpened()), 
       b'sumLevelsInt': (fullData.stats.curTotalLevel), 
       b'sumLevels': sumLevelsStr, 
       b'sumLevelsError': canDoAction, 
       b'slots': slots, 
       b'description': (unitEntity.getCensoredComment(unitMgrID=unitMgrID))}


def disableCanBeTakenButtonInSlots(slots):
    for player in slots:
        if player[b'player'] is None:
            player[b'canBeTaken'] = False

    return slots


def setFreezedInSlots(slots):
    for player in slots:
        if player[b'player'] is not None and player[b'selectedVehicle'] is not None:
            player[b'isFreezed'] = True
            player[b'isDragNDropFreezed'] = False
        player[b'canBeTaken'] = False

    return slots


def makeStrongholdVehicleVO(vehicle, levelsRange=None, vehicleTypes=None, isCurrentPlayer=True, frozenVehicles=None):
    vehicleVO = makeVehicleVO(vehicle, levelsRange=levelsRange, vehicleTypes=vehicleTypes, isCurrentPlayer=isCurrentPlayer)
    if frozenVehicles is not None:
        _updateStrongholdEventVehicleVO(vehicleVO, frozenVehicles)
    return vehicleVO


def _updateStrongholdEventVehicleVO(vehicleVO, frozenVehicles):
    if not vehicleVO[b'isReadyToFight']:
        return False
    if frozenVehicles == FrozenVehiclesConstants.ALL_VEHICLES_FROZEN or vehicleVO[b'intCD'] in frozenVehicles:
        vehicleVO[b'state'] = b'frozenVehicle'
        return True
    return False
