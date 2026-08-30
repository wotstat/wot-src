import nations
from gui.shared.gui_items.processors.vehicle import SetEnhancementProcessor, DismountEnhancementProcessor
from gui.shared.items_parameters import params
from helpers import dependency
from items import vehicles
from skeletons.gui.shared import IItemsCache
from web.web_client_api import w2c, w2capi, Field, W2CSchema
from web.web_client_api.shop import ItemsWebApiMixin

class _VehicleInfoSchema(W2CSchema):
    vehicle_id = Field(type=(int, long))


class _VehicleEnhancementEquipSchema(W2CSchema):
    vehicle_int_cd = Field(required=True, type=int)
    slot = Field(required=True, type=int)
    enhancement_id = Field(required=True, type=int)


class _VehicleEnhancementDismountSchema(W2CSchema):
    vehicle_int_cd = Field(required=True, type=int)
    slot = Field(required=True, type=int)


@w2capi(name=b'vehicles', key=b'action')
class VehiclesWebApi(W2CSchema, ItemsWebApiMixin):
    itemsCache = dependency.descriptor(IItemsCache)

    @w2c(_VehicleInfoSchema, b'vehicle_info')
    def vehicleInfo(self, cmd):
        try:
            vehicle = vehicles.getVehicleType(cmd.vehicle_id)
        except Exception:
            res = {b'error': b'vehicle_id is invalid.'}
        else:
            res = {b'vehicle': {b'vehicle_id': (vehicle.compactDescr), 
                            b'tag': (vehicle.name), 
                            b'name': (vehicle.userString), 
                            b'short_name': (vehicle.shortUserString), 
                            b'nation': (nations.NAMES[vehicle.id[0]]), 
                            b'type': (vehicles.getVehicleClassFromVehicleType(vehicle)), 
                            b'tier': (vehicle.level), 
                            b'is_premium': (bool(b'premium' in vehicle.tags))}}

        return res

    @w2c(_VehicleEnhancementEquipSchema, b'vehicle_enhancement_equip')
    def setVehicleEnhancement(self, cmd):
        success, error = False, b''
        vehicle = self.itemsCache.items.getItemByCD(cmd.vehicle_int_cd)
        if vehicle:
            processor = SetEnhancementProcessor(cmd.slot, cmd.enhancement_id, vehicle)
            response = yield processor.request()
            if response:
                success, error = response.success, response.userMsg
            else:
                error = b'Undefined server error'
        else:
            error = b'Vehicle not found'
        yield {b'success': success, 
           b'error': error}
        return

    @w2c(_VehicleEnhancementDismountSchema, b'vehicle_enhancement_dismount')
    def dismountVehicleEnhancement(self, cmd):
        success, error, serverResponse = False, b'', {}
        vehicle = self.itemsCache.items.getItemByCD(cmd.vehicle_int_cd)
        if vehicle:
            processor = DismountEnhancementProcessor(cmd.slot, vehicle)
            response = yield processor.request()
            if response:
                success, error = response.success, response.userMsg
                if response.auxData:
                    dismountResult, enhancementID = response.auxData
                    serverResponse = {b'dismount_result': dismountResult, 
                       b'enhancement_id': enhancementID}
            else:
                error = b'Undefined server error'
        else:
            error = b'Vehicle not found'
        yield {b'success': success, 
           b'error': error, 
           b'response': serverResponse}
        return

    @w2c(_VehicleInfoSchema, b'vehicle_params')
    def vehicleParams(self, cmd):
        if not vehicles.g_list.isVehicleExistingByCD(cmd.vehicle_id):
            res = {b'error': b'vehicle_id is invalid.'}
        else:
            stockVehicle = self.itemsCache.items.getStockVehicle(cmd.vehicle_id)
            vehicle = self.itemsCache.items.getItemByCD(cmd.vehicle_id)
            vehicleParams = params.VehicleParams(stockVehicle)
            res = {b'vehicle': {b'vehicle_id': (vehicle.compactDescr), 
                            b'type_user_name': (vehicle.typeUserName), 
                            b'user_name': (vehicle.userName), 
                            b'nation': (vehicle.nationName), 
                            b'type': (vehicle.type), 
                            b'level': (vehicle.level), 
                            b'is_premium': (vehicle.isPremium), 
                            b'health': (vehicleParams.maxHealth), 
                            b'hull_armor': (vehicleParams.hullArmor), 
                            b'turret_armor': (vehicleParams.turretArmor), 
                            b'avg_damage': (self.__getAvgDamageShells(vehicle.descriptor)), 
                            b'piercing_power': (self.__getPiercingPowerShells(vehicle.descriptor)), 
                            b'reload_time': (vehicleParams.reloadTime), 
                            b'clip_fire_rate': (vehicleParams.clipFireRate)}}
        return res

    @staticmethod
    def __getAvgDamageShells(vehDescr):
        result = []
        for gunShot in vehDescr.gun.shots:
            result.append(gunShot.shell.damage[0])

        return tuple(result)

    @staticmethod
    def __getPiercingPowerShells(vehDescr):
        result = []
        for gunShot in vehDescr.gun.shots:
            result.append(gunShot.piercingPower.x)

        return tuple(result)
