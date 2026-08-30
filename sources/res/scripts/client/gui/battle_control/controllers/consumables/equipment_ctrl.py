import itertools, logging
from collections import namedtuple
from functools import partial
from typing import TYPE_CHECKING
import BigWorld, Event, SoundGroups
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from AvatarInputHandler.AimingSystems import getShotTargetInfo
from PlayerEvents import g_playerEvents
from aih_constants import CTRL_MODE_NAME
from comp7_common import ROLE_EQUIPMENT_TAG
from constants import VEHICLE_SETTING, EQUIPMENT_STAGES, ARENA_BONUS_TYPE
from fun_random.gui.fun_gui_constants import MEDKIT_DURATION
from gui.shared.system_factory import collectEquipmentItem
from gui.Scaleform.genConsts.ANIMATION_TYPES import ANIMATION_TYPES
from gui.Scaleform.genConsts.BATTLE_MARKERS_CONSTS import BATTLE_MARKERS_CONSTS
from gui.battle_control import avatar_getter, vehicle_getter
from gui.battle_control.battle_constants import makeExtraName, VEHICLE_COMPLEX_ITEMS, BATTLE_CTRL_ID, DestroyTimerViewState, VEHICLE_VIEW_STATE
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as _TIMER_STATES
from gui.battle_control.controllers.interfaces import IBattleController
from gui.shared.utils.MethodsRules import MethodsRules
from gui.shared.utils.decorators import ReprInjector
from gui.sounds.epic_sound_constants import EPIC_SOUND
from helpers import i18n, dependency
from items import vehicles, EQUIPMENT_TYPES, ITEM_TYPES
from points_of_interest_shared import POI_EQUIPMENT_TAG
from shared_utils import findFirst, forEach, CONST_CONTAINER
from skeletons.gui.battle_session import IBattleSessionProvider
from soft_exception import SoftException
if TYPE_CHECKING:
    from items.artefacts import Equipment
_ActivationError = namedtuple(b'_ActivationError', b'key ctx')
_ROLE_EQUIPMENT_ANIMATION_TYPE = ANIMATION_TYPES.MOVE_ORANGE_BAR_UP | ANIMATION_TYPES.SHOW_COUNTER_ORANGE
_logger = logging.getLogger(__name__)

class NotApplyingError(_ActivationError):
    pass


class InCooldownError(_ActivationError):

    def __new__(cls, name):
        return super(InCooldownError, cls).__new__(cls, b'equipmentIsInCooldown', {b'name': name})

    def __init__(self, name):
        super(InCooldownError, self).__init__(b'equipmentIsInCooldown', {b'name': name})
        return


class NotReadyError(_ActivationError):

    def __new__(cls, name):
        return super(NotReadyError, cls).__new__(cls, b'orderNotReady', {b'name': name})

    def __init__(self, name):
        super(NotReadyError, self).__init__(b'orderNotReady', {b'name': name})
        return


class PoiUnavailableError(_ActivationError):

    def __new__(cls, name):
        return super(PoiUnavailableError, cls).__new__(cls, b'equipmentPoiUnavailable', {b'name': name})

    def __init__(self, name):
        super(PoiUnavailableError, self).__init__(b'equipmentPoiUnavailable', {b'name': name})
        return


class Comp7RoleSkillUnavailable(_ActivationError):

    def __new__(cls, name):
        return super(Comp7RoleSkillUnavailable, cls).__new__(cls, b'comp7RoleSkillUnavailable', {b'name': name})

    def __init__(self, name):
        super(Comp7RoleSkillUnavailable, self).__init__(b'comp7RoleSkillUnavailable', {b'name': name})
        return


class Comp7RoleSkillAlreadyActivated(_ActivationError):

    def __new__(cls, name):
        return super(Comp7RoleSkillAlreadyActivated, cls).__new__(cls, b'comp7RoleSkillAlreadyActivated', {b'name': name})

    def __init__(self, name):
        super(Comp7RoleSkillAlreadyActivated, self).__init__(b'comp7RoleSkillAlreadyActivated', {b'name': name})
        return


class Comp7RoleSkillCooldown(_ActivationError):

    def __new__(cls, name):
        return super(Comp7RoleSkillCooldown, cls).__new__(cls, b'comp7RoleSkillCooldown', {b'name': name})

    def __init__(self, name):
        super(Comp7RoleSkillCooldown, self).__init__(b'comp7RoleSkillCooldown', {b'name': name})
        return


class AbilityExhausted(_ActivationError):

    def __new__(cls, name):
        return super(AbilityExhausted, cls).__new__(cls, b'abilityExhausted', {b'name': name})

    def __init__(self, name):
        super(AbilityExhausted, self).__init__(b'abilityExhausted', {b'name': name})
        return


class AbilityAlreadyActivated(_ActivationError):

    def __new__(cls, name):
        return super(AbilityAlreadyActivated, cls).__new__(cls, b'abilityAlreadyActivated', {b'name': name})

    def __init__(self, name):
        super(AbilityAlreadyActivated, self).__init__(b'abilityAlreadyActivated', {b'name': name})
        return


class AbilityCooldown(_ActivationError):

    def __new__(cls, name):
        return super(AbilityCooldown, cls).__new__(cls, b'abilityCooldown', {b'name': name})

    def __init__(self, name):
        super(AbilityCooldown, self).__init__(b'abilityCooldown', {b'name': name})
        return


class NeedEntitySelection(_ActivationError):
    pass


class IgnoreEntitySelection(_ActivationError):
    pass


class EquipmentSound(object):
    _soundMap = {251: b'battle_equipment_251', 507: b'battle_equipment_507', 
       1019: b'battle_equipment_1019', 
       763: b'battle_equipment_763', 
       1531: b'battle_equipment_1531', 
       46331: b'battle_equipment_1531', 
       1275: b'battle_equipment_1275'}

    @staticmethod
    def getSounds():
        return EquipmentSound._soundMap.values()

    @staticmethod
    def playSound(ID):
        soundName = EquipmentSound._soundMap.get(ID, None)
        if soundName is not None:
            SoundGroups.g_instance.playSound2D(soundName)
        return

    @staticmethod
    def playReady(item):
        equipment = vehicles.g_cache.equipments()[item.getEquipmentID()]
        if equipment is not None:
            if equipment.soundNotification is not None:
                avatar_getter.getSoundNotifications().play(equipment.soundNotification)
        return


@ReprInjector.simple((
 b'_tags', b'tags'), (
 b'_quantity', b'quantity'), (
 b'_stage', b'stage'), (
 b'_prevStage', b'prevStage'), (
 b'_timeRemaining', b'timeRemaining'), (
 b'_totalTime', b'totalTime'), (
 b'_animationType', b'animationType'))
class _EquipmentItem(object):
    __slots__ = (b'_tags', b'_descriptor', b'_quantity', b'_stage', b'_prevStage', b'_timeRemaining', b'_prevQuantity', b'_totalTime', b'_animationType', b'_serverPrevStage')

    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags):
        super(_EquipmentItem, self).__init__()
        self._tags = tags
        self._descriptor = descriptor
        self._quantity = 0
        self._stage = 0
        self._serverPrevStage = None
        self._prevStage = 0
        self._prevQuantity = 0
        self._timeRemaining = 0
        self._totalTime = totalTime
        self._animationType = ANIMATION_TYPES.MOVE_ORANGE_BAR_UP | ANIMATION_TYPES.SHOW_COUNTER_ORANGE | ANIMATION_TYPES.DARK_COLOR_TRANSFORM
        self.update(quantity, stage, timeRemaining, totalTime)
        return

    def getAnimationType(self):
        return self._animationType

    def setAnimationType(self, animationType):
        self._animationType = animationType
        return

    def setServerPrevStage(self, prevStage):
        self._serverPrevStage = prevStage
        return

    def getTags(self):
        return self._tags

    def isEntityRequired(self):
        return False

    def getEntitiesIterator(self, avatar=None):
        raise SoftException(b'Invokes getEntitiesIterator, than it is not required')
        return

    def getGuiIterator(self, avatar=None):
        raise SoftException(b'Invokes getGuiIterator, than it is not required')
        return

    @property
    def isAvailableToUse(self):
        return self.getQuantity() > 0 and self.isReady

    def canActivate(self, entityName=None, avatar=None):
        if self._timeRemaining > 0 and self._stage and self._stage not in (
         EQUIPMENT_STAGES.DEPLOYING, EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.SHARED_COOLDOWN):
            result = False
            error = _ActivationError(b'equipmentAlreadyActivated', {b'name': (self._descriptor.userString)})
        elif self._stage and self._stage not in (
         EQUIPMENT_STAGES.READY, EQUIPMENT_STAGES.PREPARING):
            result = False
            error = None
            if self._stage == EQUIPMENT_STAGES.ACTIVE:
                error = _ActivationError(b'equipmentAlreadyActivated', {b'name': (self._descriptor.userString)})
            elif self._stage == EQUIPMENT_STAGES.COOLDOWN and self._quantity:
                error = InCooldownError(self._descriptor.userString)
        elif self._quantity <= 0:
            result = False
            error = None
        else:
            result = True
            error = None
        return (result, error)

    def getActivationCode(self, entityName=None, avatar=None):
        return

    def isActivated(self):
        return self._stage == EQUIPMENT_STAGES.ACTIVE

    def clear(self):
        self._descriptor = None
        self._quantity = 0
        self._prevQuantity = 0
        self._stage = 0
        self._prevStage = 0
        self._timeRemaining = 0
        self._totalTime = 0
        return

    def update(self, quantity, stage, timeRemaining, totalTime):
        self._prevQuantity = self._quantity
        self._quantity = quantity
        self._prevStage = self._stage
        self._stage = stage
        self._timeRemaining = timeRemaining
        self._totalTime = totalTime
        self._soundUpdate(self._prevQuantity, quantity)
        return

    def updateMapCase(self, stage=None):
        return

    def activate(self, entityName=None, avatar=None):
        if b'avatar' in self._descriptor.tags:
            avatar_getter.activateAvatarEquipment(self.getEquipmentID(), avatar)
        else:
            avatar_getter.changeVehicleSetting(VEHICLE_SETTING.ACTIVATE_EQUIPMENT, self.getActivationCode(entityName, avatar), avatar=avatar)
        return

    def deactivate(self):
        if not self.canDeactivate():
            return
        if b'avatar' in self._descriptor.tags:
            avatar_getter.activateAvatarEquipment(self.getEquipmentID())
        else:
            avatar_getter.changeVehicleSetting(VEHICLE_SETTING.ACTIVATE_EQUIPMENT, self.getEquipmentID())
        return

    @property
    def isReusable(self):
        return self._descriptor and self._descriptor.reuseCount != 0

    @property
    def isReady(self):
        return self._stage == EQUIPMENT_STAGES.READY

    @property
    def becomeReady(self):
        return self.isReady and self._serverPrevStage in (
         EQUIPMENT_STAGES.DEPLOYING, EQUIPMENT_STAGES.UNAVAILABLE,
         EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.SHARED_COOLDOWN,
         EQUIPMENT_STAGES.EXHAUSTED, EQUIPMENT_STAGES.NOT_RUNNING)

    @property
    def becomeActive(self):
        return self._stage == EQUIPMENT_STAGES.ACTIVE and self._serverPrevStage == EQUIPMENT_STAGES.READY

    @property
    def becomeDeactivated(self):
        return self._serverPrevStage == EQUIPMENT_STAGES.ACTIVE and self._stage != EQUIPMENT_STAGES.ACTIVE

    @property
    def becomeAvailable(self):
        return self.getPrevQuantity() <= 0 and self.getQuantity() > 0

    def getDescriptor(self):
        return self._descriptor

    def getQuantity(self):
        return self._quantity

    def getPrevQuantity(self):
        return self._prevQuantity

    def isQuantityUsed(self):
        return b'showQuantity' in self._descriptor.tags

    def getStage(self):
        return self._stage

    def getPrevStage(self):
        return self._prevStage

    def getTimeRemaining(self):
        return self._timeRemaining

    def getTotalTime(self):
        return self._totalTime

    def getMarker(self):
        return self._descriptor.name.split(b'_')[0]

    def getEnemyMarker(self):
        return self.getMarker()

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_GREEN

    def getEnemyMarkerColor(self):
        return self.getMarkerColor()

    def getEquipmentID(self):
        _, innationID = self._descriptor.id
        return innationID

    def isAvatar(self):
        return self._descriptor and b'avatar' in self._descriptor.tags

    def _soundUpdate(self, prevQuantity, quantity):
        if prevQuantity > quantity and self._stage != self._prevStage:
            if self._stage != EQUIPMENT_STAGES.NOT_RUNNING:
                EquipmentSound.playSound(self._descriptor.compactDescr)
        if self.becomeReady:
            EquipmentSound.playReady(self)
        return

    def canDeactivate(self):
        return True

    def setLocked(self, isLocked):
        return

    def isLocked(self):
        return False


