from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.early_access.tooltips.early_access_tooltip_chapter_model import EarlyAccessTooltipChapterModel

class EarlyAccessEntryPointTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(EarlyAccessEntryPointTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentTimestamp(self):
        return self._getNumber(0)

    def setCurrentTimestamp(self, value):
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
        return EarlyAccessTooltipChapterModel

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

    def getIsPostprogression(self):
        return self._getBool(5)

    def setIsPostprogression(self, value):
        self._setBool(5, value)
        return

    def getIsPaused(self):
        return self._getBool(6)

    def setIsPaused(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(EarlyAccessEntryPointTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'currentTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addArrayProperty(b'chapters', Array())
        self._addNumberProperty(b'receivedTokens', 0)
        self._addNumberProperty(b'totalTokens', 0)
        self._addBoolProperty(b'isPostprogression', False)
        self._addBoolProperty(b'isPaused', False)
        return
