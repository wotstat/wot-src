from frameworks.wulf import WindowFlags, ViewSettings, WindowLayer
from gui.Scaleform.daapi.view.meta.TutorialDialogMeta import TutorialDialogMeta
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from helpers import dependency
from skeletons.tutorial import ITutorialLoader
from tutorial.control import TutorialProxyHolder
from tutorial.data.bootcamp.effects import RequestExclusiveHintEffect
from tutorial.data.conditions import Conditions
from tutorial.data.effects import SimpleEffect, EFFECT_TYPE
from tutorial.data.events import ClickEvent
from tutorial.gui import GUI_EFFECT_NAME
from tutorial.logger import LOG_ERROR

class TutorialPopUp(AbstractWindowView, TutorialProxyHolder):

    def __init__(self, content):
        super(TutorialPopUp, self).__init__()
        self._content = content
        return

    @property
    def content(self):
        return self._content

    @property
    def tutorial(self):
        return self._tutorial

    def _onMouseClicked(self, targetKey):
        if not self._gui:
            return
        if targetKey in self._content:
            targetID = self._content[targetKey]
            if targetID:
                self._gui.onGUIInput(ClickEvent(targetID))
        else:
            LOG_ERROR(b'Target not found in data', targetKey)
        return


class TutorialDialog(TutorialPopUp, TutorialDialogMeta):

    def _stop(self, needCloseWindow=True):
        self._content.clear()
        self._gui.effects.stop(GUI_EFFECT_NAME.SHOW_DIALOG, effectID=self.uniqueName)
        if needCloseWindow:
            self.destroy()
        return

    def submit(self):
        self._onMouseClicked(b'submitID')
        self._stop()
        return

    def cancel(self):
        self._onMouseClicked(b'cancelID')
        self._stop()
        return

    def onCustomButton(self, needStopEffect, needCloseWindow):
        self._onMouseClicked(b'customID')
        if needStopEffect:
            self._stop(needCloseWindow)
        return

    def onWindowClose(self):
        self.cancel()
        return


class TutorialWindow(TutorialPopUp):

    def _stop(self):
        self._content.clear()
        self._gui.effects.stop(GUI_EFFECT_NAME.SHOW_WINDOW, effectID=self.uniqueName)
        return

    def onWindowClose(self):
        self._onMouseClicked(b'closeID')
        self._stop()
        return


class TutorialWulfWindow(LobbyWindow, TutorialProxyHolder):
    __slots__ = (b'__effectData',)
    tutorialLoader = dependency.descriptor(ITutorialLoader)

    def __init__(self, content, effectData):
        super(TutorialWulfWindow, self).__init__(content=content, wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.WINDOW)
        self.__effectData = effectData
        return

    def getLayoutID(self):
        content = self.content
        if content is not None:
            return content.getLayoutID()
        else:
            return 0

    def setResultVar(self, value):
        varID = self.__effectData.get(b'resultVarID')
        if varID:
            self._tutorial.getVars().set(varID, value)
        else:
            LOG_ERROR(b'no variable ID provided to save resultVarID!')
        return

    def submit(self):
        self._gui.effects.stop(GUI_EFFECT_NAME.SHOW_DIALOG, effectID=self.__effectData[b'dialogID'])
        self.destroy()
        return

    def showHint(self, hintName):
        hintEffect = RequestExclusiveHintEffect(hintName, None, Conditions())
        hintFuncEffect = self._ctrlFactory.createFuncEffect(hintEffect)
        hintFuncEffect.triggerEffect()
        updateEffect = SimpleEffect(EFFECT_TYPE.UPDATE_EXCLUSIVE_HINTS, Conditions())
        updateFuncEffect = self._ctrlFactory.createFuncEffect(updateEffect)
        updateFuncEffect.triggerEffect()
        return


class TutorialWulfWindowView(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(self.getLayoutID())
        settings.model = self._createModel()
        settings.args = args
        settings.kwargs = kwargs
        super(TutorialWulfWindowView, self).__init__(settings)
        return

    def submit(self):
        window = self.getParentWindow()
        if window is not None:
            window.submit()
        return

    def setResultVar(self, value):
        window = self.getParentWindow()
        if window is not None:
            window.setResultVar(value)
        return

    def getLayoutID(self):
        raise NotImplementedError
        return

    def _createModel(self):
        raise NotImplementedError
        return

    def _showHint(self, hintName):
        window = self.getParentWindow()
        if window is not None:
            window.showHint(hintName)
        return
