import WWISE, BigWorld, BattleReplay, Windowing
from PlayerEvents import g_playerEvents
from bootcamp.Bootcamp import BOOTCAMP_SOUND, BOOTCAMP_UI_COMPONENTS
from constants import WOT_GAMEPLAY
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.BCIntroVideoPageMeta import BCIntroVideoPageMeta
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.app_loader.settings import APP_NAME_SPACE
from bootcamp.BootCampEvents import g_bootcampEvents
from bootcamp.BootcampSettings import getBattleDefaults
from debug_utils_bootcamp import LOG_ERROR_BOOTCAMP
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from gui.Scaleform.locale.BOOTCAMP import BOOTCAMP
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.game_control import IBootcampController, IDemoAccCompletionController
PATH_BACKGROUNDS = b'../maps/icons/bootcamp/loading/{0}_{1}.png'
PATH_BACKGROUNDS_CORE = b'../maps/icons/bootcamp/loading/{0}_{1}_core.png'
LINKAGE_BACKGROUNDS = b'{0}Page{1}UI'

class INTRO_HIGHLIGHT_TYPE(object):
    START_BUTTON = 0
    ARROWS = 1
    WELCOME_START_BUTTON = 2


class BCIntroPage(BCIntroVideoPageMeta):
    bootcampCtrl = dependency.descriptor(IBootcampController)
    appLoader = dependency.descriptor(IAppLoader)
    demoAccController = dependency.descriptor(IDemoAccCompletionController)

    def __init__(self, settings):
        super(BCIntroPage, self).__init__()
        self._videoPlayerVisible = False
        self._movieFile = None
        self._backgroundVideo = None
        self._backgroundVideoBufferTime = None
        self._backgroundMusicStartEvent = None
        self._backgroundMusicStopEvent = None
        self._backgroundMusicPauseEvent = None
        self._backgroundMusicResumeEvent = None
        self._lessonNumber = settings.get(b'lessonNumber', 0)
        self._tutorialPages = settings.get(b'tutorialPages', [])
        self._autoStart = settings.get(b'autoStart', False)
        self._showSkipOption = (BattleReplay.isPlaying() or settings.get)(b'showSkipOption', True) if 1 else False
        self._isReferralEnabled = settings.get(b'isReferralEnabled', False)
        self._isChoice = settings.get(b'isChoice', False)
        self._highlightingMask = 0
        self._goToBattleEvent = lambda : g_bootcampEvents.onGameplayChoice(WOT_GAMEPLAY.BOOTCAMP, WOT_GAMEPLAY.ON)
        self._isWindowAccessible = True
        self._delayedVideoStart = False
        return

    def videoFinished(self):
        self._onFinish()
        self.as_showIntroPageS(len(self._tutorialPages) == 0, self.bootcampCtrl.needAwarding())
        return

    def videoStarted(self):
        if self._movieFile and self._backgroundMusicStartEvent:
            WWISE.WW_eventGlobal(self._backgroundMusicStartEvent)
        return

    def goToBattle(self):
        BigWorld.callback(0.1, self._goToBattleEvent)
        if self._isCurrentlyHighlighting(INTRO_HIGHLIGHT_TYPE.START_BUTTON):
            self._setHighlighting(INTRO_HIGHLIGHT_TYPE.START_BUTTON, False)
        return

    def skipBootcamp(self):
        if self._isChoice:
            if self.demoAccController.isDemoAccount:
                self.demoAccController.runDemoAccRegistration()
                self.goToBattle()
            else:
                g_bootcampEvents.onGameplayChoice(WOT_GAMEPLAY.BOOTCAMP, WOT_GAMEPLAY.OFF)
        else:
            self.bootcampCtrl.runBootcamp()
        return

    def handleError(self, data):
        LOG_ERROR_BOOTCAMP((b'Video error - {0}').format(data))
        self._onFinish()
        return

    @staticmethod
    def _getBackgroundBlind(imagePath):
        if imagePath in RES_ICONS.MAPS_ICONS_BOOTCAMP_LOADING_ALL_CORE_ENUM:
            return imagePath
        return b''

    @staticmethod
    def _getTutorialPageVO(pageId, bigSize):
        battleDefaults = getBattleDefaults()
        lessonProps = battleDefaults[b'lessonPages'][pageId]
        pathBackgroundSize = b'big' if bigSize else b'small'
        linkageBackgroundSize = b'Big' if bigSize else b'Small'
        voSettings = {b'background': (PATH_BACKGROUNDS.format(pageId, pathBackgroundSize)), 
           b'backgroundBlind': (BCIntroPage._getBackgroundBlind(PATH_BACKGROUNDS_CORE.format(pageId, pathBackgroundSize))), 
           b'rendererLinkage': (LINKAGE_BACKGROUNDS.format(pageId, linkageBackgroundSize))}
        voSettings.update(lessonProps)
        return voSettings

    def _populate(self):
        super(BCIntroPage, self)._populate()
        Waiting.hide(b'login')
        self.as_showIntroPageS(False)
        self._isWindowAccessible = Windowing.isWindowAccessible() if self._canWindowBePaused() else True
        if self._movieFile:
            if self._isWindowAccessible:
                self._start()
            else:
                self._delayedVideoStart = True
            if self._canWindowBePaused():
                Windowing.addWindowAccessibilitynHandler(self._onWindowAccessibilityChanged)
        else:
            self._start()
        if self._shouldHighlight(INTRO_HIGHLIGHT_TYPE.ARROWS):
            self._setHighlighting(INTRO_HIGHLIGHT_TYPE.ARROWS, True)
        g_playerEvents.onDisconnected += self._onDisconnected
        return

    def _canWindowBePaused(self):
        return not BigWorld.checkUnattended()

    def _dispose(self):
        g_playerEvents.onDisconnected -= self._onDisconnected
        for highlightType in (INTRO_HIGHLIGHT_TYPE.ARROWS, INTRO_HIGHLIGHT_TYPE.START_BUTTON):
            if self._isCurrentlyHighlighting(highlightType):
                self._setHighlighting(highlightType, False)

        self.appLoader.detachCursor(APP_NAME_SPACE.SF_BATTLE)
        if self._movieFile and self._canWindowBePaused():
            Windowing.removeWindowAccessibilityHandler(self._onWindowAccessibilityChanged)
        if self._movieFile and self._backgroundMusicStopEvent:
            WWISE.WW_eventGlobal(self._backgroundMusicStopEvent)
        super(BCIntroPage, self)._dispose()
        return

    def _start(self):
        listSmall = []
        listBig = []
        for pageId in self._tutorialPages:
            listSmall.append(self._getTutorialPageVO(pageId, False))
            listBig.append(self._getTutorialPageVO(pageId, True))

        pageCount = len(listSmall)
        label = BOOTCAMP.BTN_TUTORIAL_START if self._showSkipOption and self._lessonNumber == 0 else BOOTCAMP.BTN_CONTINUE_PREBATTLE
        self.as_setDataS({b'isReferralEnabled': (self._isReferralEnabled), 
           b'isBootcampCloseEnabled': (self._isReferralEnabled), 
           b'referralDescription': (BOOTCAMP.WELLCOME_BOOTCAMP_REFERRAL), 
           b'showTutorialPages': (pageCount > 0), 
           b'backgroundVideo': (self._backgroundVideo), 
           b'source': (self._movieFile), 
           b'lessonPagesSmallData': listSmall, 
           b'lessonPagesBigData': listBig, 
           b'autoStart': (self._autoStart), 
           b'navigationButtonsVisible': (pageCount > 1), 
           b'videoPlayerVisible': (self._videoPlayerVisible), 
           b'allowSkipButton': (self._showSkipOption), 
           b'selectButtonLabel': label, 
           b'bufferTime': (self._backgroundVideoBufferTime), 
           b'rewards': [
                      self._getReward(BOOTCAMP.WELLCOME_BOOTCAMP_REWARDS_PREMIUM, RES_ICONS.MAPS_ICONS_BOOTCAMP_REWARDS_PREM_BIG_176X102, [
                       BOOTCAMP.TOOLTIP_PROGRESSION_LABEL_PREMIUM,
                       BOOTCAMP.TOOLTIP_PROGRESSION_DESCRIPTION_PREMIUM,
                       RES_ICONS.MAPS_ICONS_BOOTCAMP_REWARDS_TOOLTIPS_BCPREMIUMPLUS, 50]),
                      self._getReward(BOOTCAMP.WELLCOME_BOOTCAMP_REWARDS_GOLD, RES_ICONS.MAPS_ICONS_BOOTCAMP_REWARDS_GOLD_BIG_176X102, [
                       BOOTCAMP.TOOLTIP_PROGRESSION_LABEL_GOLD,
                       BOOTCAMP.TOOLTIP_PROGRESSION_DESCRIPTION_GOLD,
                       RES_ICONS.MAPS_ICONS_BOOTCAMP_REWARDS_TOOLTIPS_BCGOLD, 50]),
                      self._getReward(BOOTCAMP.WELLCOME_BOOTCAMP_REWARDS_MEDAL, RES_ICONS.MAPS_ICONS_BOOTCAMP_REWARDS_BCACHIEVEMENT_BIG_176X102, [
                       BOOTCAMP.TOOLTIP_PROGRESSION_LABEL_MEDAL,
                       BOOTCAMP.TOOLTIP_PROGRESSION_DESCRIPTION_MEDAL,
                       RES_ICONS.MAPS_ICONS_BOOTCAMP_REWARDS_TOOLTIPS_BCACHIEVEMENT, 50])]})
        return

    def _onDisconnected(self):
        self.destroy()
        return

    def _onFinish(self):
        self.as_loadedS()
        return

    def onHighlightShow(self):
        self.soundManager.playSound(BOOTCAMP_SOUND.NEW_UI_ELEMENT_SOUND)
        return

    def _isCurrentlyHighlighting(self, highlightType):
        return self._highlightingMask & 1 << highlightType != 0

    def _setHighlighting(self, highlightType, doHighlight):
        eventId = VIEW_ALIAS.BOOTCAMP_ADD_HIGHLIGHT if doHighlight else VIEW_ALIAS.BOOTCAMP_REMOVE_HIGHLIGHT
        if highlightType in [INTRO_HIGHLIGHT_TYPE.START_BUTTON, INTRO_HIGHLIGHT_TYPE.WELCOME_START_BUTTON]:
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(eventId), ctx=BOOTCAMP_UI_COMPONENTS.START_BATTLE_BUTTON if highlightType == INTRO_HIGHLIGHT_TYPE.START_BUTTON else BOOTCAMP_UI_COMPONENTS.WELCOME_START_BATTLE_BUTTON), EVENT_BUS_SCOPE.BATTLE)
        elif highlightType == INTRO_HIGHLIGHT_TYPE.ARROWS:
            for highlightName in (b'LoadingRightButton', b'LoadingLeftButton'):
                g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(eventId), ctx=highlightName), EVENT_BUS_SCOPE.BATTLE)

        else:
            LOG_ERROR_BOOTCAMP((b'Unknown highlight type - {0}').format(highlightType))
        if doHighlight:
            self._highlightingMask |= 1 << highlightType
        else:
            self._highlightingMask &= ~(1 << highlightType)
        return

    def _shouldHighlight(self, highlightType):
        if self._autoStart:
            return False
        if highlightType == INTRO_HIGHLIGHT_TYPE.START_BUTTON:
            return True
        if highlightType == INTRO_HIGHLIGHT_TYPE.ARROWS:
            return len(self._tutorialPages) > 1
        LOG_ERROR_BOOTCAMP((b'Unknown highlight type - {0}').format(highlightType))
        return False

    def _onWindowAccessibilityChanged(self, isAccessible):
        if self._isWindowAccessible == isAccessible:
            return
        self._isWindowAccessible = isAccessible
        if isAccessible and self._delayedVideoStart:
            self._start()
            self._delayedVideoStart = False
        else:
            self._applyWindowAccessibility()
        return

    def _applyWindowAccessibility(self):
        if self._isWindowAccessible:
            self._resumePlayback()
        else:
            self._pausePlayback()
        return

    def _pausePlayback(self):
        self.as_pausePlaybackS()
        if self._backgroundMusicPauseEvent:
            WWISE.WW_eventGlobal(self._backgroundMusicPauseEvent)
        return

    def _resumePlayback(self):
        self.as_resumePlaybackS()
        if self._backgroundMusicResumeEvent:
            WWISE.WW_eventGlobal(self._backgroundMusicResumeEvent)
        return

    def _getReward(self, label, icon, specialArgs):
        specialArgs[3:3] = [
         None, None]
        return {b'label': label, 
           b'icon': icon, 
           b'isSpecial': True, 
           b'specialAlias': (TOOLTIPS_CONSTANTS.BOOTCAMP_REWARD_PROGRESS), 
           b'specialArgs': specialArgs}
