import enum, BigWorld, AnimationSequence
from script_component.DynamicScriptComponent import DynamicScriptComponent
from items import vehicles
from vehicle_systems.stricted_loading import makeCallbackWeak
from helpers import newFakeModel

class SequenceEffect(object):
    __slots__ = (b'__isActive', b'__isPlaying', b'__animator', b'__bindNode', b'__spaceID', b'__model', b'__owner', b'__config', b'__timeToFinish', b'__loadingTaskID', b'__unapplyCbkID', b'__sequencePath', b'__weakref__')

    def __init__(self, entity, data):
        self.__isActive = False
        self.__isPlaying = False
        self.__animator = None
        self.__bindNode = None
        self.__spaceID = None
        self.__model = None
        self.__owner = entity
        self.__config = data
        self.__timeToFinish = 0
        self.__loadingTaskID = None
        self.__unapplyCbkID = None
        self.__sequencePath = self.__config[b'path']
        return

    def apply(self, startTime):
        if self.__config[b'duration'] > 0:
            finishTime = startTime + self.__config[b'duration']
            self.__timeToFinish = finishTime - BigWorld.serverTime()
            if self.__timeToFinish <= 0:
                return
        if self.__isPlaying:
            self.__restart()
            return
        self.__isActive = True
        self.__applyVisualEffects()
        return

    def unapply(self):
        self.__unapplyVisualEffects()
        if self.__unapplyCbkID is not None:
            BigWorld.cancelCallback(self.__unapplyCbkID)
            self.__unapplyCbkID = None
        self.__isActive = False
        self.__timeToFinish = 0
        return

    def destroy(self):
        self.__owner = None
        self.__config = None
        self.__model = None
        self.__animator = None
        self.__bindNode = None
        return

    def __applyVisualEffects(self):
        if self.__isPlaying:
            return
        self.__cancelLoadingTask()
        self.__spaceID = BigWorld.player().spaceID
        loader = AnimationSequence.Loader(self.__sequencePath, self.__spaceID)
        self.__loadingTaskID = BigWorld.loadResourceListBG((loader,), makeCallbackWeak(self.__onLoaded))
        return

    def __onLoaded(self, resourceRefs):
        self.__loadingTaskID = None
        if self.__sequencePath not in resourceRefs.failedIDs and self.__sequencePath in resourceRefs.keys() and resourceRefs[self.__sequencePath] is not None:
            self.__animator = resourceRefs[self.__sequencePath]
            self.__animator.loopCount = self.__config[b'loopCount']
        if self.__isActive and self.__owner.model and self.__animator is not None:
            self.__attachModel()
        return

    def __cancelLoadingTask(self):
        if self.__loadingTaskID is None:
            return
        else:
            BigWorld.stopLoadResourceListBGTask(self.__loadingTaskID)
            self.__loadingTaskID = None
            return

    def __attachModel(self):
        self.__model = newFakeModel()
        canStart = False
        nodeName = self.__config[b'bindNode']
        if nodeName == b'HP_gunFire':
            multiGun = self.__owner.typeDescriptor.turret.multiGun
            gunIndex = self.__owner.activeGunIndex
            isDualGun = self.__owner.typeDescriptor.isDualgunVehicle
            nodeName = multiGun[gunIndex].gunFire if isDualGun and multiGun and gunIndex is not None else b'HP_gunFire'
        self.__bindNode = self.__owner.model.node(nodeName)
        if self.__bindNode is not None:
            self.__bindNode.attach(self.__model)
            canStart = True
        if canStart:
            self.__animator.bindTo(AnimationSequence.ModelWrapperContainer(self.__model, self.__spaceID))
            self.__animator.start()
            self.__isPlaying = True
            if self.__timeToFinish > 0:
                self.__unapplyCbkID = BigWorld.callback(self.__timeToFinish, self.unapply)
        return

    def __unapplyVisualEffects(self):
        if not self.__isPlaying:
            return
        self.__cancelLoadingTask()
        self.__detachModel()
        return

    def __detachModel(self):
        if self.__animator is not None and self.__isActive:
            self.__animator.stop()
            self.__animator = None
            self.__isPlaying = False
        if self.__bindNode is not None and not self.__bindNode.isDangling:
            self.__bindNode.detach(self.__model)
        self.__model = None
        self.__bindNode = None
        self.__spaceID = None
        return

    def __restart(self):
        if self.__unapplyCbkID is not None:
            BigWorld.cancelCallback(self.__unapplyCbkID)
            self.__unapplyCbkID = None
        self.__attachModel()
        return


class WTVisualEffect(DynamicScriptComponent):
    __slots__ = (b'__sequences',)

    class OwnerType(enum.IntEnum):
        NONE = -1
        SELF = 0
        TEAM_MATE = 1
        ENEMY = 2

    def __init__(self):
        super(WTVisualEffect, self).__init__()
        self.__sequences = None
        self.__activate(self.startTime)
        return

    def onDestroy(self):
        self.__stopSequence()
        self.__destroySequence()
        super(WTVisualEffect, self).onDestroy()
        return

    def _onAvatarReady(self):
        self.__activate(self.startTime)
        return

    def __stopSequence(self):
        if self.__sequences is None:
            return
        else:
            for sequenceID in self.__sequences:
                self.__sequences[sequenceID].unapply()

            return

    def __destroySequence(self):
        if self.__sequences is None:
            return
        else:
            for sequenceID in self.__sequences:
                self.__sequences[sequenceID].destroy()

            self.__sequences = None
            return

    def set_equipmentID(self, prev):
        if self.equipmentID > 0:
            self.__activate(self.startTime)
        else:
            self.__stopSequence()
        return

    def __activate(self, startTime):
        if self.entity.isDestroyed or self.equipmentID <= 0 or self.ownerType == self.OwnerType.NONE:
            return
        self.__initSequncesData()
        self.__startSequences(startTime)
        return

    def __initSequncesData(self):
        if self.__sequences is None:
            self.__sequences = self.__getSequences(self.ownerType)
        return

    def __getEffectData(self):
        equipment = vehicles.g_cache.equipments()[self.equipmentID]
        return equipment.effects

    def __getSequences(self, ownerType):
        sequences = self.__getEffectData().get(b'sequences')
        if sequences is not None:
            key = self.__ownerTypeToStr(ownerType)
            sequence = sequences.get(key)
            if sequence:
                return {seqID: SequenceEffect(self.entity, sequence[seqID]) for seqID in sequence.keys()}
        return

    def __startSequences(self, startTime):
        if self.__sequences:
            self.__sequences[self.sequenceID].apply(startTime)
        return

    def __ownerTypeToStr(self, ownerType):
        if ownerType == self.OwnerType.SELF:
            return b'owner'
        if ownerType == self.OwnerType.TEAM_MATE:
            return b'teamMate'
        if ownerType == self.OwnerType.ENEMY:
            return b'enemy'
        return b''
