from __future__ import absolute_import, division
import functools, logging, BigWorld, CGF, Triggers, UIComponents
from cgf_script.registration import ComponentProperty as CompProp, registerComponent
from constants import IS_CLIENT, IS_CGF_DUMP, IS_EDITOR
from helpers import dependency
from hints.battle import manager as battleHintsModelsMgr
from PlayerEvents import g_playerEvents
from helpers import isPlayerAvatar
from GenericComponents import TimedActivatedComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional
if IS_CLIENT:
    from skeletons.gui.battle_session import IBattleSessionProvider
    from gui.battle_control import avatar_getter
else:
    avatar_getter = None

    class IBattleSessionProvider(object):
        pass


if IS_EDITOR or IS_CGF_DUMP:

    class Vehicle(object):
        pass


else:
    from Vehicle import Vehicle
_logger = logging.getLogger(__name__)

def _isAvatarReady():
    return isPlayerAvatar() and BigWorld.player().userSeesWorld()


class RandomEventZoneUINotificationType(object):
    DANGER_ZONE = b'dangerZone'
    WARNING_ZONE = b'warningZone'
    MAP_DEATH_ZONE = b'mapDeathZone'


class WeatherZoneUINotificationType(object):
    BLIZZARD_ZONE = b'blizzardZone'
    FIRE_ZONE = b'fireZone'
    FOG_ZONE = b'fogZone'
    RAIN_ZONE = b'rainZone'
    SANDSTORM_ZONE = b'sandstormZone'
    SMOKE_ZONE = b'smokeZone'
    TORNADO_ZONE = b'tornadoZone'


@registerComponent
class ZoneMarker(object):
    category = b'UI'
    editorTitle = b'Zone Marker'
    domain = CGF.Domain.ClientEditor
    isVisibleOnMinimap = CompProp(type=CGF.PropertyType.Bool, value=True, editorName=b'Visible on minimap')
    isVisibleOn3DScene = CompProp(type=CGF.PropertyType.Bool, value=False, editorName=b'Visible on 3D scene')
    reduceDuration = CompProp(type=CGF.PropertyType.Float, value=0.0, editorName=b'Duration reduce')

    def __init__(self):
        super(ZoneMarker, self).__init__()
        self.id = None
        self.startTime = 0
        self.finishTime = 0
        return

    @property
    def duration(self):
        return max(self.finishTime - self.startTime, 0)

    @property
    def markerProgress(self):
        if self.isActive():
            restTime = self.finishTime - BigWorld.serverTime()
            if self.duration and restTime > 0:
                return float(restTime) / self.duration * 100
        return 0.0

    def isActive(self):
        return self.finishTime >= BigWorld.serverTime() >= self.startTime


@registerComponent
class WeatherZoneUINotification(object):
    category = b'UI'
    editorTitle = b'Zone with weather UI Notification'
    domain = CGF.Domain.ClientEditor
    trigger = CompProp(type=CGF.PropertyType.Link, editorName=b'Trigger', value=Triggers.AreaTriggerComponent)
    zoneType = CompProp(type=CGF.PropertyType.String, editorName=b'Zone Type', value=WeatherZoneUINotificationType.BLIZZARD_ZONE, annotations={b'comboBox': {(WeatherZoneUINotificationType.BLIZZARD_ZONE): (WeatherZoneUINotificationType.BLIZZARD_ZONE), 
                     (WeatherZoneUINotificationType.FIRE_ZONE): (WeatherZoneUINotificationType.FIRE_ZONE), 
                     (WeatherZoneUINotificationType.FOG_ZONE): (WeatherZoneUINotificationType.FOG_ZONE), 
                     (WeatherZoneUINotificationType.RAIN_ZONE): (WeatherZoneUINotificationType.RAIN_ZONE), 
                     (WeatherZoneUINotificationType.SANDSTORM_ZONE): (WeatherZoneUINotificationType.SANDSTORM_ZONE), 
                     (WeatherZoneUINotificationType.SMOKE_ZONE): (WeatherZoneUINotificationType.SMOKE_ZONE), 
                     (WeatherZoneUINotificationType.TORNADO_ZONE): (WeatherZoneUINotificationType.TORNADO_ZONE)}})

    def __init__(self):
        super(WeatherZoneUINotification, self).__init__()
        self.id = None
        self.enterReactionID = None
        self.exitReactionID = None
        self.inZoneVehicles = set([])
        return


