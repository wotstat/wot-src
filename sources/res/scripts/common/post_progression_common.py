from __future__ import absolute_import
from typing import Dict, Set, List, Callable, Optional, TYPE_CHECKING
from copy import copy
from itertools import chain
from future.utils import viewitems
if TYPE_CHECKING:
    from items.components.post_progression_components import ProgressionTree
    from items.vehicles import VehicleDescriptor
SERVER_SETTINGS_KEY = b'vehicle_post_progression_config'
EXT_DATA_SLOT_KEY = b'customRoleSlotTypeId'
EXT_DATA_PROGRESSION_KEY = b'vehPostProgression'
SETUPS_FEATURES = (b'shells_consumables_switch', b'opt_dev_boosters_switch')
ROLESLOT_FEATURE = b'roleSlot'
FEATURES_NAMES = SETUPS_FEATURES + (ROLESLOT_FEATURE,)
POST_PROGRESSION_UNLOCK_MODIFICATIONS_PRICES = (b'unlockBaseModificationCost', b'unlockPairModificationCost', b'Modification10000xp', b'Modification20000xp', b'Modification25000xp', b'Modification30000xp', b'Modification40000xp')
POST_PROGRESSION_BUY_MODIFICATIONS_PRICES = (b'buyPairModificationCost',)
CUSTOM_ROLE_SLOT_CHANGE_PRICE = b'customRoleSlotChangeCost'
POST_PROGRESSION_UNLOCK_AND_BUY_MODIFICATIONS_PRICES = POST_PROGRESSION_UNLOCK_MODIFICATIONS_PRICES + POST_PROGRESSION_BUY_MODIFICATIONS_PRICES
POST_PROGRESSION_ALL_PRICES = POST_PROGRESSION_UNLOCK_AND_BUY_MODIFICATIONS_PRICES + (CUSTOM_ROLE_SLOT_CHANGE_PRICE,)
ALLOWED_CURRENCIES_FOR_TREE_STEP = {
 b'xp'}
ALLOWED_CURRENCIES_FOR_BUY_MODIFICATION_STEP = {b'credits'}
ALLOWED_CURRENCIES_FOR_CUSTOM_ROLE_SLOT_CHANGE = {b'credits'}
ALLOWED_ACTIONS_CATEGORIES = {25, 26, 27, 28, 29, 
 30, 31}
ID_THRESHOLD = 16384
VEH_SKILL_TREE_ID_OFFSET = 10000

class ACTION_TYPES:
    MODIFICATION = 1
    PAIR_MODIFICATION = 2
    FEATURE = 3
    BIT_PACK = 4


class PAIR_TYPES:
    NOT_SET = 0
    FIRST = 1
    SECOND = 2


class TankSetupLayouts(object):
    OPTIONAL_DEVICES = b'devicesLayout'
    EQUIPMENT = b'eqsLayout'
    SHELLS = b'shellsLayout'
    BATTLE_BOOSTERS = b'boostersLayout'


class TankSetups(object):
    OPTIONAL_DEVICES = b'devicesSetups'
    EQUIPMENT = b'eqsSetups'
    SHELLS = b'shellsSetups'
    BATTLE_BOOSTERS = b'boostersSetups'


class TankSetupGroupsId(object):
    EQUIPMENT_AND_SHELLS = 1
    OPTIONAL_DEVICES_AND_BOOSTERS = 2


TANK_SETUP_GROUPS = {(TankSetupGroupsId.OPTIONAL_DEVICES_AND_BOOSTERS): (
                                                     TankSetupLayouts.OPTIONAL_DEVICES,
                                                     TankSetupLayouts.BATTLE_BOOSTERS), 
   (TankSetupGroupsId.EQUIPMENT_AND_SHELLS): (
                                            TankSetupLayouts.EQUIPMENT,
                                            TankSetupLayouts.SHELLS)}
MAX_LAYOUTS_NUMBER_ON_VEHICLE = {(TankSetupGroupsId.OPTIONAL_DEVICES_AND_BOOSTERS): 2, 
   (TankSetupGroupsId.EQUIPMENT_AND_SHELLS): 2}
