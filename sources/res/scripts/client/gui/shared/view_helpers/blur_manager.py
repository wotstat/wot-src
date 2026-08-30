from __future__ import absolute_import
import logging, typing, weakref
from future.utils import listvalues
from math import isnan
import GUI
from collections import deque
from gui.app_loader.settings import APP_NAME_SPACE as _SPACE
from helpers import dependency
from ids_generators import Int32IDGenerator
from shared_utils import findFirst
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.game_control import IBlurEffect, IBlurController
if typing.TYPE_CHECKING:
    from Math import Vector4
_DEFAULT_BLUR_ANIM_REPEAT_COUNT = 10
_DEFAULT_UI_BLUR_RADIUS = 20
_logger = logging.getLogger(__name__)
_idsGenerator = Int32IDGenerator()

class BlurEffect(IBlurEffect):

    def __init__(self, manager, config):
        self._blurId = next(_idsGenerator)
        self._config = config
        self._manager = manager
        self._manager.registerBlur(self)
        return

    @property
    def blurId(self):
        return self._blurId

    def fini(self):
        self._manager.unregisterBlur(self)
        self._manager = None
        return

    def enable(self):
        for config in self._config:
            config.enabled = True

        self._manager.updateBlur(self)
        return

    def disable(self):
        for config in self._config:
            config.enabled = False

        self._manager.updateBlur(self)
        return

    @property
    def config(self):
        return self._config

    def updateConfig(self, config):
        if {type(x) for x in config} != {type(x) for x in self._config}:
            _logger.error(b"Can't update blur config with different blur types")
        self._config = config
        self._manager.updateBlur(self)
        return


class BlurManager(object):

    def __init__(self):
        self._cache = deque()
        return

    def fini(self):
        self.clear()
        return

    def clear(self):
        activeBlur = self._activeBlur()
        if activeBlur is not None:
            for config in activeBlur.config:
                config.BLUR_CLS.unregister(blur=activeBlur, restoredBlur=None)

        self._cache.clear()
        return

    def registerBlur(self, blur):
        prevBlur = self._activeBlur()
        self._cache.append(weakref.ref(blur))
        for config in blur.config:
            config.BLUR_CLS.register(prevBlur=prevBlur, blur=blur)

        if prevBlur:
            for config in prevBlur.config:
                config.BLUR_CLS.register(prevBlur=prevBlur, blur=blur)

        self._validateCache()
        return

    def unregisterBlur(self, blur):
        if self._isBlurInCache(blur):
            isActiveBlur = blur is self._activeBlur()
            self._cache.remove(weakref.ref(blur))
            prevBlur = self._activeBlur()
            if isActiveBlur:
                if prevBlur is not None:
                    for config in prevBlur.config:
                        config.BLUR_CLS.apply(blur=prevBlur)

            for config in blur.config:
                if isActiveBlur or config.persistent:
                    config.BLUR_CLS.unregister(blur=blur, restoredBlur=prevBlur if isActiveBlur else None)

        return

    def updateBlur(self, blur):
        if self._isBlurInCache(blur) and blur is self._activeBlur():
            for config in blur.config:
                config.BLUR_CLS.apply(blur=blur)

        return

    def _activeBlur(self):
        blurRef = findFirst((lambda ref: ref() is not None), reversed(self._cache))
        if blurRef is not None:
            return blurRef()
        else:
            self._validateCache()
            return

    def _validateCache(self):
        toDelete = []
        for itemRef in self._cache:
            if itemRef() is None:
                toDelete.append(itemRef)

        for item in toDelete:
            self._cache.remove(item)

        return bool(toDelete)

    def _isBlurInCache(self, blur):
        if weakref.ref(blur) in self._cache:
            return True
        return False


class Blur(object):

    @classmethod
    def register(cls, prevBlur, blur):
        if prevBlur is not None:
            prevConfig = cls.getSpecificConfig(prevBlur.config)
            if prevConfig is not None and not prevConfig.persistent:
                cls.disable(prevBlur)
        cls.apply(blur)
        return

    @classmethod
    def unregister(cls, blur, restoredBlur=None):
        specificConfig = cls.getSpecificConfig(blur.config)
        if specificConfig is not None:
            cls.disable(blur)
        if restoredBlur is not None:
            cls.apply(restoredBlur)
        return

    @classmethod
    def getSpecificConfig(cls, config):
        raise NotImplementedError
        return

    @classmethod
    def apply(cls, blur):
        raise NotImplementedError
        return

    @classmethod
    def disable(cls, blur):
        raise NotImplementedError
        return


