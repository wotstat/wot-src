from frameworks.wulf import ViewModel
from halloween.gui.impl.gen.view_models.views.common.anomalies_matrix.anomalies_matrix_model import AnomaliesMatrixModel

class AnomaliesViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=2, commands=1):
        super(AnomaliesViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def matrix(self):
        return self._getViewModel(0)

    @staticmethod
    def getMatrixType():
        return AnomaliesMatrixModel

    def getSkinId(self):
        return self._getNumber(1)

    def setSkinId(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(AnomaliesViewModel, self)._initialize()
        self._addViewModelProperty(b'matrix', AnomaliesMatrixModel())
        self._addNumberProperty(b'skinId', 0)
        self.onClose = self._addCommand(b'onClose')
        return
