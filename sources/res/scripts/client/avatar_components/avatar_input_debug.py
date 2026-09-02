import BigWorld, constants, pickle, Input, typing, logging
from Input import TriggerEvent
from gui.battle_control import event_dispatcher as gui_event_dispatcher
if typing.TYPE_CHECKING:
    from Avatar import PlayerAvatar
_logger = logging.getLogger(__name__)

class AvatarInputDebug(object):

    def __init__(self):
        self._profile = b'DEBUG_PLAYER_INPUT_PROFILE'
        return

    @property
    def _player(self):
        return BigWorld.player()

    def start(self):
        if not Input.inputSystem().hasProfile(self._profile):
            _logger.error(b'Input profile %s is not added.', self._profile)
            return
        self.__bindAction(b'ACTION_TOGGLE_GUI_VISIBILITY', self.__toggleGuiVisibility)
        self.__bindAction(b'ACTION_PLAYER_HEAL', self.__heal)
        self.__bindAction(b'ACTION_PLAYER_RELOAD_GUN', self.__reloadGun)
        self.__bindAction(b'ACTION_PLAYER_START_FIRE', self.__startFire)
        self.__bindAction(b'ACTION_PLAYER_EXPLODE', self.__explode)
        self.__bindAction(b'ACTION_PLAYER_BREAK_LEFT_TRACK', self.__breakLeftTrack)
        self.__bindAction(b'ACTION_PLAYER_BREAK_RIGHT_TRACK', self.__breakRightTrack)
        self.__bindAction(b'ACTION_PLAYER_DESTROY_SELF', self.__destroySelf)
        self.__bindAction(b'ACTION_PLAYER_KILL_ENGINE', self.__killEngine)
        self.__bindAction(b'ACTION_PLAYER_DAMAGE_DEVICE_AMMOBAYHEALTH', self.__damageDeviceAmmoBayHealth)
        self.__bindAction(b'ACTION_PLAYER_DAMAGE_DEVICE_FUELTANKHEALTH', self.__damageDeviceFuelTankHealth)
        self.__bindAction(b'ACTION_PLAYER_DAMAGE_DEVICE_ENGINEHEALTH', self.__damageDeviceEngineHealth)
        self.__bindAction(b'ACTION_PLAYER_DAMAGE_DEVICE_GUNHEALTH', self.__damageDeviceGunHealth)
        self.__bindAction(b'ACTION_TOGGLE_PIERCING_DEBUG_PANEL', self.__togglePiercingDebugPanel)
        self.__bindAction(b'ACTION_MAKE_SCREENSHOT', self.__makeScreenShot)
        self.__bindAction(b'ACTION_TOGGLE_CLIENT_FILTERS', self.__toggleClientFilters)
        self.__bindAction(b'ACTION_MOVE_VEHICLE', self.__moveVehicle)
        self.__bindAction(b'ACTION_PLAYER_PICKUP', self.__pickup)
        self.__bindAction(b'ACTION_PLAYER_HOT_RELOAD', self.__hotReload)
        self.__bindAction(b'ACTION_PLAYER_LOG_TKILL_RATINGS', self.__logTkillRatings)
        self.__bindAction(b'ACTION_TOGGLE_TELEPORT', self.__toggleTeleport)
        self.__bindAction(b'ACTION_PLAYER_RESPAWN_VEHICLE', self.__respawnVehicle)
        self.__bindAction(b'ACTION_PLAYER_PICKUP_ROLL', self.__pickupRoll)
        self.__bindAction(b'ACTION_PLAYER_CAPTURECLOSESTBASE', self.__captureClosestBase)
        self.__bindAction(b'ACTION_PLAYER_TELEPORTTOSHOTPOINT', self.__teleportToShotPoint)
        self.__bindAction(b'ACTION_PLAYER_SETSIGNAL', self.__setSignal)
        self.__bindAction(b'ACTION_PLAYER_NAVIGATETO', self.__navigateTo)
        self.__bindAction(b'ACTION_PLAYER_TOGGLEPAUSEAI', self.__togglePauseAI)
        self.__bindAction(b'ACTION_ADD_AREA_MARKER', self.__addAreaMarker)
        self.__bindAction(b'ACTION_REMOVE_ALL_MARKERS', self.__removeAllMarkers)
        self.__bindAction(b'ACTION_ADD_VEHICLE_MARKER', self.__addVehicleMarker)
        self.__bindAction(b'ACTION_PLAYER_KILLENEMYTEAM', self.__killEnemyTeam)
        self.__bindAction(b'ACTION_PLAYER_STUN', self.__stun)
        self.__bindAction(b'ACTION_PLAYER_KILL_TURRET', self.__killTurret)
        self.__bindAction(b'ACTION_PLAYER_KILL_TANKMAN', self.__killTankman)
        self.__bindAction(b'ACTION_PLAYER_SWITCH_SERVER_MARKER', self.__toggleShowServerMarker)
        Input.inputSystem().activateProfile(self._profile)
        return

    def stop(self):
        if Input.inputSystem().hasProfile(self._profile):
            Input.inputSystem().deactivateProfile(self._profile, unbindAllReactions=True)
        return

    def __bindAction(self, actionName, callback):
        action = Input.inputSystem().findAction(self._profile, actionName)
        if action:
            action.bindEventReaction(TriggerEvent.Triggered, callback)
            action.setPredicate(self.__predicate)
        return

    def __predicate(self):
        return constants.HAS_DEV_RESOURCES and self._player.userSeesWorld()

    def __toggleGuiVisibility(self):
        gui_event_dispatcher.toggleGUIVisibility()
        return

    def __heal(self):
        self._player.base.setDevelopmentFeature(0, b'heal', 0, b'')
        return

    def __reloadGun(self):
        self._player.base.setDevelopmentFeature(0, b'reload_gun', 0, b'')
        return

    def __startFire(self):
        self._player.base.setDevelopmentFeature(0, b'start_fire', 0, b'')
        return

    def __explode(self):
        self._player.base.setDevelopmentFeature(0, b'explode', 0, b'')
        return

    def __breakLeftTrack(self):
        self._player.base.setDevelopmentFeature(0, b'break_left_track', 0, b'')
        return

    def __breakRightTrack(self):
        self._player.base.setDevelopmentFeature(0, b'break_right_track', 0, b'')
        return

    def __destroySelf(self):
        self._player.base.setDevelopmentFeature(0, b'destroy_self', 0, b'')
        return

    def __killEngine(self):
        self._player.base.setDevelopmentFeature(0, b'kill_engine', 0, b'')
        return

    def __damageDeviceAmmoBayHealth(self):
        self._player.base.setDevelopmentFeature(0, b'damage_device', 500, b'ammoBayHealth')
        return

    def __damageDeviceFuelTankHealth(self):
        self._player.base.setDevelopmentFeature(0, b'damage_device', 500, b'fuelTankHealth')
        return

    def __damageDeviceEngineHealth(self):
        self._player.base.setDevelopmentFeature(0, b'damage_device', 500, b'engineHealth')
        return

    def __damageDeviceGunHealth(self):
        self._player.base.setDevelopmentFeature(0, b'damage_device', 500, b'gunHealth')
        return

    def __togglePiercingDebugPanel(self):
        gui_event_dispatcher.togglePiercingDebugPanel()
        return

    def __makeScreenShot(self):

        def makeScreenShot(fileType, fileMask):
            BigWorld.screenShot(fileType, fileMask)
            return

        makeScreenShot(fileType=b'jpg', fileMask=b'./../screenshots/')
        return

    def __toggleClientFilters(self):
        vehicle = BigWorld.entity(self._player.playerVehicleID)
        vehicle.filter.enableClientFilters = not vehicle.filter.enableClientFilters
        return

    def __moveVehicle(self):
        self._player.moveVehicle(1, True)
        return

    def __pickup(self):
        self._player.base.setDevelopmentFeature(0, b'pickup', 0, b'straight')
        return

    def __hotReload(self):
        if BigWorld.spaceReload(self._player.spaceID):
            self._player.base.setDevelopmentFeature(0, b'hot_reload', 0, b'')
        return

    def __logTkillRatings(self):
        self._player.base.setDevelopmentFeature(0, b'log_tkill_ratings', 0, b'')
        return

    def __toggleTeleport(self):
        self._player.isTeleport = not self._player.isTeleport
        return

    def __respawnVehicle(self):
        self._player.base.setDevelopmentFeature(0, b'respawn_vehicle', 0, b'')
        return

    def __pickupRoll(self):
        self._player.base.setDevelopmentFeature(0, b'pickup', 0, b'roll')
        return

    def __captureClosestBase(self):
        self._player.base.setDevelopmentFeature(0, b'captureClosestBase', 0, b'')
        return

    def __teleportToShotPoint(self):
        self._player.base.setDevelopmentFeature(0, b'teleportToShotPoint', 0, b'')
        return

    def __setSignal(self):
        self._player.base.setDevelopmentFeature(0, b'setSignal', 3, b'')
        return

    def __navigateTo(self):
        self._player.base.setDevelopmentFeature(0, b'navigateTo', 0, pickle.dumps((tuple(self._player.inputHandler.getDesiredShotPoint()), None, False, 2.0), -1))
        return

    def __togglePauseAI(self):
        self._player.base.setDevelopmentFeature(0, b'togglePauseAI', 0, b'')
        return

    def __addAreaMarker(self):
        self._player.addOrRemoveMarkerTo(key=0)
        return

    def __removeAllMarkers(self):
        self._player.addOrRemoveMarkerTo(key=1)
        return

    def __addVehicleMarker(self):
        self._player.addOrRemoveMarkerTo(key=2)
        return

    def __killEnemyTeam(self):
        self._player.base.setDevelopmentFeature(0, b'killEnemyTeam', 0, b'')
        return

    def __stun(self):
        self._player.base.setDevelopmentFeature(0, b'stun', 0, b'')
        return

    def __killTurret(self):
        self._player.base.setDevelopmentFeature(0, b'kill_turret', 0, b'')
        return

    def __killTankman(self):
        self._player.base.setDevelopmentFeature(0, b'kill_tankman', 0, b'loader')
        return

    def __toggleShowServerMarker(self):
        self._player.gunRotator.showServerMarker = not self._player.gunRotator.showServerMarker
        return
