from gui.prb_control.entities.base.squad.components import SquadRestrictionsProvider

class SquadRestrictionsMixin(object):

    def __init__(self):
        self.__squadRestrictionsProvider = self._createSquadRestrictionsProvider()
        return

    def initRestrictedRoleDataProvider(self, unit):
        self.__squadRestrictionsProvider.init(unit)
        return

    def finiRestrictedRoleDataProvider(self):
        self.__squadRestrictionsProvider.fini()
        return

    def isSquadRestrictionValid(self):
        return self.__squadRestrictionsProvider.isValid()

    def isVehicleSuitableForSquad(self, vehicle):
        hasSlot, _ = self.__squadRestrictionsProvider.hasSlotForVehicle(vehicle, ignoreOwnVehiclesInUnit=True)
        return hasSlot

    def hasSlotForVehicle(self, vehicle):
        return self.__squadRestrictionsProvider.hasSlotForVehicle(vehicle)

    @property
    def squadRestrictions(self):
        raise NotImplementedError
        return

    @classmethod
    def _createSquadRestrictionsProvider(cls):
        return SquadRestrictionsProvider()