def getHints():
    if IS_CGF_DUMP:
        return {}
    battleHintsModelsMgr.init()
    return {v.uniqueName: v.uniqueName for v in battleHintsModelsMgr.get().getAll()}


@registerComponent
class ZoneHint(object):
    category = b'UI'
    editorTitle = b'Zone hint'
    domain = CGF.Domain.ClientEditor
    trigger = CompProp(type=CGF.PropertyType.Link, editorName=b'Trigger', value=Triggers.AreaTriggerComponent)
    hintUniqName = CompProp(type=CGF.PropertyType.String, editorName=b'zone battle hint', value=b'', annotations={b'comboBox': (getHints())})

    def __init__(self):
        super(ZoneHint, self).__init__()
        self.id = None
        self.enterReactionID = None
        self.exitReactionID = None
        self.inZoneVehicles = set([])
        return


@registerComponent
class RandomEventZoneUINotification(object):
    category = b'UI'
    editorTitle = b'Zone with timer UI Notification'
    domain = CGF.Domain.ClientEditor
    trigger = CompProp(type=CGF.PropertyType.Link, editorName=b'Trigger', value=Triggers.AreaTriggerComponent)
    zoneType = CompProp(type=CGF.PropertyType.String, editorName=b'Zone Type', value=RandomEventZoneUINotificationType.DANGER_ZONE, annotations={b'comboBox': {(RandomEventZoneUINotificationType.WARNING_ZONE): (RandomEventZoneUINotificationType.WARNING_ZONE), 
                     (RandomEventZoneUINotificationType.DANGER_ZONE): (RandomEventZoneUINotificationType.DANGER_ZONE), 
                     (RandomEventZoneUINotificationType.MAP_DEATH_ZONE): (RandomEventZoneUINotificationType.MAP_DEATH_ZONE)}})

    def __init__(self):
        super(RandomEventZoneUINotification, self).__init__()
        self.id = None
        self.startTime = 0
        self.finishTime = 0
        self.enterReactionID = None
        self.exitReactionID = None
        self.inZoneVehicles = set([])
        return

    def isActive(self):
        return self.finishTime >= BigWorld.serverTime()


