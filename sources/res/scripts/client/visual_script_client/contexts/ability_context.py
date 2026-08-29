from visual_script_client.contexts.vehicle_context import VehicleContextClient
from visual_script.context import vse_event_out, vse_set_property, vse_get_property
from visual_script.misc import ASPECT
from visual_script.slot_types import SLOT_TYPE
from constants import EQUIPMENT_STAGES

class AbilityContextClient(VehicleContextClient):

    def __init__(self, vehicle, equipmentName=None):
        super(AbilityContextClient, self).__init__(vehicle)
        self.canActivate = True
        self.errorKey = None
        self.equipmentName = equipmentName or b''
        return

    @vse_get_property(SLOT_TYPE.STR, display_name=b'equipmentName', description=b'', aspects=[
     ASPECT.CLIENT])
    def getEquipmentName(self):
        return self.equipmentName

    @vse_get_property(SLOT_TYPE.STR, display_name=b'abilityStage', description=b'', aspects=[
     ASPECT.CLIENT])
    def getAbilityStage(self):
        return EQUIPMENT_STAGES.toString(self._vehicle.dynamicComponents[self.equipmentName].equipmentStatePublic[b'stage'])

    @vse_set_property(SLOT_TYPE.BOOL, display_name=b'Set CanActivate', description=b'', aspects=[
     ASPECT.CLIENT])
    def setCanActivate(self, canActivate):
        self.canActivate = canActivate
        if canActivate:
            self.errorKey = None
        return

    @vse_set_property(SLOT_TYPE.STR, display_name=b'Set ErrorKey', description=b'KeyName of currently the severest error to be displayed in UI', aspects=[
     ASPECT.CLIENT])
    def setErrorKey(self, errorKey):
        self.errorKey = errorKey if errorKey else None
        return

    @vse_event_out(display_name=b'OnCanActive', description=b'Calls to check whether ability can be activated', aspects=[
     ASPECT.CLIENT])
    def canActive(self):
        return

    @vse_event_out(SLOT_TYPE.INT, display_name=b'OnSetErrorState', description=b'Calls when error state changes', aspects=[
     ASPECT.CLIENT])
    def onSetErrorState(self, errorState):
        return

    @vse_event_out(display_name=b'OnReady', description=b'Calls when ability ready', aspects=[
     ASPECT.CLIENT])
    def ready(self):
        return

    @vse_event_out(display_name=b'OnActivated', description=b'Calls when ability activated', aspects=[
     ASPECT.CLIENT])
    def active(self):
        return

    @vse_event_out(display_name=b'OnCooldown', description=b'Calls when ability becomes cooldown', aspects=[
     ASPECT.CLIENT])
    def cooldown(self):
        return

    @vse_event_out(display_name=b'OnExhausted', description=b'Calls when ability becomes exhausted', aspects=[
     ASPECT.CLIENT])
    def exhausted(self):
        return

    @vse_event_out(display_name=b'OnPrepared', description=b'Calls when ability becomes preparing', aspects=[
     ASPECT.CLIENT])
    def preparing(self):
        return

    @vse_event_out(display_name=b'OnCleanup', description=b'Calls when ability becomes cleanup', aspects=[
     ASPECT.CLIENT])
    def cleanup(self):
        return

    @vse_event_out(display_name=b'OnUnavailable', description=b'Calls when ability unavailable', aspects=[
     ASPECT.CLIENT])
    def unavailable(self):
        return

    @vse_event_out(display_name=b'OnDeploying', description=b'Calls when ability becomes deploying', aspects=[
     ASPECT.CLIENT])
    def deploying(self):
        return

    def notrunning(self):
        return
