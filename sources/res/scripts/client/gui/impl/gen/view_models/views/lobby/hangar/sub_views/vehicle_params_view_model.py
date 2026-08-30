from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_group_view_model import VehicleParamGroupViewModel

class VehicleParamsViewModel(ViewModel):
    __slots__ = (b'onGroupClick',)

    def __init__(self, properties=1, commands=1):
        super(VehicleParamsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getGroups(self):
        return self._getArray(0)

    def setGroups(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getGroupsType():
        return VehicleParamGroupViewModel

    def _initialize(self):
        super(VehicleParamsViewModel, self)._initialize()
        self._addArrayProperty(b'groups', Array())
        self.onGroupClick = self._addCommand(b'onGroupClick')
        return
