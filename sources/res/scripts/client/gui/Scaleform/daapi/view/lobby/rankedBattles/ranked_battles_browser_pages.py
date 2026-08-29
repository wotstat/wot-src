from helpers import dependency
from gui.Scaleform.daapi.view.lobby.components.browser_view_page import BrowserPageComponent
from gui.Scaleform.daapi.view.lobby.hangar.BrowserView import BrowserView
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_battles_page import IResetablePage
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_MAIN_PAGE_SOUND_SPACE, RANKED_OVERLAY_SOUND_SPACE, Sounds, AmbientType
from skeletons.gui.game_control import IRankedBattlesController
from web.web_client_api.ranked_battles import createRankedBattlesWebHandlers, createRankedOverlayHandlers

class RankedBrowserPage(BrowserPageComponent, IResetablePage):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self):
        super(RankedBrowserPage, self).__init__()
        self.__ctx = self.__rankedController.getWebOpenPageCtx()
        self.__isInited = False
        return

    def reset(self):
        self._updateSounds(self.__rankedController.getSoundManager())
        ctx = self.__rankedController.getWebOpenPageCtx()
        if self.__isInited:
            if ctx is not None and (ctx.get(b'webParams', b'') or ctx.get(b'clientParams', {})):
                self.__ctx = ctx
                self.invalidateUrl()
            elif self._isForcedRefresh() or self._wasError:
                self.refreshUrl()
        return

    def _isForcedRefresh(self):
        return False

    def _getWebHandlers(self):
        return createRankedBattlesWebHandlers()

    def _getUrl(self):
        url = self._getBaseUrl(**self.__getClientParams()) + self.__patchUrlByCtx()
        self.__isInited = True
        self.__ctx = None
        return url

    def _getBaseUrl(self, **kwargs):
        raise NotImplementedError
        return

    def _updateSounds(self, soundManager):
        return

    def __getClientParams(self):
        if self.__ctx is not None:
            return self.__ctx.get(b'clientParams', {})
        else:
            return {}

    def __patchUrlByCtx(self):
        if self.__ctx is not None:
            return self.__ctx.get(b'webParams', b'')
        else:
            return b''


class RankedLandingView(BrowserView):
    _BROWSER_SOUND_SPACE = RANKED_MAIN_PAGE_SOUND_SPACE
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def onEscapePress(self):
        self.onCloseBtnClick()
        return

    def _populate(self):
        super(RankedLandingView, self)._populate()
        self._populateSoundEnv(self.__rankedController.getSoundManager())
        self.__rankedController.onUpdated += self._checkDestroy
        return

    def _dispose(self):
        self.__rankedController.onUpdated -= self._checkDestroy
        self._disposeSoundEnv(self.__rankedController.getSoundManager())
        self.__rankedController.onKillWebOverlays()
        super(RankedLandingView, self)._dispose()
        return

    def _populateSoundEnv(self, soundManager):
        soundManager.onSoundModeChanged(True, Sounds.PROGRESSION_STATE_LEAGUES)
        return

    def _disposeSoundEnv(self, soundManager):
        if self.__rankedController.isRankedPrbActive():
            if self.__rankedController.isAccountMastered():
                soundManager.setProgressSound()
            else:
                soundManager.setDefaultProgressSound()
        else:
            self.__rankedController.getSoundManager().onSoundModeChanged(False)
        return

    def _checkDestroy(self):
        return


class RankedShopLandingView(RankedLandingView):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def _populateSoundEnv(self, soundManager):
        soundManager.onSoundModeChanged(True, Sounds.PROGRESSION_STATE_SHOP)
        soundManager.setAmbient(AmbientType.HANGAR)
        return

    def _checkDestroy(self):
        if not self.__rankedController.isRankedShopEnabled():
            self.onEscapePress()
        return


class RankedYearLBLandingView(RankedLandingView):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def _checkDestroy(self):
        if not self.__rankedController.isYearLBEnabled():
            self.onEscapePress()
        return


class RankedWebOverlay(WebView):
    _COMMON_SOUND_SPACE = RANKED_OVERLAY_SOUND_SPACE
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def webHandlers(self):
        return createRankedOverlayHandlers()

    def _populate(self):
        super(RankedWebOverlay, self)._populate()
        self.__rankedController.onKillWebOverlays += self.__destroy
        return

    def _dispose(self):
        self.__rankedController.onKillWebOverlays -= self.__destroy
        super(RankedWebOverlay, self)._dispose()
        return

    def __destroy(self):
        self.onEscapePress()
        return
