from __future__ import absolute_import
from typing import List, Tuple, Union, Any, Optional, TYPE_CHECKING
from dict2model import models, fields, utils
from dict2model.schemas import Schema, validate
from gui.game_control.wotlda.constants import EQUIPMENT_ARCHETYPE_1, EQUIPMENT_ARCHETYPE_2, EQUIPMENT_ARCHETYPE_3, ExpectedArchetypes, OptDeviceAssistType, LOADOUT_USAGE_PERCENTAGE
from renewable_subscription_common.optional_devices_usage_config import VehicleLoadout, EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP
if TYPE_CHECKING:
    from dict2model.fields import Number
    _OptDevicePreset = Tuple[OptDeviceAssistType, int, List[VehicleLoadout]]
_MODERNIZED_ARCHETYPES_TO_SIMPLE_DEVICES = {b'modernizedAimDrivesAimingStabilizer': b'enhancedAimDrives', 
   b'modernizedTurbochargerRotationMechanism': b'turbocharger', 
   b'modernizedExtraHealthReserveAntifragmentationLining': b'extraHealthReserve', 
   b'modernizedImprovedSightsEnhancedAimDrives': b'improvedSights'}
_SIMPLE_DEVICES_TO_MODERNIZED_ARCHETYPES = {b'enhancedAimDrives': b'modernizedAimDrivesAimingStabilizer', 
   b'turbocharger': b'modernizedTurbochargerRotationMechanism', 
   b'extraHealthReserve': b'modernizedExtraHealthReserveAntifragmentationLining', 
   b'improvedSights': b'modernizedImprovedSightsEnhancedAimDrives'}

class VehicleIdField(fields.Integer):

    def _deserialize(self, incoming, **kwargs):
        if incoming is None:
            return
        else:
            return super(VehicleIdField, self)._deserialize(incoming, **kwargs)


class PercentageField(fields.Float):

    def _deserialize(self, incoming, **kwargs):
        if incoming is None:
            return 0
        else:
            return super(PercentageField, self)._deserialize(incoming, **kwargs)


class NullString(fields.String):

    def _deserialize(self, incoming, **kwargs):
        if incoming is None:
            return b''
        else:
            return self._convert(incoming)


class OneOfArchetypes(validate.OneOf):

    def __call__(self, incoming):
        if incoming:
            super(OneOfArchetypes, self).__call__(incoming)
        return


class EquipmentField(NullString):

    def __init__(self):
        super(EquipmentField, self).__init__(required=True, default=None, deserializedValidators=OneOfArchetypes(ExpectedArchetypes))
        return


class EmptyLoadoutField(fields.UniCapList):

    def _convert(self, incoming, skipValidation, converter, **kwargs):
        if not incoming:
            return {}
        return super(EmptyLoadoutField, self)._convert(incoming, skipValidation, converter, **kwargs)


class PercentRange(validate.Range):

    def __init__(self):
        super(PercentRange, self).__init__(minValue=0.0, maxValue=100.0)
        return

    def __call__(self, incoming):
        if incoming is None:
            return
        else:
            super(PercentRange, self).__call__(incoming)
            return


class BaseOptDeviceLoadoutModel(models.Model):
    __slots__ = (b'linkedVehicleID', b'equipmentArchetype1', b'equipmentArchetype2', b'equipmentArchetype3', b'usagePercentage')

    def __init__(self, vehicle_id, equipment_archetype_id_1, equipment_archetype_id_2, equipment_archetype_id_3, usage_percentage):
        super(BaseOptDeviceLoadoutModel, self).__init__()
        self.linkedVehicleID = vehicle_id
        self.equipmentArchetype1 = equipment_archetype_id_1
        self.equipmentArchetype2 = equipment_archetype_id_2
        self.equipmentArchetype3 = equipment_archetype_id_3
        self.usagePercentage = usage_percentage
        return

    def getDevices(self, getModernized=False):
        devices = [device for device in (self.equipmentArchetype1, self.equipmentArchetype2, self.equipmentArchetype3) if device]
        if not getModernized:
            return [_MODERNIZED_ARCHETYPES_TO_SIMPLE_DEVICES.get(device, device) for device in devices]
        return [self._getDeviceTierArchetype(device) for device in devices]

    def _getDeviceTierArchetype(self, device):
        return _SIMPLE_DEVICES_TO_MODERNIZED_ARCHETYPES.get(device, device)