class _RefillEquipmentItem(object):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)
    _PRE_REFILL_TIME = 3

    def __init__(self, *args, **kwargs):
        self._preRefillCallback = None
        super(_RefillEquipmentItem, self).__init__(*args, **kwargs)
        return

    def update(self, quantity, stage, timeRemaining, totalTime):
        super(_RefillEquipmentItem, self).update(quantity, stage, timeRemaining, totalTime)
        if timeRemaining > self._PRE_REFILL_TIME:
            if self._preRefillCallback is not None:
                self.clear()
            self._preRefillCallback = BigWorld.callback(timeRemaining - self._PRE_REFILL_TIME, self._preRefill)
        if self.isReady and self._prevStage in (EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.SHARED_COOLDOWN):
            self._refillComplete()
        return

    def clear(self):
        if self._preRefillCallback is not None:
            BigWorld.cancelCallback(self._preRefillCallback)
            self._preRefillCallback = None
        return

    def _preRefill(self):
        self._preRefillCallback = None
        SoundGroups.g_instance.playSound2D(b'be_pre_replenishment')
        return

    def _refillComplete(self):
        SoundGroups.g_instance.playSound2D(b'be_replenishment_full')
        return


class _AutoItem(_EquipmentItem):

    def canActivate(self, entityName=None, avatar=None):
        return (False, None)


class _TriggerItem(_EquipmentItem):

    def getActivationCode(self, entityName=None, avatar=None):
        flag = 1 if self._timeRemaining == 0 else 0
        return (flag << 16) + self._descriptor.id[1]


class _ExpandedItem(_EquipmentItem):

    def isEntityRequired(self):
        return not self._descriptor.repairAll

    def canActivate(self, entityName=None, avatar=None):
        result, error = super(_ExpandedItem, self).canActivate(entityName, avatar)
        if not result:
            return (result, error)
        return self._canActivate(entityName, avatar)

    def getActivationCode(self, entityName=None, avatar=None):
        if not self.isEntityRequired():
            return 65536 + self._descriptor.id[1]
        else:
            extrasDict = avatar_getter.getVehicleExtrasDict(avatar)
            if entityName is None:
                return
            extraName = makeExtraName(entityName)
            if extraName not in extrasDict:
                return
            return (extrasDict[extraName].index << 16) + self._descriptor.id[1]
            return

    def _getEntitiesAreSafeKey(self):
        return b''

    def _getEntityIsSafeKey(self):
        return b''

    def _getEntityUserString(self, entityName, avatar=None):
        extrasDict = avatar_getter.getVehicleExtrasDict(avatar)
        extraName = makeExtraName(entityName)
        if extraName in extrasDict:
            userString = extrasDict[extraName].deviceUserString
        else:
            userString = entityName
        return userString

    def _canActivate(self, entityName=None, avatar=None):
        deviceStates = avatar_getter.getVehicleDeviceStates(avatar)
        if not deviceStates:
            return (False, _ActivationError(self._getEntitiesAreSafeKey(), None))
        else:
            if entityName is None:
                for item in self.getEntitiesIterator():
                    if item[0] in deviceStates:
                        isEntityNotRequired = not self.isEntityRequired()
                        return (isEntityNotRequired, None if isEntityNotRequired else NeedEntitySelection(b'', None))

                return (
                 False, _ActivationError(self._getEntitiesAreSafeKey(), None))
            return self._canApplyForEntity(entityName, deviceStates)

    def _canApplyForEntity(self, entityName, deviceStates):
        if entityName not in deviceStates:
            return (False,
             NotApplyingError(self._getEntityIsSafeKey(), {b'entity': (self._getEntityUserString(entityName))}))
        else:
            return (
             True, None)


