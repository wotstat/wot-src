import logging, random, string
from collections import namedtuple
from functools import partial
from enum import Enum
import AnimationSequence, BigWorld, Math, WWISE, DecalMap, SoundGroups, helpers, material_kinds
from PixieBG import PixieBG
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.battle_session import IBattleSessionProvider
from soft_exception import SoftException
from vehicle_systems.sound_objects import getGunSoundObject, getGunSoundObjectDistance
from constants import IS_EDITOR
from wrapped_reflection_framework import reflectedNamedTuple
if not IS_EDITOR:
    from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS
_logger = logging.getLogger(__name__)
COLOR_WHITE = 4294967295L
_ALLOW_DYNAMIC_LIGHTS = True
KeyPoint = namedtuple(b'KeyPoint', (b'name', b'time'))
EffectsTimeLine = namedtuple(b'EffectsTimeLine', (b'keyPoints', b'effectsList'))
EffectsTimeLinePrereqs = reflectedNamedTuple(b'EffectsTimeLinePrereqs', (b'keyPoints', b'effectsList', b'prereqs'))

class SpecialKeyPointNames(object):
    START = b'start'
    END = b'end'
    STATIC = b'static'


__START_KEY_POINT = KeyPoint(SpecialKeyPointNames.START, 0.0)
SoundStartParam = namedtuple(b'SoundStartParam', (b'name', b'value'))

def _isPyModel(model):
    return model is not None and model.__class__.__name__ == b'Model'


def reload():
    import __builtin__
    from sys import modules
    __builtin__.reload(modules[reload.__module__])
    return


class EFFECT_DELETE_REASON(Enum):
    LIST_DESTRUCTION = 0
    REACHED_END_KEY = 1
    KEEP_POSTEFFECTS = 2
    FORCE_DELETE = 3


class EffectsList(object):
    __slots__ = (b'__effectDescList', b'relatedEffects')

    def __init__(self, section):
        super(EffectsList, self).__init__()
        self.__effectDescList = []
        self.relatedEffects = {}
        for s in section.items():
            effDesc = _createEffectDesc(s[0], s[1])
            if effDesc is not None:
                self.__effectDescList.append(effDesc)

        return

    def prerequisites(self):
        out = []
        for effDesc in self.__effectDescList:
            out += effDesc.prerequisites()

        for relatedEffect in self.relatedEffects.itervalues():
            out += relatedEffect.effectsList.prerequisites()

        return out

    def attachTo(self, model, data, key, **args):
        if not data.has_key(b'_EffectsList_effects'):
            data[b'_EffectsList_effects'] = []
        for eff in self.__effectDescList:
            if eff.startKey == key:
                if args.has_key(b'keyPoints'):
                    startTime = endTime = 0
                    for keyPoint in args[b'keyPoints']:
                        if keyPoint.name == eff.startKey:
                            startTime = keyPoint.time
                        endTime = keyPoint.time
                        if keyPoint.name == eff.endKey:
                            break

                    eff.duration = endTime - startTime
                eff.create(model, data[b'_EffectsList_effects'], args)

        return

    def reattachTo(self, model, data):
        effects = data.get(b'_EffectsList_effects', ())
        for elem in effects:
            elem[b'typeDesc'].reattach(elem, model)

        return

    def detachFrom(self, data, key, reason=EFFECT_DELETE_REASON.REACHED_END_KEY):
        effects = data[b'_EffectsList_effects']
        for elem in effects[:]:
            if elem[b'typeDesc'].endKey == key:
                if elem[b'typeDesc'].delete(elem, reason):
                    effects.remove(elem)

        return

    def detachAllFrom(self, data, keepPosteffects=False, forceDelete=False):
        effects = data.get(b'_EffectsList_effects', None)
        if effects is None:
            return
        else:
            if keepPosteffects:
                reason = EFFECT_DELETE_REASON.KEEP_POSTEFFECTS
            elif forceDelete:
                reason = EFFECT_DELETE_REASON.FORCE_DELETE
            else:
                reason = EFFECT_DELETE_REASON.LIST_DESTRUCTION
            for elem in effects[:]:
                if elem[b'typeDesc'].delete(elem, reason):
                    effects.remove(elem)

            if not keepPosteffects:
                return
            del data[b'_EffectsList_effects']
            return

    def descriptors(self):
        return self.__effectDescList


class EffectsListPlayer(object):
    effectsList = property((lambda self: self.__effectsList))
    isPlaying = property((lambda self: self.__isStarted))
    activeEffects = set()
    clearInProgress = False

    @staticmethod
    def clear():
        import BattleReplay
        replayCtrl = BattleReplay.g_replayCtrl
        if not replayCtrl.isPlaying:
            EffectsListPlayer.clearInProgress = True
            for effect in EffectsListPlayer.activeEffects:
                effect.stop()

            EffectsListPlayer.clearInProgress = False
            return
        else:
            warpDelta = replayCtrl.warpTime - replayCtrl.currentTime
            EffectsListPlayer.clearInProgress = True
            for effect in EffectsListPlayer.activeEffects:
                if effect.__waitForKeyOff and warpDelta > 0.0:
                    continue
                if effect.__curKeyPoint is not None:
                    effectCurTime = effect.__curKeyPoint.time
                else:
                    effectCurTime = 0.0
                if warpDelta <= 0.0 or effect.__keyPoints[-1].time - effectCurTime < warpDelta:
                    if effect.__callbackFunc is not None:
                        effect.__callbackFunc()
                    effect.stop()

            EffectsListPlayer.clearInProgress = False
            return

    def __init__(self, effectsList, keyPoints, **args):
        self.__keyPoints = keyPoints
        self.__effectsList = effectsList
        self.__args = args
        self.__args[b'keyPoints'] = self.__keyPoints
        self.__curKeyPoint = None
        self.__callbackFunc = None
        self.__callbackID = None
        self.__keyPointIdx = -1
        self.__isStarted = False
        self.__waitForKeyOff = False
        self.__data = dict()
        return

    def play(self, model, startKeyPoint=None, callbackFunc=None, waitForKeyOff=False):
        needPlay, newKey = self.__isNeedToPlay(waitForKeyOff)
        if not needPlay:
            return
        else:
            if newKey is not None:
                startKeyPoint = newKey
            if self.__isStarted:
                _logger.error(b'player already started. To restart it you must before call stop().')
                return
            EffectsListPlayer.activeEffects.add(self)
            self.__isStarted = True
            self.__callbackID = None
            self.__model = model
            self.__callbackFunc = callbackFunc
            self.__waitForKeyOff = waitForKeyOff
            keyPoint = self.__getKeyPointIdx(startKeyPoint)
            self.__keyPointIdx = keyPoint if startKeyPoint is not None and keyPoint is not None else 0
            self.__keyPointIdx -= 1
            self.__effectsList.attachTo(self.__model, self.__data, None, **self.__args)
            firstTimePoint = self.__keyPoints[self.__keyPointIdx + 1].time
            if self.__keyPointIdx < 0 and startKeyPoint is None and firstTimePoint > 0.0:
                self.__callbackID = BigWorld.callback(firstTimePoint, self.__playKeyPoint)
            else:
                self.__playKeyPoint(waitForKeyOff)
            return

    def keyOff(self, waitForNextKeyOff=False):
        if self.__isStarted:
            self.__playKeyPoint(waitForNextKeyOff)
        return

    def reattachTo(self, model):
        self.__effectsList.reattachTo(model, self.__data)
        self.__model = model
        return

    def __isNeedToPlay(self, waitForKeyOff):
        if helpers.gEffectsDisabled():
            return (False, None)
        else:
            if IS_EDITOR:
                return (True, None)
            import BattleReplay
            replayCtrl = BattleReplay.g_replayCtrl
            if replayCtrl.isPlaying:
                entity_id = -1
                if b'entity_id' in self.__args:
                    entity_id = self.__args[b'entity_id']
                need_play = True
                if entity_id > -1:
                    need_play = replayCtrl.isNeedToPlay(entity_id)
                if need_play:
                    if replayCtrl.isTimeWarpInProgress:
                        if not waitForKeyOff:
                            warpDelta = replayCtrl.warpTime - replayCtrl.currentTime
                            if self.__keyPoints[-1].time / 2 < warpDelta:
                                return (
                                 False, None)
                    else:
                        return (
                         True, None)
                for key in self.__keyPoints:
                    if key.name == SpecialKeyPointNames.STATIC:
                        return (True, SpecialKeyPointNames.STATIC)

                return (False, None)
            return (True, None)

    def stop(self, keepPosteffects=False, forceCallback=False, forceDelete=False):
        if self.__isStarted:
            if forceCallback and self.__callbackFunc is not None:
                self.__callbackFunc()
        if not EffectsListPlayer.clearInProgress:
            EffectsListPlayer.activeEffects.discard(self)
        self.__isStarted = False
        if self.__callbackID is not None:
            BigWorld.cancelCallback(self.__callbackID)
            self.__callbackID = None
        if self.__effectsList is not None:
            self.__effectsList.detachAllFrom(self.__data, keepPosteffects, forceDelete)
        self.__model = None
        self.__data = dict()
        self.__curKeyPoint = None
        self.__callbackFunc = None
        return

    def __getKeyPointIdx(self, name):
        for i, keyPoint in enumerate(self.__keyPoints):
            if keyPoint.name == name:
                return i

        return

    def __playKeyPoint(self, waitForKeyOff=False):
        self.__callbackID = None
        try:
            self.__keyPointIdx += 1
            if self.__keyPointIdx + 1 >= len(self.__keyPoints):
                if self.__callbackFunc:
                    self.__callbackFunc()
                self.stop()
                return
            self.__curKeyPoint = self.__keyPoints[self.__keyPointIdx]
            nextKeyPoint = self.__keyPoints[self.__keyPointIdx + 1]
            self.__effectsList.detachFrom(self.__data, self.__curKeyPoint.name)
            self.__effectsList.attachTo(self.__model, self.__data, self.__curKeyPoint.name, **self.__args)
            deltaTime = nextKeyPoint.time - self.__curKeyPoint.time
            if deltaTime == 0.0:
                self.__playKeyPoint(waitForKeyOff)
            elif not waitForKeyOff:
                self.__callbackID = BigWorld.callback(deltaTime, self.__playKeyPoint)
        except Exception:
            _logger.exception(b'Play key point exception')

        return


