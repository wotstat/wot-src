from frameworks.wulf import ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.parallax_model import ParallaxModel

class ParallaxViewModel(ViewModel):
    __slots__ = (b'onSlide',)

    def __init__(self, properties=2, commands=1):
        super(ParallaxViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def parallax(self):
        return self._getViewModel(0)

    @staticmethod
    def getParallaxType():
        return ParallaxModel

    def getIsParallaxEnabled(self):
        return self._getBool(1)

    def setIsParallaxEnabled(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(ParallaxViewModel, self)._initialize()
        self._addViewModelProperty(b'parallax', ParallaxModel())
        self._addBoolProperty(b'isParallaxEnabled', False)
        self.onSlide = self._addCommand(b'onSlide')
        return
