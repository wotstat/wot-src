from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.bootcamp.bootcamp_reward_item_model import BootcampRewardItemModel

class BootcampLessonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(BootcampLessonModel, self).__init__(properties=properties, commands=commands)
        return

    def getLessonNumber(self):
        return self._getNumber(0)

    def setLessonNumber(self, value):
        self._setNumber(0, value)
        return

    def getCompleted(self):
        return self._getBool(1)

    def setCompleted(self, value):
        self._setBool(1, value)
        return

    def getCurrent(self):
        return self._getBool(2)

    def setCurrent(self, value):
        self._setBool(2, value)
        return

    def getTooltipId(self):
        return self._getNumber(3)

    def setTooltipId(self, value):
        self._setNumber(3, value)
        return

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRewardsType():
        return BootcampRewardItemModel

    def _initialize(self):
        super(BootcampLessonModel, self)._initialize()
        self._addNumberProperty(b'lessonNumber', 0)
        self._addBoolProperty(b'completed', False)
        self._addBoolProperty(b'current', False)
        self._addNumberProperty(b'tooltipId', 0)
        self._addArrayProperty(b'rewards', Array())
        return