class _EffectDesc(object):
    __slots__ = (b'startKey', b'endKey', b'_nodeName', b'duration')

    def __init__(self, dataSection):
        self.startKey = intern(dataSection.readString(b'startKey'))
        if not self.startKey:
            _raiseWrongConfig(b'startKey', self.TYPE)
        self.endKey = dataSection.readString(b'endKey')
        nodeName = dataSection.readString(b'position')
        if nodeName:
            self._nodeName = [intern(name) for name in string.split(nodeName, b'/')]
        else:
            self._nodeName = []
        return

    def prerequisites(self):
        return []

    def reattach(self, elem, model):
        return

    def create(self, model, effects, args):
        return

    def delete(self, elem, reason):
        return True


class _PixieEffectDesc(_EffectDesc):
    __slots__ = (b'_files', b'_havokFiles', b'_force', b'_surfaceMatKinds', b'_orientByClosestSurfaceNormal', b'_alwaysUpdate', b'__prototypePixies')
    TYPE = b'_PixieEffectDesc'

    def __init__(self, dataSection):
        super(_PixieEffectDesc, self).__init__(dataSection)
        self._files = [f for f in dataSection.readStrings(b'file') if f]
        if not self._files:
            _raiseWrongConfig(b'file', self.TYPE)
        self._force = 0
        key = b'force'
        if dataSection.has_key(key):
            self._force = dataSection.readInt(key, 0)
            if self._force < 0:
                _raiseWrongConfig(key, self.TYPE)
        if dataSection.has_key(b'surfaceMatKind'):
            matKindNames = dataSection.readString(b'surfaceMatKind', b'').split(b' ')
            self._surfaceMatKinds = []
            for matKindName in matKindNames:
                self._surfaceMatKinds += material_kinds.EFFECT_MATERIAL_IDS_BY_NAMES.get(matKindName, [])

        else:
            self._surfaceMatKinds = None
        self._orientByClosestSurfaceNormal = dataSection.readBool(b'orientBySurfaceNormal', False)
        self._alwaysUpdate = dataSection.readBool(b'alwaysUpdateModel', False)
        self.__prototypePixies = {}
        return

    def prerequisites(self):
        return self._files

    def reattach(self, elem, model):
        newPos = elem[b'newPos']
        nodePos = self._nodeName
        elem[b'model'] = model
        if newPos is not None:
            nodePos = string.split(newPos[0], b'/') if newPos[0] else []
        if elem[b'pixie'].pixie is not None and elem[b'node'] is not None:
            elem[b'node'].detach(elem[b'pixie'].pixie)
            elem[b'node'] = _findTargetNode(model, nodePos, newPos[1] if newPos and len(newPos) > 1 else None, self._orientByClosestSurfaceNormal, elem[b'surfaceNormal'])
            elem[b'node'].attach(elem[b'pixie'].pixie)
        else:
            elem[b'node'] = _findTargetNode(model, nodePos, None, self._orientByClosestSurfaceNormal, elem[b'surfaceNormal'])
        return

    def create(self, model, effects, args):
        elem = {}
        node = args.get(b'node', None)
        if node is None:
            elem[b'newPos'] = newPos = args.get(b'position', None)
            nodePos = self._nodeName
            if newPos is not None:
                nodePos = string.split(newPos[0], b'/') if newPos[0] else []
            scale = args.get(b'scale')
            if scale is not None:
                elem[b'scale'] = scale
            elem[b'surfaceNormal'] = args.get(b'surfaceNormal', None)
            surfaceMatKind = args.get(b'surfaceMatKind', None)
            if surfaceMatKind is not None and self._surfaceMatKinds is not None:
                if surfaceMatKind not in self._surfaceMatKinds:
                    return
            elem[b'node'] = _findTargetNode(model, nodePos, newPos[1] if newPos and len(newPos) > 1 else None, self._orientByClosestSurfaceNormal, elem[b'surfaceNormal'])
        else:
            elem[b'node'] = node
        elem[b'model'] = model
        elem[b'typeDesc'] = self
        elem[b'pixie'] = None
        eFile = random.choice(self._files)
        prototypePixie = self.__prototypePixies.get(eFile)
        modifiers = {}
        if args.get(b'havokSpawnedDestructibles', False):
            modifiers[b'doHavokDebrisSpawned'] = True
        tintColor = args.get(b'tintColor', COLOR_WHITE)
        if tintColor != COLOR_WHITE:
            modifiers[b'tintColor'] = tintColor
        if not modifiers:
            modifiers = None
        if prototypePixie is not None:
            elem[b'pixie'] = PixieBG(eFile, None, prototypePixie.clone(), None, modifiers)
            self._callbackCreate(elem)
        else:
            elem[b'file'] = eFile
            elem[b'pixie'] = PixieBG(eFile, self._callbackAfterLoading, None, elem, modifiers)
        effects.append(elem)
        return

    def delete(self, elem, reason):
        pixieDef = elem.get(b'pixie', None)
        if pixieDef is not None:
            if pixieDef.pixie is not None:
                elem[b'node'].detach(elem[b'pixie'].pixie)
            isForceKill = reason == EFFECT_DELETE_REASON.FORCE_DELETE
            pixieDef.destroy(isForceKill)
        elem[b'pixie'] = None
        elem[b'node'] = None
        return True

    def _callbackAfterLoading(self, pixieBG, elem):
        if elem is not None:
            self.__prototypePixies[elem[b'file']] = pixieBG.pixie.clone()
            self._callbackCreate(elem)
        return

    def _callbackCreate(self, elem):
        scale = elem.get(b'scale')
        pixie = elem[b'pixie']
        node = elem[b'node']
        if pixie is not None and node is not None:
            if scale is not None:
                pixie.scale(scale)
            pixie.force(self._force)
            node.attach(pixie.pixie)
        return