GROUP_ID_BY_LAYOUT = {layout: groupName for layout in TANK_SETUP_GROUPS.items()}
FEATURE_BY_GROUP_ID = {(TankSetupGroupsId.EQUIPMENT_AND_SHELLS): b'shells_consumables_switch', 
   (TankSetupGroupsId.OPTIONAL_DEVICES_AND_BOOSTERS): b'opt_dev_boosters_switch'}
GROUP_ID_BY_FEATURE = {feature: groupID for groupID, feature in FEATURE_BY_GROUP_ID.items()}
DEFAULT_LAYOUT_CAPACITY = 1
SWITCH_LAYOUT_CAPACITY = 2
POST_PROGRESSION_UNLOCKS_IDX = 0
POST_PROGRESSION_PAIRS_IDX = 1
POST_PROGRESSION_FEATURES_IDX = 2
POST_PROGRESSION_DISABLED_SWITCHES_IDX = 3

def extractSelectedSetup(setups, setupsIndexes):
    selectedSetup = {}
    for tankSetupId, tankSetupGroup in TANK_SETUP_GROUPS.items():
        chosenIndex = setupsIndexes.get(tankSetupId, 0)
        for tankSetupLayout in tankSetupGroup:
            tankSetups = tankSetupLayout.replace(b'Layout', b'Setups')
            layout = setups[tankSetups]
            selectedSetup[tankSetups] = layout[chosenIndex] if chosenIndex < len(layout) else []

    return selectedSetup


def getSelectedVehicleAmmo(setup):
    return setup[TankSetups.SHELLS] + getSetupInAmmoFormatForEquipment(setup[TankSetups.EQUIPMENT]) + getSetupInAmmoFormatForEquipment(setup[TankSetups.BATTLE_BOOSTERS])


def getSetupInAmmoFormatForEquipment(setup):
    equipmentSetup = []
    for element in setup:
        equipmentSetup += (element, 1)

    return equipmentSetup


def makeActionCompDescr(actionType, itemId, subId=0):
    actionType = int(actionType)
    return subId << 18 | itemId << 4 | actionType


def makeDefaultSetupsIndexes():
    return {(TankSetupGroupsId.OPTIONAL_DEVICES_AND_BOOSTERS): 0, 
       (TankSetupGroupsId.EQUIPMENT_AND_SHELLS): 0}


def makeDefaultSetupsInVehicle():
    return {(TankSetups.SHELLS): [[]], (TankSetups.BATTLE_BOOSTERS): [[]], (TankSetups.EQUIPMENT): [[]], (TankSetups.OPTIONAL_DEVICES): [[]]}


def parseActionCompDescr(compDescr):
    actionType = compDescr & 15
    itemID = compDescr >> 4 & ID_THRESHOLD - 1
    subId = compDescr >> 18 & ID_THRESHOLD - 1
    return (actionType, itemID, subId)


def unpackVehSetupsIndexes(vehSetupsIndexes):
    return dict(zip(vehSetupsIndexes[0::2], vehSetupsIndexes[1::2]))


def packVehSetupsIndexes(vehSetupsIndexes):
    return list(chain(*viewitems(vehSetupsIndexes)))


def getLayoutCapacity(invData, layout, vehDescr):
    if layout == TankSetupLayouts.SHELLS:
        capacity = len(invData.get(layout, {}).get((vehDescr.turret.compactDescr, vehDescr.gun.compactDescr), ()))
    else:
        capacity = len(invData.get(layout, ()))
    return capacity


def packPostProgression(unlocks, pairs, tree):
    atPirModification = ACTION_TYPES.PAIR_MODIFICATION
    result = []
    packed = 0
    pos = 0
    for step in tree.ppBattleIndex:
        actionID, _ = step.action
        if actionID == atPirModification:
            value = 0
            if step.id in unlocks:
                value = pairs.get(step.id, 0)
            packed |= value << pos
            pos += 2
        elif step.id in unlocks:
            packed |= 1 << pos
        pos += 1

    mask = 268435455
    while packed:
        result.append((packed & mask) << 4 | ACTION_TYPES.BIT_PACK)
        packed >>= 28

    return result


