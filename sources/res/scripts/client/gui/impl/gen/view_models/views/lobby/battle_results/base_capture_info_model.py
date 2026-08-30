from frameworks.wulf import ViewModel

class BaseCaptureInfoModel(ViewModel):
    __slots__ = ()
    CAPTURE_POINTS = b'capturePoints'
    DROPPED_CAPTURE_POINTS = b'droppedCapturePoints'

    def __init__(self, properties=2, commands=0):
        super(BaseCaptureInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getCapturePoints(self):
        return self._getNumber(0)

    def setCapturePoints(self, value):
        self._setNumber(0, value)
        return

    def getDroppedCapturePoints(self):
        return self._getNumber(1)

    def setDroppedCapturePoints(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(BaseCaptureInfoModel, self)._initialize()
        self._addNumberProperty(b'capturePoints', 0)
        self._addNumberProperty(b'droppedCapturePoints', 0)
        return