class _AnimationEffectDesc(_EffectDesc):
    __slots__ = (b'_name',)
    TYPE = b'_AnimationEffectDesc'

    def __init__(self, dataSection):
        super(_AnimationEffectDesc, self).__init__(dataSection)
        self._name = dataSection.readString(b'name')
        if not self._name:
            _raiseWrongConfig(b'name', self.TYPE)
        return

    def create(self, model, effects, args):
        targetModel = _findTargetModel(model, self._nodeName)
        animator = None
        if _isPyModel(targetModel):
            clipResource = targetModel.deprecatedGetAnimationClipResource(self._name)
            spaceID = BigWorld.player().spaceID
            loader = AnimationSequence.Loader(clipResource, spaceID)
            animator = loader.loadSync()
            animator.bindTo(AnimationSequence.ModelWrapperContainer(model, spaceID))
            animator.start()
        else:
            raise SoftException(b'EffectsList trying to play old animation <%s> on compoud model <%s>.' % (self._name, self.TYPE))
        effects.append({b'typeDesc': self, b'animator': animator})
        return

    def delete(self, elem, reason):
        if elem[b'animator'] is None:
            return True
        else:
            if reason == EFFECT_DELETE_REASON.KEEP_POSTEFFECTS:
                if self.endKey:
                    elem[b'animator'].stop()
                    return True
                return False
            elem[b'animator'].stop()
            return True
            return


class _VisibilityEffectDesc(_EffectDesc):
    __slots__ = (b'_hasInitial', b'_initial')
    TYPE = b'_VisibilityEffectDesc'

    def __init__(self, dataSection):
        super(_VisibilityEffectDesc, self).__init__(dataSection)
        self._hasInitial = False
        self._initial = False
        key = b'initial'
        if dataSection.has_key(key):
            self._initial = dataSection.readBool(key, False)
            self._hasInitial = True
        return

    def create(self, model, effects, args):
        targetModel = _findTargetModel(model, self._nodeName)
        if self._hasInitial:
            targetModel.visible = self._initial
        else:
            targetModel.visible = not targetModel.visible
        effects.append({b'typeDesc': self, b'model': targetModel})
        return

    def delete(self, elem, reason):
        if self._hasInitial:
            elem[b'model'].visible = not self._initial
        else:
            elem[b'model'].visible = not elem[b'model'].visible
        return True


class _ModelEffectDesc(_EffectDesc):
    __slots__ = (b'_modelName', b'_animation')
    TYPE = b'_ModelEffectDesc'

    def __init__(self, dataSection):
        super(_ModelEffectDesc, self).__init__(dataSection)
        self._modelName = dataSection.readString(b'name')
        if not self._modelName:
            _raiseWrongConfig(b'name', self.TYPE)
        self._animation = None
        key = b'animation'
        if dataSection.has_key(key):
            self._animation = dataSection.readString(key)
        return

    def prerequisites(self):
        return [
         self._modelName]

    def reattach(self, elem, model):
        elem[b'node'].detach(elem[b'attachment'])
        newPos = elem[b'newPos']
        nodeName = self._nodeName
        if newPos is not None:
            nodeName = string.split(newPos[0], b'/') if newPos[0] else []
        targetNode = _findTargetNode(model, nodeName, newPos[1] if newPos and len(newPos) > 1 else None)
        targetNode.attach(model)
        return

    def create(self, model, effects, args):
        currentModel = BigWorld.Model(self._modelName)
        newPos = args.get(b'position', None)
        nodeName = self._nodeName
        if newPos is not None:
            nodeName = string.split(newPos[0], b'/') if newPos[0] else []
        targetNode = _findTargetNode(model, nodeName, newPos[1] if newPos and len(newPos) > 1 else None)
        targetNode.attach(currentModel)
        animator = None
        if self._animation:
            clipResource = model.deprecatedGetAnimationClipResource(self._animation)
            spaceID = BigWorld.player().spaceID
            loader = AnimationSequence.Loader(clipResource, spaceID)
            animator = loader.loadSync()
            animator.bindTo(AnimationSequence.ModelWrapperContainer(model, spaceID))
            animator.start()
        elem = {b'typeDesc': self, 
           b'model': model, 
           b'animator': animator, 
           b'attachment': currentModel, 
           b'newPos': newPos, 
           b'node': targetNode}
        effects.append(elem)
        return currentModel

    def delete(self, elem, reason):
        elem[b'node'].detach(elem[b'attachment'])
        return True


def _getDamageSize(args):
    damageFactor = args.get(b'damageFactor', -1)
    if damageFactor > -1:
        damage_size = b'SWITCH_ext_damage_size_medium'
        if damageFactor < 4335.0 / 100.0:
            damage_size = b'SWITCH_ext_damage_size_small'
        elif damageFactor > 8925.0 / 100.0:
            damage_size = b'SWITCH_ext_damage_size_large'
        return damage_size
    return


def _isVehiclePresent(args):
    vehicle = args.get(b'entity', None)
    if vehicle is not None:
        return vehicle.isAlive() and vehicle.isStarted
    else:
        return True


class _BaseSoundEvent(_EffectDesc):
    __slots__ = (b'_soundName', b'_parameters')

    def __init__(self, dataSection):
        super(_BaseSoundEvent, self).__init__(dataSection)
        self._parameters = None
        return

    def reattach(self, elem, model):
        sound = elem.get(b'sound')
        if sound is not None:
            elem[b'node'] = node = _findTargetNodeSafe(model, self._nodeName)
            sound.matrixProvider = node.actualNode
        else:
            elem[b'node'] = None
        return

    def delete(self, elem, reason):
        soundObject = elem.get(b'sound', None)
        if soundObject is not None:
            if reason != EFFECT_DELETE_REASON.LIST_DESTRUCTION:
                soundObject.stopAll()
            elem[b'sound'] = None
        if elem.has_key(b'node'):
            elem[b'node'] = None
        return True

    def prerequisites(self):
        return []

    def _isPlayer(self, args):
        if IS_EDITOR:
            return (True, None)
        else:
            entityID = None
            if args.has_key(b'entity'):
                entityID = args[b'entity'].id
                isPlayerVehicle = BigWorld.player().playerVehicleID == entityID
            else:
                isPlayerVehicle = args.get(b'isPlayerVehicle', False)
            return (isPlayerVehicle, entityID)

    def _getName(self, args):
        isPlayer, pID = self._isPlayer(args)
        return (self._soundName[0 if isPlayer else 1], pID)

    def _register(self, effects, node, sound, args=None):
        effects.append(self._makeElem(node, sound))
        return

    def _makeElem(self, node, sound):
        return {b'typeDesc': self, b'node': node, b'sound': sound}


class _ShotSoundEffectDesc(_BaseSoundEvent):
    __slots__ = ()
    TYPE = b'_ShotSoundEffectDesc'

    def __init__(self, dataSection):
        super(_ShotSoundEffectDesc, self).__init__(dataSection)
        self._soundName = ((dataSection.readString(b'wwsoundPC', b''),), (dataSection.readString(b'wwsoundNPC', b''),))
        return

    def create(self, model, effects, args):
        vehicle = args.get(b'entity', None)
        if vehicle is not None and vehicle.isAlive() and vehicle.isStarted:
            isPlayer, _ = self._isPlayer(args)
            soundName = self._soundName[0 if isPlayer else 1]
            soundObject = getGunSoundObject(vehicle)
            for sndName in soundName:
                soundObject.play(sndName)

            distance = getGunSoundObjectDistance(vehicle)
            soundObject.setRTPC(b'RTPC_ext_control_reflections_priority', distance)
        return


