import math
from Math import Vector3
from items.components import component_constants

class HangarConfig(object):
    __slots__ = [
     0, 1, 2, 3, 4, 
     5, 6, 7, 8, 
     9, 10, 
     11, 12, 
     13, 14, 15]

    def __init__(self):
        self.cfg = {}
        self.vStartAngles = Vector3()
        self.vStartPos = Vector3()
        self.emblemsAlphaDamaged = component_constants.ZERO_FLOAT
        self.emblemsAlphaUndamaged = component_constants.ZERO_FLOAT
        self.shadowLightDir = Vector3()
        self.shadowModelName = component_constants.EMPTY_STRING
        self.shadowForwardYOffset = component_constants.ZERO_FLOAT
        self.shadowDeferredYOffset = component_constants.ZERO_FLOAT
        self.shadowDefaultTextureName = component_constants.EMPTY_STRING
        self.shadowEmptyTextureName = component_constants.EMPTY_STRING
        self.vehicleGunPitch = component_constants.ZERO_FLOAT
        self.vehicleTurretYaw = component_constants.ZERO_FLOAT
        self.camMinDistVehicleHullLengthK = component_constants.ZERO_FLOAT
        self.camCapsuleScale = Vector3()
        self.camCapsuleGunScale = Vector3()
        return

    def __iter__(self):
        return iter(self.cfg)

    def __getitem__(self, key):
        return self.cfg[key]

    def __setitem__(self, key, value):
        self.cfg[key] = value
        return

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

        return

    def loadConfig(self, xml, defaultCfg=None):
        if defaultCfg is None:
            defaultCfg = self
        defaultFakeShadowOffsetsCfg = {b'shadow_forward_y_offset': 0.0, b'shadow_deferred_y_offset': 0.0}
        self.vStartAngles = self.loadConfigValue(b'v_start_angles', xml, xml.readVector3, defaultCfg)
        self.vStartPos = self.loadConfigValue(b'v_start_pos', xml, xml.readVector3, defaultCfg)
        self.emblemsAlphaDamaged = self.loadConfigValue(b'emblems_alpha_damaged', xml, xml.readFloat, defaultCfg)
        self.emblemsAlphaUndamaged = self.loadConfigValue(b'emblems_alpha_undamaged', xml, xml.readFloat, defaultCfg)
        self.shadowLightDir = self.loadConfigValue(b'shadow_light_dir', xml, xml.readVector3, defaultCfg)
        self.shadowModelName = self.loadConfigValue(b'shadow_model_name', xml, xml.readString, defaultCfg)
        self.shadowForwardYOffset = self.loadConfigValue(b'shadow_forward_y_offset', xml, xml.readFloat, defaultFakeShadowOffsetsCfg)
        self.shadowDeferredYOffset = self.loadConfigValue(b'shadow_deferred_y_offset', xml, xml.readFloat, defaultFakeShadowOffsetsCfg)
        self.shadowDefaultTextureName = self.loadConfigValue(b'shadow_default_texture_name', xml, xml.readString, defaultCfg)
        self.shadowEmptyTextureName = self.loadConfigValue(b'shadow_empty_texture_name', xml, xml.readString, defaultCfg)
        defaultVehicleAnglesCfg = {b'vehicle_gun_pitch': 0.0, b'vehicle_turret_yaw': 0.0}
        self.vehicleGunPitch = self.loadConfigValue(b'vehicle_gun_pitch', xml, xml.readFloat, defaultVehicleAnglesCfg)
        self.vehicleTurretYaw = self.loadConfigValue(b'vehicle_turret_yaw', xml, xml.readFloat, defaultVehicleAnglesCfg)
        for i in range(0, 3):
            self.vStartAngles[i] = self[b'v_start_angles'][i] = math.radians(self[b'v_start_angles'][i])

        self.camMinDistVehicleHullLengthK = self.loadConfigValue(b'cam_min_dist_vehicle_hull_length_k', xml, xml.readFloat, defaultCfg)
        self.camCapsuleScale = self.loadConfigValue(b'cam_capsule_scale', xml, xml.readVector3, defaultCfg)
        self.camCapsuleGunScale = self.loadConfigValue(b'cam_capsule_gun_scale', xml, xml.readVector3, defaultCfg)
        return

    def loadDefaultHangarConfig(self, xml, hangarPathKey):
        self.shadowModelName = self.loadConfigValue(b'shadow_model_name', xml, xml.readString)
        self.shadowDefaultTextureName = self.loadConfigValue(b'shadow_default_texture_name', xml, xml.readString)
        self.shadowEmptyTextureName = self.loadConfigValue(b'shadow_empty_texture_name', xml, xml.readString)
        self.loadConfigValue(hangarPathKey, xml, xml.readString)
        return

    def loadCustomizationConfig(self, xml):
        defaultFakeShadowOffsetsCfg = {b'shadow_forward_y_offset': 0.0, 
           b'shadow_deferred_y_offset': 0.0}
        self.vStartPos = self.loadConfigValue(b'v_start_pos', xml, xml.readVector3, self)
        self.vStartAngles = self.loadConfigValue(b'v_start_angles', xml, xml.readVector3, self)
        self.shadowForwardYOffset = self.loadConfigValue(b'shadow_forward_y_offset', xml, xml.readFloat, defaultFakeShadowOffsetsCfg)
        self.shadowDeferredYOffset = self.loadConfigValue(b'shadow_deferred_y_offset', xml, xml.readFloat, defaultFakeShadowOffsetsCfg)
        return

    def loadSecondaryConfig(self, xml):
        defaultShadowOffsetsCfg = {b'shadow_forward_y_offset': 0.0, 
           b'shadow_deferred_y_offset': 0.0}
        self.vStartPos = self.loadConfigValue(b'v_start_pos', xml, xml.readVector3, self)
        self.vStartAngles = self.loadConfigValue(b'v_start_angles', xml, xml.readVector3, self)
        for i in range(0, 3):
            self.vStartAngles[i] = self[b'v_start_angles'][i] = math.radians(self[b'v_start_angles'][i])

        self.shadowForwardYOffset = self.loadConfigValue(b'shadow_forward_y_offset', xml, xml.readFloat, defaultShadowOffsetsCfg)
        self.shadowDeferredYOffset = self.loadConfigValue(b'shadow_deferred_y_offset', xml, xml.readFloat, defaultShadowOffsetsCfg)
        return

    def loadConfigValue(self, name, xml, fn, defaultCfg=None):
        if xml.has_key(name):
            self[name] = fn(name)
        else:
            self[name] = defaultCfg.get(name) if defaultCfg is not None else None
        return self[name]
