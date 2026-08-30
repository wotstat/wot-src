from gui.impl.gen.view_models.views.lobby.common.selectable_reward_base_model import SelectableRewardBaseModel

class RewardsSelectionViewModel(SelectableRewardBaseModel):
    __slots__ = (b'onLoadedView',)

    def __init__(self, properties=1, commands=1):
        super(RewardsSelectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(RewardsSelectionViewModel, self)._initialize()
        self.onLoadedView = self._addCommand(b'onLoadedView')
        return
