from __future__ import absolute_import
import logging
from functools import partial
import BigWorld, CGF, Math
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent
from cgf_components_common.material_component import MaterialComponent
from cgf_components.on_shot_components import EffectOnShotComponent, SoundOnShotComponent
from cgf_script.registration import registerReplicableComponent
from Event import Event
from material_kinds import EFFECT_MATERIAL_INDEXES_BY_IDS, EFFECT_MATERIAL_INDEXES_BY_NAMES
_logger = logging.getLogger(__name__)
_DIR_UP = Math.Vector3(0.0, 1.0, 0.0)

@registerReplicableComponent
class ShotsReceiver(ReplicableDynamicScriptComponent):
    editorTitle = b'Shots Receiver'

    def __init__(self):
        super(ShotsReceiver, self).__init__()
        self.onShot = Event()
        return

    def receiveShot(self, hitPoint, hitDir, speed, normal, shotID, effectIndex, prefabEffectIndex, shellType, shellCaliber, matKind, damagedDestructibles):
        self.onShot(hitPoint, hitDir, speed, normal, shotID, effectIndex, prefabEffectIndex, shellType, shellCaliber, matKind, damagedDestructibles)
        return


class ShotReceiverSystem(CGF.System):
    ShotActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(ShotsReceiver))
    ShotDeactivated = CGF.DeactivateReaction(CGF.ReactRw(ShotsReceiver))
    EffectAccess = CGF.AccessReaction(CGF.Has(ShotsReceiver), EffectOnShotComponent, CGF.TransformComponent)
    SoundAccess = CGF.AccessReaction(CGF.Has(ShotsReceiver), SoundOnShotComponent, CGF.TransformComponent)
    ExplosionAccess = CGF.AccessReaction(CGF.Has(ShotsReceiver), CGF.No(EffectOnShotComponent))
    MaterialAccess = CGF.AccessReaction(CGF.Rw(MaterialComponent))
    Reactions = CGF.Reactions(ShotActivated, ShotDeactivated, EffectAccess, SoundAccess, ExplosionAccess, MaterialAccess)

    def update(self):
        for receiver in self.reaction(self.ShotDeactivated):
            receiver.onShot -= self.__onShot

        for go, receiver in self.reaction(self.ShotActivated):
            receiver.onShot += partial(self.__onShot, go)

        return

    def __onShot(self, go, hitPoint, hitDir, speed, normal, shotID, effectIndex, prefabEffectIndex, shellType, shellCaliber, matKind, damagedDestructibles):
        effectAccess = self.reaction(self.EffectAccess)
        soundAccess = self.reaction(self.SoundAccess)
        explosionAccess = self.reaction(self.ExplosionAccess)
        normal.normalise()
        shot = {b'hitPoint': hitPoint, 
           b'hitDir': hitDir, 
           b'speed': speed, 
           b'normal': normal, 
           b'shotID': (int(shotID)), 
           b'effectIndex': (int(effectIndex)), 
           b'prefabEffectIndex': (int(prefabEffectIndex)), 
           b'shellType': (int(shellType)), 
           b'caliber': (float(shellCaliber)), 
           b'matKind': (int(matKind)), 
           b'damagedDestructibles': damagedDestructibles}
        effect, tr = effectAccess.find(go)
        sound, tr = soundAccess.find(go)
        if effect and tr:
            self.__processEffect(go, shot, effect.effectPath, tr)
        if sound and tr:
            self.__processSound(go, shot, sound.soundPath, tr)
        if explosionAccess.contains(go):
            self.__processExplosion(go, shot)
        return

    def __processExplosion(self, gameObject, shot):
        materialIdx = 0
        materialAccess = self.reaction(self.MaterialAccess)
        if EFFECT_MATERIAL_INDEXES_BY_IDS.has_key(shot[b'matKind']):
            materialIdx = EFFECT_MATERIAL_INDEXES_BY_IDS[shot[b'matKind']]
        else:
            material = materialAccess.find(gameObject)
            if material:
                materialIdx = EFFECT_MATERIAL_INDEXES_BY_NAMES[material.kind]
        BigWorld.player().explodeProjectile(shot[b'shotID'], shot[b'effectIndex'], shot[b'prefabEffectIndex'], materialIdx, shot[b'shellType'], shot[b'caliber'], shot[b'hitPoint'], shot[b'hitDir'], shot[b'speed'], shot[b'damagedDestructibles'])
        return

    def __processEffect(self, gameObject, shot, effectPath, transform):
        position, normal = shot[b'hitPoint'], shot[b'normal']
        localTransform = transform.worldTransform
        localTransform.invert()
        localPosition = localTransform.applyPoint(position)
        localNormal = localTransform.applyVector(normal)
        localNormal.normalise()
        shotEffectTransform = Math.createVectorRotationMatrix(_DIR_UP, localNormal)
        shotEffectTransform.translation = localPosition
        CGF.loadAndCreatePrefabWithParent(effectPath, gameObject, shotEffectTransform)
        return

    def __processSound(self, gameObject, shot, soundPath, transform):
        position = shot[b'hitPoint']
        localTransform = transform.worldTransform
        localTransform.invert()
        localPosition = localTransform.applyPoint(position)
        CGF.loadAndCreatePrefabWithParent(soundPath, gameObject, localPosition)
        return
