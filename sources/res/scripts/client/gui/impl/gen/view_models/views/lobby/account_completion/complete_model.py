from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_overlay_view_model import BaseOverlayViewModel

class CompleteModel(BaseOverlayViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=2):
        super(CompleteModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(2)

    def setTitle(self, value):
        self._setResource(2, value)
        return

    def getSubTitle(self):
        return self._getResource(3)

    def setSubTitle(self, value):
        self._setResource(3, value)
        return

    def _initialize(self):
        super(CompleteModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'subTitle', R.invalid())
        return
