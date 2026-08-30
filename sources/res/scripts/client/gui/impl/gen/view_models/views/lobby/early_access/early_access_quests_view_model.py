from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.early_access.early_access_chapter_model import EarlyAccessChapterModel
from gui.impl.gen.view_models.views.lobby.early_access.early_access_quest_model import EarlyAccessQuestModel

class QuestsViewTooltipStates(Enum):
    QUEST = b'quest'
    CHAPTER = b'chapter'


class EarlyAccessQuestsViewModel(ViewModel):
    __slots__ = (b'onClose', b'goToVehicle', b'goToInfo')

    def __init__(self, properties=5, commands=3):
        super(EarlyAccessQuestsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)
        return

    def getChapters(self):
        return self._getArray(1)

    def setChapters(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getChaptersType():
        return EarlyAccessChapterModel

    def getQuests(self):
        return self._getArray(2)

    def setQuests(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getQuestsType():
        return EarlyAccessQuestModel

    def getFromTimestamp(self):
        return self._getNumber(3)

    def setFromTimestamp(self, value):
        self._setNumber(3, value)
        return

    def getToTimestamp(self):
        return self._getNumber(4)

    def setToTimestamp(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(EarlyAccessQuestsViewModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        self._addArrayProperty(b'chapters', Array())
        self._addArrayProperty(b'quests', Array())
        self._addNumberProperty(b'fromTimestamp', 0)
        self._addNumberProperty(b'toTimestamp', 0)
        self.onClose = self._addCommand(b'onClose')
        self.goToVehicle = self._addCommand(b'goToVehicle')
        self.goToInfo = self._addCommand(b'goToInfo')
        return
