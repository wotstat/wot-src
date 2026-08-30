from gui.impl.gen.view_models.views.lobby.common.selectable_reward_base_model import SelectableRewardBaseModel

class RewardsSelectionViewModel(SelectableRewardBaseModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
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

    def getIsExtra(self):
        return self._getBool(3)

    def setIsExtra(self, value):
        self._setBool(3, value)
        return

    def getIsHoliday(self):
        return self._getBool(4)

    def setIsHoliday(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(RewardsSelectionViewModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'chapterID', 0)
        self._addBoolProperty(b'isExtra', False)
        self._addBoolProperty(b'isHoliday', False)
        return
