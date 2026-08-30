import typing
from enum import unique, IntEnum
import Event
from debug_utils import LOG_ERROR
if typing.TYPE_CHECKING:
    from skeletons.tutorial import ComponentID, ITutorialLoader

class GUI_EFFECT_NAME(object):
    SHOW_DIALOG = b'ShowDialog'
    SHOW_WINDOW = b'ShowWindow'
    SHOW_HINT = b'ShowHint'
    SET_CRITERIA = b'SetCriteria'
    SET_VIEW_CRITERIA = b'SetViewCriteria'
    SET_TRIGGER = b'SetTrigger'
    SET_ITEM_PROPS = b'SetItemProps'
    PLAY_ANIMATION = b'PlayAnimation'


class GUIProxy(object):

    def __init__(self):
        super(GUIProxy, self).__init__()
        self.eManager = Event.EventManager()
        self.onGUILoaded = Event.Event(self.eManager)
        self.onGUIInput = Event.Event(self.eManager)
        self.onPageChanging = Event.Event(self.eManager)
        self.onPageReady = Event.Event(self.eManager)
        self.onItemFound = Event.Event(self.eManager)
        self.onItemLost = Event.Event(self.eManager)
        self.onViewLoaded = Event.Event(self.eManager)
        self.onViewDisposed = Event.Event(self.eManager)
        return

    def init(self):
        return True

    def show(self):
        return

    def fini(self):
        return

    def clear(self):
        return

    def lock(self):
        return

    def release(self):
        return

    def loadConfig(self, filePath):
        return

    def reloadConfig(self, filePath):
        return

    def getSceneID(self):
        return

    def goToScene(self, sceneID):
        return

    def isViewPresent(self, layer, criteria):
        return False

    def closeView(self, layer, criteria):
        return

    def playEffect(self, effectName, args):
        return False

    def stopEffect(self, effectName, effectID, effectSubType=None):
        return

    def isEffectRunning(self, effectName, effectID=None, effectSubType=None):
        return False

    def showWaiting(self, messageID, isSingle=False):
        return

    def hideWaiting(self, messageID=None):
        return

    def showMessage(self, text, lookupType=None):
        return

    def showI18nMessage(self, key, *args, **kwargs):
        return

    def showServiceMessage(self, data, msgTypeName):
        return 0

    def getItemsOnScene(self):
        return set()

    def closePopUps(self):
        return

    def isGuiDialogDisplayed(self):
        return False

    def isTutorialDialogDisplayed(self, dialogID):
        return False

    def isTutorialWindowDisplayed(self, windowID):
        return False

    def findItem(self, itemID, criteria):
        return

    def invokeCommand(self, command):
        return

    def getGuiRoot(self):
        return

    def setDispatcher(self, dispatcher):
        return

    def getDispatcher(self):
        return


class GUIDispatcher(object):

    def __init__(self):
        super(GUIDispatcher, self).__init__()
        self._loader = None
        self._isDisabled = False
        self._isStarted = False
        return

    def start(self, loader):
        if self._isStarted:
            return False
        self._isStarted = True
        self._loader = loader
        return True

    def stop(self):
        if not self._isStarted:
            return False
        else:
            self.clearGUI()
            self._loader = None
            return True

    def findGUI(self, root=None):
        return False

    def clearGUI(self):
        return

    def stopTraining(self):
        result = False
        if self._loader:
            result = self._loader.stop()
        else:
            LOG_ERROR(b'Tutorial can not be stopped, loader is not defined')
        return result

    def refuseTraining(self):
        result = False
        if self._loader:
            result = self._loader.refuse()
        else:
            LOG_ERROR(b'Tutorial can not be refuse, loader is not defined')
        return result

    def startTraining(self, settingsID, state):
        result = False
        if self._loader:
            result = self._loader.run(settingsID, state)
        else:
            LOG_ERROR(b'Tutorial can not be run, loader is not defined')
        return result

    def setDisabled(self, disabled):
        self._isDisabled = disabled
        return


@unique
class GuiType(IntEnum):
    UNDEFINED = 0
    SCALEFORM = 1
    WULF = 2


ComponentDescr = typing.NamedTuple(b'ComponentDescr', (
 (
  b'ID', str), (b'viewType', GuiType), (b'viewId', str), (b'path', str)))

class IGuiImpl(object):
    __slots__ = (b'onComponentFound', b'onTriggerActivated', b'onComponentDisposed', b'onEffectCompleted', b'onInit')
    if typing.TYPE_CHECKING:
        onComponentFound = None
        onComponentDisposed = None
        onTriggerActivated = None
        onEffectCompleted = None
        onInit = None

    def clear(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def showEffect(self, componentID, viewID, effectType, effectData, effectBuilder=b''):
        raise NotImplementedError
        return

    def hideEffect(self, componentID, viewID, effectType, effectBuilder=b''):
        raise NotImplementedError
        return

    def setDescriptions(self, items):
        raise NotImplementedError
        return

    def setSystemEnabled(self, enabled):
        raise NotImplementedError
        return

    def setCriteria(self, name, value):
        raise NotImplementedError
        return

    def setViewCriteria(self, componentID, viewUniqueName):
        raise NotImplementedError
        return

    def setTriggers(self, componentID, triggers):
        raise NotImplementedError
        return

    def supportedViewTypes(self):
        raise NotImplementedError
        return

    def isInited(self):
        raise NotImplementedError
        return