class _NodeSoundEffectDesc(_BaseSoundEvent):
    TYPE = b'_NodeSoundEffectDesc'
    effectUniqId = 0
    __slots__ = (b'_dopplerEffect',)

    def __init__(self, dataSection):
        super(_NodeSoundEffectDesc, self).__init__(dataSection)
        self._soundName = (dataSection.readStrings(b'wwsoundPC'), dataSection.readStrings(b'wwsoundNPC'))
        self._dopplerEffect = dataSection.readString(b'doppler', b'')
        return

    @classmethod
    def nextUniqueID(cls):
        uniqueID = cls.effectUniqId
        cls.effectUniqId += 1
        return uniqueID

    def create(self, model, effects, args):
        soundName, _ = self._getName(args)
        if soundName is None or len(soundName) < 1:
            return
        if _isVehiclePresent(args):
            node, local = _getHitPoint(model, self._nodeName, args)
            objectName = soundName[0] + str(self.nextUniqueID())
            soundObject = SoundGroups.g_instance.WWgetSoundObject(objectName, node.actualNode, local)
            if soundObject is not None:
                damage_size = _getDamageSize(args)
                if damage_size is not None:
                    soundObject.setSwitch(b'SWITCH_ext_damage_size', damage_size)
                startParams = args.get(b'soundParams', ())
                for soundStartParam in startParams:
                    soundObject.setRTPC(soundStartParam.name, soundStartParam.value)

                if self._parameters is not None:
                    for soundStartParam in self._parameters:
                        soundObject.setRTPC(soundStartParam.name, soundStartParam.value)

                if self._dopplerEffect:
                    soundObject.setDopplerEffect(self._dopplerEffect)
                for sndName in soundName:
                    if sndName:
                        soundObject.play(sndName)

                self._register(effects, node, soundObject, args=args)
                return soundObject
        else:
            return
        return


class _TracerSoundEffectDesc(_NodeSoundEffectDesc):
    __slots__ = (b'__tracerDelaySound',)
    TYPE = b'_TracerSoundEffectDesc'
    shellTypesMap = {b'AP': 0, b'HE': 1, b'HC': 2, b'APCR': 3}

    def __init__(self, dataSection):
        super(_TracerSoundEffectDesc, self).__init__(dataSection)
        shellType = dataSection.readString(b'type', b'').split()[0]
        shellType = _TracerSoundEffectDesc.shellTypesMap.get(shellType, 0)
        self._parameters = [
         SoundStartParam(b'psb_shell_type', shellType)]
        delaySoundSection = dataSection[b'tracerDelaySound']
        self.__tracerDelaySound = _TracerDelaySound(delaySoundSection) if delaySoundSection is not None else None
        return

    def _getName(self, args):
        isPlayer, id = self._isPlayer(args)
        return (self._soundName[0 if isPlayer else 1], id)

    def create(self, model, effects, args):
        _, attackerID = self._isPlayer(args)
        if not self._canCreateSoundObject(attackerID):
            return None
        else:
            return super(_TracerSoundEffectDesc, self).create(model, effects, args)

    def delete(self, elem, reason):
        state = elem.get(b'tracerDelaySoundState')
        if state is not None and self.__tracerDelaySound is not None:
            self.__tracerDelaySound.delete(state)
        if reason != EFFECT_DELETE_REASON.LIST_DESTRUCTION:
            soundObject = elem.get(b'sound', None)
            if soundObject is not None:
                if self._dopplerEffect is not None:
                    soundObject.stopDopplerEffect()
                isPlayer = elem.get(b'isPlayer', True)
                soundObject.play(b'psb_pc_stop' if isPlayer else b'psb_npc_stop')
        super(_TracerSoundEffectDesc, self).delete(elem, EFFECT_DELETE_REASON.LIST_DESTRUCTION)
        return

    def _isPlayer(self, args):
        attackerID = args.get(b'attackerID', None)
        avatar = BigWorld.player()
        if not avatar.isVehicleAlive and attackerID is not None:
            return (attackerID == BigWorld.player().playerVehicleID, attackerID)
        else:
            isPlayerVehicle, entityID = super(_TracerSoundEffectDesc, self)._isPlayer(args)
            return (isPlayerVehicle, attackerID or entityID)

    def _canCreateSoundObject(self, attackerID):
        return True

    def _register(self, effects, node, sound, args=None):
        args = args or {}
        elem = self._makeElem(node, sound)
        isPlayer, _ = self._isPlayer(args)
        elem[b'isPlayer'] = isPlayer
        if self.__tracerDelaySound is not None:
            state = self.__tracerDelaySound.create(sound, args)
            elem[b'tracerDelaySoundState'] = state
        effects.append(elem)
        return


class _AutoShootTracerSoundEffectDesc(_TracerSoundEffectDesc):
    __slots__ = ()
    TYPE = b'_AutoShootTracerSoundEffectDesc'
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _canCreateSoundObject(self, attackerID):
        if attackerID is not None and self.__sessionProvider.shared.battleSpamCtrl is not None:
            return self.__sessionProvider.shared.battleSpamCtrl.filterAutoShootTracerSound(attackerID)
        else:
            return super(_AutoShootTracerSoundEffectDesc, self)._canCreateSoundObject(attackerID)


class _CollisionSoundEffectDesc(_BaseSoundEvent):
    __slots__ = ()
    TYPE = b'_CollisionSoundEffectDesc'

    def __init__(self, dataSection):
        super(_CollisionSoundEffectDesc, self).__init__(dataSection)
        self._parameters = None
        pcSounds, npcSounds = dataSection.readString(b'wwsoundPC', b''), dataSection.readString(b'wwsoundNPC', b'')
        if pcSounds == b'' and npcSounds == b'':
            pcSounds = npcSounds = dataSection.readString(b'wwsound', b'')
        pcSounds = self.__parceNames(pcSounds)
        npcSounds = self.__parceNames(npcSounds)
        self._soundName = (
         pcSounds, npcSounds)
        return

    def __parceNames(self, events):
        if events == b'':
            return None
        else:
            events = events.split(b';')
            resultEvents = ([], [])
            lineNum = 0
            for eventLists in events:
                for evntName in eventLists.split(b','):
                    resultEvents[lineNum].append(evntName.split()[0])

                lineNum += 1

            return resultEvents

    def _getName(self, args):
        isPlayer, pID = self._isPlayer(args)
        isTracks = args.get(b'isTracks', False)
        sounds = self._soundName[0 if isPlayer else 1]
        if sounds is not None:
            return (sounds[1 if isTracks else 0], pID)
        else:
            return (
             b'', pID)

    def create(self, model, effects, args):
        soundNames, _ = self._getName(args)
        if soundNames is None or len(soundNames) < 1 or not _isVehiclePresent(args):
            return
        soundParams = args.get(b'soundParams', [])
        impulse = args.get(b'impulse', None)
        if impulse is not None:
            impulseParam = SoundStartParam(b'RTPC_ext_collision_impulse_object', impulse)
            soundParams.append(impulseParam)
        damage_size = _getDamageSize(args)
        soundSwitches = None
        if damage_size is not None:
            soundSwitches = (
             b'SWITCH_ext_damage_size', damage_size)
        node, local = _getHitPoint(model, self._nodeName, args)
        position = Math.Matrix(node.actualNode)
        position.translation += local
        for soundName in soundNames:
            WWISE.playSound(soundName, position, soundParams, (soundSwitches,))

        return


class _CollisionDamageSoundEffectDesc(_BaseSoundEvent):

    def __init__(self, dataSection):
        super(_CollisionDamageSoundEffectDesc, self).__init__(dataSection)
        self._soundName = (dataSection.readString(b'wwsoundPC'), dataSection.readString(b'wwsoundNPC'))
        return

    def create(self, model, effects, args):
        soundEvent, _ = self._getName(args)
        if not soundEvent:
            return
        damageFactor = args.get(b'damageFactor')
        if not damageFactor:
            return
        if damageFactor < 17.0:
            damageSize = b'SWITCH_ext_damage_size_small'
        elif damageFactor < 35.0:
            damageSize = b'SWITCH_ext_damage_size_medium'
        else:
            damageSize = b'SWITCH_ext_damage_size_large'
        node, _ = _getHitPoint(model, self._nodeName, args)
        position = Math.Matrix(node.actualNode)
        WWISE.playSound(soundEvent, position, [], ((b'SWITCH_ext_damage_size', damageSize),))
        return


class _DestructionSoundEffectDesc(_BaseSoundEvent):
    TYPE = b'_DestructionSoundEffectDesc'
    __slots__ = ()

    def __init__(self, dataSection):
        super(_DestructionSoundEffectDesc, self).__init__(dataSection)
        self._soundName = dataSection.readString(b'wwsound', b'')
        self.__readParameters(dataSection)
        return

    def create(self, model, list, args):
        if self._soundName == b'':
            return
        else:
            node = _findTargetNodeSafe(model, self._nodeName)
            WWISE.playSound(self._soundName, Math.Matrix(node.actualNode), self._parameters)
            return

    def __readParameters(self, dataSection):
        self._parameters = []
        section = dataSection[b'params']
        if section is None:
            return
        else:
            for param in section.items():
                name = b'RTPC_ext_objects_' + param[0].strip()
                value = param[1].asFloat
                if value > 0.0:
                    self._parameters.append(SoundStartParam(name, value))

            return


