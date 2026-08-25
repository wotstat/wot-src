from comp7_light.gui.impl.gen.view_models.views.lobby.battle_quest_awards_model import BattleQuestAwardsModel, BattleStatus
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_packers import getComp7LightBonusPacker
from comp7_light.gui.sounds_constants import GENERAL_SOUND_SPACE
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData
from gui.impl.gen import R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses

class BattleQuestAwardsView(ViewImpl):
    __slots__ = (b'__tooltipData', b'_stage')
    _COMMON_SOUND_SPACE = GENERAL_SOUND_SPACE

    def __init__(self, stage):
        settings = ViewSettings(R.views.comp7_light.mono.lobby.battle_quest_awards_view())
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
        bonuses = self.__awardsFactory(rewardsData)
        with self.viewModel.transaction() as model:
            model.setBattleStatus((isFinishStage or BattleStatus).INPROGRESS if 1 else BattleStatus.COMPLETED)
            model.setLevel(level)
            rewards = model.getRewards()
            packBonusModelAndTooltipData(bonuses, rewards, self.__tooltipData, getComp7LightBonusPacker())
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

    @staticmethod
    def __awardsFactory(items, ctx=None):
        bonuses = []
        for key, value in items.iteritems():
            bonuses.extend(getNonQuestBonuses(key, value, ctx))

        return bonuses


class BattleQuestAwardsViewWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, stage, parent=None):
        super(BattleQuestAwardsViewWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.TOP_WINDOW, content=BattleQuestAwardsView(stage), parent=parent)
        return
