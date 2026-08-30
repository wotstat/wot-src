from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.tooltips.armory_yard_tooltip_chapter_model import ArmoryYardTooltipChapterModel

class EntryPointActiveTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(EntryPointActiveTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuestsInProgress(self):
        return self._getNumber(0)

    def setQuestsInProgress(self, value):
        self._setNumber(0, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(1)

    def setEndTimestamp(self, value):
        self._setNumber(1, value)
        return

    def getChapters(self):
        return self._getArray(2)

    def setChapters(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getChaptersType():
        return ArmoryYardTooltipChapterModel

    def getReceivedTokens(self):
        return self._getNumber(3)

    def setReceivedTokens(self, value):
        self._setNumber(3, value)
        return

    def getTotalTokens(self):
        return self._getNumber(4)

    def setTotalTokens(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(EntryPointActiveTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'questsInProgress', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addArrayProperty(b'chapters', Array())
        self._addNumberProperty(b'receivedTokens', 0)
        self._addNumberProperty(b'totalTokens', 0)
        return