ImpactNames = namedtuple(b'ImpactNames', (b'impactNPC_PC', b'impactPC_NPC', b'impactNPC_NPC', b'impactFNPC_PC'))

class _SoundEffectDesc(_EffectDesc):
    __slots__ = (b'_soundName', b'_soundNames', b'_switch_impact_surface', b'_switch_shell_type', b'_dynamic', b'_stopSyncVisual', b'_impactNames')
    TYPE = b'_SoundEffectDesc'
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, dataSection):
        super(_SoundEffectDesc, self).__init__(dataSection)
        self._soundName = None
        self._soundNames = None
        self._switch_impact_surface = None
        self._switch_shell_type = None
        self._stopSyncVisual = False
        if dataSection.has_key(b'wwsoundPC') and dataSection.has_key(b'wwsoundNPC'):
            self._soundNames = (intern(dataSection.readString(b'wwsoundPC')), intern(dataSection.readString(b'wwsoundNPC')))
        else:
            self._soundName = intern(dataSection.readString(b'wwsound'))
        self._impactNames = ImpactNames(tuple(intern(soundName) for soundName in dataSection.readStrings(b'impactNPC_PC')), tuple(intern(soundName) for soundName in dataSection.readStrings(b'impactPC_NPC')), tuple(intern(soundName) for soundName in dataSection.readStrings(b'impactNPC_NPC')), tuple(intern(soundName) for soundName in dataSection.readStrings(b'impactFNPC_PC')))
        if dataSection.has_key(b'SWITCH_ext_impact_surface'):
            self._switch_impact_surface = intern(dataSection.readString(b'SWITCH_ext_impact_surface'))
        if dataSection.has_key(b'SWITCH_ext_shell_type'):
            self._switch_shell_type = intern(dataSection.readString(b'SWITCH_ext_shell_type'))
        if not self._soundName and not self._soundNames and not self._impactNames:
            _raiseWrongConfig(b'wwsound or wwsoundNPC/wwsoundPC or impact tags', dataSection)
        self._stopSyncVisual = dataSection.readBool(b'stopSyncVisual', False)
        return

    def reattach(self, elem, model):
        sound = elem.get(b'sound')
        if sound is not None:
            elem[b'node'] = node = _findTargetNodeSafe(model, self._nodeName)
            sound.matrixProvider = node.actualNode
        else:
            elem[b'node'] = None
        return

    def create(self, model, effects, args):
        if IS_EDITOR or not args.get(b'playSound', True):
            return
        soundName = b'EMPTY_EVENT'
        entityID = args.get(b'entity_id', None)
        playerID = BigWorld.player().playerVehicleID
        observedVehicleID = BigWorld.player().observedVehicleID
        attachedVehicle = BigWorld.player().getVehicleAttached()
        attackerID = args.get(b'attackerID')
        if entityID is not None:
            isPlayerVehicle = playerID == entityID or not BigWorld.entity(playerID).isAlive() and entityID == observedVehicleID
        else:
            isPlayerVehicle = args.get(b'isPlayerVehicle')
            if isPlayerVehicle is None:
                if args.has_key(b'entity') and hasattr(args[b'entity'], b'isPlayerVehicle'):
                    isPlayerVehicle = args[b'entity'].isPlayerVehicle
                else:
                    isPlayerVehicle = False
        if attackerID is None or attachedVehicle is None:
            fromPC = False
        else:
            fromPC = attackerID == playerID or not BigWorld.entity(playerID).isAlive() and attachedVehicle.id == attackerID
        if not fromPC:
            soundName = self._soundNames[0 if isPlayerVehicle else 1] if self._soundNames is not None else self._soundName
        if entityID is not None:
            if soundName.startswith(b'expl_') and playerID != entityID:
                soundName = self._soundNames[1] if self._soundNames is not None else self._soundName
        elem = {b'typeDesc': self}
        elem[b'node'] = node = _findTargetNodeSafe(model, self._nodeName)
        pos = Math.Matrix(node.actualNode).translation
        startParams = args.get(b'soundParams', ())
        if self._stopSyncVisual:
            objectName = soundName + b'_NODE_' + str(entityID) + b'_' + str(self._nodeName)
            elem[b'sound'] = SoundGroups.g_instance.WWgetSoundObject(objectName, node.actualNode)
            if SoundGroups.DEBUG_TRACE_EFFECTLIST is True:
                _logger.debug(b'SOUND: EffectList dynamic, %s, %s, %s, %s, %s', soundName, args, node.actualNode, self._nodeName, elem[b'sound'])
            if SoundGroups.DEBUG_TRACE_STACK is True:
                import traceback
                traceback.print_stack()
            for soundStartParam in startParams:
                elem[b'sound'].setRTPC(soundStartParam.name, soundStartParam.value)

            elem[b'sound'].play(soundName)
        elif self._switch_shell_type:
            if self._impactNames is None:
                raise SoftException(b'impact tags are invalid <%s> <%s> <%s> <%s>' % (
                 self._soundName, self._soundNames, self._switch_impact_surface, self._switch_shell_type))
            m = Math.Matrix(node.actualNode)
            hitdir = args.get(b'hitdir')
            if hitdir is not None:
                m.translation -= hitdir
            if fromPC:
                soundNames = self._impactNames.impactPC_NPC
            elif isPlayerVehicle:
                isAlly = self.__sessionProvider.getArenaDP().isAlly(attackerID)
                soundNames = self._impactNames.impactNPC_PC
                if isAlly:
                    isFriendlyFireMode = self.__sessionProvider.arenaVisitor.bonus.isFriendlyFireMode()
                    isCustomAllyDamageEffect = self.__sessionProvider.arenaVisitor.bonus.hasCustomAllyDamageEffect()
                    soundNames = None
                    if isFriendlyFireMode and isCustomAllyDamageEffect:
                        soundNames = self._impactNames.impactFNPC_PC or self._impactNames.impactNPC_PC
                if not BigWorld.entity(playerID).isAlive():
                    if self.__sessionProvider is not None:
                        spectator = self.__sessionProvider.shared.spectator
                        if spectator is not None and spectator.spectatorViewMode in (
                         EPIC_CONSTS.SPECTATOR_MODE_FREECAM, EPIC_CONSTS.SPECTATOR_MODE_FOLLOW):
                            soundNames = self._impactNames.impactNPC_NPC
            else:
                soundNames = self._impactNames.impactNPC_NPC
            if hitdir is not None:
                t = m.applyToOrigin()
                m.setRotateY(hitdir.yaw)
                m.translation = t
            sound = SoundGroups.g_instance.WWgetSoundObject(soundNames[0] if soundNames else b'_MODEL_' + str(id(model)), None, m.translation)
            if SoundGroups.DEBUG_TRACE_EFFECTLIST is True:
                _logger.debug(b'SOUND: EffectList impacts, %s, %s, %s, %s', soundNames, args, str(id(model)), sound)
            if SoundGroups.DEBUG_TRACE_STACK is True:
                import traceback
                traceback.print_stack()
            if sound is not None and soundNames is not None:
                if self._switch_impact_surface:
                    sound.setSwitch(b'SWITCH_ext_impact_surface', self._switch_impact_surface)
                sound.setSwitch(b'SWITCH_ext_shell_type', self._switch_shell_type)
                damage_size = _getDamageSize(args)
                if damage_size is not None:
                    sound.setSwitch(b'SWITCH_ext_damage_size', damage_size)
                self.__setFriendlyFireRTPC(attackerID, sound, soundNames)
                for soundName in soundNames:
                    sound.play(soundName)

                for soundStartParam in startParams:
                    sound.setRTPC(soundStartParam.name, soundStartParam.value)

        elif startParams:
            sound = SoundGroups.g_instance.WWgetSoundObject(soundName + b'_POS_' + str(id(pos)), None, pos)
            if SoundGroups.DEBUG_TRACE_EFFECTLIST is True:
                _logger.debug(b'SOUND: EffectList WWgetSoundPos, %s, %s, %s, %s', soundName, args, sound, pos)
            if SoundGroups.DEBUG_TRACE_STACK is True:
                import traceback
                traceback.print_stack()
            if sound is not None:
                sound.play(soundName)
                for soundStartParam in startParams:
                    sound.setRTPC(soundStartParam.name, soundStartParam.value)

        else:
            idd = SoundGroups.g_instance.playSoundPos(soundName, pos)
            if SoundGroups.DEBUG_TRACE_EFFECTLIST is True:
                _logger.debug(b'SOUND: EffectList playSoundPos, %s, %s, %s, %s', soundName, args, idd, pos)
            if SoundGroups.DEBUG_TRACE_STACK is True:
                import traceback
                traceback.print_stack()
            if idd == 0:
                _logger.error(b'Failed to start sound effect, event ' + soundName)
        effects.append(elem)
        return

    def delete(self, elem, reason):
        if elem.has_key(b'sound') and elem[b'sound'] is not None:
            elem[b'sound'].stopAll()
            elem[b'sound'] = None
        if elem.has_key(b'node'):
            elem[b'node'] = None
        return True

    def prerequisites(self):
        return []

    def __setFriendlyFireRTPC(self, attackerID, sound, soundNames):
        if soundNames == self._impactNames.impactFNPC_PC and attackerID is not None:
            playerVehiclePosition = BigWorld.player().getOwnVehiclePosition()
            attackerVehicle = BigWorld.entity(attackerID)
            if attackerVehicle is not None:
                distance = (playerVehiclePosition - attackerVehicle.position).length
                sound.setRTPC(b'RTPC_ext_distance_friendly_attacker', distance)
        return


