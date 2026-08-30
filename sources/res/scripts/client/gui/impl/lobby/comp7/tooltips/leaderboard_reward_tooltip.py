from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.leaderboard_reward_tooltip_model import LeaderboardRewardTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel

class LeaderboardRewardTooltip(ViewImpl):
    __slots__ = (b'__place',)

    def __init__(self, place):
        self.__place = place
        settings = ViewSettings(R.views.lobby.comp7.tooltips.LeaderboardRewardTooltip())
        settings.model = LeaderboardRewardTooltipModel()
        super(LeaderboardRewardTooltip, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(LeaderboardRewardTooltip, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(LeaderboardRewardTooltip, self)._initialize(*args, **kwargs)
        self.__fillModel()
        return

    @replaceNoneKwargsModel
    def __fillModel(self, model=None):
        model.setPlace(self.__place)
        return
