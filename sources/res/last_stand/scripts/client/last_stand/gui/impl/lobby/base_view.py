from __future__ import absolute_import
import typing
from frameworks.wulf import WindowLayer
from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from helpers import dependency
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow, LobbyNotificationWindow
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared.view_helpers.blur_manager import CachedBlur
from last_stand.skeletons.ls_controller import ILSController
from skeletons.gui.app_loader import IAppLoader

class BaseView(ViewImpl, IGlobalListener):
    lsCtrl = dependency.descriptor(ILSController)

    def onPrbEntitySwitched(self):
        if not self.lsCtrl.isAvailable():
            self._onClose()
        return

    def _subscribe(self):
        super(BaseView, self)._subscribe()
        self.lsCtrl.onEventDisabled += self._onEventDisabled
        return

    def _unsubscribe(self):
        self.lsCtrl.onEventDisabled -= self._onEventDisabled
        super(BaseView, self)._unsubscribe()
        return

    def _onLoading(self, *args, **kwargs):
        super(BaseView, self)._onLoading(*args, **kwargs)
        self.startGlobalListening()
        return

    def _finalize(self):
        self.stopGlobalListening()
        super(BaseView, self)._finalize()
        return

    def _onEventDisabled(self):
        if not self.lsCtrl.isAvailable():
            self._onClose()
        return

    def _onClose(self):
        self.destroyWindow()
        return


class SwitcherPresenter(ViewComponent, IGlobalListener):
    lsCtrl = dependency.descriptor(ILSController)

    def __init__(self):
        super(SwitcherPresenter, self).__init__(R.aliases.last_stand.shared.Switcher())
        return

    def onPrbEntitySwitched(self):
        if not self.lsCtrl.isAvailable():
            self._onClose()
        return

    def _onLoading(self, *args, **kwargs):
        super(SwitcherPresenter, self)._onLoading(*args, **kwargs)
        self.startGlobalListening()
        self.lsCtrl.onEventDisabled += self._onEventDisabled
        return

    def _finalize(self):
        self.stopGlobalListening()
        self.lsCtrl.onEventDisabled -= self._onEventDisabled
        super(SwitcherPresenter, self)._finalize()
        return

    def _onEventDisabled(self):
        if not self.lsCtrl.isAvailable():
            self._onClose()
        return

    def _onClose(self):
        self.destroyWindow()
        return


class EventLobbyWindow(LobbyWindow):
    __appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, wndFlags, decorator=None, content=None, parent=None, layer=WindowLayer.UNDEFINED):
        super(EventLobbyWindow, self).__init__(wndFlags=wndFlags, decorator=decorator, content=content, parent=parent, layer=layer)
        self._blur = None
        return

    def _initialize(self):
        super(EventLobbyWindow, self)._initialize()
        self._blur = CachedBlur(enabled=True, ownLayer=self.layer - 1)
        containerManager = self.__appLoader.getApp().containerManager
        if containerManager:
            containerManager.onViewAddedToContainer += self.__onViewLoaded
        return

    def __onViewLoaded(self, _, *args):
        self._blur.enable()
        return

    def _finalize(self):
        if self._blur:
            self._blur.fini()
        containerManager = self.__appLoader.getApp().containerManager
        if containerManager:
            containerManager.onViewAddedToContainer -= self.__onViewLoaded
        super(EventLobbyWindow, self)._finalize()
        return


class EventLobbyNotificationWindow(LobbyNotificationWindow):
    __appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, wndFlags, decorator=None, content=None, parent=None, layer=WindowLayer.UNDEFINED):
        super(EventLobbyNotificationWindow, self).__init__(wndFlags=wndFlags, decorator=decorator, content=content, parent=parent, layer=layer)
        self._blur = None
        return

    def load(self):
        if self._blur is None:
            self._blur = CachedBlur(enabled=True, ownLayer=self.layer - 1)
        super(EventLobbyNotificationWindow, self).load()
        return

    def _initialize(self):
        super(EventLobbyNotificationWindow, self)._initialize()
        containerManager = self.__appLoader.getApp().containerManager
        if containerManager:
            containerManager.onViewAddedToContainer += self.__onViewLoaded
        return

    def __onViewLoaded(self, _, *args):
        self._blur.enable()
        return

    def _finalize(self):
        if self._blur:
            self._blur.fini()
        containerManager = self.__appLoader.getApp().containerManager
        if containerManager:
            containerManager.onViewAddedToContainer -= self.__onViewLoaded
        super(EventLobbyNotificationWindow, self)._finalize()
        return