class _DecalEffectDesc(_EffectDesc):
    __slots__ = (b'_texName', b'_bumpTexName', b'_smTexName', b'_groupName', b'_size', b'_randomYaw', b'_variation')
    TYPE = b'_DecalEffectDesc'

    def __init__(self, dataSection):
        _EffectDesc.__init__(self, dataSection)
        self._texName = dataSection.readString(b'texName').split()
        self._bumpTexName = dataSection.readString(b'bumpTexName').split()
        self._smTexName = dataSection.readString(b'smTexName').split()
        self._groupName = intern(dataSection.readString(b'groupName'))
        self._size = dataSection.readVector2(b'size')
        self._randomYaw = dataSection.readBool(b'randomYaw')
        self._variation = dataSection.readFloat(b'variation', 0.0)
        return

    def create(self, model, effects, args):
        if not args.get(b'showDecal', True) or not BigWorld.isDynamicDecalEnabled():
            return
        if not self._texName:
            return
        texIndex = random.randrange(len(self._texName))
        texName = intern(self._texName[texIndex])
        bumpTexName = intern(self._bumpTexName[texIndex]) if texIndex < len(self._bumpTexName) else b''
        smTexName = intern(self._smTexName[texIndex]) if texIndex < len(self._smTexName) else b''
        rayStart = args[b'start']
        rayEnd = args[b'end']
        size = self._size.scale(random.uniform(1.0 - self._variation, 1.0 + self._variation))
        size = args.get(b'size', size)
        center = 0.5 * (rayStart + rayEnd)
        extent = rayEnd - rayStart
        extent.normalise()
        extent *= size.length * 0.707
        BigWorld.wg_addDecal(self._groupName, center - extent, center + extent, size, (self._randomYaw or args)[b'yaw'] if 1 else random.uniform(0.0, 3.14), DecalMap.g_instance.getIndex(texName), DecalMap.g_instance.getIndex(bumpTexName), DecalMap.g_instance.getIndex(smTexName))
        return

    def delete(self, elem, reason):
        return True


class _ShockWaveEffectDesc(_EffectDesc):
    __slots__ = ()
    TYPE = b'_ShockWaveEffectDesc'

    def __init__(self, dataSection):
        raise SoftException(b"'shockWave' effect is obsolete, use Dynamic Cameras API instead.")
        return


class _PostProcessEffectDesc(_EffectDesc):
    __slots__ = ()
    TYPE = b'_PostProcessEffectDesc'

    def prerequisites(self):
        return []

    def create(self, model, list, args):
        return

    def delete(self, elem, reason):
        return True


class _FlashBangEffectDesc(_EffectDesc):
    __slots__ = (b'_duration', b'_keyframes', b'__fba', b'__clbackId')
    TYPE = b'_FlashBangEffectDesc'
    renderSettings = BigWorld.WGRenderSettings()
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, dataSection):
        super(_FlashBangEffectDesc, self).__init__(dataSection)
        self._duration = 0.0
        self._keyframes = list()
        self.__fba = None
        self.__clbackId = None
        for stage in dataSection[b'stages'].values():
            self._keyframes += [(self._duration, stage.readVector4(b'color', Math.Vector4(0, 0, 0, 0)))]
            self._duration += stage.asFloat

        return

    def prerequisites(self):
        return []

    def create(self, model, list, args):
        isFlashBangAllowed = True
        if not IS_EDITOR:
            inputHandler = getattr(BigWorld.player(), b'inputHandler')
            isFlashBangAllowed = bool(inputHandler is None or inputHandler.isFlashBangAllowed)
        attackerID = args.get(b'attackerID', None)
        isFlashBangAllowed = isFlashBangAllowed and self._isMarkedForPlay(args)
        if isFlashBangAllowed and attackerID is not None and self.__sessionProvider.shared.battleSpamCtrl is not None:
            isFlashBangAllowed = self.__sessionProvider.shared.battleSpamCtrl.filterFullscreenEffects(attackerID)
        if isFlashBangAllowed:
            if self.__fba is not None:
                self.renderSettings.removeFlashBangAnimation(self.__fba)
                BigWorld.cancelCallback(self.__clbackId)
                self.__clbackId = None
            self.__fba = Math.Vector4Animation()
            self.__fba.keyframes = self._keyframes
            if IS_EDITOR:
                self._duration = 0.2
            self.__fba.duration = self._duration
            self.renderSettings.flashBangAnimation(self.__fba)
            self.__clbackId = BigWorld.callback(self._duration - 0.05, self.__removeMe)
        elem = {}
        elem[b'typeDesc'] = self
        list.append(elem)
        return

    @classmethod
    def _isMarkedForPlay(cls, args):
        return args.get(b'showFlashBang', True)

    def __removeMe(self):
        if self.__fba is not None:
            self.renderSettings.removeFlashBangAnimation(self.__fba)
            self.__clbackId = None
            self.__fba = None
        return

    def delete(self, elem, reason):
        if self.__clbackId is not None:
            BigWorld.cancelCallback(self.__clbackId)
            self.__clbackId = None
        self.__removeMe()
        return True


class _FriendlyFlashBangEffectDesc(_FlashBangEffectDesc):
    TYPE = b'_FriendlyFlashBangEffectDesc'

    @classmethod
    def _isMarkedForPlay(cls, args):
        return args.get(b'showFriendlyFlashBang', False)


class _StopEmissionEffectDesc(_EffectDesc):
    __slots__ = ()
    TYPE = b'_StopEmissionEffectDesc'

    def create(self, model, effects, args):
        for elem in effects:
            pixie = elem.get(b'pixie')
            if pixie is not None:
                pixie.stopEmission()

        return


