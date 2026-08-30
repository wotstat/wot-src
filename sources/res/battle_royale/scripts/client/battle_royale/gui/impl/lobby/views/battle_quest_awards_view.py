from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_quest_awards_model import BattleQuestAwardsModel, BattleStatus
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo
from battle_royale.gui.impl.lobby.tooltips.proxy_currency_tooltip_view import ProxyCurrencyTooltipView
from battle_royale.gui.impl.lobby.views.bonus_packer import getBonusPacker
from battle_royale.gui.sounds_constants import GENERAL_SOUND_SPACE
from frameworks.wulf import ViewSettings, WindowFlags
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData, useBigAwardInjection
from gui.impl.gen import R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses

def awardsFactory(items, ctx=None):
    bonuses = []
    for key, value in items.iteritems():
        bonuses.extend(getNonQuestBonuses(key, value, ctx))

    return bonuses


class BattleQuestAwardsView(ViewImpl):
    _COMMON_SOUND_SPACE = GENERAL_SOUND_SPACE
    __slots__ = (b'__tooltipData', b'_stage')

    def __init__(self, stage):
        settings = ViewSettings(R.views.battle_royale.mono.lobby.battle_quest_awards_view())
        settings.model = BattleQuestAwardsModel()
        self.__tooltipData = {}
        self._stage = stage
        super(BattleQuestAwardsView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(BattleQuestAwardsView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(BattleQuestAwardsView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.battle_royale.mono.lobby.tooltips.proxy_currency_tooltip():
            return ProxyCurrencyTooltipView()
        return super(BattleQuestAwardsView, self).createToolTipContent(event, contentID)

    def getTooltipData(self, event):
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipData.get(tooltipId)

    def updateModel(self):
        level = self._stage.get(b'stage', 0)
        isFinishStage = self._stage.get(b'finishStage', False)
        rewardsData = self._stage.get(b'detailedRewards', ())
        bonuses = awardsFactory(rewardsData)
        with self.viewModel.transaction() as model:
            setEventInfo(model.eventInfo)
            model.setBattleStatus((isFinishStage or BattleStatus).INPROGRESS if 1 else BattleStatus.COMPLETED)
            model.setLevel(level)
            rewards = model.getRewards()
            with useBigAwardInjection():
                packBonusModelAndTooltipData(bonuses, rewards, self.__tooltipData, getBonusPacker())
        return

    def _onLoading(self, *args, **kwargs):
        super(BattleQuestAwardsView, self)._onLoading(args, kwargs)
        self.updateModel()
        self.__addListeners()
        return

    def _finalize(self):
        self.__removeListeners()
        return

    def __addListeners(self):
        with self.viewModel.transaction() as model:
            model.onClose += self.__onClose
            model.onApprove += self.__onApprove
        return

    def __removeListeners(self):
        with self.viewModel.transaction() as model:
            model.onClose -= self.__onClose
            model.onApprove -= self.__onApprove
        return

    def __onClose(self):
        self.destroyWindow()
        return

    def __onApprove(self):
        self.__onClose()
        return


class BattleQuestAwardsViewWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, stage, parent=None):
        super(BattleQuestAwardsViewWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=BattleQuestAwardsView(stage), parent=parent)
        return
