from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.conversion_tooltip_book_model import ConversionTooltipBookModel

class ConversionTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ConversionTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getDescription(self):
        return self._getResource(1)

    def setDescription(self, value):
        self._setResource(1, value)
        return

    def getBooksList(self):
        return self._getArray(2)

    def setBooksList(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBooksListType():
        return ConversionTooltipBookModel

    def _initialize(self):
        super(ConversionTooltipModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addArrayProperty(b'booksList', Array())
        return