class _LightEffectDesc(_EffectDesc):
    __slots__ = (b'_innerRadius', b'_outerRadius', b'_castShadows', b'_color', b'_alwaysUpdate', b'_colorAnimation', b'_multiplierAnimation', b'_offset')
    TYPE = b'_LightEffectDesc'

    def __init__(self, dataSection):
        super(_LightEffectDesc, self).__init__(dataSection)
        self._innerRadius = dataSection.readFloat(b'innerRadius', 1)
        self._outerRadius = dataSection.readFloat(b'outerRadius', 2)
        self._castShadows = dataSection.readBool(b'castShadows', False)
        self._color = dataSection.readVector4(b'color', Math.Vector4(1, 1, 1, 1))
        self._offset = dataSection.readVector3(b'offset', Math.Vector3(0, 0, 0))
        self._alwaysUpdate = dataSection.readBool(b'alwaysUpdateModel', True)
        self._colorAnimation = []
        self._multiplierAnimation = []
        for ds in dataSection.values():
            if ds.name == b'animation':
                t = ds.readFloat(b'time')
                color = ds.readVector3(b'color')
                multiplier = ds.readFloat(b'multiplier')
                self._colorAnimation.append((t, Math.Vector4(color[0], color[1], color[2], 1.0)))
                self._multiplierAnimation.append((t, Math.Vector4(multiplier)))

        return

    def reattach(self, elem, model):
        if not _ALLOW_DYNAMIC_LIGHTS:
            return
        else:
            if elem[b'isDynCollision']:
                self.delete(elem, EFFECT_DELETE_REASON.FORCE_DELETE)
                return
            nodePos = self._nodeName
            if elem[b'newPos'] is not None:
                nodePos = string.split(elem[b'newPos'][0], b'/') if elem[b'newPos'][0] else []
            node = _findTargetNode(model, nodePos)
            elem[b'source'] = node.actualNode
            if elem[b'light'] is not None:
                elem[b'light'].source = elem[b'source']
            return

    def create(self, model, effects, args):
        if not _ALLOW_DYNAMIC_LIGHTS:
            return
        else:
            elem = dict()
            elem[b'isDynCollision'] = args.get(b'isDynCollision', False)
            if elem[b'isDynCollision']:
                componentIdx = args.get(b'componentIdx')
                entity_id = args.get(b'entity_id')
                if componentIdx is None or entity_id is None:
                    return
                provider = _getDynCollisionTransformProvider(entity_id, componentIdx)
                if not provider:
                    return
                elem[b'source'] = provider
            else:
                elem[b'newPos'] = args.get(b'position', None)
                nodePos = self._nodeName
                if elem[b'newPos'] is not None:
                    nodePos = string.split(elem[b'newPos'][0], b'/') if elem[b'newPos'][0] else []
                node = _findTargetNode(model, nodePos)
                elem[b'source'] = node.actualNode
            elem[b'typeDesc'] = self
            elem[b'light'] = None
            if not IS_EDITOR:
                elem[b'callback'] = BigWorld.callback(0.01, partial(self._callbackCreate, elem))
            effects.append(elem)
            return

    def _callbackCreate(self, elem):
        light = BigWorld.PyOmniLight()
        colorKeyFrames = []
        multiplierKeyFrames = []
        for c in self._colorAnimation:
            colorKeyFrames.append((c[0] * self.duration, c[1]))

        for m in self._multiplierAnimation:
            multiplierKeyFrames.append((m[0] * self.duration, m[1]))

        colorAnimator = Math.Vector4Animation()
        colorAnimator.duration = 10000000.0
        colorAnimator.keyframes = colorKeyFrames
        multiplierAnimator = Math.Vector4Animation()
        multiplierAnimator.duration = 10000000.0
        multiplierAnimator.keyframes = multiplierKeyFrames
        light.innerRadius = self._innerRadius
        light.outerRadius = self._outerRadius
        light.castShadows = self._castShadows
        light.offset = self._offset
        light.source = elem[b'source']
        light.colorAnimator = colorAnimator
        light.multiplierAnimator = multiplierAnimator
        elem[b'light'] = light
        elem[b'callback'] = None
        return

    def delete(self, elem, reason):
        if not _ALLOW_DYNAMIC_LIGHTS:
            return True
        else:
            if not IS_EDITOR:
                callback = elem[b'callback']
                if callback is not None:
                    BigWorld.cancelCallback(callback)
                    elem[b'callback'] = None
            if elem[b'light'] is not None:
                elem[b'light'].destroyLight()
                elem[b'light'] = None
            return True


class _TracerDelaySound(object):
    __slots__ = (b'_soundName', b'__soundDelayBeforeEnd')
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, dataSection):
        self._soundName = (
         dataSection.readString(b'wwsoundEnemy', b''),
         dataSection.readString(b'wwsoundAlly', b''))
        self.__soundDelayBeforeEnd = dataSection.readFloat(b'delayBeforeEnd', 0.0)
        return

    def create(self, soundObject, args):
        collisionTime = args.get(b'collisionTime', None)
        entityID = args.get(b'attackerID', -1)
        if entityID > 0 and self.__needPlay(collisionTime, entityID):
            state = _TracerDelaySoundState(soundObject=soundObject)
            state.soundCallback = BigWorld.callback(collisionTime - self.__soundDelayBeforeEnd, (lambda : self.__playSound(state, self.__getSoundName(entityID))))
            return state
        else:
            return

    def delete(self, state):
        if state.soundCallback is not None:
            BigWorld.cancelCallback(state.soundCallback)
            state.soundCallback = None
        state.soundObject = None
        return

    def __needPlay(self, collisionTime, entityID):
        return collisionTime is not None and collisionTime > self.__soundDelayBeforeEnd and self.__getSoundName(entityID)

    def __playSound(self, state, soundName):
        if SoundGroups.DEBUG_TRACE_EFFECTLIST:
            _logger.debug(b'SOUND: EffectList _TracerDelaySoundEffectDesc, name=%s', soundName)
        if state.soundObject is not None:
            state.soundObject.play(soundName)
        state.soundCallback = None
        return

    def __getSoundName(self, entityID):
        if self.__sessionProvider.getArenaDP().isAlly(entityID):
            return self._soundName[1]
        return self._soundName[0]


class _TracerDelaySoundState(object):
    __slots__ = (b'soundObject', b'soundCallback')

    def __init__(self, soundObject=None, soundCallback=None):
        self.soundObject = soundObject
        self.soundCallback = soundCallback
        return


_effectDescFactory = {b'pixie': _PixieEffectDesc, 
   b'animation': _AnimationEffectDesc, 
   b'sound': _SoundEffectDesc, 
   b'splashSound': _NodeSoundEffectDesc, 
   b'collisionSound': _CollisionSoundEffectDesc, 
   b'collisionDamageSound': _CollisionDamageSoundEffectDesc, 
   b'tracerSound': _TracerSoundEffectDesc, 
   b'shotSound': _ShotSoundEffectDesc, 
   b'visibility': _VisibilityEffectDesc, 
   b'model': _ModelEffectDesc, 
   b'decal': _DecalEffectDesc, 
   b'shockWave': _ShockWaveEffectDesc, 
   b'flashBang': _FlashBangEffectDesc, 
   b'friendlyFlashBang': _FriendlyFlashBangEffectDesc, 
   b'stopEmission': _StopEmissionEffectDesc, 
   b'posteffect': _PostProcessEffectDesc, 
   b'light': _LightEffectDesc, 
   b'destructionSound': _DestructionSoundEffectDesc, 
   b'lifetimeSound': _DestructionSoundEffectDesc, 
   b'autoShootTracerSound': _AutoShootTracerSoundEffectDesc}

def _createEffectDesc(eType, dataSection):
    if not dataSection.values():
        return
    else:
        factoryMethod = _effectDescFactory.get(eType)
        if factoryMethod is not None:
            return factoryMethod(dataSection)
        raise SoftException(b'EffectsList factory has no class associated with type %s.' % eType)
        return


def _raiseWrongConfig(paramName, effectType):
    raise SoftException(b'missing or wrong parameter <%s> in effect descriptor <%s>.' % (paramName, effectType))
    return


def __getTransformAlongNormal(localTransform, worldTransform, normal):
    originalTranslation = Math.Vector3(0, 0, 0) if localTransform is None else localTransform.translation
    localTransform = Math.Matrix()
    localTransform.setRotateYPR((normal.yaw, normal.pitch + 1.57,
     0))
    invWorldOrient = Math.Matrix(worldTransform)
    invWorldOrient.translation = Math.Vector3(0, 0, 0)
    invWorldOrient.invert()
    localTransform.postMultiply(invWorldOrient)
    localTransform.translation = originalTranslation
    return localTransform


