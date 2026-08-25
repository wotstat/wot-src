from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from typing import Optional
    from gui.shared.gui_items.dossier import AccountDossier
    from gui.shared.gui_items.vehicle_mechanics.module_mechanic_item import ModuleMechanicItem
    from gui.shared.gui_items.vehicle_mechanics.vehicle_mechanic_item import VehicleMechanicItem
    from gui.veh_post_progression.models.progression import PostProgressionItem
    from items.vehicles import VehicleType
    from post_progression_common import VehicleState
    from gui.shared.gui_items.vehicle_modules import VehicleGun
    from dossiers2.common.DossierDescr import DossierDescr
    from vehicles.mechanics.mechanic_constants import VehicleMechanic

class IGuiItemsFactory(object):

    def clear(self):
        raise NotImplementedError
        return

    def createGuiItemsOfSameType(self, itemTypeIdx, compactDecrs, proxy, *args, **kwargs):
        raise NotImplementedError
        return

    def createGuiItem(self, itemTypeIdx, *args, **kwargs):
        raise NotImplementedError
        return

    def createGuiItemFromCompactDescr(self, compactDescr, *args, **kwargs):
        raise NotImplementedError
        return

    def createShell(self, intCompactDescr, count=0, proxy=None, isBoughtForCredits=False):
        raise NotImplementedError
        return

    def createEquipment(self, intCompactDescr, proxy=None, isBoughtForCredits=False):
        raise NotImplementedError
        return

    def createOptionalDevice(self, intCompactDescr, proxy=None):
        raise NotImplementedError
        return

    def createVehicleGun(self, intCompactDescr, proxy=None, descriptor=None):
        raise NotImplementedError
        return

    def createVehicleChassis(self, intCompactDescr, proxy=None, descriptor=None):
        raise NotImplementedError
        return

    def createVehicleTurret(self, intCompactDescr, proxy=None, descriptor=None):
        raise NotImplementedError
        return

    def createVehicleEngine(self, intCompactDescr, proxy=None, descriptor=None):
        raise NotImplementedError
        return

    def createVehicleRadio(self, intCompactDescr, proxy=None, descriptor=None):
        raise NotImplementedError
        return

    def createVehicleFuelTank(self, intCompactDescr, proxy=None, descriptor=None):
        raise NotImplementedError
        return

    def createVehicle(self, strCompactDescr=None, inventoryID=-1, typeCompDescr=None, proxy=None, extData=None, invData=None):
        raise NotImplementedError
        return

    def createTankman(self, strCompactDescr, inventoryID=-1, vehicle=None, dismissedAt=None, proxy=None, vehicleSlotIdx=-1, bonusSkillsLevels=None):
        raise NotImplementedError
        return

    def createTankmanDossier(self, tmanDescr, tankmanDossierDescr, extDossier, playerDBID=None, currentVehicleItem=None):
        raise NotImplementedError
        return

    def createAccountDossier(self, dossier, playerDBID=None, rated7x7Seasons=None):
        raise NotImplementedError
        return

    def createVehicleDossier(self, dossier, vehTypeCompDescr, playerDBID=None):
        raise NotImplementedError
        return

    def createBadge(self, descriptor, proxy=None, extraData=None, receivedBadges=None):
        raise NotImplementedError
        return

    def createLootBox(self, lootBoxID, lootBoxConfig, count):
        raise NotImplementedError
        return

    def createCustomization(self, intCompactDescr, proxy=None):
        raise NotImplementedError
        return

    def createOutfit(self, strCompactDescr=None, component=None, vehicleCD=b''):
        raise NotImplementedError
        return

    def createVehPostProgression(self, vehIntCD, state, vehType):
        raise NotImplementedError
        return

    def createModuleMechanicItem(self, mechanic, moduleType):
        raise NotImplementedError
        return

    def createVehicleMechanicItem(self, mechanic, vehIntCD):
        raise NotImplementedError
        return
