from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.sub_views.simple_text_view_model import SimpleTextViewModel

class IconViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(IconViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def iconLabel(self):
        return self._getViewModel(0)

    @staticmethod
    def getIconLabelType():
        return SimpleTextViewModel

    def getPath(self):
        return self._getResource(1)

    def setPath(self, value):
        self._setResource(1, value)
        return

    def _initialize(self):
        super(IconViewModel, self)._initialize()
        self._addViewModelProperty(b'iconLabel', SimpleTextViewModel())
        self._addResourceProperty(b'path', R.invalid())
        return