class _ActivatableEquipment(_RefillEquipmentItem, _EquipmentItem):

    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
        self.__totalCooldownTime = descriptor.cooldownSeconds
        self.__totalActiveTime = descriptor.activeSeconds
        super(_ActivatableEquipment, self).__init__(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        return

    def getTotalCooldownTime(self):
        return self.__totalCooldownTime

    def getAnimationType(self):
        if self._stage == EQUIPMENT_STAGES.ACTIVE:
            return ANIMATION_TYPES.MOVE_GREEN_BAR_DOWN | ANIMATION_TYPES.SHOW_COUNTER_GREEN
        return super(_ActivatableEquipment, self).getAnimationType()

    def update(self, quantity, stage, timeRemaining, totalTime):
        super(_ActivatableEquipment, self).update(quantity, stage, timeRemaining, totalTime)
        if stage == EQUIPMENT_STAGES.ACTIVE and self._prevStage != EQUIPMENT_STAGES.ACTIVE:
            totalTime = self.__totalActiveTime
        else:
            self.__totalCooldownTime = totalTime
        self._totalTime = totalTime
        return


class _ExtinguisherItem(_ActivatableEquipment):

    def canActivate(self, entityName=None, avatar=None):
        result, error = super(_ExtinguisherItem, self).canActivate(entityName, avatar)
        if not result:
            return (result, error)
        else:
            if not avatar_getter.isVehicleInFire(avatar):
                return (False,
                 _ActivationError(b'extinguisherDoesNotActivated', {b'name': (self._descriptor.userString)}))
            return (
             True, None)

    def getActivationCode(self, entityName=None, avatar=None):
        return 65536 + self._descriptor.id[1]


class _MedKitItem(_ActivatableEquipment, _ExpandedItem):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def getActivationCode(self, entityName=None, avatar=None):
        activationCode = super(_MedKitItem, self).getActivationCode(entityName, avatar)
        if activationCode is None and avatar_getter.isVehicleStunned() and self.isReusable:
            extrasDict = avatar_getter.getVehicleExtrasDict(avatar)
            activationCode = (extrasDict[makeExtraName(b'commander')].index << 16) + self._descriptor.id[1]
        return activationCode

    def getEntitiesIterator(self, avatar=None):
        return vehicle_getter.TankmenStatesIterator(avatar_getter.getVehicleDeviceStates(avatar), avatar_getter.getVehicleTypeDescriptor(avatar))

    def getGuiIterator(self, avatar=None):
        for name, state in self.getEntitiesIterator(avatar):
            yield (
             name, name, state)

        return

    def _canActivate(self, entityName=None, avatar=None):
        result, error = super(_MedKitItem, self)._canActivate(entityName, avatar)
        if avatar:
            vehicle = BigWorld.entities.get(avatar.playerVehicleID)
            if self.__isFunRandom() and vehicle.health < vehicle.maxHealth:
                invalidateState = self.__sessionProvider.invalidateVehicleState
                itemName = self.getDescriptor().name
                totalTime = int(MEDKIT_DURATION.get(itemName)) - 1
                sType = VEHICLE_VIEW_STATE.HEALING_LARGE if itemName == b'largeMedkit' else VEHICLE_VIEW_STATE.HEALING_SMALL
                invalidateState(sType, DestroyTimerViewState(sType, totalTime, _TIMER_STATES.WARNING_VIEW))
                BigWorld.callback(totalTime, (lambda : invalidateState(sType, DestroyTimerViewState(sType, None, None))))
                return (
                 True, None)
        if not result and type(error) not in (NeedEntitySelection, NotApplyingError) and avatar_getter.isVehicleStunned() and self.isReusable:
            return (True, IgnoreEntitySelection(b'', None))
        else:
            return (
             result, error)

    def _canApplyForEntity(self, entityName, deviceStates):
        if entityName not in deviceStates:
            if not avatar_getter.isVehicleStunned():
                return (False,
                 NotApplyingError(self._getEntityIsSafeKey(), {b'entity': (self._getEntityUserString(entityName))}))
            return (
             self.isReusable, None)
        else:
            return (
             True, None)

    def _getEntitiesAreSafeKey(self):
        if self.__isFunRandom():
            return b'FEPmedkitAllTankmenAreSafe'
        return b'medkitAllTankmenAreSafe'

    def _getEntityIsSafeKey(self):
        return b'medkitTankmanIsSafe'

    def __isFunRandom(self):
        return BONUS_CAPS.checkAny(self.__sessionProvider.arenaVisitor.getArenaBonusType(), b'HEALING_KIT')


class _RepairKitItem(_ActivatableEquipment, _ExpandedItem):

    def getEntitiesIterator(self, avatar=None):
        return vehicle_getter.VehicleDeviceStatesIterator(avatar_getter.getVehicleDeviceStates(avatar), avatar_getter.getVehicleTypeDescriptor(avatar))

    def getGuiIterator(self, avatar=None):
        return vehicle_getter.VehicleGUIItemStatesIterator(avatar_getter.getVehicleDeviceStates(avatar), avatar_getter.getVehicleTypeDescriptor(avatar))

    def _getEntitiesAreSafeKey(self):
        return b'repairkitAllDevicesAreNotDamaged'

    def _getEntityIsSafeKey(self):
        return b'repairkitDeviceIsNotDamaged'

    def _getEntityUserString(self, entityName, avatar=None):
        if entityName in VEHICLE_COMPLEX_ITEMS:
            return i18n.makeString((b'#ingame_gui:devices/{0}').format(entityName))
        return super(_RepairKitItem, self)._getEntityUserString(entityName, avatar)


class _RepairCrewAndModules(_ExpandedItem):

    def getEntitiesIterator(self, avatar=None):
        return itertools.chain(vehicle_getter.VehicleDeviceStatesIterator(avatar_getter.getVehicleDeviceStates(avatar), avatar_getter.getVehicleTypeDescriptor(avatar)), vehicle_getter.TankmenStatesIterator(avatar_getter.getVehicleDeviceStates(avatar), avatar_getter.getVehicleTypeDescriptor(avatar)))

    def canActivate(self, entityName=None, avatar=None):
        result, error = super(_RepairCrewAndModules, self).canActivate(entityName, avatar)
        if not result and type(error) not in (NeedEntitySelection, NotApplyingError) and avatar_getter.isVehicleStunned():
            return (True, IgnoreEntitySelection(b'', None))
        else:
            return (
             result, error)

    def _getEntitiesAreSafeKey(self):
        return b'crewAndDevicesAreOk'

    def _getEntityIsSafeKey(self):
        return b''

    def _getEntityUserString(self, entityName, avatar=None):
        if entityName in VEHICLE_COMPLEX_ITEMS:
            return i18n.makeString((b'#ingame_gui:devices/{0}').format(entityName))
        return super(_RepairCrewAndModules, self)._getEntityUserString(entityName, avatar)


class _OrderItem(_TriggerItem):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    _ACTIVATION_COOLDOWN = 0.2
    _lastActivationTime = 0

    def deactivate(self):
        if self._descriptor is not None:
            super(_OrderItem, self).deactivate()
        return

    def canActivate(self, entityName=None, avatar=None):
        if self._timeRemaining > 0 and self._stage and self._stage in (
         EQUIPMENT_STAGES.DEPLOYING, EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.SHARED_COOLDOWN):
            error = self._getErrorMsg()
            return (
             False, error)
        else:
            result, error = super(_OrderItem, self).canActivate(entityName, avatar)
            if result:
                currentTime = BigWorld.time()
                if currentTime - _OrderItem._lastActivationTime > _OrderItem._ACTIVATION_COOLDOWN:
                    _OrderItem._lastActivationTime = currentTime
                else:
                    _logger.info(b'Attempt to use Arcade equipments simultaneously!')
                    return (False, None)
            return (
             result, error)

    def update(self, quantity, stage, timeRemaining, totalTime):
        self.updateMapCase(stage)
        super(_OrderItem, self).update(quantity, stage, timeRemaining, totalTime)
        return

    def updateMapCase(self, stage=None):
        if not BigWorld.player().isObserver() or BigWorld.player().isObserverFPV:
            if self._stage == stage or self._stage == EQUIPMENT_STAGES.NOT_RUNNING:
                return
            if stage is None:
                stage = self._stage
            from AvatarInputHandler import MapCaseMode
            if stage == EQUIPMENT_STAGES.PREPARING and self._needActivateMapCase():
                MapCaseMode.activateMapCase(self.getEquipmentID(), partial(self.deactivate), self.getAimingControlMode())
            elif self._stage == EQUIPMENT_STAGES.PREPARING:
                if self._needActivateMapCase():
                    MapCaseMode.turnOffMapCase(self.getEquipmentID(), self.getAimingControlMode())
                else:
                    self.deactivate()
        return

    def _getErrorMsg(self):
        return NotReadyError(self._descriptor.userString)

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import MapCaseControlMode
        return MapCaseControlMode

    def _needActivateMapCase(self):
        inputHandler = avatar_getter.getInputHandler()
        arenaVisitor = self.__sessionProvider.arenaVisitor
        if inputHandler is not None and arenaVisitor is not None:
            return not (inputHandler.ctrlModeName == CTRL_MODE_NAME.POSTMORTEM and arenaVisitor.getArenaBonusType() in ARENA_BONUS_TYPE.BATTLE_ROYALE_RANGE)
        return True


class _ArtilleryItem(_OrderItem):

    def getMarker(self):
        return b'artillery_yellow'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_YELLOW


class _ArtilleryAOEFort(_ArtilleryItem):

    def getMarker(self):
        return b'artillery_fort_ally'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_GREEN

    def getEnemyMarker(self):
        return b'artillery_fort_enemy'

    def getEnemyMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_RED


class _EpicArtilleryItem(_OrderItem):

    def getMarker(self):
        return b'artillery'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_GREEN

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import EpicMapCaseControlMode
        return EpicMapCaseControlMode


class _ArcadeArtilleryItem(_ArtilleryItem):

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import ArcadeMapCaseControlMode
        return ArcadeMapCaseControlMode

    def getMarker(self):
        return b'artillery'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_GREEN


class _BomberItem(_OrderItem):

    def getMarker(self):
        return b'bomber'

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import EpicMapCaseControlMode
        return EpicMapCaseControlMode


class _BattleRoyaleBomber(_BomberItem):

    def _getErrorMsg(self):
        return InCooldownError(self._descriptor.userString)


class _ArcadeBomberItem(_BomberItem):

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import ArcadeMapCaseControlMode
        return ArcadeMapCaseControlMode

    def _getErrorMsg(self):
        if self._quantity:
            return InCooldownError(self._descriptor.userString)
        else:
            return


class _ArcadeMineFieldItem(_OrderItem):

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import ArcadeMapCaseControlMode
        return ArcadeMapCaseControlMode


class _ArcadeMineFieldEpicBattleItem(_OrderItem):

    def update(self, quantity, stage, timeRemaining, totalTime):
        if stage == EQUIPMENT_STAGES.PREPARING and self._stage != stage:
            SoundGroups.g_instance.playSound2D(EPIC_SOUND.EB_ABILITY_MINEFIELD_APPLY)
        super(_ArcadeMineFieldEpicBattleItem, self).update(quantity, stage, timeRemaining, totalTime)
        return

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import AracdeMinefieldControleMode
        return AracdeMinefieldControleMode


class _PoiMineFieldItem(_OrderItem):
    pass


class _ReconItem(_OrderItem):

    def getMarker(self):
        return b'recon'


class _SmokeItem(_OrderItem):

    def getMarker(self):
        return b'smoke'


class _BattleRoyaleSmokeItem(_SmokeItem):

    def _getErrorMsg(self):
        return InCooldownError(self._descriptor.userString)


class _ArcadeSmokeItem(_SmokeItem):

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import ArcadeMapCaseControlMode
        return ArcadeMapCaseControlMode

    def _getErrorMsg(self):
        if self._quantity:
            return InCooldownError(self._descriptor.userString)
        else:
            return


class _PoiSmokeItem(_SmokeItem):
    pass


class _StealthRadarItem(_OrderItem):
    pass


class _InspireItem(_OrderItem):
    pass


class _AfterburningItem(_TriggerItem):
    __slots__ = (b'__totalDeployingTime', b'__totalConsumingTime', b'__totalRechargingTime', b'__totalCooldownTime', b'_prevTimeRemaining', b'__fullyChargedSoundCbId', b'__almostChargedSoundCbId', b'__almostChargedSound', b'__playingSoundObj')
    _FULL_CHARGE_DELAY_SOUND_TIME = 5.0
    _ALMOST_CHARGED_SOUND_ID = b'be_pre_replenishment'
    _EXAUSTED_SOUND_ID = b'be_nitro_empty'
    _STOPPED_BY_USER_SOUND_ID = b'be_nitro_stop'
    _ACTIVATED_SOUND_ID = b'be_nitro_activating'

    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
        self.__totalDeployingTime = descriptor.deploySeconds
        self.__totalConsumingTime = descriptor.consumeSeconds
        self.__totalRechargingTime = descriptor.rechargeSeconds
        self.__totalCooldownTime = descriptor.cooldownSeconds
        self._prevTimeRemaining = -1
        self.__fullyChargedSoundCbId = None
        self.__almostChargedSoundCbId = None
        self.__almostChargedSound = None
        self.__playingSoundObj = None
        super(_AfterburningItem, self).__init__(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        return

    def getTags(self):
        return (b'afterburning',)

    def clear(self):
        super(_AfterburningItem, self).clear()
        if self.__playingSoundObj and self.__playingSoundObj.isPlaying:
            self.__playingSoundObj.stop()
        self.__playingSoundObj = None
        if self.__fullyChargedSoundCbId is not None:
            BigWorld.cancelCallback(self.__fullyChargedSoundCbId)
        if self.__almostChargedSoundCbId is not None:
            BigWorld.cancelCallback(self.__almostChargedSoundCbId)
        return

    def update(self, quantity, stage, timeRemaining, totalTime):
        self._prevTimeRemaining = self._timeRemaining
        if self._stage != stage and self._stage in (EQUIPMENT_STAGES.READY, EQUIPMENT_STAGES.PREPARING):
            self._cleanReadyStageSounds()
        super(_AfterburningItem, self).update(quantity, stage, timeRemaining, totalTime)
        if stage == EQUIPMENT_STAGES.ACTIVE and self._prevStage != EQUIPMENT_STAGES.ACTIVE:
            self._animationType = ANIMATION_TYPES.MOVE_GREEN_BAR_DOWN | ANIMATION_TYPES.CENTER_COUNTER | ANIMATION_TYPES.GREEN_GLOW_SHOW | ANIMATION_TYPES.DARK_COLOR_TRANSFORM
            totalTime = self.__totalConsumingTime
            self.__createAndPlaySound(self._ACTIVATED_SOUND_ID)
        elif stage == EQUIPMENT_STAGES.PREPARING:
            self._animationType = ANIMATION_TYPES.MOVE_GREEN_BAR_UP | ANIMATION_TYPES.SHOW_COUNTER_GREEN
            if self._prevStage != stage and self._prevStage != EQUIPMENT_STAGES.COOLDOWN:
                self._animationType |= ANIMATION_TYPES.GREEN_GLOW_HIDE
            totalTime = self.__totalRechargingTime
            self.__processReadyStateSounds(timeRemaining)
            if self._prevStage == EQUIPMENT_STAGES.ACTIVE:
                self.__playSoundOnce(self._STOPPED_BY_USER_SOUND_ID)
        elif stage == EQUIPMENT_STAGES.DEPLOYING:
            self._animationType = ANIMATION_TYPES.MOVE_ORANGE_BAR_UP | ANIMATION_TYPES.SHOW_COUNTER_ORANGE
            totalTime = self.__totalDeployingTime
        elif stage == EQUIPMENT_STAGES.COOLDOWN:
            self._animationType = ANIMATION_TYPES.MOVE_ORANGE_BAR_UP | ANIMATION_TYPES.SHOW_COUNTER_ORANGE | ANIMATION_TYPES.FILL_PARTIALLY
            totalTime = self.__totalCooldownTime
            if self._prevStage == EQUIPMENT_STAGES.ACTIVE:
                self.__playSoundOnce(self._EXAUSTED_SOUND_ID)
        elif stage == EQUIPMENT_STAGES.READY and self.becomeReady:
            self.__processReadyStateSounds(timeRemaining)
        self._totalTime = totalTime
        return

    def canActivate(self, entityName=None, avatar=None):
        result, error = False, None
        if self._stage in (EQUIPMENT_STAGES.READY, EQUIPMENT_STAGES.PREPARING, EQUIPMENT_STAGES.ACTIVE):
            result = True
        elif self._stage == EQUIPMENT_STAGES.COOLDOWN and self._quantity:
            error = InCooldownError(self._descriptor.userString)
        elif self._stage == EQUIPMENT_STAGES.DEPLOYING:
            error = NotReadyError(self._descriptor.userString)
        return (result, error)

    def getEntitiesIterator(self, avatar=None):
        return []

    @property
    def becomeReady(self):
        return super(_AfterburningItem, self).becomeReady

    def _soundUpdate(self, prevQuantity, quantity):
        return

    def _cleanReadyStageSounds(self):
        self.__cleanFullReadySound()
        self.__cleanAlmostReadySound()
        return

    def _playChargedSound(self):
        EquipmentSound.playReady(self)
        self.__fullyChargedSoundCbId = None
        return

    def _playAlmostChargedSound(self):
        if self.__almostChargedSound is None:
            self.__almostChargedSound = SoundGroups.g_instance.getSound2D(self._ALMOST_CHARGED_SOUND_ID)
        else:
            self.__almostChargedSound.stop()
        self.__almostChargedSound.play()
        self.__almostChargedSoundCbId = None
        return

    def __processReadyStateSounds(self, timeRemaining):
        if timeRemaining > -1:
            self.__cleanFullReadySound()
            self.__fullyChargedSoundCbId = BigWorld.callback(timeRemaining, self._playChargedSound)
            if timeRemaining >= self._FULL_CHARGE_DELAY_SOUND_TIME:
                self.__cleanAlmostReadySound()
                if self.__almostChargedSound is not None:
                    self.__almostChargedSound.stop()
                self.__almostChargedSoundCbId = BigWorld.callback(timeRemaining - self._FULL_CHARGE_DELAY_SOUND_TIME, self._playAlmostChargedSound)
        elif self.becomeReady:
            self.__cleanFullReadySound()
            self._playChargedSound()
        return

    def __cleanAlmostReadySound(self):
        if self.__almostChargedSoundCbId is not None:
            BigWorld.cancelCallback(self.__almostChargedSoundCbId)
            self.__almostChargedSoundCbId = None
        return

    def __cleanFullReadySound(self):
        if self.__fullyChargedSoundCbId is not None:
            BigWorld.cancelCallback(self.__fullyChargedSoundCbId)
            self.__fullyChargedSoundCbId = None
        return

    def __playSoundOnce(self, sound):
        SoundGroups.g_instance.playSound2D(sound)
        return

    def __createAndPlaySound(self, sound):
        self.__playingSoundObj = SoundGroups.g_instance.getSound2D(sound)
        self.__playingSoundObj.play()
        return


class _RegenerationKitItem(_EquipmentItem):

    def canActivate(self, entityName=None, avatar=None):
        if self._timeRemaining <= 0 < self._quantity and self._stage in (
         EQUIPMENT_STAGES.READY, EQUIPMENT_STAGES.PREPARING):
            result = True
            error = None
        else:
            result = False
            error = None
            if self._stage == EQUIPMENT_STAGES.COOLDOWN and self._quantity:
                error = NotReadyError(self._descriptor.userString)
        if not result or not avatar:
            return (result, error)
        else:
            vehicle = BigWorld.entities.get(avatar.playerVehicleID)
            if not vehicle or vehicle.health >= vehicle.maxHealth and not any(deviceState in (b'destroyed', b'critical') for deviceState in avatar.deviceStates.itervalues()):
                return (
                 False, _ActivationError(b'vehicleIsNotDamaged', {b'name': (self._descriptor.userString)}))
            return (
             True, None)

    def getActivationCode(self, entityName=None, avatar=None):
        return 65536 + self._descriptor.id[1]

    def getAnimationType(self):
        if self._stage == EQUIPMENT_STAGES.ACTIVE:
            return ANIMATION_TYPES.MOVE_GREEN_BAR_DOWN | ANIMATION_TYPES.SHOW_COUNTER_ORANGE | ANIMATION_TYPES.DARK_COLOR_TRANSFORM
        return super(_RegenerationKitItem, self).getAnimationType()


class _BaseAbilityItem(_TriggerItem):
    _PRE_REFILL_TIME = 3

    def __init__(self, *args):
        self._canDeactivate = False
        self._preRefillCallback = None
        super(_BaseAbilityItem, self).__init__(*args)
        return

    def canDeactivate(self):
        return super(_BaseAbilityItem, self).canDeactivate() and self._canDeactivate

    def getEntitiesIterator(self, avatar=None):
        return iter(())

    def getGuiIterator(self, avatar=None):
        return iter(())

    def deactivate(self):
        super(_BaseAbilityItem, self).deactivate()
        self._canDeactivate = False
        return

    def getAnimationType(self):
        if self._stage == EQUIPMENT_STAGES.ACTIVE:
            return ANIMATION_TYPES.MOVE_GREEN_BAR_DOWN | ANIMATION_TYPES.SHOW_COUNTER_GREEN | ANIMATION_TYPES.DARK_COLOR_TRANSFORM
        return super(_BaseAbilityItem, self).getAnimationType()

    def _getErrorMsg(self):
        if self._stage == EQUIPMENT_STAGES.ACTIVE:
            return AbilityAlreadyActivated(self._descriptor.userString)
        if self._stage == EQUIPMENT_STAGES.COOLDOWN:
            return AbilityCooldown(self._descriptor.userString)
        if self._stage in (EQUIPMENT_STAGES.EXHAUSTED, EQUIPMENT_STAGES.UNAVAILABLE):
            return AbilityExhausted(self._descriptor.userString)
        return NotReadyError(self._descriptor.userString)

    def _playSound(self, soundTypeName):
        equipment = vehicles.g_cache.equipments()[self.getEquipmentID()]
        soundName = getattr(equipment, soundTypeName, None)
        if soundName is not None:
            SoundGroups.g_instance.playSound2D(soundName)
        return

    def _soundUpdate(self, prevQuantity, quantity):
        super(_BaseAbilityItem, self)._soundUpdate(prevQuantity, quantity)
        if self.becomeActive:
            self._playSound(b'activationSound')
        if self.becomeDeactivated:
            self._playSound(b'deactivationSound')
        timeRemaining = self.getTimeRemaining()
        if timeRemaining > self._PRE_REFILL_TIME and self._stage in (EQUIPMENT_STAGES.COOLDOWN,
         EQUIPMENT_STAGES.SHARED_COOLDOWN):
            if self._preRefillCallback is not None:
                self._cancelCallback()
            self._preRefillCallback = BigWorld.callback(timeRemaining - self._PRE_REFILL_TIME, self._preRefill)
        return

    def _preRefill(self):
        self._preRefillCallback = None
        self._playSound(b'refillSound')
        return

    def _cancelCallback(self):
        BigWorld.cancelCallback(self._preRefillCallback)
        self._preRefillCallback = None
        return

    def clear(self):
        super(_BaseAbilityItem, self).clear()
        if self._preRefillCallback is not None:
            self._cancelCallback()
        return


class _VisualScriptItem(_BaseAbilityItem):

    def canActivate(self, entityName=None, avatar=None):
        if not avatar:
            avatar = BigWorld.player()
        visualScriptEquipment = self._getComponent(avatar)
        if visualScriptEquipment is not None:
            _, errorKey = visualScriptEquipment.canActivate()
            if errorKey is not None:
                return (False, _ActivationError(errorKey, {b'name': (self._descriptor.userString)}))
        else:
            _logger.error(b'Missing VisualScriptEquipment dynamic component.')
            return (False, None)
        if self._stage in (EQUIPMENT_STAGES.UNAVAILABLE, EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.NOT_RUNNING,
         EQUIPMENT_STAGES.EXHAUSTED):
            error = self._getErrorMsg()
            return (
             False, error)
        else:
            return super(_VisualScriptItem, self).canActivate(entityName=entityName, avatar=avatar)

    def _getComponent(self, avatar=None):
        if not avatar:
            avatar = BigWorld.player()
        vehicle = avatar.getVehicleAttached()
        if vehicle is not None:
            return vehicle.dynamicComponents.get(self._descriptor.name)
        else:
            return

    def _getErrorMsg(self):
        stage = self.getStage()
        if stage == EQUIPMENT_STAGES.COOLDOWN:
            return InCooldownError(self._descriptor.userString)
        return NotReadyError(self._descriptor.userString)

    def updateMapCase(self, stage=None):
        if BigWorld.player().isObserver() and not BigWorld.player().isObserverFPV:
            return
        else:
            aimingControlMode = self._getAimingControlMode()
            if aimingControlMode is None:
                return
            if self._stage == stage:
                return
            if stage is None:
                stage = self._stage
            from AvatarInputHandler import MapCaseMode
            if stage == EQUIPMENT_STAGES.PREPARING:
                MapCaseMode.activateMapCase(self.getEquipmentID(), partial(self.deactivate), aimingControlMode)
            elif self._stage == EQUIPMENT_STAGES.PREPARING:
                MapCaseMode.turnOffMapCase(self.getEquipmentID(), aimingControlMode)
            return

    def update(self, quantity, stage, timeRemaining, totalTime):
        self.updateMapCase(stage)
        if stage != self._stage:
            self._canDeactivate = stage in (EQUIPMENT_STAGES.PREPARING,)
        super(_VisualScriptItem, self).update(quantity, stage, timeRemaining, totalTime)
        if stage in (EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.ACTIVE):
            self._totalTime = timeRemaining
        elif stage in (
         EQUIPMENT_STAGES.UNAVAILABLE,
         EQUIPMENT_STAGES.READY,
         EQUIPMENT_STAGES.PREPARING,
         EQUIPMENT_STAGES.EXHAUSTED):
            self._totalTime = 0
        return

    def _getAimingControlMode(self):
        return


class _PoiEquipmentItemVS(_VisualScriptItem):

    def canActivate(self, entityName=None, avatar=None):
        if not self._getComponent():
            return (False, self._getErrorMsg())
        return super(_PoiEquipmentItemVS, self).canActivate(entityName, avatar)

    def _getErrorMsg(self):
        if self._stage in (EQUIPMENT_STAGES.UNAVAILABLE, EQUIPMENT_STAGES.NOT_RUNNING, EQUIPMENT_STAGES.EXHAUSTED):
            return PoiUnavailableError(self._descriptor.userString)
        return super(_PoiEquipmentItemVS, self)._getErrorMsg()

    def clear(self):
        _EquipmentItem.clear(self)
        return

    def _soundUpdate(self, prevQuantity, quantity):
        _EquipmentItem._soundUpdate(self, prevQuantity, quantity)
        return


class _PoiArtilleryItem(_ArtilleryItem):

    def getMarker(self):
        return b'artillery_fort_ally'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_GREEN

    def _getErrorMsg(self):
        if self._stage in (EQUIPMENT_STAGES.UNAVAILABLE, EQUIPMENT_STAGES.NOT_RUNNING, EQUIPMENT_STAGES.EXHAUSTED):
            return PoiUnavailableError(self._descriptor.userString)
        return super(_PoiArtilleryItem, self)._getErrorMsg()

    def canActivate(self, entityName=None, avatar=None):
        if self._stage in (EQUIPMENT_STAGES.UNAVAILABLE, EQUIPMENT_STAGES.NOT_RUNNING, EQUIPMENT_STAGES.EXHAUSTED):
            return (False, self._getErrorMsg())
        return super(_PoiArtilleryItem, self).canActivate(entityName, avatar)


class _RoleSkillVSItem(_VisualScriptItem):

    def update(self, quantity, stage, timeRemaining, totalTime):
        prevQuantity = self._prevQuantity
        super(_RoleSkillVSItem, self).update(quantity, stage, timeRemaining, totalTime)
        self._prevQuantity = prevQuantity
        self._quantity = self.getQuantity()
        return

    def _getErrorMsg(self):
        if self._stage == EQUIPMENT_STAGES.UNAVAILABLE:
            return Comp7RoleSkillUnavailable(self._descriptor.userString)
        if self._stage == EQUIPMENT_STAGES.ACTIVE:
            return Comp7RoleSkillAlreadyActivated(self._descriptor.userString)
        if self._stage == EQUIPMENT_STAGES.COOLDOWN:
            return Comp7RoleSkillCooldown(self._descriptor.userString)
        return super(_RoleSkillVSItem, self)._getErrorMsg()

    def getQuantity(self):
        component = self._getComponent()
        if component is None:
            return 0
        else:
            available, _ = self.canActivate()
            return int(available)

    def canActivate(self, entityName=None, avatar=None):
        if self._stage in (EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.ACTIVE, EQUIPMENT_STAGES.UNAVAILABLE):
            return (False, self._getErrorMsg())
        return super(_RoleSkillVSItem, self).canActivate(entityName, avatar)

    def clear(self):
        _EquipmentItem.clear(self)
        return

    def _soundUpdate(self, prevQuantity, quantity):
        _EquipmentItem._soundUpdate(self, prevQuantity, quantity)
        return


class _AbilitySkillVSItem(_VisualScriptItem):

    def _getErrorMsg(self):
        return _BaseAbilityItem._getErrorMsg(self)

    def canActivate(self, entityName=None, avatar=None):
        if self._stage in (
         EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.ACTIVE,
         EQUIPMENT_STAGES.EXHAUSTED, EQUIPMENT_STAGES.UNAVAILABLE):
            return (False, self._getErrorMsg())
        return super(_AbilitySkillVSItem, self).canActivate(entityName, avatar)


class _AbilitySkillItem(_BaseAbilityItem):

    def canActivate(self, entityName=None, avatar=None):
        if self._stage in (
         EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.ACTIVE,
         EQUIPMENT_STAGES.EXHAUSTED, EQUIPMENT_STAGES.UNAVAILABLE):
            return (False, self._getErrorMsg())
        return super(_AbilitySkillItem, self).canActivate(entityName, avatar)


class _DeferredRoleSkillVSItem(_RoleSkillVSItem):
    _ACTIVATION_COOLDOWN = 0.2
    _lastActivationTime = 0

    def __init__(self, *args):
        super(_DeferredRoleSkillVSItem, self).__init__(*args)
        g_playerEvents.onRoundFinished += self.__onRoundFinished
        return

    def clear(self):
        super(_DeferredRoleSkillVSItem, self).clear()
        g_playerEvents.onRoundFinished -= self.__onRoundFinished
        return

    def canActivate(self, entityName=None, avatar=None):
        result, error = super(_DeferredRoleSkillVSItem, self).canActivate(entityName, avatar)
        if result and avatar:
            currentTime = BigWorld.time()
            if currentTime - self._lastActivationTime < self._ACTIVATION_COOLDOWN:
                return (False, None)
            self._lastActivationTime = currentTime
        return (result, error)

    def __onRoundFinished(self, *_):
        from AvatarInputHandler import MapCaseMode
        MapCaseMode.turnOffMapCase(self.getEquipmentID(), self._getAimingControlMode())
        return


class _RoleSkillReconVSItem(_DeferredRoleSkillVSItem):

    def _getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import MapCaseControlMode
        return MapCaseControlMode


class _RoleSkillArtyVSItem(_DeferredRoleSkillVSItem):

    def _getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import MapCaseControlMode
        return MapCaseControlMode

    def getMarker(self):
        return b'artillery_fort_ally'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_GREEN


class _GameplayConsumableItem(_TriggerItem):

    def getTags(self):
        return (b'trappoint',)

    def getEntitiesIterator(self, avatar=None):
        return []


class _RepairPointItem(_TriggerItem):

    def getTags(self):
        return (b'repairpoint',)

    def getEntitiesIterator(self, avatar=None):
        return []


def _isBattleRoyaleBattle():
    if BigWorld.player() is not None:
        return BigWorld.player().arena.bonusType in ARENA_BONUS_TYPE.BATTLE_ROYALE_RANGE
    else:
        return False


def _triggerItemFactory(descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
    if descriptor.name.startswith(b'arcade_artillery'):
        return _ArcadeArtilleryItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'arcade_bomber'):
        return _ArcadeBomberItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'arcade_minefield_epic_battle'):
        return _ArcadeMineFieldEpicBattleItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'arcade_minefield'):
        return _ArcadeMineFieldItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'artillery_epic'):
        return _EpicArtilleryItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'artillery_aoe_fort'):
        return _ArtilleryAOEFort(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'artillery'):
        return _ArtilleryItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'bomber'):
        return _getBomberItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'smoke'):
        return _getSmokeItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'inspire'):
        return _InspireItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'arcade_smoke'):
        return _ArcadeSmokeItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'recon'):
        return _ReconItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'afterburning'):
        return _AfterburningItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'stealth_radar'):
        return _StealthRadarItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'fl_regenerationKit'):
        return _RegenerationKitItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    return _TriggerItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)


