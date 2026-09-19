from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class AwardCongratsViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(AwardCongratsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getIsCommunityVoted(self):
        return self._getBool(1)

    def setIsCommunityVoted(self, value):
        self._setBool(1, value)
        return

    def getBonuses(self):
        return self._getArray(2)

    def setBonuses(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusItemViewModel

    def _initialize(self):
        super(AwardCongratsViewModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addBoolProperty(b'isCommunityVoted', False)
        self._addArrayProperty(b'bonuses', Array())
        self.onClose = self._addCommand(b'onClose')
        return
