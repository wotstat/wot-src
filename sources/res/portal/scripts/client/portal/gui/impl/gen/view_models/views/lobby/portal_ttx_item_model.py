from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.params_ttx_model import ParamsTtxModel

class PortalTtxItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PortalTtxItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getParams(self):
        return self._getArray(2)

    def setParams(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getParamsType():
        return ParamsTtxModel

    def _initialize(self):
        super(PortalTtxItemModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addArrayProperty(b'params', Array())
        return
