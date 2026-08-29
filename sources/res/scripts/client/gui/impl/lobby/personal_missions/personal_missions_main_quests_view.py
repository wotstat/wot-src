import logging, typing
from frameworks.wulf import ViewFlags, ViewSettings
from gui.Scaleform.framework.managers.optimization_manager import ExternalFullscreenGraphicsOptimizationComponent
from gui.impl.gen import R
from gui.impl.lobby.personal_missions.tooltips.personal_missions_quests_type_tooltip import PersonalMissionsQuestsTypeTooltip
from gui.impl.lobby.personal_missions.tooltips.quest_card_tooltip import QuestCardTooltip
from gui.impl.lobby.personal_missions.tooltips.vehicle_tabs_tooltip import VehicleTabsTooltip
from gui.impl.lobby.personal_missions.tooltips.personal_missions_quest_info_tooltip import PersonalMissionsQuestInfoTooltip
from frameworks.wulf.view.submodel_presenter import PageSubModelPresenter
from gui.impl.gen.view_models.views.lobby.personal_missions.personal_missions_main_quests_view_model import PersonalMissionsMainQuestsViewModel, PageViewIdEnum
from gui.impl.lobby.personal_missions.pages.personal_missions_quest_page import PersonalMissionQuestPage
from gui.impl.lobby.personal_missions.pages.personal_missions_quests_page import PersonalMissionQuestsPage
from gui.impl.pub import ViewImpl
from gui.server_events.events_dispatcher import showPersonalMissionsOperationsMap
from helpers import dependency
from personal_missions import PM_BRANCH
from skeletons.gui.game_control import IPersonalMissionsController
from gui.server_events.pm3_constants import PERSONAL_MISSIONS_3_SOUND_SPACE, SOUNDS
from gui.sounds.voice_over_phrase_player import VoiceOverHandler
_logger = logging.getLogger(__name__)

