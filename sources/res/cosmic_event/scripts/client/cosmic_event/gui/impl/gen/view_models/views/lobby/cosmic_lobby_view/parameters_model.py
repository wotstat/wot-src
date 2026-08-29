from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from cosmic_event.gui.impl.gen.view_models.views.lobby.tooltips.specification_tooltip_model import SpecificationTooltipModel

class ParameterEnum(Enum):
    STABILITY = b'stability'
    ACCELERATION = b'acceleration'
    MAX_SPEED = b'maxSpeed'
    FIRE_RATE = b'fireRate'
    SHOT_POWER = b'shotPower'


class ParametersModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ParametersModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)
        return

    def getParameterName(self):
        return ParameterEnum(self._getString(1))

    def setParameterName(self, value):
        self._setString(1, value.value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getParameterDesc(self):
        return self._getString(3)

    def setParameterDesc(self, value):
        self._setString(3, value)
        return

    def getTooltipArgs(self):
        return self._getArray(4)

    def setTooltipArgs(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getTooltipArgsType():
        return SpecificationTooltipModel

    def _initialize(self):
        super(ParametersModel, self)._initialize()
        self._addNumberProperty(b'value', 0)
        self._addStringProperty(b'parameterName')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'parameterDesc', b'')
        self._addArrayProperty(b'tooltipArgs', Array())
        return
