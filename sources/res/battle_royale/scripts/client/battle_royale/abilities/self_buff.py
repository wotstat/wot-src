from __future__ import absolute_import
import BigWorld, CGF
from typing import List
from cgf_script.registration import ComponentProperty, registerComponent
from constants import IS_CLIENT
from helpers import dependency
import GenericComponents
from items import vehicles
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicle_systems.model_assembler import loadAppearancePrefab
from battle_royale.abilities.common import getEffectSuffixForGunLength
if IS_CLIENT:
    from VehicleSelfBuffComponent import VehicleSelfBuffComponent
    from InBattleUpgrades import UpgradeInProgressComponent
else:

    class VehicleSelfBuffComponent(object):
        pass


    class UpgradeInProgressComponent(object):
        pass


_GUN_LENGTH_RANGES = {b'short': (0.0, 2.0), 
   b'med': (2.0, 4.0), 
   b'med_02': (4.0, 5.0), 
   b'long': (
           5.0, float(b'inf'))}

@registerComponent
class SelfBuffComponent(object):
    editorTitle = b'Self Buff Component'
    group = b'Abilities'
    domain = CGF.Domain.Client
    gunNode = ComponentProperty(type=CGF.PropertyType.Link, value=CGF.GameObject, editorName=b'Gun Node')


@registerComponent
class SelfBuffNodeComponent(object):
    editorTitle = b'Self Buff Node Component'
    group = b'Abilities'
    domain = CGF.Domain.Client
    effectPathTemplate = ComponentProperty(type=CGF.PropertyType.String, value=b'', editorName=b'Effect Path Template')


class SelfBuffSystem(CGF.System):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    VehicleSelfBuffActivated = CGF.ActivateReaction(CGF.ReactRw(VehicleSelfBuffComponent))
    UpgradeDeactivated = CGF.DeactivateReaction(CGF.ReactRo(UpgradeInProgressComponent), CGF.Rw(VehicleSelfBuffComponent))
    SelfBuffNodeAccess = CGF.AccessReaction(CGF.Rw(SelfBuffNodeComponent))
    Reactions = CGF.Reactions(VehicleSelfBuffActivated, UpgradeDeactivated, SelfBuffNodeAccess)

    def update(self):
        for _, vehicleSelfBuffComponent in self.reaction(self.UpgradeDeactivated):
            self.inBattleUpgradeCompleted(vehicleSelfBuffComponent)

        for vehicleSelfBuffComponent in self.reaction(self.VehicleSelfBuffActivated):
            self.visualizeSelfBuff(vehicleSelfBuffComponent)

        return

    def visualizeSelfBuff(self, vehicleSelfBuffComponent):
        self.__launch(vehicleSelfBuffComponent)
        return

    def __launch(self, vehicleSelfBuffComponent):
        vehicle = vehicleSelfBuffComponent.entity
        if vehicle.isDestroyed:
            return
        appearance = vehicle.appearance
        finishTime = vehicleSelfBuffComponent.finishTime

        def postloadSetup(root, _, queue):
            selfBuffComponent = queue.component(root, SelfBuffComponent)
            node = queue.pendingGameObject(selfBuffComponent.gunNode)
            self.__setupVFX(node, appearance, queue)
            queue.createComponent(root, GenericComponents.RemoveGoDelayedComponent, finishTime - BigWorld.serverTime())
            return

        equipmentID = vehicles.g_cache.equipmentIDs().get(VehicleSelfBuffComponent.EQUIPMENT_NAME)
        equipment = vehicles.g_cache.equipments()[equipmentID]
        loadAppearancePrefab(equipment.usagePrefab, appearance, postloadSetup, False)
        return

    def __setupVFX(self, nodeGO, appearance, queue):
        nodeComponent = queue.component(nodeGO, SelfBuffNodeComponent)
        effectName = getEffectSuffixForGunLength(_GUN_LENGTH_RANGES, appearance)
        if queue.hasComponent(nodeGO, GenericComponents.AnimatorComponent):
            queue.removeComponent(nodeGO, GenericComponents.AnimatorComponent)
        queue.createComponent(nodeGO, GenericComponents.AnimatorComponent, nodeComponent.effectPathTemplate.format(effectName), 0, 1, -1, True, b'')
        return

    def inBattleUpgradeCompleted(self, vehicleSelfBuffComponent):
        self.__launch(vehicleSelfBuffComponent)
        return
