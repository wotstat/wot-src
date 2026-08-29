from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.popovers.filter_control_view_model import FilterControlViewModel

class BattleMattersFilterPopoverViewModel(ViewModel):
    __slots__ = (b'onToggleFilter',)
    ARG_CONTROL_TYPE = b'name'
    ARG_CONTROL_NATION = b'nation'

    def __init__(self, properties=2, commands=1):
        super(BattleMattersFilterPopoverViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTypes(self):
        return self._getArray(0)

    def setTypes(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getTypesType():
        return FilterControlViewModel

    def getNations(self):
        return self._getArray(1)

    def setNations(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getNationsType():
        return FilterControlViewModel

    def _initialize(self):
        super(BattleMattersFilterPopoverViewModel, self)._initialize()
        self._addArrayProperty(b'types', Array())
        self._addArrayProperty(b'nations', Array())
        self.onToggleFilter = self._addCommand(b'onToggleFilter')
        return