class ImmediateSceneBlur(Blur):

    @classmethod
    def getSpecificConfig(cls, config):
        return findFirst((lambda x: isinstance(x, ImmediateSceneBlurConfig)), config)

    @classmethod
    def apply(cls, blur):
        specificConfig = ImmediateSceneBlur.getSpecificConfig(blur.config)
        if specificConfig is None:
            return
        else:
            spaceID = specificConfig.spaceID
            settings = specificConfig.settings
            GUI.enableBackgroundBlurFeature(spaceID, specificConfig.enabled)
            if not specificConfig.enabled:
                return
            GUI.setBackgroundBlurType(spaceID, settings[b'type'])
            GUI.setBlurDispatches(spaceID, settings[b'dispatches'])
            GUI.setBackgroundBlurApplianceType(spaceID, settings[b'applienceType'])
            GUI.setRadialApplianceBlurRadius(spaceID, settings[b'applienceRadius'])
            GUI.setBlurIntensity(spaceID, settings[b'intensity'])
            GUI.setBlurMipsCount(spaceID, settings[b'mipsCount'])
            GUI.setBlurAlphaParams(spaceID, settings[b'alphaParams'][b'center'], settings[b'alphaParams'][b'start'], settings[b'alphaParams'][b'end'])
            GUI.setBlurParams(spaceID, settings[b'params'][b'hstart'], settings[b'params'][b'hend'], settings[b'params'][b'vstart'], settings[b'params'][b'vend'])
            GUI.enableBlurDirection(spaceID, settings[b'direction'][b'top'], settings[b'direction'][b'right'], settings[b'direction'][b'bottom'], settings[b'direction'][b'left'])
            GUI.setHorizontalBlurParams(spaceID, settings[b'horizontalParams'][b'leftStart'], settings[b'horizontalParams'][b'leftEnd'], settings[b'horizontalParams'][b'rightStart'], settings[b'horizontalParams'][b'rightEnd'])
            GUI.setVerticalBlurParams(spaceID, settings[b'verticalParams'][b'topStart'], settings[b'verticalParams'][b'topEnd'], settings[b'verticalParams'][b'bottomStart'], settings[b'verticalParams'][b'bottomEnd'])
            GUI.setVerticalBlurAlphas(spaceID, settings[b'verticalAlphas'][b'topStart'], settings[b'verticalAlphas'][b'topEnd'], settings[b'verticalAlphas'][b'bottomStart'], settings[b'verticalAlphas'][b'bottomEnd'])
            GUI.setHorizontalBlurAlphas(spaceID, settings[b'horizontalAlphas'][b'leftStart'], settings[b'horizontalAlphas'][b'leftEnd'], settings[b'horizontalAlphas'][b'rightStart'], settings[b'horizontalAlphas'][b'rightEnd'])
            x, y = settings[b'center']
            width, height = GUI.screenResolution()
            if isnan(x):
                x = int(width / 2.0)
            if isnan(y):
                y = int(height / 2.0)
            GUI.setBlurCenter(spaceID, x, y)
            return

    @classmethod
    def disable(cls, blur):
        specificConfig = cls.getSpecificConfig(blur.config)
        if specificConfig is not None:
            GUI.enableBackgroundBlurFeature(specificConfig.spaceID, False)
        return


class SceneBlur(Blur):
    _globalBlur = GUI.WGUIBackgroundBlur()
    _rects = set()

    @classmethod
    def unregister(cls, blur, restoredBlur=None):
        specificConfig = cls.getSpecificConfig(blur.config)
        if specificConfig is not None:
            cls.disable(blur)
            cls._clearRects()
        if restoredBlur is not None:
            specificRestoredConfig = cls.getSpecificConfig(restoredBlur.config)
            if specificRestoredConfig is not None:
                specificRestoredConfig.fadeTime = 0
                cls.apply(restoredBlur)
        return

    @classmethod
    def getSpecificConfig(cls, config):
        return findFirst((lambda x: isinstance(x, SceneBlurConfig)), config)

    @classmethod
    def apply(cls, blur):
        specificConfig = SceneBlur.getSpecificConfig(blur.config)
        if specificConfig is None:
            return
        else:
            cls._clearRects()
            SceneBlur._globalBlur.enable = specificConfig.enabled
            if not specificConfig.enabled:
                return
            SceneBlur._globalBlur.fadeTime = specificConfig.fadeTime
            if specificConfig.blurRadius is not None:
                SceneBlur._globalBlur.blurRadius = specificConfig.blurRadius
            for rect in specificConfig.rects:
                rectID = next(_idsGenerator)
                SceneBlur._rects.add(rectID)
                SceneBlur._globalBlur.addRect(rectID, rect)

            return

    @classmethod
    def disable(cls, blur):
        SceneBlur._globalBlur.enable = False
        return

    @classmethod
    def _clearRects(cls):
        for id in SceneBlur._rects:
            SceneBlur._globalBlur.removeRect(id)

        SceneBlur._rects.clear()
        return


