from frameworks.wulf import Map, ViewModel

class VehicleMenuModel(ViewModel):
    __slots__ = (b'onNavigate',)
    DISABLED = b'disabled'
    ENABLED = b'enabled'
    WARNING = b'warning'
    CRITICAL = b'critical'
    UNAVAILABLE = b'unavailable'
    PRO_BOOST_TOOLTIP_LOCKED = b'locked'
    PRO_BOOST_TOOLTIP_ACTIVE = b'active'
    PRO_BOOST_TOOLTIP_LOCKED_ACTIVE = b'lockedActive'
    PRO_BOOST_TOOLTIP_INCOMPATIBLE_VEHICLE = b'incompatibleVehicle'
    PRO_BOOST_TOOLTIP_INCOMPATIBLE_MODE = b'incompatibleMode'
    BATTLE_NEEDED = b'battleNeeded'
    CREW_MEMBERS_RETIRED = b'crewMembersRetired'

    def __init__(self, properties=1, commands=1):
        super(VehicleMenuModel, self).__init__(properties=properties, commands=commands)
        return

    def getMenuEntries(self):
        return self._getMap(0)

    def setMenuEntries(self, value):
        self._setMap(0, value)
        return

    @staticmethod
    def getMenuEntriesType():
        return (int, unicode)

    def _initialize(self):
        super(VehicleMenuModel, self)._initialize()
        self._addMapProperty(b'menuEntries', Map(int, unicode))
        self.onNavigate = self._addCommand(b'onNavigate')
        return
