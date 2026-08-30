from __future__ import absolute_import
from account_helpers import AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR
from account_helpers.settings_core.settings_constants import GuiSettingsBehavior
from frameworks.wulf import WindowLayer
from gui import GUI_SETTINGS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.impl import backport
from gui.impl.gen import R
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_MAIN_PAGE_SOUND_SPACE
from gui.ranked_battles.ranked_helpers import getRankedBattlesIntroPageUrl
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.RankedBattlesIntroMeta import RankedBattlesIntroMeta
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS
from gui.shared import event_dispatcher, events, EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showBrowserOverlayView
from gui.shared.utils.functions import getUniqueViewName
from gui.shared.formatters import text_styles
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IRankedBattlesController
from web.web_client_api import webApiCollection, ui as ui_web_api, sound as sound_web_api
BLOCKS_COUNT = 3

class RankedBattlesIntro(LobbySubView, RankedBattlesIntroMeta):
    _COMMON_SOUND_SPACE = RANKED_MAIN_PAGE_SOUND_SPACE
    __rankedController = dependency.descriptor(IRankedBattlesController)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def onAcceptClick(self):
        self.__setShowStateFlags()
        self.onClose()
        return

    def onClose(self):
        self.__setShowStateFlags()
        event_dispatcher.showHangar()
        return

    def onDetailedClick(self):
        url = GUI_SETTINGS.lookup(b'infoPageRanked')
        showBrowserOverlayView(url, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(
         WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))
        return

    def onPlayVideoClick(self):
        self.__showVideo()
        return

    def _populate(self):
        super(RankedBattlesIntro, self)._populate()
        self.__update()
        self.__rankedController.onUpdated += self.__update
        self.__rankedController.onGameModeStatusUpdated += self.__update
        self.__rankedController.onGameModeStatusTick += self.__updateTimer
        return

    def _dispose(self):
        self.__rankedController.onGameModeStatusTick -= self.__updateTimer
        self.__rankedController.onGameModeStatusUpdated -= self.__update
        self.__rankedController.onUpdated -= self.__update
        super(RankedBattlesIntro, self)._dispose()
        return

    def __update(self, _=None):
        headerData = {b'title': (backport.text(R.strings.ranked_battles.rankedBattle.title())), 
           b'mainDescr': (backport.text(R.strings.ranked_battles.introPage.description())), 
           b'extraDescr': None, 
           b'tooltip': None}
        blocksData = []
        for index in range(BLOCKS_COUNT):
            index += 1
            imgSource = backport.image(R.images.gui.maps.icons.rankedBattles.intro.dyn((b'block{}').format(index))())
            title = text_styles.promoSubTitle(backport.text(R.strings.ranked_battles.introPage.blocks.dyn((b'block{}').format(index)).title()))
            descr = text_styles.mainBig(backport.text(R.strings.ranked_battles.introPage.blocks.dyn((b'block{}').format(index)).description()))
            blocksData.append({b'imgSource': imgSource, 
               b'title': title, 
               b'description': descr})

        if not self.__rankedController.isYearRewardEnabled():
            blocksData[-1][b'imgSource'] = backport.image(R.images.gui.maps.icons.rankedBattles.intro.yearRewardDisabled())
            blocksData[-1][b'description'] = text_styles.mainBig(backport.text(R.strings.ranked_battles.introPage.blocks.yearRewardDisabled()))
        url = getRankedBattlesIntroPageUrl()
        self.__state = RANKEDBATTLES_CONSTS.INTRO_STATE_NORMAL
        if self.__rankedController.isFrozen():
            self.__state = RANKEDBATTLES_CONSTS.INTRO_STATE_DISABLED
            if not self.__rankedController.getSeasonsPassed() and not self.__rankedController.getCurrentSeason():
                self.__state = RANKEDBATTLES_CONSTS.INTRO_STATE_BEFORE_SEASON
        if self.__state == RANKEDBATTLES_CONSTS.INTRO_STATE_DISABLED:
            self.as_setAlertMessageBlockDataS({b'alertIcon': (backport.image(R.images.gui.maps.icons.library.alertBigIcon())), 
               b'statusText': (text_styles.vehicleStatusCriticalText(backport.text(R.strings.ranked_battles.introPage.alert.disabled()))), 
               b'buttonVisible': False})
        elif self.__state == RANKEDBATTLES_CONSTS.INTRO_STATE_BEFORE_SEASON:
            self.__updateTimer()
        if self.__state != RANKEDBATTLES_CONSTS.INTRO_STATE_NORMAL and self.__rankedController.getRankedWelcomeCallback() is None:
            self.__rankedController.setRankedWelcomeCallback((lambda : None))
        self.as_setDataS({b'state': (self.__state), 
           b'hasURL': (bool(url)), 
           b'headerData': headerData, 
           b'blocksData': blocksData})
        return

    def __updateTimer(self):
        timeTill = self.__rankedController.getTimer()
        if self.__state == RANKEDBATTLES_CONSTS.INTRO_STATE_BEFORE_SEASON:
            self.as_setBeforeSeasonBlockDataS({b'title': (text_styles.highlightText(backport.text(R.strings.ranked_battles.introPage.alert.beforeSeason()))), 
               b'time': (text_styles.highlightText(backport.getTillTimeStringByRClass(timeTill, R.strings.ranked_battles.introPage.timeLeft))), 
               b'iconSrc': (backport.image(R.images.gui.maps.icons.library.ClockIcon_1()))})
        return

    def __showVideo(self):
        webHandlers = webApiCollection(ui_web_api.CloseViewWebApi, sound_web_api.SoundWebApi, sound_web_api.HangarSoundWebApi)
        alias = VIEW_ALIAS.BROWSER_VIEW
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(alias, getUniqueViewName(alias)), ctx={b'url': (getRankedBattlesIntroPageUrl()), 
           b'webHandlers': webHandlers, 
           b'returnAlias': (self.alias)}), EVENT_BUS_SCOPE.LOBBY)
        return

    def __getShowStateFlags(self):
        defaults = AccountSettings.getFilterDefault(GUI_START_BEHAVIOR)
        return self.__settingsCore.serverSettings.getSection(GUI_START_BEHAVIOR, defaults)

    def __setShowStateFlags(self):
        if self.__state != RANKEDBATTLES_CONSTS.INTRO_STATE_NORMAL:
            return
        stateFlags = self.__getShowStateFlags()
        stateFlags[GuiSettingsBehavior.RANKED_WELCOME_VIEW_SHOWED] = True
        self.__settingsCore.serverSettings.setSectionSettings(GUI_START_BEHAVIOR, stateFlags)
        return