def _comp7ItemFactory(descriptor, quantity, stage, timeRemaining, totalTime, tag=None):
    if descriptor.name.startswith(b'comp7_recon'):
        itemClass = _RoleSkillReconVSItem
    elif descriptor.name.startswith(b'comp7_redline'):
        itemClass = _RoleSkillArtyVSItem
    else:
        itemClass = _RoleSkillVSItem
    return itemClass(descriptor, quantity, stage, timeRemaining, totalTime, tag)


def _poiItemFactory(descriptor, quantity, stage, timeRemaining, totalTime, tag=None):
    if descriptor.name.startswith(b'poi_artillery_aoe'):
        itemClass = _PoiArtilleryItem
    elif descriptor.name.startswith(b'poi_smoke'):
        itemClass = _PoiSmokeItem
    elif descriptor.name.startswith(b'poi_minefield'):
        itemClass = _PoiMineFieldItem
    else:
        itemClass = _PoiEquipmentItemVS
    return itemClass(descriptor, quantity, stage, timeRemaining, totalTime, tag)


def _getBomberItem(descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
    isBattleRoyaleMode = _isBattleRoyaleBattle()
    if isBattleRoyaleMode:
        return _BattleRoyaleBomber(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    return _BomberItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)


def _getSmokeItem(descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
    isBattleRoyaleMode = _isBattleRoyaleBattle()
    if isBattleRoyaleMode:
        return _BattleRoyaleSmokeItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    return _SmokeItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)


_EQUIPMENT_TAG_TO_ITEM = {(b'fuel',): _AutoItem, 
   (b'stimulator',): _AutoItem, 
   (b'trigger',): _triggerItemFactory, 
   (b'extinguisher',): _ExtinguisherItem, 
   (b'medkit',): _MedKitItem, 
   (b'repairkit',): _RepairKitItem, 
   (b'regenerationKit',): _RegenerationKitItem, 
   (b'medkit', b'repairkit'): _RepairCrewAndModules, 
   (ROLE_EQUIPMENT_TAG,): _comp7ItemFactory, 
   (b'visualScriptAbilityEquipment',): _AbilitySkillVSItem, 
   (b'abilityEquipment',): _AbilitySkillItem, 
   (POI_EQUIPMENT_TAG,): _poiItemFactory}

class _DAMAGE_PANEL_EQUIPMENT(CONST_CONTAINER):
    EXTINGUISHER = b'extinguisher'
    MEDKIT = b'medkit'
    REPAIRKIT = b'repairkit'


def _getInitialTagsAndClass(descriptor, tagsToItems):
    descrTags = descriptor.tags
    tagsCandidate, clazzCandidate = tuple(), None
    for requiredTags, itemClass in tagsToItems.iteritems():
        for tag in requiredTags:
            if tag not in descrTags:
                break
        else:
            if len(requiredTags) > len(tagsCandidate):
                tagsCandidate = requiredTags
                clazzCandidate = itemClass

    return (
     tagsCandidate, clazzCandidate)


class EquipmentsController(MethodsRules, IBattleController):
    __slots__ = (b'_eManager', b'__arena', b'_order', b'_equipments', b'__preferredPosition', b'__equipmentCount', b'onEquipmentAdded', b'onEquipmentUpdated', b'onEquipmentMarkerShown', b'onEquipmentCooldownInPercent', b'onEquipmentCooldownTime', b'onCombatEquipmentUsed', b'onEquipmentReset', b'onEquipmentsCleared')

    def __init__(self, setup):
        super(EquipmentsController, self).__init__()
        self._eManager = Event.EventManager()
        self.onEquipmentAdded = Event.Event(self._eManager)
        self.onSlotWaited = Event.Event(self._eManager)
        self.onSlotBlocked = Event.Event(self._eManager)
        self.onEquipmentUpdated = Event.Event(self._eManager)
        self.onEquipmentReset = Event.Event(self._eManager)
        self.onEquipmentsCleared = Event.Event(self._eManager)
        self.onEquipmentMarkerShown = Event.Event(self._eManager)
        self.onEquipmentAreaCreated = Event.Event(self._eManager)
        self.onEquipmentCooldownInPercent = Event.Event(self._eManager)
        self.onEquipmentCooldownTime = Event.Event(self._eManager)
        self.onUpdateDamageModifier = Event.Event(self._eManager)
        self.onShowGlowForSlot = Event.Event(self._eManager)
        self.onShowBlinkReloadTime = Event.Event(self._eManager)
        self.onCombatEquipmentUsed = Event.Event(self._eManager)
        self._order = []
        self._equipments = {}
        self.__preferredPosition = None
        self.__equipmentCount = 0
        self.__arena = setup.arenaEntity
        return

    def __repr__(self):
        return (b'EquipmentsController({0!r:s})').format(self._equipments)

    def getControllerID(self):
        return BATTLE_CTRL_ID.EQUIPMENTS

    def startControl(self, *args):
        self.__arena.onCombatEquipmentUsed += self.onCombatEquipmentUsed
        return

    def stopControl(self):
        self.__arena.onCombatEquipmentUsed -= self.onCombatEquipmentUsed
        self.__arena = None
        self.clear(leave=True)
        return

    @classmethod
    def _findExtendItem(cls, isReplay, name, *args):
        return collectEquipmentItem(name, isReplay, args)

    @classmethod
    def createItem(cls, descriptor, quantity, stage, timeRemaining, totalTime):
        item = cls._findExtendItem(False, descriptor.name, descriptor, quantity, stage, timeRemaining, totalTime)
        if item:
            return item
        tags, clazz = _getInitialTagsAndClass(descriptor, _EQUIPMENT_TAG_TO_ITEM)
        if tags:
            item = clazz(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        else:
            item = _EquipmentItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        return item

    def clear(self, leave=True):
        super(EquipmentsController, self).clear(True)
        _logger.debug(b'EquipmentsController CLEARED')
        if leave:
            self._eManager.clear()
        self._order = []
        while self._equipments:
            _, item = self._equipments.popitem()
            item.clear()

        self.__equipmentCount = 0
        if not leave:
            self.onEquipmentsCleared()
        return

    def cancel(self):
        item = findFirst((lambda item: item.getStage() == EQUIPMENT_STAGES.PREPARING and item.canDeactivate()), self._equipments.itervalues())
        if item is not None:
            item.deactivate()
            return True
        else:
            return False

    def hasEquipment(self, intCD):
        return intCD in self._equipments

    def iterEquipmentsByTag(self, tag, condition=None):
        return ((intCD, item) for intCD, item in self._equipments.iteritems() if tag in item.getTags() and (condition is None or condition(item)))

    def getEquipmentNameByID(self, itemID):
        item = vehicles.g_cache.equipments().get(itemID, None)
        if item is not None:
            return item.name
        else:
            return

    def getEquipment(self, intCD):
        try:
            item = self._equipments[intCD]
        except KeyError:
            _logger.error(b'Equipment is not found. %d', intCD)
            item = None

        return item

    def getOrderedEquipmentsLayout(self):
        return [(intCD, self._equipments[intCD]) for intCD in self._order if intCD]

    @MethodsRules.delayable()
    def notifyPlayerVehicleSet(self, vID):
        vehicle = BigWorld.entity(vID)
        if vehicle is not None:
            self.__equipmentCount = vehicle.typeDescriptor.type.supplySlots.getAmountForType(ITEM_TYPES.equipment, EQUIPMENT_TYPES.regular)
        else:
            self.__equipmentCount = 0
        return

    @MethodsRules.delayable(b'notifyPlayerVehicleSet')
    def setEquipment(self, intCD, quantity, stage, timeRemaining, totalTime):
        _logger.debug(b'Equipment added: intCD=%d, quantity=%d, stage=%s, timeRemaining=%d, totalTime=%d', intCD, quantity, stage, timeRemaining, totalTime)
        item = None
        if not intCD:
            if len(self._order) < self.__equipmentCount:
                self._order.append(0)
                self.onEquipmentAdded(0, None)
        elif intCD in self._equipments:
            item = self._equipments[intCD]
            item.update(quantity, stage, timeRemaining, totalTime)
            self.onEquipmentUpdated(intCD, item)
        else:
            descriptor = vehicles.getItemByCompactDescr(intCD)
            if b'hidden' in descriptor.tags:
                return
            if descriptor.equipmentType in (EQUIPMENT_TYPES.regular, EQUIPMENT_TYPES.battleAbilities):
                item = self.createItem(descriptor, quantity, stage, timeRemaining, totalTime)
                self._equipments[intCD] = item
                self._order.append(intCD)
                item.updateMapCase()
                self.onEquipmentAdded(intCD, item)
        if item:
            item.setServerPrevStage(None)
        return

    def updateMapCase(self):
        for item in self._equipments.itervalues():
            item.updateMapCase()

        return

    @MethodsRules.delayable(b'notifyPlayerVehicleSet')
    def resetEquipment(self, oldIntCD, newIntCD, quantity, stage, timeRemaining, totalTime):
        if oldIntCD not in self._order:
            return
        oldOrderIndex = self._order.index(oldIntCD)
        del self._equipments[oldIntCD]
        _logger.debug(b'Equipment reset: oldIntCD=%d, newIntCD=%d, quantity=%d, stage=%s, timeRemaining=%d, totalTime=%d', oldIntCD, newIntCD, quantity, stage, timeRemaining, totalTime)
        descriptor = vehicles.getItemByCompactDescr(newIntCD)
        item = self.createItem(descriptor, quantity, stage, timeRemaining, totalTime)
        self._equipments[newIntCD] = item
        self._order[oldOrderIndex] = newIntCD
        self.onEquipmentReset(oldIntCD, newIntCD, item)
        return

    def setServerPrevStage(self, prevStage, intCD):
        if intCD in self._equipments:
            self._equipments[intCD].setServerPrevStage(prevStage)
        return

    def getEquipments(self):
        return self._equipments

    def getActivatedEquipments(self):
        activatedEquipments = {}
        for intCD, equipment in self._equipments.iteritems():
            if equipment.isActivated():
                activatedEquipments[intCD] = equipment

        return activatedEquipments

    def getActivationCode(self, intCD, entityName=None, avatar=None):
        code = None
        item = self.getEquipment(intCD)
        if item:
            code = item.getActivationCode(entityName, avatar)
        return code

    def canActivate(self, intCD, entityName=None, avatar=None):
        result, error = False, None
        item = self.getEquipment(intCD)
        if item:
            result, error = item.canActivate(entityName, avatar)
        return (result, error)

    def changeSetting(self, intCD, entityName=None, avatar=None):
        if not avatar_getter.isVehicleAlive(avatar):
            return (False, None)
        else:
            result, error = False, None
            item = self.getEquipment(intCD)
            if item:
                result, error = self.__doChangeSetting(item, entityName, avatar)
            return (result, error)

    def changeSettingByTag(self, tag, entityName=None, avatar=None):
        if not avatar_getter.isVehicleAlive(avatar) or not _DAMAGE_PANEL_EQUIPMENT.hasValue(tag):
            return (False, None)
        else:
            result, error = False, None
            filteredItems = [item for item in self._equipments.itervalues() if tag in item.getTags()]
            for item in filteredItems:
                result, error = self.__doChangeSetting(item, entityName, avatar)
                if result:
                    return (True, error)

            return (
             result, error)

    def showMarker(self, eq, pos, direction, time, team=None):
        item = findFirst((lambda e: e.getEquipmentID() == eq.id[1]), self._equipments.itervalues())
        if item is None:
            item = self.createItem(eq, 0, -1, 0, 0)
        self.onEquipmentMarkerShown(item, pos, direction, time, team)
        return

    def consumePreferredPosition(self):
        value = self.__preferredPosition
        self.__preferredPosition = None
        return value

    def __doChangeSetting(self, item, entityName=None, avatar=None):
        result, error = item.canActivate(entityName, avatar)
        if result and avatar_getter.isPlayerOnArena(avatar):
            if item.getStage() == EQUIPMENT_STAGES.PREPARING:
                item.deactivate()
            else:
                avatar = BigWorld.player()
                curCtrl = avatar.inputHandler.ctrl
                if curCtrl is not None and curCtrl.isEnabled:
                    desiredShotPoint = curCtrl.getDesiredShotPoint(ignoreAimingMode=True)
                    vehicle = avatar.getVehicleAttached()
                    gunRotator = avatar.gunRotator
                    if gunRotator:
                        hitPoint, _ = getShotTargetInfo(vehicle, desiredShotPoint, gunRotator)
                        if vehicle and vehicle.position.distTo(hitPoint) < vehicle.position.distTo(desiredShotPoint):
                            desiredShotPoint = hitPoint
                    self.__preferredPosition = desiredShotPoint
                forEach((lambda e: e.deactivate()), [e for e in self._equipments.itervalues() if e.getStage() == EQUIPMENT_STAGES.PREPARING])
                item.activate(entityName, avatar)
        return (
         result, error)


class _ReplayItem(_EquipmentItem):
    __slots__ = (b'__cooldownTime',)

    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
        super(_ReplayItem, self).__init__(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        self.__cooldownTime = BigWorld.serverTime() + timeRemaining
        return

    def init(self, *args, **kwargs):
        return

    def update(self, quantity, stage, timeRemaining, totalTime):
        super(_ReplayItem, self).update(quantity, stage, timeRemaining, totalTime)
        self.__cooldownTime = BigWorld.serverTime() + timeRemaining
        return

    def getEntitiesIterator(self, avatar=None):
        return []

    def getGuiIterator(self, avatar=None):
        return []

    def canActivate(self, entityName=None, avatar=None):
        return (False, None)

    def getReplayTimeRemaining(self):
        return max(0, self.__cooldownTime - BigWorld.serverTime())

    def getCooldownPercents(self):
        totalTime = self.getTotalTime()
        timeRemaining = self.getReplayTimeRemaining()
        if totalTime > 0:
            return round(float(totalTime - timeRemaining) / totalTime * 100.0)
        return 0.0


class _ReplayExtinguisherItem(_ReplayItem, _ActivatableEquipment):
    pass


class _ReplayMedKitItem(_ReplayItem, _ActivatableEquipment):
    __slots__ = (b'__cooldownTime',)

    def getEntitiesIterator(self, avatar=None):
        return vehicle_getter.TankmenStatesIterator(avatar_getter.getVehicleDeviceStates(avatar), avatar_getter.getVehicleTypeDescriptor(avatar))


class _ReplayRepairKitItem(_ReplayItem, _ActivatableEquipment):
    __slots__ = (b'__cooldownTime',)

    def getEntitiesIterator(self, avatar=None):
        return vehicle_getter.VehicleDeviceStatesIterator(avatar_getter.getVehicleDeviceStates(avatar), avatar_getter.getVehicleTypeDescriptor(avatar))


class _ReplayOrderItem(_ReplayItem):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def deactivate(self):
        if self._descriptor is not None:
            super(_ReplayOrderItem, self).deactivate()
        return

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import MapCaseControlMode
        return MapCaseControlMode

    def update(self, quantity, stage, timeRemaining, totalTime):
        from AvatarInputHandler import MapCaseMode
        if stage == EQUIPMENT_STAGES.PREPARING and self._stage != stage and self._needActivateMapCase():
            MapCaseMode.activateMapCase(self.getEquipmentID(), partial(self.deactivate), self.getAimingControlMode())
        elif self._stage == EQUIPMENT_STAGES.PREPARING and self._stage != stage:
            if self._needActivateMapCase():
                MapCaseMode.turnOffMapCase(self.getEquipmentID(), self.getAimingControlMode())
            else:
                self.deactivate()
        super(_ReplayOrderItem, self).update(quantity, stage, timeRemaining, totalTime)
        return

    def _needActivateMapCase(self):
        inputHandler = avatar_getter.getInputHandler()
        arenaVisitor = self.__sessionProvider.arenaVisitor
        if inputHandler is not None and arenaVisitor is not None:
            return not (inputHandler.ctrlModeName == CTRL_MODE_NAME.POSTMORTEM and arenaVisitor.getArenaBonusType() in ARENA_BONUS_TYPE.BATTLE_ROYALE_RANGE)
        return True


class _ReplayArtilleryItem(_ReplayOrderItem):

    def getMarker(self):
        return b'artillery_yellow'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_YELLOW


class _ReplayArtilleryAOEFort(_ReplayArtilleryItem):

    def getMarker(self):
        return b'artillery_fort_ally'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_GREEN

    def getEnemyMarker(self):
        return b'artillery_fort_enemy'

    def getEnemyMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_RED


class _ReplayArcadeArtilleryItem(_ReplayOrderItem):

    def getMarker(self):
        return b'artillery'


class _ReplayBomberItem(_ReplayOrderItem):

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import ArcadeMapCaseControlMode
        return ArcadeMapCaseControlMode

    def getMarker(self):
        return b'bomber'


class _ReplayReconItem(_ReplayOrderItem):

    def getMarker(self):
        return b'recon'


class _ReplaySmokeItem(_ReplayOrderItem):

    def getMarker(self):
        return b'smoke'


class _ReplayMineFieldItem(_ReplayOrderItem):

    def getAimingControlMode(self):
        from AvatarInputHandler.MapCaseMode import ArcadeMapCaseControlMode
        return ArcadeMapCaseControlMode


class _ReplayAfterburningItem(_ReplayItem):
    __slots__ = (b'__totalDeployingTime', b'__totalConsumingTime', b'__totalRechargingTime', b'__totalCooldownTime', b'_prevTimeRemaining', b'__fullyChargedSoundCbId', b'__almostChargedSoundCbId', b'__almostChargedSound', b'__playingSoundObj', b'_animationType', b'_totalTime')
    _FULL_CHARGE_DELAY_SOUND_TIME = 5.0
    _ALMOST_CHARGED_SOUND_ID = b'be_pre_replenishment'
    _EXAUSTED_SOUND_ID = b'be_nitro_empty'
    _STOPPED_BY_USER_SOUND_ID = b'be_nitro_stop'
    _ACTIVATED_SOUND_ID = b'be_nitro_activating'

    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
        self.__totalDeployingTime = descriptor.deploySeconds
        self.__totalConsumingTime = descriptor.consumeSeconds
        self.__totalRechargingTime = descriptor.rechargeSeconds
        self.__totalCooldownTime = descriptor.cooldownSeconds
        self._prevTimeRemaining = -1
        self.__fullyChargedSoundCbId = None
        self.__almostChargedSoundCbId = None
        self.__almostChargedSound = None
        self.__playingSoundObj = None
        super(_ReplayAfterburningItem, self).__init__(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        return

    def getTags(self):
        return (b'afterburning',)

    def clear(self):
        super(_ReplayAfterburningItem, self).clear()
        if self.__playingSoundObj and self.__playingSoundObj.isPlaying:
            self.__playingSoundObj.stop()
        self.__playingSoundObj = None
        if self.__fullyChargedSoundCbId is not None:
            BigWorld.cancelCallback(self.__fullyChargedSoundCbId)
        if self.__almostChargedSoundCbId is not None:
            BigWorld.cancelCallback(self.__almostChargedSoundCbId)
        return

    def update(self, quantity, stage, timeRemaining, totalTime):
        self._prevTimeRemaining = self._timeRemaining
        if self._stage != stage and self._stage in (EQUIPMENT_STAGES.READY, EQUIPMENT_STAGES.PREPARING):
            self._cleanReadyStageSounds()
        super(_ReplayAfterburningItem, self).update(quantity, stage, timeRemaining, totalTime)
        if stage == EQUIPMENT_STAGES.ACTIVE and self._prevStage != EQUIPMENT_STAGES.ACTIVE:
            self._animationType = ANIMATION_TYPES.MOVE_GREEN_BAR_DOWN | ANIMATION_TYPES.CENTER_COUNTER | ANIMATION_TYPES.GREEN_GLOW_SHOW | ANIMATION_TYPES.DARK_COLOR_TRANSFORM
            totalTime = self.__totalConsumingTime
            self.__createAndPlaySound(self._ACTIVATED_SOUND_ID)
        elif stage == EQUIPMENT_STAGES.PREPARING:
            self._animationType = ANIMATION_TYPES.MOVE_GREEN_BAR_UP | ANIMATION_TYPES.SHOW_COUNTER_GREEN
            if self._prevStage != stage and self._prevStage != EQUIPMENT_STAGES.COOLDOWN:
                self._animationType |= ANIMATION_TYPES.GREEN_GLOW_HIDE
            totalTime = self.__totalRechargingTime
            self.__processReadyStateSounds(timeRemaining)
            if self._prevStage == EQUIPMENT_STAGES.ACTIVE:
                self.__playSoundOnce(self._STOPPED_BY_USER_SOUND_ID)
        elif stage == EQUIPMENT_STAGES.DEPLOYING:
            self._animationType = ANIMATION_TYPES.MOVE_ORANGE_BAR_UP | ANIMATION_TYPES.SHOW_COUNTER_ORANGE
            totalTime = self.__totalDeployingTime
        elif stage == EQUIPMENT_STAGES.COOLDOWN:
            self._animationType = ANIMATION_TYPES.MOVE_ORANGE_BAR_UP | ANIMATION_TYPES.SHOW_COUNTER_ORANGE | ANIMATION_TYPES.FILL_PARTIALLY
            totalTime = self.__totalCooldownTime
            if self._prevStage == EQUIPMENT_STAGES.ACTIVE:
                self.__playSoundOnce(self._EXAUSTED_SOUND_ID)
        elif stage == EQUIPMENT_STAGES.READY and self.becomeReady:
            self.__processReadyStateSounds(timeRemaining)
        self._totalTime = totalTime
        return

    def canActivate(self, entityName=None, avatar=None):
        result, error = False, None
        if self._stage in (EQUIPMENT_STAGES.READY, EQUIPMENT_STAGES.PREPARING, EQUIPMENT_STAGES.ACTIVE):
            result = True
        elif self._stage == EQUIPMENT_STAGES.COOLDOWN:
            error = InCooldownError(self._descriptor.userString)
        elif self._stage == EQUIPMENT_STAGES.DEPLOYING:
            error = NotReadyError(self._descriptor.userString)
        return (result, error)

    def getEntitiesIterator(self, avatar=None):
        return []

    @property
    def becomeReady(self):
        return super(_ReplayAfterburningItem, self).becomeReady

    def _soundUpdate(self, prevQuantity, quantity):
        return

    def _cleanReadyStageSounds(self):
        self.__cleanFullReadySound()
        self.__cleanAlmostReadySound()
        return

    def _playChargedSound(self):
        EquipmentSound.playReady(self)
        self.__fullyChargedSoundCbId = None
        return

    def _playAlmostChargedSound(self):
        if self.__almostChargedSound is None:
            self.__almostChargedSound = SoundGroups.g_instance.getSound2D(self._ALMOST_CHARGED_SOUND_ID)
        else:
            self.__almostChargedSound.stop()
        self.__almostChargedSound.play()
        self.__almostChargedSoundCbId = None
        return

    def __processReadyStateSounds(self, timeRemaining):
        if timeRemaining > -1:
            self.__cleanFullReadySound()
            self.__fullyChargedSoundCbId = BigWorld.callback(timeRemaining, self._playChargedSound)
            if timeRemaining >= self._FULL_CHARGE_DELAY_SOUND_TIME:
                self.__cleanAlmostReadySound()
                if self.__almostChargedSound is not None:
                    self.__almostChargedSound.stop()
                self.__almostChargedSoundCbId = BigWorld.callback(timeRemaining - self._FULL_CHARGE_DELAY_SOUND_TIME, self._playAlmostChargedSound)
        elif self.becomeReady:
            self.__cleanFullReadySound()
            self._playChargedSound()
        return

    def __cleanAlmostReadySound(self):
        if self.__almostChargedSoundCbId is not None:
            BigWorld.cancelCallback(self.__almostChargedSoundCbId)
            self.__almostChargedSoundCbId = None
        return

    def __cleanFullReadySound(self):
        if self.__fullyChargedSoundCbId is not None:
            BigWorld.cancelCallback(self.__fullyChargedSoundCbId)
            self.__fullyChargedSoundCbId = None
        return

    def __playSoundOnce(self, sound):
        SoundGroups.g_instance.getSound2D(sound)
        return

    def __createAndPlaySound(self, sound):
        self.__playingSoundObj = SoundGroups.g_instance.getSound2D(sound)
        self.__playingSoundObj.play()
        return


class _ReplayLargeRepairKitBattleRoyaleItem(_ReplayItem):
    __slots__ = (b'__totalCooldownTime',)

    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
        self.__totalCooldownTime = descriptor.cooldownSeconds
        super(_ReplayLargeRepairKitBattleRoyaleItem, self).__init__(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        return

    def update(self, quantity, stage, timeRemaining, totalTime):
        super(_ReplayLargeRepairKitBattleRoyaleItem, self).update(quantity, stage, timeRemaining, totalTime)
        if stage == EQUIPMENT_STAGES.COOLDOWN:
            totalTime = self.__totalCooldownTime
        self._totalTime = totalTime
        return


class _ReplayRegenerationKitBattleRoyaleItem(_ReplayItem):
    __slots__ = (b'__totalCooldownTime', b'__healTime')

    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
        self.__totalCooldownTime = descriptor.cooldownSeconds
        self.__healTime = descriptor.healTime
        super(_ReplayRegenerationKitBattleRoyaleItem, self).__init__(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        return

    def update(self, quantity, stage, timeRemaining, totalTime):
        super(_ReplayRegenerationKitBattleRoyaleItem, self).update(quantity, stage, timeRemaining, totalTime)
        if stage == EQUIPMENT_STAGES.COOLDOWN:
            totalTime = self.__totalCooldownTime
            self._animationType = ANIMATION_TYPES.MOVE_ORANGE_BAR_UP | ANIMATION_TYPES.SHOW_COUNTER_ORANGE | ANIMATION_TYPES.FILL_PARTIALLY
        elif stage == EQUIPMENT_STAGES.ACTIVE:
            totalTime = self.__healTime
            self._animationType = ANIMATION_TYPES.MOVE_GREEN_BAR_DOWN | ANIMATION_TYPES.SHOW_COUNTER_GREEN | ANIMATION_TYPES.FILL_PARTIALLY
        self._totalTime = totalTime
        return


class _ReplayPoiEquipmentItemVS(_ReplayItem, _PoiEquipmentItemVS):

    def _getErrorMsg(self):
        return _PoiEquipmentItemVS._getErrorMsg(self)

    def getAnimationType(self):
        return _PoiEquipmentItemVS.getAnimationType(self)

    def update(self, quantity, stage, timeRemaining, totalTime):
        return _PoiEquipmentItemVS.update(self, quantity, stage, timeRemaining, totalTime)


class _ReplayPoiArtilleryItem(_ReplayItem, _PoiArtilleryItem):

    def _getErrorMsg(self):
        return _PoiArtilleryItem.getErrorMsg(self)

    def canActivate(self, entityName=None, avatar=None):
        return _PoiArtilleryItem.canActivate(entityName, avatar)


class _ReplayRoleSkillVSItem(_ReplayItem, _RoleSkillVSItem):

    def getAnimationType(self):
        return _RoleSkillVSItem.getAnimationType(self)

    def update(self, quantity, stage, timeRemaining, totalTime):
        _ReplayItem.update(self, quantity, stage, timeRemaining, totalTime)
        _RoleSkillVSItem.update(self, quantity, stage, timeRemaining, totalTime)
        return

    def canActivate(self, entityName=None, avatar=None):
        return _RoleSkillVSItem.canActivate(self, entityName, avatar)

    def _getErrorMsg(self):
        return _RoleSkillVSItem._getErrorMsg(self)


class _ReplayAbilitySkillVSItem(_ReplayItem, _AbilitySkillVSItem):

    def _soundUpdate(self, prevQuantity, quantity):
        _ReplayItem._soundUpdate(self, prevQuantity, quantity)
        _AbilitySkillVSItem._soundUpdate(self, prevQuantity, quantity)
        return

    def getAnimationType(self):
        return _AbilitySkillVSItem.getAnimationType(self)

    def update(self, quantity, stage, timeRemaining, totalTime):
        _ReplayItem.update(self, quantity, stage, timeRemaining, totalTime)
        _AbilitySkillVSItem.update(self, quantity, stage, timeRemaining, totalTime)
        return

    def canActivate(self, entityName=None, avatar=None):
        return _AbilitySkillVSItem.canActivate(self, entityName, avatar)

    def _getErrorMsg(self):
        return _AbilitySkillVSItem._getErrorMsg(self)


class _ReplayAbilitySkillItem(_ReplayItem, _AbilitySkillItem):

    def _soundUpdate(self, prevQuantity, quantity):
        _ReplayItem._soundUpdate(self, prevQuantity, quantity)
        _AbilitySkillItem._soundUpdate(self, prevQuantity, quantity)
        return

    def getAnimationType(self):
        return _AbilitySkillItem.getAnimationType(self)

    def update(self, quantity, stage, timeRemaining, totalTime):
        _ReplayItem.update(self, quantity, stage, timeRemaining, totalTime)
        _AbilitySkillItem.update(self, quantity, stage, timeRemaining, totalTime)
        return

    def canActivate(self, entityName=None, avatar=None):
        return _AbilitySkillItem.canActivate(self, entityName, avatar)

    def _getErrorMsg(self):
        return _AbilitySkillItem._getErrorMsg(self)


class _ReplayRoleSkillArtyVSItem(_ReplayRoleSkillVSItem):

    def getMarker(self):
        return b'artillery_fort_ally'


def _replayComp7ItemFactory(descriptor, quantity, stage, timeRemaining, totalTime, tag=None):
    if descriptor.name.startswith(b'comp7_redline'):
        itemClass = _ReplayRoleSkillArtyVSItem
    else:
        itemClass = _ReplayRoleSkillVSItem
    return itemClass(descriptor, quantity, stage, timeRemaining, totalTime, tag)


def _replayPoiItemFactory(descriptor, quantity, stage, timeRemaining, totalTime, tag=None):
    if descriptor.name.startswith(b'poi_artillery_aoe'):
        itemClass = _ReplayPoiArtilleryItem
    elif descriptor.name.startswith(b'poi_smoke'):
        itemClass = _ReplaySmokeItem
    elif descriptor.name.startswith(b'poi_minefield'):
        itemClass = _ReplayMineFieldItem
    else:
        itemClass = _ReplayPoiEquipmentItemVS
    return itemClass(descriptor, quantity, stage, timeRemaining, totalTime, tag)


def _replayTriggerItemFactory(descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
    if descriptor.name.startswith(b'arcade_artillery'):
        return _ReplayArcadeArtilleryItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'artillery_epic'):
        return _ReplayArcadeArtilleryItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'artillery_aoe_fort'):
        return _ReplayArtilleryAOEFort(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'arcade_bomber'):
        return _ReplayBomberItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'arcade_minefield'):
        return _ReplayOrderItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'artillery'):
        return _ReplayArtilleryItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'bomber'):
        return _ReplayBomberItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'recon'):
        return _ReplayReconItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'smoke'):
        return _ReplaySmokeItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'arcade_smoke'):
        return _ReplaySmokeItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.endswith(b'afterburning'):
        return _ReplayAfterburningItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'large_repairkit_battle_royale'):
        return _ReplayLargeRepairKitBattleRoyaleItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'regenerationKit'):
        return _ReplayRegenerationKitBattleRoyaleItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    if descriptor.name.startswith(b'spawn_kamikaze'):
        return _ReplayOrderItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
    return _ReplayItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)