def combinePackedCDs(actionCDs):
    packedCDs = [actionCD >> 4 for actionCD in actionCDs if actionCD & 15 == ACTION_TYPES.BIT_PACK]
    if not packedCDs:
        return 0
    packed = 0
    num_bits = 28
    for i, value in enumerate(packedCDs):
        packed |= value << num_bits * i

    return packed


def unpackActiveModifications(actionCDs, vppCache, treeID):
    result = []
    packed = combinePackedCDs(actionCDs)
    if not packed:
        return result
    tree = vppCache.trees.get(treeID)
    if not tree:
        return result
    atPairModification = ACTION_TYPES.PAIR_MODIFICATION
    atModification = ACTION_TYPES.MODIFICATION
    pos = 0
    for step in tree.ppBattleIndex:
        actionID, itemID = step.action
        if actionID == atPairModification:
            value = packed >> pos & 3
            pos += 2
            if value == PAIR_TYPES.FIRST:
                result.append(vppCache.pairs[itemID].first[0])
            elif value == PAIR_TYPES.SECOND:
                result.append(vppCache.pairs[itemID].second[0])
        elif actionID == atModification:
            if packed >> pos & 1:
                result.append(itemID)
            pos += 1
        else:
            pos += 1

    return result


def unpackActionCDs(actionCDs, vppCache, treeID):
    result = [actionCD for actionCD in actionCDs if actionCD & 15 != ACTION_TYPES.BIT_PACK]
    packed = combinePackedCDs(actionCDs)
    if not packed:
        return result
    tree = vppCache.trees.get(treeID)
    if not tree:
        return result
    atPairModification = ACTION_TYPES.PAIR_MODIFICATION
    pos = 0
    for step in tree.ppBattleIndex:
        actionID, itemID = step.action
        if actionID == atPairModification:
            value = packed >> pos & 3
            pos += 2
            if value:
                result.append(makeActionCompDescr(actionID, itemID, value))
        elif packed >> pos & 1:
            result.append(makeActionCompDescr(actionID, itemID, 0))
        pos += 1

    atBitPack = ACTION_TYPES.BIT_PACK
    result.extend([actionCD >> 4 for actionCD in actionCDs if actionCD & 15 != atBitPack])
    return result


