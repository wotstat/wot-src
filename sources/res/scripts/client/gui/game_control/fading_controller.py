from __future__ import absolute_import
from future.utils import viewvalues
from gui.impl.common.fade_manager import FadeManager, DefaultFadingCover
from wg_async import wg_await, wg_async
from skeletons.gui.game_control import IFadingController

class FadingController(IFadingController):

    def __init__(self):
        super(FadingController, self).__init__()
        self._managerByLayer = {}
        return

    @wg_async
    def show(self, layerID):
        fadeManager = self._getFadeManager(layerID)
        if not fadeManager.isAnimating:
            yield wg_await(fadeManager.show())
        return

    @wg_async
    def hide(self, layerID):
        fadeManager = self._getFadeManager(layerID)
        if fadeManager.isAnimating:
            yield wg_await(fadeManager.hide())
        return

    def onDisconnected(self):
        self._hideImmediately()
        return

    def onAvatarBecomePlayer(self):
        self._hideImmediately()
        return

    def onAccountBecomePlayer(self):
        self._hideImmediately()
        return

    def _hideImmediately(self):
        for fadeManager in viewvalues(self._managerByLayer):
            fadeManager.hideImmediately()

        return

    def _getFadeManager(self, layerID):
        if layerID in self._managerByLayer:
            return self._managerByLayer[layerID]
        fadeManager = FadeManager(layer=layerID, coverFactory=DefaultFadingCover)
        self._managerByLayer[layerID] = fadeManager
        return fadeManager
