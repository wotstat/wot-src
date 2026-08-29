import json, logging, typing, BigWorld, Event, ResMgr
from constants import DEFAULT_HANGAR_SCENE
from soft_exception import SoftException
from PlayerEvents import g_playerEvents
from helpers import dependency
from gui.prb_control.entities.listener import IGlobalListener
from gui.Scaleform.Waiting import Waiting
from skeletons.gui.game_control import IHangarSpaceSwitchController
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from gui.shared.utils.hangar_space_reloader import ErrorFlags
from shared_utils import nextTick
from skeletons.gui.shared.utils import IHangarSpaceReloader, IHangarSpace
from gui.shared.utils.HangarSpace import g_execute_after_hangar_space_inited
from gui.ClientHangarSpace import SERVER_CMD_CHANGE_HANGAR, SERVER_CMD_CHANGE_HANGAR_PREM, getDefaultHangarPath, SERVER_CMD_CHANGE_HANGAR_ALT, getHangarFullVisibilityMask, g_clientHangarSpaceOverride, initializeHangarsCFG
_logger = logging.getLogger(__name__)

class DefaultHangarSpaceConfig(object):

    def __init__(self):
        self._visibilityMask = {True: None, False: None}
        self._spaceIdOverride = {}
        self._environment = {True: b'', False: b''}
        return

    def getVisibilityMask(self, isPremium):
        if self._visibilityMask[isPremium] is not None:
            return self._visibilityMask[isPremium]
        else:
            return getHangarFullVisibilityMask(self.getHangarSpaceId(isPremium))

    def discardVisibilityMaskOverride(self, isPremium):
        self._visibilityMask[isPremium] = None
        return

    def setVisibilityMask(self, isPremium, visibilityMask):
        self._visibilityMask[isPremium] = visibilityMask
        return

    def getHangarSpaceId(self, isPremium):
        path = self._spaceIdOverride.get(isPremium)
        if path is not None:
            return path
        else:
            return getDefaultHangarPath(isPremium)

    def setSpaceIdOverride(self, isPremium, newId):
        self._spaceIdOverride[isPremium] = newId
        return

    def discardSpaceIdOverride(self, isPremium):
        self._spaceIdOverride[isPremium] = None
        return

    def getEnvironment(self, isPremium):
        return self._environment[isPremium]

    def setEnvironment(self, isPremium, newEnvironment):
        self._environment[isPremium] = newEnvironment
        return

    def discardEnvironment(self, isPremium):
        self._environment[isPremium] = b''
        return

    def clear(self):
        self._visibilityMask = {True: None, False: None}
        self._environment = {True: b'', False: b''}
        self._spaceIdOverride = {}
        return


class SceneSpaceConfig(object):

    def __init__(self, spaceId=None, waitingMessage=None, waitingBackground=None, spaceIdOverride=None, visibilityMask=None, environment=b'', customEventMode=False):
        self._waitingMessage = waitingMessage
        self._waitingBackground = waitingBackground
        self._spaceId = spaceId
        self._spaceIdOverride = spaceIdOverride
        self._visibilityMask = visibilityMask
        self._environment = environment
        self._customEventMode = customEventMode
        return

    @property
    def waitingMessage(self):
        return self._waitingMessage

    @property
    def waitingBackground(self):
        return self._waitingBackground

    def getVisibilityMask(self):
        if self._visibilityMask is not None:
            return self._visibilityMask
        else:
            return getHangarFullVisibilityMask(self.getHangarSpaceId())

    def isCustomEventMode(self):
        return self._customEventMode

    def discardVisibilityMaskOverride(self):
        self._visibilityMask = None
        return

    def setVisibilityMask(self, visibilityMask):
        self._visibilityMask = visibilityMask
        return

    def getEnvironment(self):
        if self._environment is not None:
            return self._environment
        else:
            return b''

    def discardEnvironment(self):
        self._environment = b''
        return

    def setEnvironment(self, environment):
        self._environment = environment
        return

    def getHangarSpaceId(self):
        if self._spaceIdOverride is not None:
            return self._spaceIdOverride
        else:
            return self._spaceId

    def setSpaceIdOverride(self, newId):
        self._spaceIdOverride = newId
        return

    def discardSpaceIdOverride(self):
        self._spaceIdOverride = None
        return