class VehicleState(object):
    __slots__ = (b'_unlocks', b'_pairs', b'_features', b'_disabledSwitches')

    def __init__(self, data=None):
        data = data or self.getDefaultState()
        self._unlocks = copy(data[POST_PROGRESSION_UNLOCKS_IDX])
        self._pairs = copy(data[POST_PROGRESSION_PAIRS_IDX])
        self._features = copy(data[POST_PROGRESSION_FEATURES_IDX])
        self._disabledSwitches = copy(data[POST_PROGRESSION_DISABLED_SWITCHES_IDX])
        return

    __hash__ = None

    def __eq__(self, other):
        return self.unlocks == other.unlocks and self.pairs == other.pairs and self.features == other.features and self._disabledSwitches == other.disabledSwitches

    def __ne__(self, other):
        return not self == other

    def __or__(self, other):
        result = VehicleState(self.toRawData())
        for stepID in other.unlocks:
            result.addUnlock(stepID)

        for stepID, pairTypeID in viewitems(other.pairs):
            result.setPair(stepID, pairTypeID)

        for featureID in other.features:
            result.addFeature(featureID)

        for groupID in other._disabledSwitches:
            result.addDisabledSwitch(groupID)

        return result

    @property
    def unlocks(self):
        return self._unlocks

    @property
    def pairs(self):
        return self._pairs

    @property
    def features(self):
        return self._features

    @property
    def disabledSwitches(self):
        return self._disabledSwitches

    def addDisabledSwitch(self, groupID):
        if groupID not in self._disabledSwitches:
            self._disabledSwitches.append(groupID)
        return

    def removeDisabledSwitch(self, groupID):
        if groupID in self._disabledSwitches:
            self._disabledSwitches.remove(groupID)
        return

    def isSwitchDisabled(self, groupID):
        return groupID in self._disabledSwitches

    def isUnlocked(self, stepID):
        return stepID in self._unlocks

    def addUnlock(self, stepID):
        self._unlocks.add(stepID)
        return

    def removeUnlock(self, stepID):
        self._unlocks.discard(stepID)
        return

    def setPair(self, stepID, pairTypeID):
        self._pairs[stepID] = pairTypeID
        return

    def getPair(self, stepID):
        return self._pairs.get(stepID)

    def removePair(self, stepID):
        self._pairs.pop(stepID, None)
        return

    def hasFeature(self, featureID):
        return featureID in self._features

    def addFeature(self, featureID):
        self._features.add(featureID)
        return

    def removeFeature(self, featureID):
        self._features.discard(featureID)
        return

    def clean(self, removeUnlocks=True, removePairs=True, removeFeatures=True, removeDisabledSwitches=True):
        if removeUnlocks:
            self._unlocks = VehicleState.__getDefaultUnlocksState()
        if removePairs:
            self._pairs = VehicleState.__getDefaultPairsState()
        if removeFeatures:
            self._features = VehicleState.__getDefaultFeaturesState()
        if removeDisabledSwitches:
            self._disabledSwitches = VehicleState.__getDefaultDisabledSwitchesState()
        return

    def isEmpty(self):
        return not self.unlocks and not self.pairs and not self.features

    def isResearchedTree(self, tree):
        return self.unlocks == set(tree.steps.keys())

    def toActionCDs(self, tree):
        steps = tree.steps
        pairs = self._pairs
        notSet = PAIR_TYPES.NOT_SET
        pairModification = ACTION_TYPES.PAIR_MODIFICATION
        result = []
        for stepID in self._unlocks:
            actionID, itemID = steps[stepID].action
            result.append(makeActionCompDescr(actionID, itemID, pairs.get(stepID, notSet) if actionID == pairModification else 0))

        return result

    def toBattleActionCDsPack(self, tree):
        return packPostProgression(self._unlocks, self._pairs, tree)

    def toRawData(self):
        return [
         self._unlocks,
         self._pairs,
         self._features,
         self._disabledSwitches]

    def toggleSwitchLayout(self, groupID):
        if self.isSwitchDisabled(groupID):
            self.removeDisabledSwitch(groupID)
        else:
            self.addDisabledSwitch(groupID)
        return

    @staticmethod
    def getDefaultState():
        return [
         VehicleState.__getDefaultUnlocksState(),
         VehicleState.__getDefaultPairsState(),
         VehicleState.__getDefaultFeaturesState(),
         VehicleState.__getDefaultDisabledSwitchesState()]

    @staticmethod
    def __getDefaultUnlocksState():
        return set()

    @staticmethod
    def __getDefaultPairsState():
        return {}

    @staticmethod
    def __getDefaultFeaturesState():
        return set()

    @staticmethod
    def __getDefaultDisabledSwitchesState():
        return []


class VehiclesPostProgression(object):
    __slots__ = (b'__data', b'__dataW')
    ROOT_KEY = b'postProgression'

    def __init__(self, data, syncData=None):
        self.__data = data
        self.__dataW = syncData
        return

    @property
    def _storage(self):
        return self.__data[self.ROOT_KEY]

    @property
    def _storageW(self):
        return self.__dataW()[self.ROOT_KEY]

    def getVehicleState(self, vehTypeCD):
        return VehicleState(self._storage.get(vehTypeCD))

    def getVehicleFeaturesList(self, vehTypeCD):
        postProgression = self._storage.get(vehTypeCD, {})
        if not postProgression:
            return ()
        return tuple(postProgression[POST_PROGRESSION_FEATURES_IDX])

    def setVehicleState(self, vehTypeCD, vehicleState):
        if vehicleState.isEmpty():
            self._storageW.pop(vehTypeCD, None)
        else:
            self._storage[vehTypeCD] = vehicleState.toRawData()
            self._storageW[vehTypeCD].reset()
        return

    def removeVehicleState(self, vehTypeCD):
        self._storageW.pop(vehTypeCD, None)
        return

    def clean(self):
        self.__dataW()[self.ROOT_KEY] = self.getDefaultStorage()
        return

    @staticmethod
    def getDefaultStorage():
        return {}