class PersonalMissionsMainQuestsView(ViewImpl):
    __slots__ = (b'__pages', b'__tabId', b'__operationId', b'__questId', b'__graphicOptimization', b'__voiceHandler', b'__chainId')
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_3_SOUND_SPACE
    __personalMissionsController = dependency.descriptor(IPersonalMissionsController)
    __TAB_SOUND_SETTINGS = {(PageViewIdEnum.QUESTS): (
                               SOUNDS.STATE_PLACE_OPERATION_SCREEN, SOUNDS.PROJECTOR), 
       (PageViewIdEnum.QUEST): (
                              SOUNDS.STATE_PLACE_TASK_SCREEN, SOUNDS.PROJECTOR_SLIDE_IN)}

    def __init__(self, layoutID, tabId=PageViewIdEnum.QUESTS, operationId=8, questId=None):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = PersonalMissionsMainQuestsViewModel()
        super(PersonalMissionsMainQuestsView, self).__init__(settings)
        self.__pages = {}
        self.__tabId = tabId
        self.__operationId = operationId
        self.__questId = questId
        self.__graphicOptimization = ExternalFullscreenGraphicsOptimizationComponent()
        self.__voiceHandler = VoiceOverHandler()
        return

    @property
    def viewModel(self):
        return super(PersonalMissionsMainQuestsView, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.personal_missions.tooltips.PersonalMissionsQuestsTypeTooltip():
            inputType = event.getArgument(b'type')
            return PersonalMissionsQuestsTypeTooltip(inputType)
        else:
            if contentID == R.views.lobby.personal_missions.tooltips.VehicleTabsTooltip():
                maxVehicleLevel = event.getArgument(b'maxVehicleLevel')
                minVehicleLevel = event.getArgument(b'minVehicleLevel')
                branchName = event.getArgument(b'branchName')
                return VehicleTabsTooltip(maxVehicleLevel, minVehicleLevel, branchName)
            if contentID == R.views.lobby.personal_missions.tooltips.QuestCardTooltip():
                questId = event.getArgument(b'questId')
                return QuestCardTooltip(questId)
            if contentID == R.views.lobby.personal_missions.tooltips.PersonalMissionsQuestInfoTooltip():
                questId = event.getArgument(b'questId')
                return PersonalMissionsQuestInfoTooltip(questId)
            if self.__currentPage.isLoaded:
                content = self.__currentPage.createToolTipContent(event, contentID)
                if content is not None:
                    return content
            return super(PersonalMissionsMainQuestsView, self).createToolTipContent(event, contentID)

    def switchPage(self, tabId, *args, **kwargs):
        if self.__currentPage.isLoaded:
            self.__currentPage.finalize()
        self.__soundHandler(tabId)
        page = self.__pages[tabId]
        page.initialize(*args, **kwargs)
        self.viewModel.setPageViewId(page.pageId)
        self.__tabId = tabId
        return

    def __soundHandler(self, tabId):
        self.__voiceHandler.createPlayer(screenId=self.__operationId)
        state, sound = self.__TAB_SOUND_SETTINGS.get(tabId)
        self.soundManager.setState(SOUNDS.STATE_SCREEN_GROUP, state)
        self.soundManager.playSound(sound)
        return

    def _finalize(self):
        self.__voiceHandler.destroyPlayer()
        self.__graphicOptimization.fini()
        self.__removeListeners()
        self.__clearPages()
        super(PersonalMissionsMainQuestsView, self)._finalize()
        return

    def _onLoading(self, *args, **kwargs):
        self.__graphicOptimization.init()
        tabId = kwargs.pop(b'tabId', None)
        if tabId is not None:
            if tabId in tuple(PageViewIdEnum):
                self.__tabId = tabId
            else:
                _logger.error(b'Wrong tabId: %s', tabId)
        self.__initPages()
        self.switchPage(tabId=self.__tabId, operationId=self.__operationId, questId=self.__questId, *args, **kwargs)
        self.__addListeners()
        self.__checkPersistentSoundsPlaying()
        return

    def __checkPersistentSoundsPlaying(self):
        if not self.soundManager.isSoundPlaying(SOUNDS.MUSIC) and not self.soundManager.isSoundPlaying(SOUNDS.AMBIENT):
            self.soundManager.playSound(SOUNDS.AMBIENT)
            self.soundManager.playSound(SOUNDS.MUSIC)
        return

    @property
    def __currentPage(self):
        return self.__pages[self.__tabId]

    def __addListeners(self):
        self.viewModel.onClose += self.__onClose
        self.viewModel.openQuest += self.__openQuest
        self.viewModel.onBackToOperations += self.__openOperations
        return

    def __removeListeners(self):
        self.viewModel.onClose -= self.__onClose
        self.viewModel.openQuest -= self.__openQuest
        self.viewModel.onBackToOperations -= self.__openOperations
        return

    def __initPages(self):
        pages = (
         PersonalMissionQuestPage(self.viewModel.quest, self),
         PersonalMissionQuestsPage(self.viewModel.quests, self))
        self.__pages = {p.pageId: p for p in pages}
        return

    def __clearPages(self):
        if self.__currentPage.isLoaded:
            self.__currentPage.finalize()
        self.__pages.clear()
        return

    def __openQuest(self, args):
        self.__questId = int(args.get(b'questId'))
        self.switchPage(tabId=PageViewIdEnum.QUEST, questId=self.__questId)
        return

    def __currentChainId(self):
        quest = self.__personalMissionsController.getQuest(int(self.__questId))
        return quest.getChainID()

    def __openOperations(self):
        self.soundManager.playSound(SOUNDS.PROJECTOR_SLIDE_OUT)
        self.switchPage(tabId=PageViewIdEnum.QUESTS, operationId=self.__operationId, chainId=self.__currentChainId(), backFromQuest=True)
        return

    def __onClose(self):
        showPersonalMissionsOperationsMap(PM_BRANCH.PERSONAL_MISSION_3)
        return
