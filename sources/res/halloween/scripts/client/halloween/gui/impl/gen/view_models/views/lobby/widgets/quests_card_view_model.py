from frameworks.wulf import ViewModel
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class QuestsCardViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(QuestsCardViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bonus(self):
        return self._getViewModel(0)

    @staticmethod
    def getBonusType():
        return BonusItemViewModel

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)
        return

    def getConditionName(self):
        return self._getString(2)

    def setConditionName(self, value):
        self._setString(2, value)
        return

    def getName(self):
        return self._getString(3)

    def setName(self, value):
        self._setString(3, value)
        return

    def getDescription(self):
        return self._getString(4)

    def setDescription(self, value):
        self._setString(4, value)
        return

    def getIsCompleted(self):
        return self._getBool(5)

    def setIsCompleted(self, value):
        self._setBool(5, value)
        return

    def getAnimateCompletion(self):
        return self._getBool(6)

    def setAnimateCompletion(self, value):
        self._setBool(6, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(7)

    def setCurrentProgress(self, value):
        self._setNumber(7, value)
        return

    def getMaximumProgress(self):
        return self._getNumber(8)

    def setMaximumProgress(self, value):
        self._setNumber(8, value)
        return

    def getEarned(self):
        return self._getNumber(9)

    def setEarned(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(QuestsCardViewModel, self)._initialize()
        self._addViewModelProperty(b'bonus', BonusItemViewModel())
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'conditionName', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'animateCompletion', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'maximumProgress', 0)
        self._addNumberProperty(b'earned', 0)
        return
