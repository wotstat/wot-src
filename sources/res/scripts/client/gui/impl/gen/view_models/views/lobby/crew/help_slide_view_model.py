from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.help_slide_section_view_model import HelpSlideSectionViewModel

class HelpSlideViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(HelpSlideViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getSections(self):
        return self._getArray(1)

    def setSections(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSectionsType():
        return HelpSlideSectionViewModel

    def _initialize(self):
        super(HelpSlideViewModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addArrayProperty(b'sections', Array())
        return
