from __future__ import absolute_import
import json, logging, BigWorld, Event, ResMgr
from constants import DEFAULT_HANGAR_SCENE
from gui.prb_control.settings import FUNCTIONAL_FLAG
from soft_exception import SoftException
from PlayerEvents import g_playerEvents
from helpers import dependency
from gui.prb_control.entities.listener import IGlobalListener
from skeletons.gui.game_control import IHangarSpaceSwitchController
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from gui.shared.utils.hangar_space_reloader import ErrorFlags
from shared_utils import nextTick
from skeletons.gui.shared.utils import IHangarSpaceReloader, IHangarSpace
from gui.ClientHangarSpace import SERVER_CMD_CHANGE_HANGAR, SERVER_CMD_CHANGE_HANGAR_PREM, getDefaultHangarPath, SERVER_CMD_CHANGE_HANGAR_ALT, getHangarFullVisibilityMask, g_clientHangarSpaceOverride
_logger = logging.getLogger(__name__)

class DefaultHangarSpaceConfig(object):

    def __init__(self):
        self._visibilityMask = {True: None, False: None}
        self._spaceIdOverride = {}
        return

    def clear(self):
        self._visibilityMask = {True: None, False: None}
        self._spaceIdOverride = {}
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
        del self._spaceIdOverride[isPremium]
        return


class SceneSpaceConfig(object):

    def __init__(self, spaceId=None, waitingMessage=None, waitingBackground=None, spaceIdOverride=None, visibilityMask=None):
        self._waitingMessage = waitingMessage
        self._waitingBackground = waitingBackground
        self._spaceId = spaceId
        self._spaceIdOverride = spaceIdOverride
        self._visibilityMask = visibilityMask
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

    def discardVisibilityMaskOverride(self):
        self._visibilityMask = None
        return

    def setVisibilityMask(self, visibilityMask):
        self._visibilityMask = visibilityMask
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


