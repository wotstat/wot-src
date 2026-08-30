import typing
from AccountCommands import RES_SUCCESS
from frameworks.wulf import WindowFlags
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_item_model import SelectableRewardItemModel
from gui.impl.gen.view_models.views.lobby.stronghold.stronghold_selectable_reward_view_model import StrongholdSelectableRewardViewModel
from gui.impl.lobby.common.selectable_reward_base import SelectableRewardBase
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.selectable_reward.common import StrongholdSelectableRewardManager
from gui.server_events.bonuses import getMergedBonusesFromDicts
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import StrongholdEvent
from gui.shared.event_dispatcher import showStrongholdSelectedRewardWindow
if typing.TYPE_CHECKING:
    from typing import Dict
    from gui.server_events.bonuses import SelectableBonus
    from gui.SystemMessages import ResultMsg

class StrongholdSelectableRewardView(SelectableRewardBase):
    __slots__ = (b'__allRewards',)
    _helper = StrongholdSelectableRewardManager

    def __init__(self):
        super(StrongholdSelectableRewardView, self).__init__(R.views.lobby.stronghold.StrongholdSelectableRewardView(), self._helper.getAvailableSelectableBonuses(), StrongholdSelectableRewardViewModel)
        self.__allRewards = {}
        return

    @property
    def viewModel(self):
        return super(StrongholdSelectableRewardView, self).getViewModel()

    def _fillRewards(self, tabName, initial=False):
        rewards = self.viewModel.selectableRewardModel.getRewards()
        with rewards.transaction() as vm:
            vm.clear()
            for rewardName, reward, state in self._prepareRewardsData(tabName):
                newReward = SelectableRewardItemModel()
                newReward.setType(reward[b'type'])
                newReward.setDecorator(reward[b'decorator'])
                newReward.setCount(0 if initial else self._getRewardsInCartCount(rewardName))
                if state != SelectableRewardItemModel.STATE_RECEIVED:
                    newReward.setPackSize(reward[b'packSize'])
                newReward.setStorageCount(reward[b'storageCount'])
                if reward[b'storageCount'] > 0 and reward[b'storageCount'] >= reward[b'maxNumber']:
                    state = SelectableRewardItemModel.STATE_RECEIVED
                newReward.setState(state)
                vm.addViewModel(newReward)

        return

    def _createReward(self, rewards, rewardName, gift, giftID, selectableReward):
        rewards[rewardName] = {b'packSize': (gift[b'count']), b'limit': (gift[b'limit']), 
           b'storageCount': (gift[b'option'].getInventoryCount()), 
           b'maxNumber': (gift[b'option'].custItem.descriptor.maxNumber), 
           b'selectableReward': [
                               (
                                selectableReward, giftID)], 
           b'receivedRewards': 0, 
           b'tooltip': (self._packer.getToolTip(gift[b'option'])), 
           b'decorator': (b'style3D' if gift[b'option'].custItem.is3D else b'style2D'), 
           b'type': (gift[b'option'].getNamePath())}
        return

    def _processReceivedRewards(self, result):
        receivedRewards = result.auxData[RES_SUCCESS]
        self.__allRewards = getMergedBonusesFromDicts([self.__allRewards, receivedRewards])
        if self.__allRewards:
            g_eventBus.handleEvent(StrongholdEvent(StrongholdEvent.STRONGHOLD_REWARD_SELECTED), scope=EVENT_BUS_SCOPE.STRONGHOLD)
            showStrongholdSelectedRewardWindow([
             self.__allRewards], True)
        self.destroyWindow()
        return


class StrongholdSelectableRewardWindow(LobbyNotificationWindow):

    def __init__(self):
        super(StrongholdSelectableRewardWindow, self).__init__(content=StrongholdSelectableRewardView(), wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN)
        return
