from frameworks.wulf import ViewModel
from open_bundle.gui.impl.gen.view_models.views.lobby.coordinate_model import CoordinateModel

class CoordinatesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CoordinatesModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def start(self):
        return self._getViewModel(0)

    @staticmethod
    def getStartType():
        return CoordinateModel

    @property
    def end(self):
        return self._getViewModel(1)

    @staticmethod
    def getEndType():
        return CoordinateModel

    def _initialize(self):
        super(CoordinatesModel, self)._initialize()
        self._addViewModelProperty(b'start', CoordinateModel())
        self._addViewModelProperty(b'end', CoordinateModel())
        return
