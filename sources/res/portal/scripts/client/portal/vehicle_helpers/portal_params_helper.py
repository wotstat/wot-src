import typing
from collections import Iterable
from itertools import izip_longest
from helpers import dependency
from portal.skeletons.portal_event_controller import IPortalEventController
from portal.gui.impl.gen.view_models.views.lobby.params_ttx_model import TtxComparisonStatus
if typing.TYPE_CHECKING:
    from typing import Optional, List
COMMON_PARAMS = (b'maxHealth', b'avgDamage', b'hullArmor', b'avgPiercingPower', b'turretArmor', b'aimingTime', b'turretRotationSpeed', b'shotDispersionAngle', b'chassisRotationSpeed', b'avgDamagePerMinute', b'enginePower', b'speedLimits')
CLASSIC_GUN_PARAMS = (b'reloadTime', b'reloadTimeSecs')
AUTORELOAD_GUN_PARAMS = (b'clipFireRate', b'autoReloadTime')
DUAL_GUN_PARAMS = (b'clipFireRate', b'reloadTimeSecs')
CLIP_GUN_PARAMS = (b'clipFireRate', b'autoReloadTime', b'reloadTime')
INVERTED_PARAMS = (b'reloadTimeSecs', b'clipFireRate', b'autoReloadTime', b'aimingTime', b'shotDispersionAngle')
MODIFIER_TO_FACTOR = {b'gun/reloadTime': b'gunReloadTimeFactor', 
   b'engine/power': b'enginePowerFactor', 
   b'damageFactor': b'damageFactor'}

class PortalParam(object):

    def __init__(self):
        self.name = None
        self.values = []
        return


class PortalParamValue(object):

    def __init__(self):
        self.value = None
        self.status = TtxComparisonStatus.DEFAULT
        return


class PortalParamsHelper(object):
    __portalController = dependency.descriptor(IPortalEventController)

    @staticmethod
    def getVehicleParams(vehicle):
        appliedModifiers = PortalParamsHelper.__portalController.getVehicleModifiers(vehicle)
        PortalParamsHelper.__applyModifiers(vehicle, appliedModifiers)
        gunParams = PortalParamsHelper.__getVehicleGunParams(vehicle.descriptor)
        neededParams = list(COMMON_PARAMS)
        allParamNames = vehicle.getParams()[b'parameters'].keys()
        insertPos = 0
        for param in gunParams:
            if param in allParamNames:
                neededParams.insert(len(COMMON_PARAMS) + 1 - insertPos * 2, param)
                insertPos += 1

        vehParams = {paramName: param for paramName, param in vehicle.getParams()[b'parameters'].iteritems() if paramName in neededParams}
        engineFwSpeed = vehicle.typeDescr.xphysics[b'engines'][vehicle.descriptor.engine.name][b'smplFwMaxSpeed']
        vehParams[b'speedLimits'][0] = engineFwSpeed
        params = []
        for paramName in neededParams:
            paramValues = vehParams.get(paramName)
            if paramValues is None:
                continue
            param = PortalParam()
            param.name = paramName
            paramValues = tuple(paramValues) if isinstance(paramValues, Iterable) else (paramValues,)
            for paramValue in paramValues:
                value = PortalParamValue()
                value.value = paramValue
                param.values.append(value)

            params.append(param)

        vehicle.descriptor.rebuildAttrs()
        return params

    @staticmethod
    def getComparedParams(originalParams, comparedParams):
        for comparedParam in comparedParams:
            originalParam = [param for param in originalParams if param.name == comparedParam.name]
            originalValues = originalParam[0].values if originalParam else []
            for i, (comparedValue, originalValue) in enumerate(izip_longest(comparedParam.values, originalValues)):
                if comparedValue is None:
                    continue
                isSecondClipFireRate = comparedParam.name == b'clipFireRate' and i == 2
                isInverse = comparedParam.name in INVERTED_PARAMS and not isSecondClipFireRate
                increaseStatus = TtxComparisonStatus.DECREASE if isInverse else TtxComparisonStatus.INCREASE
                decreaseStatus = TtxComparisonStatus.INCREASE if isInverse else TtxComparisonStatus.DECREASE
                if originalValue is not None and len(comparedParam.values) == len(originalValues):
                    if comparedValue.value > originalValue.value:
                        comparedValue.status = increaseStatus
                    elif comparedValue.value < originalValue.value:
                        comparedValue.status = decreaseStatus

        return comparedParams

    @staticmethod
    def applyModifiersAndGetParams(vehicle, modifiers):
        PortalParamsHelper.__applyModifiers(vehicle, modifiers)
        return PortalParamsHelper.getVehicleParams(vehicle)

    @staticmethod
    def __getVehicleGunParams(vehDescr):
        gunParams = CLASSIC_GUN_PARAMS
        if vehDescr.isDualgunVehicle:
            gunParams = DUAL_GUN_PARAMS
        elif vehDescr.isClipGun:
            gunParams = CLIP_GUN_PARAMS
        elif vehDescr.isAutoReloadGun:
            gunParams = AUTORELOAD_GUN_PARAMS
        return gunParams

    @staticmethod
    def __applyModifiers(vehicle, modifiers):
        attributes = vehicle.miscAttrs
        for modifier in modifiers:
            modType = modifier[b'type']
            modValue = modifier[b'modifier']
            attributes[MODIFIER_TO_FACTOR[modType]] *= modValue

        return
