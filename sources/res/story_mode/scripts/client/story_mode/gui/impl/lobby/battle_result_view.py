import typing
from logging import getLogger
import BigWorld, SoundGroups
from constants import DEATH_REASON_ALIVE
from frameworks.wulf import ViewSettings, WindowFlags
from gui.app_loader import app_getter
from gui.battle_results.settings import PLAYER_TEAM_RESULT
from gui.clans.clan_cache import g_clanCache
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.pub import ViewImpl, WindowImpl
from helpers import dependency
from skeletons.gui.battle_results import IBattleResultsService
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.app_loader import IAppLoader
from story_mode.gui.fade_in_out import UseStoryModeFading
from story_mode.gui.impl.gen.view_models.views.lobby.battle_result_view_model import BattleResultViewModel
from story_mode.gui.impl.gen.view_models.views.lobby.progress_level_model import ProgressLevelModel
from story_mode.gui.impl.mixins import DestroyWindowOnDisconnectMixin
from story_mode.gui.shared.event_dispatcher import showCongratulationsWindow
from story_mode.gui.story_mode_gui_constants import POST_BATTLE_MUSIC
from story_mode.skeletons.story_mode_controller import IStoryModeController
from story_mode_common.story_mode_constants import LOGGER_NAME
from story_mode.uilogging.story_mode.consts import LogButtons
from story_mode.uilogging.story_mode.loggers import PostBattleWindowLogger
if typing.TYPE_CHECKING:
    from gui.Scaleform.framework.application import AppEntry
_logger = getLogger(LOGGER_NAME)