_REPLAY_EQUIPMENT_TAG_TO_ITEM = {(b'fuel',): _ReplayItem, 
   (b'stimulator',): _ReplayItem, 
   (b'trigger',): _replayTriggerItemFactory, 
   (b'extinguisher',): _ReplayExtinguisherItem, 
   (b'medkit',): _ReplayMedKitItem, 
   (b'repairkit',): _ReplayRepairKitItem, 
   (b'regenerationKit',): _replayTriggerItemFactory, 
   (b'medkit', b'repairkit'): _replayTriggerItemFactory, 
   (ROLE_EQUIPMENT_TAG,): _replayComp7ItemFactory, 
   (b'visualScriptAbilityEquipment',): _ReplayAbilitySkillVSItem, 
   (POI_EQUIPMENT_TAG,): _replayPoiItemFactory, 
   (b'abilityEquipment',): _ReplayAbilitySkillItem}

class EquipmentsReplayPlayer(EquipmentsController):
    __slots__ = (b'__callbackID', b'__callbackTimeID', b'__percentGetters', b'__percents', b'__timeGetters', b'__times')

    def __init__(self, setup):
        super(EquipmentsReplayPlayer, self).__init__(setup)
        self.__callbackID = None
        self.__callbackTimeID = None
        self.__percentGetters = {}
        self.__percents = {}
        self.__timeGetters = {}
        self.__times = {}
        return

    def clear(self, leave=True):
        if leave:
            if self.__callbackID is not None:
                BigWorld.cancelCallback(self.__callbackID)
                self.__callbackID = None
            if self.__callbackTimeID is not None:
                BigWorld.cancelCallback(self.__callbackTimeID)
                self.__callbackTimeID = None
            self.__percents.clear()
            self.__percentGetters.clear()
            self.__times.clear()
            self.__timeGetters.clear()
        super(EquipmentsReplayPlayer, self).clear(leave)
        return

    @MethodsRules.delayable(b'notifyPlayerVehicleSet')
    def setEquipment(self, intCD, quantity, stage, timeRemaining, totalTime):
        super(EquipmentsReplayPlayer, self).setEquipment(intCD, quantity, stage, timeRemaining, totalTime)
        self.__percents.pop(intCD, None)
        self.__percentGetters.pop(intCD, None)
        self.__times.pop(intCD, None)
        self.__timeGetters.pop(intCD, None)
        if stage in (EQUIPMENT_STAGES.DEPLOYING,
         EQUIPMENT_STAGES.COOLDOWN,
         EQUIPMENT_STAGES.SHARED_COOLDOWN,
         EQUIPMENT_STAGES.ACTIVE) or stage == EQUIPMENT_STAGES.READY and self.getEquipment(intCD).getTimeRemaining():
            equipment = self._equipments[intCD]
            self.__percentGetters[intCD] = equipment.getCooldownPercents
            if self.__callbackID is not None:
                BigWorld.cancelCallback(self.__callbackID)
                self.__callbackID = None
            if equipment.getTotalTime() > 0:
                self.__timeGetters[intCD] = equipment.getReplayTimeRemaining
                if self.__callbackTimeID is not None:
                    BigWorld.cancelCallback(self.__callbackTimeID)
                    self.__callbackTimeID = None
            self.__timeLoop()
            self.__timeLoopInSeconds()
        return

    @classmethod
    def createItem(cls, descriptor, quantity, stage, timeRemaining, totalTime):
        item = cls._findExtendItem(True, descriptor.name, descriptor, quantity, stage, timeRemaining, totalTime)
        if item:
            return item
        tags, clazz = _getInitialTagsAndClass(descriptor, _REPLAY_EQUIPMENT_TAG_TO_ITEM)
        if tags:
            item = clazz(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        else:
            item = _ReplayItem(descriptor, quantity, stage, timeRemaining, totalTime, tags)
        return item

    def getActivationCode(self, intCD, entityName=None, avatar=None):
        return

    def canActivate(self, intCD, entityName=None, avatar=None):
        return (False, None)

    def changeSetting(self, intCD, entityName=None, avatar=None):
        return (False, None)

    def changeSettingByTag(self, tag, entityName=None, avatar=None):
        return (False, None)

    def __timeLoop(self):
        self.__callbackID = None
        self.__tick()
        self.__callbackID = BigWorld.callback(0.1, self.__timeLoop)
        return

    def __timeLoopInSeconds(self):
        self.__callbackTimeID = None
        self.__tickInSeconds()
        self.__callbackTimeID = BigWorld.callback(1, self.__timeLoopInSeconds)
        return

    def __tick(self):
        for intCD, percentGetter in self.__percentGetters.iteritems():
            percent = percentGetter()
            currentPercent = self.__percents.get(intCD)
            if currentPercent != percent:
                self.__percents[intCD] = percent
                self.onEquipmentCooldownInPercent(intCD, percent)

        return

    def __tickInSeconds(self):
        for intCD, timeGetter in self.__timeGetters.iteritems():
            time = timeGetter()
            currentTime = self.__times.get(intCD)
            if currentTime != time:
                isBaseTime = False
                if self._equipments.has_key(intCD):
                    isBaseTime = self._equipments[intCD].getStage() == EQUIPMENT_STAGES.ACTIVE
                self.__times[intCD] = time
                self.onEquipmentCooldownTime(intCD, time, isBaseTime, time == 0)

        return


__all__ = (
 b'EquipmentsController',
 b'EquipmentsReplayPlayer')
