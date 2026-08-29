import weakref, BigWorld, Math, material_kinds
from constants import IS_EDITOR
from helpers.PixieNode import PixieCache
from CustomEffect import EffectSettings
from cgf_obsolete_script.py_component import Component
from vehicle_systems.tankStructure import TankNodeNames
_ENABLE_VALUE_TRACKER = False
_ENABLE_VALUE_TRACKER_ENGINE = False
_ENABLE_PIXIE_TRACKER = False
_VEHICLE_DIRECTION_THRESHOLD = 0.1

class CustomEffectManager(Component):
    _LEFT_TRACK = 0
    _RIGHT_TRACK = 1
    _DRAW_ORDER_IDX = 50

    @property
    def variables(self):
        return self.__variableArgs

    def __init__(self, appearance):
        if _ENABLE_VALUE_TRACKER or _ENABLE_VALUE_TRACKER_ENGINE or _ENABLE_PIXIE_TRACKER:
            from helpers.ValueTracker import ValueTracker
            self.__vt = ValueTracker.instance()
        else:
            self.__vt = None
        self.__selectors = []
        self.__variableArgs = dict()
        self.__vehicle = None
        self.__appearance = appearance
        self.__engineState = appearance.detailedEngineState
        self.__prevWaterHeight = None
        self.__gearUP = False
        self.__trailParticleNodes = None
        typeDesc = appearance.typeDescriptor
        args = {}
        args[b'chassis'] = {}
        args[b'chassis'][b'model'] = appearance.compoundModel
        args[b'hull'] = {}
        args[b'hull'][b'model'] = appearance.compoundModel
        args[b'engineTags'] = typeDesc.engine.tags
        args[b'vehicleTags'] = typeDesc.type.tags
        args[b'appearance'] = appearance
        args[b'drawOrderBase'] = CustomEffectManager._DRAW_ORDER_IDX
        self.__hullSelectors = []
        self.__chassisSelectors = []
        for desc in typeDesc.hull.customEffects:
            if desc is not None:
                selector = desc.create(args)
                if selector is not None:
                    self.__selectors.append(selector)
                    self.__hullSelectors.append(selector)

        for desc in typeDesc.chassis.customEffects:
            if desc is not None:
                selector = desc.create(args)
                if selector is not None:
                    self.__selectors.append(selector)
                    self.__chassisSelectors.append(selector)

        self.__createChassisCenterNodes()
        self.__wheelsData = None
        self.__variableArgs[b'Nitro'] = 0
        PixieCache.incref()
        return

    def disableDefaultSelectors(self, disableChassis, disableHull):
        if disableChassis:
            for selector in self.__chassisSelectors:
                selector.destroy()
                self.__selectors.remove(selector)

            self.__chassisSelectors = []
        if disableHull:
            for selector in self.__hullSelectors:
                selector.destroy()
                self.__selectors.remove(selector)

            self.__hullSelectors = []
        return

    def setWheelsData(self, appearance):
        wheelsConfig = appearance.typeDescriptor.chassis.generalWheelsAnimatorConfig
        if wheelsConfig is not None:
            names = appearance.wheelsAnimator.getWheelNodeNames()
            if names:
                self.__wheelsData = names
        return

    def getParameter(self, name):
        return self.__variableArgs.get(name, 0.0)

    def destroy(self):
        self.deactivate()
        for effectSelector in self.__selectors:
            effectSelector.destroy()

        PixieCache.decref()
        self.__trailParticleNodes = None
        self.__selectors = None
        self.__engineState = None
        self.__appearance = None
        self.__variableArgs = None
        self.__vehicle = None
        if _ENABLE_PIXIE_TRACKER:
            self.__vt.addValue2(b'Pixie Count', PixieCache.pixiesCount)
        if _ENABLE_VALUE_TRACKER or _ENABLE_VALUE_TRACKER_ENGINE or _ENABLE_PIXIE_TRACKER:
            self.__vt = None
        return

    def enable(self, enable, settingsFlags=EffectSettings.SETTING_DUST):
        for effectSelector in self.__selectors:
            if effectSelector.settingsFlags() == settingsFlags:
                if enable:
                    effectSelector.start()
                else:
                    effectSelector.stop()

        return

    def setVehicle(self, vehicle):
        self.__vehicle = weakref.proxy(vehicle)
        return

    def activate(self):
        super(CustomEffectManager, self).activate()
        for effectSelector in self.__selectors:
            effectSelector.start()

        return

    def deactivate(self):
        for effectSelector in self.__selectors:
            effectSelector.stop()

        super(CustomEffectManager, self).deactivate()
        return

    def __createChassisCenterNodes(self):
        compoundModel = self.__appearance.compoundModel
        self.__trailParticleNodes = [
         compoundModel.node(TankNodeNames.TRACK_LEFT_MID),
         compoundModel.node(TankNodeNames.TRACK_RIGHT_MID)]
        return

    def onGearUp(self):
        self.__gearUP = True
        return

    def update(self):
        speedInfo = self.__vehicle.speedInfo.value
        vehicleSpeed = speedInfo[2]
        appearance = self.__appearance
        self.__variableArgs[b'speed'] = vehicleSpeed
        self.__variableArgs[b'isPC'] = isPC = isVehicleAttached(self.__vehicle)
        if vehicleSpeed > _VEHICLE_DIRECTION_THRESHOLD:
            direction = 1
        elif vehicleSpeed < -_VEHICLE_DIRECTION_THRESHOLD:
            direction = -1
        else:
            direction = 0
        self.__variableArgs[b'direction'] = direction
        self.__variableArgs[b'rotSpeed'] = speedInfo[1]
        matKindsUnderTracks = getCorrectedMatKinds(appearance)
        self.__variableArgs[b'deltaR'], self.__variableArgs[b'directionR'], self.__variableArgs[b'matkindR'] = self.__getScrollParams(appearance.trackScrollController.rightSlip(), appearance.trackScrollController.rightContact(), matKindsUnderTracks[CustomEffectManager._RIGHT_TRACK], direction)
        self.__variableArgs[b'deltaL'], self.__variableArgs[b'directionL'], self.__variableArgs[b'matkindL'] = self.__getScrollParams(appearance.trackScrollController.leftSlip(), appearance.trackScrollController.leftContact(), matKindsUnderTracks[CustomEffectManager._LEFT_TRACK], direction)
        self.__variableArgs[b'commonSlip'] = appearance.transmissionSlip
        self.__variableArgs[b'hullAngle'] = Math.calcHullAngle(self.__vehicle.matrix, self.__vehicle.filter.velocity)
        self.__variableArgs[b'isUnderWater'] = 1 if appearance.isUnderwater else 0
        self.__correctWaterNodes()
        self.__variableArgs[b'gearUp'] = self.__gearUP
        self.__variableArgs[b'RPM'] = rpm = self.__engineState.relativeRPM
        self.__gearUP = False
        self.__variableArgs[b'engineLoad'] = self.__engineState.mode
        self.__variableArgs[b'engineState'] = self.__engineState.engineState
        engineStart = self.__engineState.starting
        self.__variableArgs[b'engineStart'] = engineStart and not self.__variableArgs.get(b'__engineStarted', False)
        if engineStart or not isPC and rpm:
            self.__variableArgs[b'__engineStarted'] = True
        self.__variableArgs[b'physicLoad'] = self.__engineState.physicLoad
        if self.__wheelsData is not None:
            for wheelIndex in xrange(0, len(self.__wheelsData)):
                nodeName = self.__wheelsData[wheelIndex]
                self.__variableArgs[nodeName + b':contact'] = 0 if appearance.wheelsAnimator.wheelIsFlying(wheelIndex) else 1

        for effectSelector in self.__selectors:
            effectSelector.update(self.__variableArgs)

        if _ENABLE_VALUE_TRACKER:
            self.__vt.addValue2(b'speed', self.__variableArgs[b'speed'])
            self.__vt.addValue2(b'direction', self.__variableArgs[b'direction'])
            self.__vt.addValue2(b'rotSpeed', self.__variableArgs[b'rotSpeed'])
            self.__vt.addValue2(b'deltaR', self.__variableArgs[b'deltaR'])
            self.__vt.addValue2(b'deltaL', self.__variableArgs[b'deltaL'])
            self.__vt.addValue2(b'hullAngle', self.__variableArgs[b'hullAngle'])
            self.__vt.addValue2(b'isUnderWater', self.__variableArgs[b'isUnderWater'])
            self.__vt.addValue2(b'directionR', self.__variableArgs[b'directionR'])
            self.__vt.addValue2(b'directionL', self.__variableArgs[b'directionL'])
            if self.__variableArgs[b'matkindL'] > -1:
                materialL = material_kinds.EFFECT_MATERIAL_INDEXES_BY_IDS[self.__variableArgs[b'matkindL']]
                self.__vt.addValue(b'materialL', material_kinds.EFFECT_MATERIALS[materialL])
            else:
                self.__vt.addValue(b'materialL', b'No')
            if self.__variableArgs[b'matkindR'] > -1:
                materialR = material_kinds.EFFECT_MATERIAL_INDEXES_BY_IDS[self.__variableArgs[b'matkindR']]
                self.__vt.addValue(b'materialR', material_kinds.EFFECT_MATERIALS[materialR])
            else:
                self.__vt.addValue(b'materialR', b'No')
        if _ENABLE_VALUE_TRACKER_ENGINE:
            self.__vt.addValue2(b'engineStart', self.__variableArgs[b'engineStart'])
            self.__vt.addValue2(b'gearUP', self.__variableArgs[b'gearUp'])
            self.__vt.addValue2(b'RPM', self.__variableArgs[b'RPM'])
            self.__vt.addValue2(b'engineLoad', self.__engineState.mode)
            self.__vt.addValue2(b'physicLoad', self.__engineState.physicLoad)
        if _ENABLE_PIXIE_TRACKER:
            self.__vt.addValue2(b'Pixie Count', PixieCache.pixiesCount)
        return

    @staticmethod
    def __getScrollParams(trackScrolldelta, hasContact, matKindsUnderTrack, direction):
        matKind = -1
        scrollDelta = 0.0
        if hasContact:
            scrollDelta = trackScrolldelta
            matKind = matKindsUnderTrack
        if scrollDelta != 0.0:
            direction = 1 if scrollDelta >= 0.0 else -1
        scrollDelta = abs(scrollDelta)
        return (scrollDelta, direction, matKind)

    def __correctWaterNodes(self):
        waterHeight = 0.0 if not self.__appearance.isInWater else self.__appearance.waterHeight
        if waterHeight != self.__prevWaterHeight:
            invVehicleMatrix = Math.Matrix(self.__appearance.compoundModel.matrix)
            invVehicleMatrix.invert()
            waterShiftRel = invVehicleMatrix.applyVector(Math.Vector3(0, waterHeight, 0))
            for effectSelector in self.__selectors:
                for node in effectSelector.effectNodes:
                    if node is not None:
                        node.correctWater(waterShiftRel)

            self.__prevWaterHeight = waterHeight
        return

    def remapNode(self, fromNode, toNode=b''):
        for effectSelector in self.__selectors:
            for node in effectSelector.effectNodes:
                if node is not None:
                    node.remapNode(fromNode, toNode, self.__appearance.compoundModel)

        return


def getCorrectedMatKinds(vehicleAppearance):
    correctedMatKinds = vehicleAppearance.terrainMatKind
    if vehicleAppearance.isInWater:
        correctedMatKinds = [
         material_kinds.getWaterMatKind()] * len(correctedMatKinds)
    return correctedMatKinds


def isVehicleAttached(vehicle):
    if IS_EDITOR:
        return True
    else:
        attachedVehicle = BigWorld.player().getVehicleAttached()
        return attachedVehicle is not None and attachedVehicle.id == vehicle.id