class HangarSpaceSwitchController(IHangarSpaceSwitchController, IGlobalListener):
    hangarSpaceReloader = dependency.descriptor(IHangarSpaceReloader)
    hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        super(HangarSpaceSwitchController, self).__init__()
        self.onCheckSceneChange = Event.Event()
        self.onSpaceUpdated = Event.Event()
        self.hangarSpaceUpdated = False
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
        if self.prbEntity.getFunctionalFlags() & FUNCTIONAL_FLAG.LEGACY_INIT:
            return
        self.processPossibleSceneChange(force=True)
        g_eventBus.handleEvent(events.HangarSpacesSwitcherEvent(events.HangarSpacesSwitcherEvent.SWITCH_TO_HANGAR_SPACE), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def hangarSpaceUpdate(self, sceneName):
        if sceneName not in self._sceneSpaceParams:
            _logger.error(b'There is no space config for the key %s.', sceneName)
        if self.hangarSpaceUpdated and self.currentSceneName != sceneName:
            _logger.error(b'There is more than one component that requires space change is active!')
            return
        self.currentSceneName = sceneName
        self.hangarSpaceUpdated = True
        return

    def lockHangarOverride(self, sceneName):
        for name in self._sceneSpaceParams:
            self._sceneSpaceParams[name] = SceneSpaceConfig(sceneName)

        for isPremium in (True, False):
            self._defaultHangarSpaceConfig.setSpaceIdOverride(isPremium, sceneName)

        self.__isHangarOverridingLocked = True
        _logger.info(b'Hangar override was locked. sceneName=%s', sceneName)
        return

    def onDisconnected(self):
        self._clear()
        self._defaultHangarSpaceConfig.clear()
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

    def processPossibleSceneChange(self, force=False):
        self.hangarSpaceUpdated = False
        prevSceneName = self.currentSceneName
        self.onCheckSceneChange()
        success = None
        err = ErrorFlags.NONE
        if self.hangarSpaceUpdated:
            currentSceneConfig = self._sceneSpaceParams[self.currentSceneName]
            hangarSpacePath = self.hangarSpaceReloader.buildHangarSpacePath(currentSceneConfig.getHangarSpaceId())
            if hangarSpacePath != self.hangarSpaceReloader.hangarSpacePath:
                success, err = self.hangarSpaceReloader.changeHangarSpace(currentSceneConfig.getHangarSpaceId(), currentSceneConfig.getVisibilityMask(), currentSceneConfig.waitingMessage, currentSceneConfig.waitingBackground, force=force)
        else:
            self.currentSceneName = DEFAULT_HANGAR_SCENE
            hangarSpacePath = self._defaultHangarSpaceConfig.getHangarSpaceId(self.hangarSpace.isPremium)
            if hangarSpacePath != self.hangarSpaceReloader.hangarSpacePath:
                success, err = self.hangarSpaceReloader.changeHangarSpace(hangarSpacePath, self._defaultHangarSpaceConfig.getVisibilityMask(self.hangarSpace.isPremium), force=force)
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
            for item in switchItems.values():
                name = item.readString(b'name')
                spaceId = item.readString(b'space')
                waitingMessage = item.readString(b'waitingMessage') or None
                waitingBackground = item.readString(b'waitingBackground') or None
                self._sceneSpaceParams[name] = SceneSpaceConfig(spaceId, waitingMessage, waitingBackground)

        return

    def _onEventNotificationsChanged(self, diff):
        if self.__isHangarOverridingLocked:
            _logger.info(b'Hangar overriding is locked. Hangar notifications were skipped.')
            return
        else:
            currentSceneChanged = False
            currentSceneMaskChanged = False
            for notification in diff[b'removed']:
                if not notification[b'data']:
                    continue
                if notification[b'type'] == SERVER_CMD_CHANGE_HANGAR_ALT:
                    data = json.loads(notification[b'data'])
                    name = data[b'name']
                    sceneConfig = self._sceneSpaceParams.get(name)
                    if sceneConfig is None:
                        _logger.error(b'Cannot remove space settings for not existing scene %s', name)
                        continue
                    if b'hangar' in data:
                        sceneConfig.discardSpaceIdOverride()
                        sceneConfig.discardVisibilityMaskOverride()
                        if name == self.currentSceneName:
                            currentSceneChanged = True
                        continue
                    if b'visibilityMask' in data:
                        sceneConfig.discardVisibilityMaskOverride()
                        if name == self.currentSceneName:
                            currentSceneMaskChanged = True
                if notification[b'type'] in (SERVER_CMD_CHANGE_HANGAR, SERVER_CMD_CHANGE_HANGAR_PREM):
                    isPremium = notification[b'type'] == SERVER_CMD_CHANGE_HANGAR_PREM
                    try:
                        data = json.loads(notification[b'data'])
                        if b'hangar' in data:
                            self._defaultHangarSpaceConfig.discardSpaceIdOverride(isPremium)
                            self._defaultHangarSpaceConfig.discardVisibilityMaskOverride(isPremium)
                            if self.currentSceneName == DEFAULT_HANGAR_SCENE:
                                currentSceneChanged = True
                            continue
                        if b'visibilityMask' in data:
                            self._defaultHangarSpaceConfig.discardVisibilityMaskOverride(isPremium)
                            if self.currentSceneName == DEFAULT_HANGAR_SCENE:
                                currentSceneMaskChanged = True
                    except Exception:
                        self._defaultHangarSpaceConfig.discardSpaceIdOverride(isPremium)
                        self._defaultHangarSpaceConfig.discardVisibilityMaskOverride(isPremium)
                        if self.currentSceneName == DEFAULT_HANGAR_SCENE:
                            currentSceneChanged = True

            for notification in diff[b'added']:
                if not notification[b'data']:
                    continue
                if notification[b'type'] == SERVER_CMD_CHANGE_HANGAR_ALT:
                    data = json.loads(notification[b'data'])
                    name = data[b'name']
                    sceneConfig = self._sceneSpaceParams.get(name)
                    if sceneConfig is None:
                        _logger.error(b'Cannot add space settings for not existing scene %s', name)
                        continue
                    if b'hangar' in data:
                        sceneConfig.setSpaceIdOverride(data[b'hangar'])
                        if self.currentSceneName == name:
                            currentSceneChanged = True
                    if b'visibilityMask' in data:
                        sceneConfig.setVisibilityMask(int(data[b'visibilityMask'], 16))
                        if self.currentSceneName == name:
                            currentSceneMaskChanged = True
                if notification[b'type'] in (SERVER_CMD_CHANGE_HANGAR, SERVER_CMD_CHANGE_HANGAR_PREM):
                    isPremium = notification[b'type'] == SERVER_CMD_CHANGE_HANGAR_PREM
                    try:
                        data = json.loads(notification[b'data'])
                        if b'hangar' in data:
                            self._defaultHangarSpaceConfig.setSpaceIdOverride(isPremium, data[b'hangar'])
                            if self.currentSceneName == DEFAULT_HANGAR_SCENE:
                                currentSceneChanged = True
                        if b'visibilityMask' in data:
                            self._defaultHangarSpaceConfig.setVisibilityMask(isPremium, int(data[b'visibilityMask'], 16))
                            if self.currentSceneName == DEFAULT_HANGAR_SCENE:
                                currentSceneMaskChanged = True
                    except Exception:
                        self._defaultHangarSpaceConfig.setSpaceIdOverride(isPremium, notification[b'data'])
                        if self.currentSceneName == DEFAULT_HANGAR_SCENE:
                            currentSceneChanged = True

            if currentSceneChanged:
                if self.currentSceneName == DEFAULT_HANGAR_SCENE:
                    spaceId = self._defaultHangarSpaceConfig.getHangarSpaceId(self.hangarSpace.isPremium)
                    visibilityMask = self._defaultHangarSpaceConfig.getVisibilityMask(self.hangarSpace.isPremium)
                    if not self.hangarSpace.inited:
                        g_clientHangarSpaceOverride.setPath(spaceId, visibilityMask, isPremium=self.hangarSpace.isPremium, isReload=False)
                        spaceId = self._defaultHangarSpaceConfig.getHangarSpaceId(not self.hangarSpace.isPremium)
                        visibilityMask = self._defaultHangarSpaceConfig.getVisibilityMask(not self.hangarSpace.isPremium)
                        g_clientHangarSpaceOverride.setPath(spaceId, visibilityMask, isPremium=not self.hangarSpace.isPremium, isReload=False)
                        return
                    success, err = self.hangarSpaceReloader.changeHangarSpace(spaceId, visibilityMask)
                else:
                    currentSceneConfig = self._sceneSpaceParams[self.currentSceneName]
                    spaceId = currentSceneConfig.getHangarSpaceId()
                    visibilityMask = currentSceneConfig.getVisibilityMask()
                    if not self.hangarSpace.inited:
                        g_clientHangarSpaceOverride.setPath(spaceId, visibilityMask, isReload=False)
                        return
                    success, err = self.hangarSpaceReloader.changeHangarSpace(spaceId, visibilityMask, currentSceneConfig.waitingMessage, currentSceneConfig.waitingBackground)
                if success:
                    self.hangarSpace.onSpaceCreate += self._onSpaceCreatedCallback
                elif err == ErrorFlags.DUPLICATE_REQUEST:
                    self.onSpaceUpdated()
                elif err != ErrorFlags.NONE:
                    raise SoftException((b'Could not perform space reload, see hangar_space_reloader.py error flag {}.').format(err))
                return
            if currentSceneMaskChanged and self.hangarSpace.inited:
                if self.currentSceneName == DEFAULT_HANGAR_SCENE:
                    visibilityMask = self._defaultHangarSpaceConfig.getVisibilityMask(self.hangarSpace.isPremium)
                else:
                    visibilityMask = self._sceneSpaceParams[self.currentSceneName].getVisibilityMask()
                BigWorld.wg_setSpaceItemsVisibilityMask(self.hangarSpace.space.spaceId, visibilityMask)
            return