class UILayerBlur(Blur):

    @classmethod
    def getSpecificConfig(cls, config):
        return findFirst((lambda x: isinstance(x, UILayerBlurConfig)), config)

    @classmethod
    def apply(cls, blur):
        config = UILayerBlur.getSpecificConfig(blur.config)
        if config is None:
            return
        else:
            if not config.enabled or config.ownLayer is None:
                return
            appLoader = dependency.instance(IAppLoader)
            lobby = appLoader.getApp(_SPACE.SF_LOBBY)
            battle = appLoader.getApp(_SPACE.SF_BATTLE)
            if lobby is not None:
                lobby.blurBackgroundViews(config.ownLayer, config.blurAnimRepeatCount, config.uiBlurRadius)
            elif battle is not None:
                battle.blurBackgroundViews(config.ownLayer, config.blurAnimRepeatCount, config.uiBlurRadius)
            return

    @classmethod
    def disable(cls, blur):
        appLoader = dependency.instance(IAppLoader)
        lobby = appLoader.getApp(_SPACE.SF_LOBBY)
        battle = appLoader.getApp(_SPACE.SF_BATTLE)
        if lobby is not None:
            lobby.unblurBackgroundViews()
        elif battle is not None:
            battle.unblurBackgroundViews()
        return


class ImmediateSceneBlurConfig(object):
    BLUR_CLS = ImmediateSceneBlur

    def __init__(self, enabled=False, spaceID=0, settings=None, persistent=False):
        self.enabled = enabled
        self.spaceID = spaceID
        self.settings = settings
        self.persistent = persistent
        return


class SceneBlurConfig(object):
    BLUR_CLS = SceneBlur

    def __init__(self, enabled=False, fadeTime=0, blurRadius=None, rects=None, persistent=False):
        self.enabled = enabled
        self.fadeTime = fadeTime
        self.blurRadius = blurRadius
        self.rects = rects
        self.persistent = persistent
        return


class UILayerBlurConfig(object):
    BLUR_CLS = UILayerBlur

    def __init__(self, enabled=False, ownLayer=None, blurAnimRepeatCount=_DEFAULT_BLUR_ANIM_REPEAT_COUNT, uiBlurRadius=_DEFAULT_UI_BLUR_RADIUS, persistent=False):
        self.enabled = enabled
        self.ownLayer = ownLayer
        self.blurAnimRepeatCount = blurAnimRepeatCount
        self.uiBlurRadius = uiBlurRadius
        self.persistent = persistent
        return


class CachedBlur(object):

    def __init__(self, enabled=False, fadeTime=0, ownLayer=None, blurAnimRepeatCount=_DEFAULT_BLUR_ANIM_REPEAT_COUNT, blurRadius=None, uiBlurRadius=_DEFAULT_UI_BLUR_RADIUS):
        blurCtrl = dependency.instance(IBlurController)
        self.__sceneBlurConfig = SceneBlurConfig(enabled, fadeTime, blurRadius, [])
        self.__blurConfig = (
         UILayerBlurConfig(enabled, ownLayer, blurAnimRepeatCount, uiBlurRadius),
         self.__sceneBlurConfig)
        self.__rects = {}
        self.__blur = blurCtrl.createBlur(self.__blurConfig)
        return

    def fini(self):
        self.__blur.fini()
        return

    def enable(self):
        self.__blur.enable()
        return

    def disable(self):
        self.__blur.disable()
        return

    def addRect(self, blurRect):
        id = next(_idsGenerator)
        self.__rects[id] = blurRect
        self.__updateRects()
        return id

    def changeRect(self, rectId, blurRect):
        self.__rects[rectId] = blurRect
        self.__updateRects()
        return

    def removeRect(self, rectId):
        self.__rects.pop(rectId)
        self.__updateRects()
        return

    @property
    def config(self):
        return self.__blur.config

    @property
    def enabled(self):
        return self.__sceneBlurConfig.enabled

    def __updateRects(self):
        self.__sceneBlurConfig.rects = listvalues(self.__rects)
        self.__blur.updateConfig(self.__blurConfig)
        return