def _getDynCollisionTransformProvider(entityID, componentIDx):
    vehicle = BigWorld.entity(entityID)
    if not vehicle:
        return
    else:
        go = vehicle.appearance.collisions.getPartGameObject(componentIDx)
        if go.valid:
            return vehicle.appearance.collisions.getPartTransformProvider(componentIDx)
        return


def _getSurfaceAlignedTransform(model, nodeName, localTransform, precalculatedNormal=None):
    node = model.node(nodeName)
    if node is None:
        worldTransform = Math.Matrix(model.root)
    else:
        worldTransform = Math.Matrix(node)
    if precalculatedNormal is not None:
        return __getTransformAlongNormal(localTransform, worldTransform, precalculatedNormal)
    else:
        if localTransform is not None:
            worldTransform.preMultiply(localTransform)
        pos = worldTransform.applyToOrigin()
        normal = worldTransform.applyVector((0, 0, 1))
        offsets = (
         Math.Vector3(0, -0.1, 0), Math.Vector3(-0.1, 0, 0), Math.Vector3(0.1, 0, 0),
         Math.Vector3(0, 0, -0.1), Math.Vector3(0, 0, 0.1))
        spaceID = BigWorld.player().spaceID
        for offset in offsets:
            res = BigWorld.wg_collideSegment(spaceID, pos, pos + offset, 128)
            if res is None:
                continue
            normal = res.normal
            localTransform = __getTransformAlongNormal(localTransform, worldTransform, normal)
            break

        return localTransform


class _NodeWithLocal(object):
    actualNode = property((lambda self: self.__node))

    def __init__(self, model, nodeName=b'', local=None):
        if local is None:
            local = Math.Matrix()
            local.setIdentity()
        if _isPyModel(model):
            allAttachmentsChecked = success = False
            attachmentsChecked = 0
            while not allAttachmentsChecked and not success:
                try:
                    if attachmentsChecked > 0:
                        self.__node = model.root.attachments[attachmentsChecked - 1].node(nodeName, local)
                        success = True
                    else:
                        self.__node = model.node(nodeName, local)
                        success = True
                except Exception:
                    attachmentsChecked += 1
                    allAttachmentsChecked = True if not hasattr(model.root, b'attachments') else 1 + len(model.root.attachments) - attachmentsChecked < 1
                    self.__node = model.node(b'', local)

            self.__localMatrix = None
        else:
            if nodeName in (b'', b'Scene Root'):
                self.__node = model.root
            else:
                self.__node = model.node(nodeName)
            if self.__node is None:
                self.__node = model.root
            self.__localMatrix = local
        return

    def attach(self, attachment):
        if self.__localMatrix is None:
            self.__node.attach(attachment)
            return
        else:
            self.__node.attach(attachment, self.__localMatrix)
            return

    def __getattr__(self, item):
        return getattr(self.__node, item)


def _findTargetNode(model, nodes, localTransform=None, orientByClosestSurfaceNormal=False, precalculatedNormal=None):
    if len(nodes) > 1:
        _logger.debug(b'Slashed nodepath is not supported any longer')
    if not nodes:
        if orientByClosestSurfaceNormal:
            localTransform = _getSurfaceAlignedTransform(model, b'', localTransform, precalculatedNormal)
        return _NodeWithLocal(model, b'', localTransform)
    if orientByClosestSurfaceNormal:
        localTransform = _getSurfaceAlignedTransform(model, nodes[-1], localTransform, precalculatedNormal)
    return _NodeWithLocal(model, nodes[-1], localTransform)


def _findTargetNodeSafe(model, nodes, local=None):
    node = None
    if nodes:
        node = _findTargetNode(model, nodes, local)
    if node is None:
        node = _NodeWithLocal(model, b'', local)
    return node


def _findTargetModel(model, nodes):
    _logger.debug(b'THIS FEATURE IS NOT SUPPORTED')
    targetNode = model
    for iter in xrange(0, len(nodes)):
        found = False
        for elem in targetNode.node(nodes[iter]).attachments:
            if isinstance(elem, BigWorld.Model):
                targetNode = elem
                found = True
                break

        if not found:
            raise SoftException(b"can't find model attachments in %s" % nodes[iter])

    return targetNode


def _getHitPoint(model, nodeName, args):
    nodeDesc = args.get(b'position', None)
    nodeLocalPos = None
    if nodeDesc is not None:
        nodeName = string.split(nodeDesc[0], b'/') if nodeDesc[0] else []
        nodeLocalPos = nodeDesc[1]
    node = _findTargetNode(model, nodeName, nodeLocalPos)
    hitPoint = args.get(b'hitPoint', None)
    if hitPoint is None:
        if nodeLocalPos is not None:
            local = nodeLocalPos.translation
        else:
            local = (0.0, 0.0, 0.0)
    else:
        local = hitPoint - node.actualNode.position
    return (node, local)


def __keyPointsFromStagesSection(stagesSection):
    keyPoints = []
    stagesNames = set()
    totalTime = 0.0
    for stageName in stagesSection.keys():
        if stageName in stagesNames:
            return stageName
        duration = stagesSection.readFloat(stageName)
        stagesNames.add(stageName)
        keyPoints.append(KeyPoint(stageName, totalTime))
        totalTime += duration

    if keyPoints and keyPoints[0].name != __START_KEY_POINT.name:
        keyPoints.insert(0, __START_KEY_POINT)
    keyPoints.append(KeyPoint(SpecialKeyPointNames.END, totalTime))
    return keyPoints


def __keyPointsFromTimeLineSection(keyPointSection):
    keyPoints = []
    keyPointNames = set()
    for keyPointName in keyPointSection.keys():
        if keyPointName in keyPointNames:
            return keyPointName
        timePoint = keyPointSection.readFloat(keyPointName)
        keyPointNames.add(keyPointName)
        keyPoints.append(KeyPoint(keyPointName, timePoint))

    keyPoints.sort(key=(lambda self: self.time))
    if keyPoints and keyPoints[0].name != __START_KEY_POINT.name:
        keyPoints.insert(0, __START_KEY_POINT)
    return keyPoints


def effectsFromSection(section):
    keyPoints = None
    stagesSection = section[b'stages']
    if stagesSection is not None:
        keyPoints = __keyPointsFromStagesSection(stagesSection)
    timeLineSection = section[b'timeline']
    if timeLineSection is not None:
        if keyPoints is None:
            keyPoints = __keyPointsFromTimeLineSection(timeLineSection)
        else:
            raise SoftException(b'Both stages and timeline defined in effect %s' % section.name)
    if keyPoints is None:
        raise SoftException(b'Neither stages nor timeline defined in effect %s' % section.name)
    if isinstance(keyPoints, str):
        raise SoftException(b'Duplicate keypoint %s in effect %s' % (keyPoints, section.name))
    effectsSec = section[b'effects']
    effectList = EffectsList(effectsSec)
    if section[b'relatedEffects'] is not None:
        for tagName, subSection in section[b'relatedEffects'].items():
            effectList.relatedEffects[tagName] = effectsFromSection(subSection)

    return EffectsTimeLine(keyPoints, effectList)


class RespawnDestroyEffect(object):

    @classmethod
    def play(cls, vehicle_id):
        vehicle = BigWorld.entity(vehicle_id)
        if vehicle is None:
            return
        else:
            effects = vehicle.typeDescriptor.type.effects[b'fullDestruction']
            if not effects:
                return
            turret = None
            from DetachedTurret import DetachedTurret
            for vehTurret in DetachedTurret.allTurrets:
                if vehTurret.vehicleID == vehicle_id:
                    turret = vehTurret
                    break

            vehicle.show(False)
            cls.__playDestroyEffect(vehicle, effects)
            if turret:
                turret.changeAppearanceVisibility(False)
                cls.__playDestroyEffect(turret, effects)
                turret.stopDetachmentEffects()
            return

    @classmethod
    def __playDestroyEffect(cls, entity, effects):
        if entity.model is not None:
            fakeModel = helpers.newFakeModel()
            BigWorld.player().addModel(fakeModel)
            fakeModel.position = entity.model.position
            effectsPlayer = EffectsListPlayer(effects[0][1], effects[0][0])
            effectsPlayer.play(fakeModel, SpecialKeyPointNames.START, partial(BigWorld.player().delModel, fakeModel))
        return
