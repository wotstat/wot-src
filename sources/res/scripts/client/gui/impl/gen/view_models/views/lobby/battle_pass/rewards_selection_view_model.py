from gui.impl.gen.view_models.views.lobby.common.selectable_reward_base_model import SelectableRewardBaseModel

class RewardsSelectionViewModel(SelectableRewardBaseModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RewardsSelectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getChapterID(self):
        return self._getNumber(2)

    def setChapterID(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(RewardsSelectionViewModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'chapterID', 0)
        return