class ConfigChanges(object):

    def __init__(self, sceneChanged=False, maskChanged=False, environmentChanged=False, hotreload=True):
        self.sceneChanged = sceneChanged
        self.maskChanged = maskChanged
        self.environmentChanged = environmentChanged
        self.hotreload = hotreload
        return

    def hasChanges(self):
        return self.sceneChanged or self.maskChanged or self.environmentChanged


class HangarSpaceSwitchController(IHangarSpaceSwitchController, IGlobalListener):
    hangarSpaceReloader = dependency.descriptor(IHangarSpaceReloader)
    hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        super(HangarSpaceSwitchController, self).__init__()
        self.onCheckSceneChange = Event.Event()
        self.onSpaceUpdated = Event.Event()
        self.hangarSpaceUpdated = False
        self.customEventModeEnabled = False
        self.currentSceneName = DEFAULT_HANGAR_SCENE
        self._defaultHangars = {}
        self._sceneSpaceParams = {}
        self._defaultHangarSpaceConfig = DefaultHangarSpaceConfig()
        self.__isHangarOverridingLocked = False
        return

    def init(self):
        self._readHangarSceneSpaceSettings()
        g_playerEvents.onEventNotificationsChanged += self._onEventNotificationsChanged
        return

    def fini(self):
        g_playerEvents.onEventNotificationsChanged -= self._onEventNotificationsChanged
        return

    def onLobbyInited(self, event):
        super(HangarSpaceSwitchController, self).onLobbyInited(event)
        self.startGlobalListening()
        if not self.hangarSpace.inited or self.hangarSpace.spaceLoading():
            self.hangarSpace.onSpaceCreate += self._delayedProcessChange
        else:
            self.processPossibleSceneChange()
        return

    def onPrbEntitySwitched(self):
        self.processPossibleSceneChange()
        g_eventBus.handleEvent(events.HangarSpacesSwitcherEvent(events.HangarSpacesSwitcherEvent.SWITCH_TO_HANGAR_SPACE), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def hangarSpaceUpdate(self, sceneName):
        if sceneName not in self._sceneSpaceParams:
            _logger.error(b'There is no space config for the key %s.', sceneName)
        if self.customEventModeEnabled and not self._sceneSpaceParams[sceneName].isCustomEventMode():
            _logger.debug(b'Custom event mode is enabled. Skipping hangar space update.')
            return
        if self.hangarSpaceUpdated and self.currentSceneName != sceneName:
            _logger.error(b'There is more than one component that requires space change is active!')
            return
        self.currentSceneName = sceneName
        self.hangarSpaceUpdated = True
        return

    def lockHangarOverride(self, sceneName):
        for name in self._sceneSpaceParams.iterkeys():
            self._sceneSpaceParams[name] = SceneSpaceConfig(sceneName)

        for isPremium in (True, False):
            self._defaultHangarSpaceConfig.setSpaceIdOverride(isPremium, sceneName)

        self.__isHangarOverridingLocked = True
        _logger.info(b'Hangar override was locked. sceneName=%s', sceneName)
        return

    def onDisconnected(self):
        self._clear()
        self._defaultHangarSpaceConfig.clear()
        self.currentSceneName = DEFAULT_HANGAR_SCENE
        super(HangarSpaceSwitchController, self).onDisconnected()
        return

    def onAvatarBecomePlayer(self):
        self._clear()
        super(HangarSpaceSwitchController, self).onAvatarBecomePlayer()
        return

    def _clear(self):
        self.stopGlobalListening()
        return

    def _delayedProcessChange(self):
        self.hangarSpace.onSpaceCreate -= self._delayedProcessChange
        nextTick(self.processPossibleSceneChange)()
        return

    @g_execute_after_hangar_space_inited
    def _delayedReloadSpace(self, spaceId, visibilityMask, environment, waitingMessage=None, backgroundImage=None):
        success, err = self.hangarSpaceReloader.changeHangarSpace(spaceId, visibilityMask, environment, waitingMessage, backgroundImage)
        if success:
            self.hangarSpace.onSpaceCreate += self._onSpaceCreatedCallback
        else:
            raise SoftException((b'Could not perform space reload, see hangar_space_reloader.py error flag {}.').format(err))
        return

    def processPossibleSceneChange(self):
        self.hangarSpaceUpdated = False
        prevSceneName = self.currentSceneName
        self.onCheckSceneChange()
        success = None
        err = ErrorFlags.NONE
        if self.hangarSpaceUpdated:
            currentSceneConfig = self._sceneSpaceParams[self.currentSceneName]
            hangarSpacePath = self.hangarSpaceReloader.buildHangarSpacePath(currentSceneConfig.getHangarSpaceId())
            if hangarSpacePath != self.hangarSpaceReloader.hangarSpacePath:
                success, err = self.hangarSpaceReloader.changeHangarSpace(currentSceneConfig.getHangarSpaceId(), currentSceneConfig.getVisibilityMask(), currentSceneConfig.getEnvironment(), currentSceneConfig.waitingMessage, currentSceneConfig.waitingBackground)
        else:
            self.currentSceneName = DEFAULT_HANGAR_SCENE
            hangarSpacePath = self._defaultHangarSpaceConfig.getHangarSpaceId(self.hangarSpace.isPremium)
            if hangarSpacePath != self.hangarSpaceReloader.hangarSpacePath:
                success, err = self.hangarSpaceReloader.changeHangarSpace(hangarSpacePath, self._defaultHangarSpaceConfig.getVisibilityMask(self.hangarSpace.isPremium), self._defaultHangarSpaceConfig.getEnvironment(self.hangarSpace.isPremium))
        if success:
            self.hangarSpace.onSpaceCreate += self._onSpaceCreatedCallback
        elif err == ErrorFlags.DUPLICATE_REQUEST:
            self.onSpaceUpdated()
        elif err != ErrorFlags.NONE:
            self.currentSceneName = prevSceneName
            _logger.error(b'Could not perform space reload, see hangar_space_reloader.py error flag %d.', err)
        return

    def _onSpaceCreatedCallback(self):
        self.hangarSpace.onSpaceCreate -= self._onSpaceCreatedCallback
        self.onSpaceUpdated()
        return

    def _readHangarSceneSpaceSettings(self):
        hangarsXml = ResMgr.openSection(b'gui/hangars.xml')
        if hangarsXml and hangarsXml.has_key(b'hangar_scene_spaces'):
            switchItems = hangarsXml[b'hangar_scene_spaces']
            for name, item in switchItems.items():
                spaceId = item.readString(b'space')
                waitingMessage = item.readString(b'waitingMessage') or None
                waitingBackground = item.readString(b'waitingBackground') or None
                customEventMode = item.readBool(b'customEventMode')
                self._sceneSpaceParams[name] = SceneSpaceConfig(spaceId, waitingMessage, waitingBackground, customEventMode=customEventMode)

        return

    def _checkRemovedEventNotifications(self, diff):
        changes = ConfigChanges()
        for notification in diff[b'removed']:
            if not notification[b'data']:
                continue
            if notification[b'type'] == SERVER_CMD_CHANGE_HANGAR_ALT:
                data = json.loads(notification[b'data'])
                name = data[b'name']
                sceneConfig = self._sceneSpaceParams.get(name)
                isCurrentScene = name == self.currentSceneName
                if sceneConfig is None:
                    _logger.error(b'Cannot remove space settings for not existing scene %s', name)
                    continue
                if b'hangar' in data:
                    sceneConfig.discardSpaceIdOverride()
                    sceneConfig.discardVisibilityMaskOverride()
                    sceneConfig.discardEnvironment()
                    changes.sceneChanged |= isCurrentScene
                if b'visibilityMask' in data:
                    sceneConfig.discardVisibilityMaskOverride()
                    changes.maskChanged |= isCurrentScene
                if b'environment' in data:
                    sceneConfig.discardEnvironment()
                    changes.environmentChanged |= isCurrentScene
            if notification[b'type'] in (SERVER_CMD_CHANGE_HANGAR, SERVER_CMD_CHANGE_HANGAR_PREM):
                isPremium = notification[b'type'] == SERVER_CMD_CHANGE_HANGAR_PREM
                isCurrentScene = DEFAULT_HANGAR_SCENE == self.currentSceneName
                sceneConfig = self._defaultHangarSpaceConfig
                try:
                    data = json.loads(notification[b'data'])
                    if b'hangar' in data:
                        sceneConfig.discardSpaceIdOverride(isPremium)
                        sceneConfig.discardVisibilityMaskOverride(isPremium)
                        sceneConfig.discardEnvironment(isPremium)
                        changes.sceneChanged |= isCurrentScene
                    if b'visibilityMask' in data:
                        sceneConfig.discardVisibilityMaskOverride(isPremium)
                        changes.maskChanged |= isCurrentScene
                    if b'environment' in data:
                        sceneConfig.discardEnvironment(isPremium)
                        changes.environmentChanged |= isCurrentScene
                except Exception:
                    sceneConfig.discardSpaceIdOverride(isPremium)
                    sceneConfig.discardVisibilityMaskOverride(isPremium)
                    sceneConfig.discardEnvironment(isPremium)
                    changes.sceneChanged |= isCurrentScene

        return changes

    def _checkAddedEventNotifications(self, diff):
        changes = ConfigChanges()
        for notification in diff[b'added']:
            if not notification[b'data']:
                continue
            if notification[b'type'] == SERVER_CMD_CHANGE_HANGAR_ALT:
                data = json.loads(notification[b'data'])
                name = data[b'name']
                sceneConfig = self._sceneSpaceParams.get(name)
                isCurrentScene = self.currentSceneName == name
                hotreload = data[b'hotreload'] if b'hotreload' in data else True
                changes.hotreload = hotreload if isCurrentScene else changes.hotreload
                if sceneConfig is None:
                    _logger.error(b'Cannot add space settings for not existing scene %s', name)
                    continue
                if b'hangar' in data:
                    sceneConfig.setSpaceIdOverride(data[b'hangar'])
                    changes.sceneChanged |= isCurrentScene
                if b'visibilityMask' in data:
                    sceneConfig.setVisibilityMask(int(data[b'visibilityMask'], 16))
                    changes.maskChanged |= isCurrentScene
                if b'environment' in data:
                    sceneConfig.setEnvironment(data[b'environment'])
                    changes.environmentChanged |= isCurrentScene
            if notification[b'type'] in (SERVER_CMD_CHANGE_HANGAR, SERVER_CMD_CHANGE_HANGAR_PREM):
                sceneConfig = self._defaultHangarSpaceConfig
                isPremium = notification[b'type'] == SERVER_CMD_CHANGE_HANGAR_PREM
                isCurrentScene = self.currentSceneName == DEFAULT_HANGAR_SCENE
                try:
                    data = json.loads(notification[b'data'])
                    hotreload = data[b'hotreload'] if b'hotreload' in data else True
                    if isCurrentScene:
                        changes.hotreload = hotreload and changes.hotreload
                    if b'hangar' in data:
                        sceneConfig.setSpaceIdOverride(isPremium, data[b'hangar'])
                        changes.sceneChanged |= isCurrentScene
                    if b'visibilityMask' in data:
                        sceneConfig.setVisibilityMask(isPremium, int(data[b'visibilityMask'], 16))
                        changes.maskChanged |= isCurrentScene
                    if b'environment' in data:
                        sceneConfig.setEnvironment(isPremium, data[b'environment'])
                        changes.environmentChanged |= isCurrentScene
                except Exception:
                    sceneConfig.setSpaceIdOverride(isPremium, notification[b'data'])
                    changes.sceneChanged |= isCurrentScene

        return changes

    def _onEventNotificationsChanged(self, diff):
        if self.__isHangarOverridingLocked:
            _logger.info(b'Hangar overriding is locked. Hangar notifications were skipped.')
            return
        changes = self.__getSceneChanges(diff)
        if not changes.hasChanges():
            return
        initializeHangarsCFG()
        isDefaultScene = self.currentSceneName == DEFAULT_HANGAR_SCENE
        if isDefaultScene:
            self.__defaultSceneNotificationChanged(changes)
        else:
            self.__nonDefaultSceneNotificationChanged(changes)
        return

    def __defaultSceneNotificationChanged(self, changes):
        spaceConfig = self._defaultHangarSpaceConfig
        spaceId = spaceConfig.getHangarSpaceId(self.hangarSpace.isPremium)
        visibilityMask = spaceConfig.getVisibilityMask(self.hangarSpace.isPremium)
        environment = spaceConfig.getEnvironment(self.hangarSpace.isPremium)
        if not self.hangarSpace.inited:
            g_clientHangarSpaceOverride.setPath(spaceId, visibilityMask, environment, isPremium=self.hangarSpace.isPremium, isReload=False)
            spaceId = self._defaultHangarSpaceConfig.getHangarSpaceId(not self.hangarSpace.isPremium)
            visibilityMask = self._defaultHangarSpaceConfig.getVisibilityMask(not self.hangarSpace.isPremium)
            g_clientHangarSpaceOverride.setPath(spaceId, visibilityMask, environment, isPremium=not self.hangarSpace.isPremium, isReload=False)
            return
        self.__updateScene(changes, spaceId, visibilityMask, environment)
        return

    def __nonDefaultSceneNotificationChanged(self, changes):
        spaceConfig = self._sceneSpaceParams[self.currentSceneName]
        spaceId = spaceConfig.getHangarSpaceId()
        visibilityMask = spaceConfig.getVisibilityMask()
        environment = spaceConfig.getEnvironment()
        if not self.hangarSpace.inited:
            g_clientHangarSpaceOverride.setPath(spaceId, visibilityMask, environment, isReload=False)
            return
        self.__updateScene(changes, spaceId, visibilityMask, environment, spaceConfig.waitingMessage, spaceConfig.waitingBackground)
        return

    def __updateScene(self, changes, spaceId, visibilityMask, environment, waitingMessage=None, waitingBackground=None):
        hotreload = changes.hotreload
        buildedOldSpacePath = self.hangarSpaceReloader.buildHangarSpacePath(self.hangarSpace.spacePath)
        buildedNewSpacePath = self.hangarSpaceReloader.buildHangarSpacePath(spaceId)
        spaceChanged = changes.sceneChanged and buildedOldSpacePath != buildedNewSpacePath
        if hotreload and spaceChanged:
            self._delayedReloadSpace(spaceId, visibilityMask, environment, waitingMessage, waitingBackground)
            return
        if hotreload and changes.maskChanged:
            self.__updateVisibilityMaskForCurrentScene(spaceId, visibilityMask)
        if hotreload and changes.environmentChanged:
            self.__updateEnvironmentForCurrentScene(environment)
        g_clientHangarSpaceOverride.setPath(spaceId, visibilityMask, environment, isPremium=self.hangarSpace.isPremium, isReload=False)
        return

    def __updateVisibilityMaskForCurrentScene(self, spaceId, visibilityMask=None):
        if not self.hangarSpace.inited:
            return
        else:
            if visibilityMask is None:
                visibilityMask = getHangarFullVisibilityMask(spaceId)
            BigWorld.setSpaceItemsVisibilityMask(self.hangarSpace.spaceID, visibilityMask)
            return

    def __updateEnvironmentForCurrentScene(self, environment=None):
        if not self.hangarSpace.inited:
            return
        else:
            Waiting.show(b'loadHangarSpace')
            BigWorld.callback(5.0, (lambda : Waiting.hide(b'loadHangarSpace')))
            environmentSwitcher = BigWorld.EnvironmentSwitcher.instance()
            if environmentSwitcher is not None and environment is not None:
                environmentSwitcher.setMainEnvironment(environment, tryActivate=True)
            return

    def __getSceneChanges(self, diff):
        removeChanges = self._checkRemovedEventNotifications(diff)
        addChanges = self._checkAddedEventNotifications(diff)
        summaryChanges = ConfigChanges(sceneChanged=removeChanges.sceneChanged or addChanges.sceneChanged, maskChanged=removeChanges.maskChanged or addChanges.maskChanged, environmentChanged=removeChanges.environmentChanged or addChanges.environmentChanged, hotreload=addChanges.hotreload or not addChanges.hasChanges())
        return summaryChanges
