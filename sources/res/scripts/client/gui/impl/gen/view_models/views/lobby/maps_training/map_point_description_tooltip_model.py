from frameworks.wulf import ViewModel

class MapPointDescriptionTooltipModel(ViewModel):
    __slots__ = ()
    ARG_POINT_NAME = b'pointName'

    def __init__(self, properties=1, commands=0):
        super(MapPointDescriptionTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getPointName(self):
        return self._getString(0)

    def setPointName(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(MapPointDescriptionTooltipModel, self)._initialize()
        self._addStringProperty(b'pointName', b'')
        return
