from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.quests_card_view_model import QuestsCardViewModel

class QuestsListViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=1, commands=1):
        super(QuestsListViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuests(self):
        return self._getArray(0)

    def setQuests(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getQuestsType():
        return QuestsCardViewModel

    def _initialize(self):
        super(QuestsListViewModel, self)._initialize()
        self._addArrayProperty(b'quests', Array())
        self.onClick = self._addCommand(b'onClick')
        return