class BaseOptDeviceLoadoutSchema(Schema[BaseOptDeviceLoadoutModel]):

    def __init__(self):
        super(BaseOptDeviceLoadoutSchema, self).__init__(fields={b'vehicle_id': (VehicleIdField(required=True, default=None)), 
           EQUIPMENT_ARCHETYPE_1: (EquipmentField()), 
           EQUIPMENT_ARCHETYPE_2: (EquipmentField()), 
           EQUIPMENT_ARCHETYPE_3: (EquipmentField()), 
           LOADOUT_USAGE_PERCENTAGE: (PercentageField(required=True, default=0.0, deserializedValidators=PercentRange()))}, modelClass=BaseOptDeviceLoadoutModel)
        return


baseOptDeviceLoadoutSchema = BaseOptDeviceLoadoutSchema()

class VehicleOptDeviceLoadoutsModel(models.Model):
    __slots__ = (b'vehicleId', b'gold', b'legend')

    def __init__(self, vehicleId, gold, legend):
        super(VehicleOptDeviceLoadoutsModel, self).__init__()
        self.vehicleId = vehicleId
        self.gold = gold
        self.legend = legend
        return

    def convertToView(self):
        goldLoadouts = self._parse(self.gold)
        legendLoadouts = self._parse(self.legend)
        return (
         goldLoadouts, legendLoadouts)

    def _parse(self, loadoutModel):
        assistType = OptDeviceAssistType.NODATA
        loadouts = []
        resultVehicleID = self.vehicleId
        for loadout in loadoutModel:
            vehicleLoadouts = []
            equipment1 = EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP.get(loadout.equipmentArchetype1)
            equipment2 = EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP.get(loadout.equipmentArchetype2)
            equipment3 = EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP.get(loadout.equipmentArchetype3)
            if equipment1:
                vehicleLoadouts.append(equipment1)
            if equipment2:
                vehicleLoadouts.append(equipment2)
            if equipment3:
                vehicleLoadouts.append(equipment3)
            if not vehicleLoadouts:
                break
            vehicleLoadout = VehicleLoadout(vehicleLoadouts, loadout.usagePercentage)
            loadouts.append(vehicleLoadout)
            if assistType == OptDeviceAssistType.NODATA:
                linkedVehicleID = loadout.linkedVehicleID
                assistType = self._determineAssistType(self.vehicleId, linkedVehicleID)
                if assistType == OptDeviceAssistType.LINKED:
                    resultVehicleID = linkedVehicleID

        return (
         assistType, resultVehicleID, loadouts)

    def _determineAssistType(self, vehicleId, linkedVehicleID):
        if linkedVehicleID is None:
            return OptDeviceAssistType.COMBINED
        else:
            if linkedVehicleID == vehicleId:
                return OptDeviceAssistType.NORMAL
            if linkedVehicleID != vehicleId:
                return OptDeviceAssistType.LINKED
            return OptDeviceAssistType.NODATA


class VehicleOptDeviceLoadoutsSchema(Schema[VehicleOptDeviceLoadoutsModel]):

    def __init__(self):
        super(VehicleOptDeviceLoadoutsSchema, self).__init__(fields={b'vehicleId': (fields.Integer(required=True)), 
           b'gold': (EmptyLoadoutField(fieldOrSchema=baseOptDeviceLoadoutSchema, required=False)), 
           b'legend': (EmptyLoadoutField(fieldOrSchema=baseOptDeviceLoadoutSchema, required=False))}, modelClass=VehicleOptDeviceLoadoutsModel)
        return


vehicleOptDeviceLoadoutsSchema = VehicleOptDeviceLoadoutsSchema()