class BattleResultView(ViewImpl):
    __slots__ = (b'_uiLogger', b'__arenaUniqueId', b'__isForceOnboarding')
    _MAX_OBJECTIVES_COUNT = 1
    _ICON_OBJECTIVES = b'icon_battle_condition_win'
    _ICON_KILLS = b'icon_battle_condition_kill_vehicles'
    _ICON_DAMAGE = b'icon_battle_condition_damage'
    _ICON_ASSIST = b'icon_battle_condition_assist'
    _ICON_DAMAGE_BLOCKED = b'icon_battle_condition_damage_block'
    _battleResultsService = dependency.descriptor(IBattleResultsService)
    _storyModeCtrl = dependency.descriptor(IStoryModeController)
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _appLoader = dependency.instance(IAppLoader)

    def __init__(self, arenaUniqueId, isForceOnboarding=False):
        super(BattleResultView, self).__init__(settings=ViewSettings(layoutID=R.views.story_mode.lobby.BattleResultView(), model=BattleResultViewModel()))
        self.__arenaUniqueId = arenaUniqueId
        self.__isForceOnboarding = isForceOnboarding
        self._uiLogger = PostBattleWindowLogger()
        return

    def _getEvents(self):
        viewModel = self.getViewModel()
        return (
         (
          viewModel.onQuit, self.__onClose),
         (
          viewModel.onContinue, self.__onClose))

    def _onLoading(self, *args, **kwargs):
        super(BattleResultView, self)._onLoading(*args, **kwargs)
        if self._battleResultsService.areResultsPosted(self.__arenaUniqueId):
            self.__fillViewModel()
        else:
            _logger.error(b'Battle results missing for arena[uniqueId=%s]', self.__arenaUniqueId)
        return

    def _onLoaded(self, *args, **kwargs):
        super(BattleResultView, self)._onLoaded(*args, **kwargs)
        SoundGroups.g_instance.playSound2D(POST_BATTLE_MUSIC)
        viewModel = self.getViewModel()
        self._uiLogger.logOpen(missionId=viewModel.getMissionId() if viewModel else None, win=viewModel.getIsVictory() if viewModel else False)
        return

    def _finalize(self):
        self._uiLogger.logClose()
        super(BattleResultView, self)._finalize()
        return

    def __fillViewModel(self):
        battleResults = self._battleResultsService.getResultsVO(self.__arenaUniqueId)
        with self.getViewModel().transaction() as model:
            rBattleResult = R.strings.sm_lobby.battleResult
            missionId = battleResults[b'missionId']
            finishResult = battleResults[b'finishResult']
            model.setMissionId(missionId)
            model.setIsVictory(finishResult == PLAYER_TEAM_RESULT.WIN)
            model.setTitle(rBattleResult.dyn(PLAYER_TEAM_RESULT.DEFEAT if finishResult == PLAYER_TEAM_RESULT.DRAW else finishResult).title())
            model.setSubTitle(battleResults[b'finishReason'])
            model.setInfoName(backport.text(rBattleResult.missionName.num(missionId)()))
            model.setInfoDescription(backport.text(rBattleResult.battleDuration(), date=battleResults[b'arenaDateTime'], duration=battleResults[b'arenaDuration']))
            model.setVehicleName(backport.text(rBattleResult.vehicleName(), playerName=self._lobbyContext.getPlayerFullName(BigWorld.player().name, clanInfo=g_clanCache.clanInfo), vehicleName=battleResults[b'vehicleName']))
            model.setPlayerStatus(backport.text(rBattleResult.vehicleState.alive() if battleResults[b'vehicle'][b'deathReason'] == DEATH_REASON_ALIVE else rBattleResult.vehicleState.dead()))
            self.__fillProgressLevels(model.missionProgress, model.getProgressLevels(), battleResults)
        return

    def __fillProgressLevels(self, missionProgressModel, progressLevelsModels, battleResults):
        text = R.strings.sm_lobby.battleResult
        missionProgressModel.setValue(self._MAX_OBJECTIVES_COUNT if battleResults[b'finishResult'] == PLAYER_TEAM_RESULT.WIN else 0)
        missionProgressModel.setIcon(self._ICON_OBJECTIVES)
        missionProgressModel.setName(text.operationsCompleted())
        missionProgressModel.setTotal(self._MAX_OBJECTIVES_COUNT)
        with progressLevelsModels.transaction() as model:
            vehicle = battleResults[b'vehicle']
            model.addViewModel(self.__createProgressModel(vehicle[b'kills'], self._ICON_KILLS, text.kills()))
            model.addViewModel(self.__createProgressModel(vehicle[b'damageDealt'], self._ICON_DAMAGE, text.damageDealt()))
            model.addViewModel(self.__createProgressModel(vehicle[b'damageAssisted'], self._ICON_ASSIST, text.damageAssisted()))
            model.addViewModel(self.__createProgressModel(vehicle[b'damageBlockedByArmor'], self._ICON_DAMAGE_BLOCKED, text.damageBlockedByArmor()))
        return

    def __createProgressModel(self, value, icon, name):
        progress = ProgressLevelModel()
        progress.setValue(value)
        progress.setIcon(icon)
        progress.setName(name)
        return progress

    def __onClose(self):
        self._uiLogger.logClick(LogButtons.CONTINUE)
        if self._storyModeCtrl.needToShowAward:
            if self.__isForceOnboarding:
                showCongratulationsWindow(onClose=self._goToHangarAnimated)
            else:
                showCongratulationsWindow(isCloseVisible=True)
        elif self.__isForceOnboarding:
            self._goToHangarAnimated()
        self.destroyWindow()
        return

    @UseStoryModeFading(hide=False)
    def _goToHangarAnimated(self):
        self._appLoader.destroyBattle()
        self._storyModeCtrl.goToHangar()
        return


class BattleResultWindow(DestroyWindowOnDisconnectMixin, WindowImpl):
    __slots__ = (b'__isForceOnboarding',)

    def __init__(self, arenaUniqueId, isForceOnboarding=False):
        super(BattleResultWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=BattleResultView(arenaUniqueId, isForceOnboarding))
        self.__isForceOnboarding = isForceOnboarding
        return

    @app_getter
    def app(self):
        return

    def _onContentReady(self):
        super(BattleResultWindow, self)._onContentReady()
        if self.__isForceOnboarding:
            self.app.attachCursor()
        return
