from AccountCommands import RES_SUCCESS
from frameworks.wulf import WindowFlags
from gui import SystemMessages
from gui.impl.lobby.common.rewards_sort import getRewardTypesComparator, getRewardsComparator
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.frontline.rewards_selection_view_model import RewardsSelectionViewModel
from gui.impl.lobby.common.selectable_reward_base import SelectableRewardBase
from gui.impl.pub.lobby_window import LobbyWindow
from gui.selectable_reward.common import EpicSelectableRewardManager
from gui.shared.event_dispatcher import showHangar
from gui.sounds.filters import switchHangarOverlaySoundFilter
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from uilogging.epic_battle.constants import EpicBattleLogKeys, EpicBattleLogActions, EpicBattleLogButtons
from uilogging.epic_battle.loggers import EpicBattleTooltipLogger

class RewardsSelectionView(SelectableRewardBase):
    __slots__ = (b'__onRewardsReceivedCallback', b'__onCloseCallback', b'__onLoadedCallback', b'__isViewLoaded', b'__uiEpicBattleLogger', b'__isAutoDestroyWindowsOnReceivedRewards')
    _helper = EpicSelectableRewardManager
    _epicController = dependency.descriptor(IEpicBattleMetaGameController)

    def __init__(self, onRewardsReceivedCallback=None, onCloseCallback=None, onLoadedCallback=None, isAutoDestroyWindowsOnReceivedRewards=True):
        self.__onRewardsReceivedCallback = onRewardsReceivedCallback
        self.__onCloseCallback = onCloseCallback
        self.__onLoadedCallback = onLoadedCallback
        self.__isViewLoaded = False
        self.__isAutoDestroyWindowsOnReceivedRewards = isAutoDestroyWindowsOnReceivedRewards
        self.__uiEpicBattleLogger = EpicBattleTooltipLogger()
        super(RewardsSelectionView, self).__init__(R.views.lobby.frontline.RewardsSelectionView(), self._helper.getAvailableSelectableBonuses(), RewardsSelectionViewModel)
        return

    def _getReceivedRewards(self, rewardName):
        return 0

    @property
    def viewModel(self):
        return super(RewardsSelectionView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(RewardsSelectionView, self)._initialize(*args, **kwargs)
        self._epicController.onUpdated += self._onEpicUpdate
        switchHangarOverlaySoundFilter(on=True)
        self.__uiEpicBattleLogger.initialize(EpicBattleLogKeys.REWARDS_SELECTION_VIEW.value)
        return

    def _onLoading(self, *args, **kwargs):
        super(RewardsSelectionView, self)._onLoading(*args, **kwargs)
        self.viewModel.onLoadedView += self.__onViewLoaded
        return

    def _finalize(self):
        self.__safeCall(self.__onCloseCallback)
        switchHangarOverlaySoundFilter(on=False)
        self._epicController.onUpdated -= self._onEpicUpdate
        self.viewModel.onLoadedView -= self.__onViewLoaded
        self.__uiEpicBattleLogger.reset()
        super(RewardsSelectionView, self)._finalize()
        return

    def _onOkClick(self):
        super(RewardsSelectionView, self)._onOkClick()
        self.__uiEpicBattleLogger.log(EpicBattleLogActions.CLICK.value, EpicBattleLogButtons.REWARDS_SELECTION_CONFIRM.value, EpicBattleLogKeys.REWARDS_SELECTION_VIEW.value)
        self.destroyWindow()
        return

    def _onCloseClick(self):
        super(RewardsSelectionView, self)._onCloseClick()
        self.__uiEpicBattleLogger.log(EpicBattleLogActions.CLICK.value, EpicBattleLogButtons.REWARDS_SELECTION_CLOSE.value, EpicBattleLogKeys.REWARDS_SELECTION_VIEW.value)
        return

    def _onEpicUpdate(self, diff, *args):
        if b'isEnabled' in diff and not diff[b'isEnabled']:
            self.destroyWindow()
            showHangar()
        return

    def _getTypesComparator(self):
        return getRewardTypesComparator()

    def _getItemsComparator(self, tabName):
        return getRewardsComparator(tabName)

    def _processReceivedRewards(self, result):
        if result.success and result.auxData:
            successRewards = result.auxData.get(RES_SUCCESS, {})
            if successRewards:
                rewardsGenerator = ({group: rewards} for group, rewards in successRewards.iteritems())
                self.__safeCall(self.__onRewardsReceivedCallback, rewardsGenerator)
        else:
            SystemMessages.pushI18nMessage(backport.text(R.strings.system_messages.battlePass.rewardChoice.error()), type=SystemMessages.SM_TYPE.Error)
        if self.__isAutoDestroyWindowsOnReceivedRewards:
            self.destroyWindow()
        return

    def __onViewLoaded(self):
        if not self.__isViewLoaded:
            self.__safeCall(self.__onLoadedCallback)
            self.__isViewLoaded = True
        return

    @staticmethod
    def __safeCall(callback, *args, **kwargs):
        if callable(callback):
            callback(*args, **kwargs)
        return


class RewardsSelectionWindow(LobbyWindow):
    __slots__ = ()

    def __init__(self, onRewardsReceivedCallback=None, onCloseCallback=None, onLoadedCallback=None, isAutoDestroyWindowsOnReceivedRewards=True):
        super(RewardsSelectionWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=RewardsSelectionView(onRewardsReceivedCallback, onCloseCallback, onLoadedCallback, isAutoDestroyWindowsOnReceivedRewards))
        return