class MapZoneSystem(CGF.System):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    RandomEventUINotificationsActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(RandomEventZoneUINotification))
    RandomEventUINotificationsDeactivated = CGF.DeactivateReaction(CGF.ReactRw(RandomEventZoneUINotification))
    RandomEventUINotificationsIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(RandomEventZoneUINotification))
    RandomEventUIAndTimerActivated = CGF.ActivateReaction(CGF.Rw(RandomEventZoneUINotification), CGF.ReactRo(TimedActivatedComponent))
    RandomEventUINotificationsAccess = CGF.AccessReaction(CGF.Rw(RandomEventZoneUINotification))
    WeatherUINotificationsActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(WeatherZoneUINotification))
    WeatherUINotificationsDeactivated = CGF.DeactivateReaction(CGF.ReactRw(WeatherZoneUINotification))
    WeatherUINotificationsIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(WeatherZoneUINotification))
    WeatherUINotificationsAccess = CGF.AccessReaction(CGF.Rw(WeatherZoneUINotification))
    ZoneHintsIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(ZoneHint))
    ZoneHintsActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(ZoneHint))
    ZoneHintsDeactivated = CGF.DeactivateReaction(CGF.ReactRw(ZoneHint))
    ZoneHintsAccess = CGF.AccessReaction(CGF.Rw(ZoneHint))
    ZoneMarkerActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(ZoneMarker), CGF.TransformComponent)
    ZoneMarkerDeactivated = CGF.DeactivateReaction(CGF.ReactRw(ZoneMarker))
    ZoneMarkerIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(ZoneMarker))
    ZoneMarkerAndTimerActivated = CGF.ActivateReaction(CGF.Rw(ZoneMarker), CGF.ReactRo(TimedActivatedComponent))
    ZoneMarkerAccess = CGF.AccessReaction(CGF.Rw(ZoneMarker))
    MinimapChangerActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(UIComponents.MinimapChangerComponent))
    MinimapChangerDeactivated = CGF.DeactivateReaction(CGF.ReactRw(UIComponents.MinimapChangerComponent))
    MinimapChangerAccess = CGF.AccessReaction(CGF.Rw(UIComponents.MinimapChangerComponent))
    VehicleAccess = CGF.AccessReaction(CGF.Rw(Vehicle))
    AreaTriggerAccess = CGF.AccessReaction(CGF.Rw(Triggers.AreaTriggerComponent))
    Reactions = CGF.Reactions(RandomEventUINotificationsIterate, WeatherUINotificationsIterate, ZoneHintsIterate, ZoneMarkerActivated, ZoneMarkerDeactivated, ZoneMarkerIterate, ZoneMarkerAccess, RandomEventUINotificationsActivated, RandomEventUINotificationsDeactivated, RandomEventUINotificationsAccess, WeatherUINotificationsActivated, WeatherUINotificationsDeactivated, WeatherUINotificationsAccess, ZoneHintsActivated, ZoneHintsDeactivated, ZoneHintsAccess, MinimapChangerActivated, MinimapChangerDeactivated, MinimapChangerAccess, RandomEventUIAndTimerActivated, ZoneMarkerAndTimerActivated, VehicleAccess, AreaTriggerAccess)

    def __init__(self):
        super(MapZoneSystem, self).__init__()
        self.__subscriptionsCount = 0
        return

    def onMappingLoaded(self):
        if _isAvatarReady():
            self.__onAvatarReady()
        else:
            g_playerEvents.onAvatarReady += self.__onAvatarReady
        return

    def onMappingUnloaded(self):
        self.__subscriptionsCount = 0
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        if BigWorld.player() and isPlayerAvatar():
            BigWorld.player().onVehicleLeaveWorld -= self.__onVehicleLeaveWorld
        return

    def commonUpdate(self):
        triggerAccess = self.reaction(self.AreaTriggerAccess)
        for marker in self.reaction(self.ZoneMarkerDeactivated):
            _logger.debug(b'on maker from zone removed')
            mapZones = self.__guiSessionProvider.shared.mapZones
            if mapZones:
                mapZones.removeMarkerFromZone(marker)

        for notification in self.reaction(self.RandomEventUINotificationsDeactivated):
            _logger.debug(b'on random event zone removed')
            self.__unsubscribeTrigger(notification, triggerAccess)
            mapZones = self.__guiSessionProvider.shared.mapZones
            if mapZones:
                mapZones.removeRandomEventZone(notification)

        for notification in self.reaction(self.WeatherUINotificationsDeactivated):
            _logger.debug(b'on weather zone removed')
            self.__unsubscribeTrigger(notification, triggerAccess)
            mapZones = self.__guiSessionProvider.shared.mapZones
            if mapZones:
                mapZones.removeWeatherZone(notification)

        for hint in self.reaction(self.ZoneHintsDeactivated):
            _logger.debug(b'on zone hint removed')
            self.__unsubscribeTrigger(hint, triggerAccess)

        for changer in self.reaction(self.MinimapChangerDeactivated):
            _logger.debug(b'on transformed zone removed: %s', changer.layerId)
            mapZones = self.__guiSessionProvider.shared.mapZones
            if mapZones:
                mapZones.removeTransformedZone(changer)

        minimapChangerAccess = self.reaction(self.MinimapChangerAccess)
        for go, changer in self.reaction(self.MinimapChangerActivated):
            _logger.debug(b'on transformed zone added: %s', changer.layerId)
            mapZones = self.__guiSessionProvider.shared.mapZones
            if mapZones:
                mapZones.addTransformedZone((lambda go=go: minimapChangerAccess.find(go)))

        for zone, timed in self.reaction(self.ZoneMarkerAndTimerActivated):
            reduce = max(zone.reduceDuration, 0.0)
            zone.startTime = timed.serverStartTime
            zone.finishTime = max(timed.serverStartTime, timed.serverEndTime - reduce)

        for zone, timed in self.reaction(self.RandomEventUIAndTimerActivated):
            zone.startTime = timed.serverStartTime
            zone.finishTime = timed.serverEndTime

        for go, hint in self.reaction(self.ZoneHintsActivated):
            _logger.debug(b'on zone hint added')
            self.__subscribeTrigger(go, hint, self.ZoneHintsAccess, triggerAccess, self.__onEnterZoneHint, self.__onExitZoneHint)

        for go, notification in self.reaction(self.WeatherUINotificationsActivated):
            _logger.debug(b'on weather zone added')
            self.__subscribeTrigger(go, notification, self.WeatherUINotificationsAccess, triggerAccess, self.__onEnterWeatherZone, self.__onExitWeatherZone)

        for go, notification in self.reaction(self.RandomEventUINotificationsActivated):
            _logger.debug(b'on random event zone added')
            self.__subscribeTrigger(go, notification, self.RandomEventUINotificationsAccess, triggerAccess, self.__onEnterRandomEventZone, self.__onExitRandomEventZone)

        zoneMarkerAccess = self.reaction(self.ZoneMarkerAccess)
        for go, marker, tr in self.reaction(self.ZoneMarkerActivated):
            _logger.debug(b'on marker to zone added')
            marker.id = go.id
            mapZones = self.__guiSessionProvider.shared.mapZones
            if mapZones:
                mapZones.addMarkerToZone((lambda go=go: zoneMarkerAccess.find(go)), tr.worldTransform)

        return

    def periodUpdate(self):
        for marker in self.reaction(self.ZoneMarkerIterate):
            _logger.debug(b'on marker updated')
            mapZones = self.__guiSessionProvider.shared.mapZones
            if mapZones:
                mapZones.onMarkerProgressUpdated(marker)

        return

    def __subscribeTrigger(self, go, zone, zoneAccessType, triggerAccess, enterCallback, exitCallback):
        zone.id = go.id
        trigger = triggerAccess.find(zone.trigger)
        if trigger:
            self.__subscribeVehicleChanges()
            zone.enterReactionID = trigger.addEnterReaction(functools.partial(self.__onEnterZone, go, enterCallback, zoneAccessType))
            zone.exitReactionID = trigger.addExitReaction(functools.partial(self.__onExitZone, go, exitCallback, zoneAccessType))
        return

    def __unsubscribeTrigger(self, zone, triggerAccess):
        trigger = triggerAccess.find(zone.trigger)
        if trigger:
            self.__unsubscribeVehicleChanges()
            if zone.enterReactionID:
                trigger.removeEnterReaction(zone.enterReactionID)
            if zone.exitReactionID:
                trigger.removeExitReaction(zone.exitReactionID)
        return

    def __onEnterZone(self, go, enterCallback, zoneAccessType, who, _):
        zoneAccess = self.reaction(zoneAccessType)
        vehicleAccess = self.reaction(self.VehicleAccess)
        vehicle = CGF.findParentWithReaction(who, vehicleAccess)
        zone = zoneAccess.find(go)
        if vehicle and zone and zone is not None:
            zone.inZoneVehicles.add(vehicle.id)
            if vehicle.id == avatar_getter.getVehicleIDAttached() and vehicle.isAlive():
                enterCallback(zone)
        return

    def __onExitZone(self, go, exitCallback, zoneAccessType, who, _):
        zoneAccess = self.reaction(zoneAccessType)
        vehicleAccess = self.reaction(self.VehicleAccess)
        vehicle = CGF.findParentWithReaction(who, vehicleAccess)
        zone = zoneAccess.find(go)
        if vehicle and zone and zone is not None:
            zone.inZoneVehicles.discard(vehicle.id)
            if vehicle.id == avatar_getter.getVehicleIDAttached():
                exitCallback(zone)
        return

    def __onEnterRandomEventZone(self, zoneNotification):
        _logger.debug(b'on enter random event zone')
        mapZones = self.__guiSessionProvider.shared.mapZones
        if mapZones and zoneNotification.isActive():
            mapZones.enterRandomEventZone(zoneNotification)
        return

    def __onExitRandomEventZone(self, zoneNotification):
        _logger.debug(b'on exit random event zone')
        mapZones = self.__guiSessionProvider.shared.mapZones
        if mapZones:
            mapZones.exitRandomEventZone(zoneNotification)
        return

    def __onEnterWeatherZone(self, zoneNotification):
        _logger.debug(b'on enter weather zone')
        mapZones = self.__guiSessionProvider.shared.mapZones
        if mapZones:
            mapZones.enterWeatherZone(zoneNotification)
        return

    def __onExitWeatherZone(self, zoneNotification):
        _logger.debug(b'on exit weather zone')
        mapZones = self.__guiSessionProvider.shared.mapZones
        if mapZones:
            mapZones.exitWeatherZone(zoneNotification)
        return

    def __onEnterZoneHint(self, zoneHint):
        _logger.debug(b'on enter zone hint')
        controller = self.__guiSessionProvider.dynamic.battleHints
        if controller:
            controller.showHint(hintName=zoneHint.hintUniqName)
        else:
            _logger.warning(b'No battle hints controller on show hint call.')
        return

    def __onExitZoneHint(self, zoneHint):
        _logger.debug(b'on exit zone hint')
        controller = self.__guiSessionProvider.dynamic.battleHints
        if controller:
            controller.removeHint(hintName=zoneHint.hintUniqName, hide=True)
        else:
            _logger.warning(b'No battle hints controller on hide hint call.')
        return

    def __subscribeVehicleChanges(self):
        player = BigWorld.player()
        if player:
            consistentMatrices = player.consistentMatrices
            if not self.__subscriptionsCount and consistentMatrices:
                consistentMatrices.onVehicleMatrixBindingChanged += self.__onVehicleChanged
            self.__subscriptionsCount += 1
        return

    def __unsubscribeVehicleChanges(self):
        player = BigWorld.player()
        if player:
            consistentMatrices = player.consistentMatrices
            self.__subscriptionsCount -= 1
            if not self.__subscriptionsCount and consistentMatrices:
                consistentMatrices.onVehicleMatrixBindingChanged -= self.__onVehicleChanged
        return

    def __onVehicleChanged(self, *args, **kwargs):
        avatarVehicle = BigWorld.player().getVehicleAttached()
        mapZones = self.__guiSessionProvider.shared.mapZones
        if avatarVehicle is None or not avatarVehicle.isAlive() or mapZones is None:
            return
        for reZone in sorted(self.reaction(self.RandomEventUINotificationsIterate), key=(lambda z: z.zoneType == RandomEventZoneUINotificationType.DANGER_ZONE), reverse=True):
            if avatarVehicle.id in reZone.inZoneVehicles:
                mapZones.enterRandomEventZone(reZone)

        for wZone in self.reaction(self.WeatherUINotificationsIterate):
            if avatarVehicle.id in wZone.inZoneVehicles:
                mapZones.enterWeatherZone(wZone)

        return

    def __onAvatarReady(self):
        BigWorld.player().onVehicleLeaveWorld += self.__onVehicleLeaveWorld
        return

    def __onVehicleLeaveWorld(self, vehicle):
        for reZone in self.reaction(self.RandomEventUINotificationsIterate):
            reZone.inZoneVehicles.discard(vehicle.id)

        for wZone in self.reaction(self.WeatherUINotificationsIterate):
            wZone.inZoneVehicles.discard(vehicle.id)

        for hintZone in self.reaction(self.ZoneHintsIterate):
            hintZone.inZoneVehicles.discard(vehicle.id)

        return
