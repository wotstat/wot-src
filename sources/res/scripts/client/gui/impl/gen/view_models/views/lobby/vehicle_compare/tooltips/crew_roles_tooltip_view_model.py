from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.tooltips.crew_member_model import CrewMemberModel

class CrewRolesTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CrewRolesTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)
        return

    def getCrew(self):
        return self._getArray(1)

    def setCrew(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getCrewType():
        return CrewMemberModel

    def _initialize(self):
        super(CrewRolesTooltipViewModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addArrayProperty(b'crew', Array())
        return
