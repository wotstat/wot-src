from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ApplicationMeta(BaseDAAPIComponent):

    def setLoaderMgr(self, mgr):
        self._printOverrideError(b'setLoaderMgr')
        return

    def setGlobalVarsMgr(self, mgr):
        self._printOverrideError(b'setGlobalVarsMgr')
        return

    def setSoundMgr(self, mgr):
        self._printOverrideError(b'setSoundMgr')
        return

    def setCursorMgr(self, mgr):
        self._printOverrideError(b'setCursorMgr')
        return

    def setContainerMgr(self, mgr):
        self._printOverrideError(b'setContainerMgr')
        return

    def setContextMenuMgr(self, mgr):
        self._printOverrideError(b'setContextMenuMgr')
        return

    def setPopoverMgr(self, mgr):
        self._printOverrideError(b'setPopoverMgr')
        return

    def setColorSchemeMgr(self, mgr):
        self._printOverrideError(b'setColorSchemeMgr')
        return

    def setEventLogMgr(self, mgr):
        self._printOverrideError(b'setEventLogMgr')
        return

    def setTooltipMgr(self, mgr):
        self._printOverrideError(b'setTooltipMgr')
        return

    def setVoiceChatMgr(self, mgr):
        self._printOverrideError(b'setVoiceChatMgr')
        return

    def setUtilsMgr(self, mgr):
        self._printOverrideError(b'setUtilsMgr')
        return

    def setTweenMgr(self, mgr):
        self._printOverrideError(b'setTweenMgr')
        return

    def setGameInputMgr(self, mgr):
        self._printOverrideError(b'setGameInputMgr')
        return

    def setCacheMgr(self, mgr):
        self._printOverrideError(b'setCacheMgr')
        return

    def setTextMgr(self, mgr):
        self._printOverrideError(b'setTextMgr')
        return

    def setTutorialMgr(self, mgr):
        self._printOverrideError(b'setTutorialMgr')
        return

    def setImageManager(self, mgr):
        self._printOverrideError(b'setImageManager')
        return

    def setGraphicsOptimizationManager(self, mgr):
        self._printOverrideError(b'setGraphicsOptimizationManager')
        return

    def setUILoggerMgr(self, mgr):
        self._printOverrideError(b'setUILoggerMgr')
        return

    def handleGlobalKeyEvent(self, command):
        self._printOverrideError(b'handleGlobalKeyEvent')
        return

    def onAsInitializationCompleted(self):
        self._printOverrideError(b'onAsInitializationCompleted')
        return

    def as_isDAAPIInitedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_isDAAPIInited()
        return

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()
        return

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()
        return

    def as_registerManagersS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_registerManagers()
        return

    def as_loadLibrariesS(self, list):
        if self._isDAAPIInited():
            return self.flashObject.as_loadLibraries(list)
        return

    def as_updateStageS(self, w, h, scale):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStage(w, h, scale)
        return

    def as_blurBackgroundViewsS(self, ownLayer, blurAnimRepeatCount):
        if self._isDAAPIInited():
            return self.flashObject.as_blurBackgroundViews(ownLayer, blurAnimRepeatCount)
        return

    def as_unblurBackgroundViewsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_unblurBackgroundViews()
        return
