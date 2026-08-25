from __future__ import absolute_import
import math, logging, BigWorld, GenericComponents, Triggers, CGF, math_utils, Math
from cgf_script.registration import ComponentProperty, registerComponent
from cgf_demo.demo_category import DEMO_CATEGORY
from helpers import isPlayerAccount
_logger = logging.getLogger(__name__)

@registerComponent
class TestMaterialParamManipulator(object):
    group = DEMO_CATEGORY
    editorTitle = b'Test Material Param Manipulator'
    domain = CGF.Domain.Client
    model = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'model', value=GenericComponents.DynamicModelComponent)
    paramName = ComponentProperty(type=CGF.PropertyType.String, editorName=b'paramName', value=b'g_tintColor')


class TestMaterialManipulatorSystem(CGF.System):
    ManipulatorIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(TestMaterialParamManipulator))
    ModelAccess = CGF.AccessReaction(CGF.Rw(GenericComponents.DynamicModelComponent))
    Reactions = CGF.Reactions(ManipulatorIterate, ModelAccess)

    def update(self):
        modelAccess = self.reaction(self.ModelAccess)
        for manipulator in self.reaction(self.ManipulatorIterate):
            model = modelAccess.find(manipulator.model)
            model.setMaterialParameterVector4(manipulator.paramName, Math.Vector4(0, math.sin(self.clock.gameTime), 1, 0))

        return


@registerComponent
class HierarchyModifier(object):
    group = DEMO_CATEGORY
    editorTitle = b'Hierarchy Modifier'
    domain = CGF.Domain.Client
    gameObject1 = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Game Object 1', value=b'GameObject1')
    gameObject2 = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Game Object 2', value=b'GameObject2')
    gameObject3 = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Game Object 3', value=b'GameObject3')
    areaTrigger1 = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Area Trigger1', value=Triggers.AreaTriggerComponent)
    areaTrigger2 = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Area Trigger2', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        super(HierarchyModifier, self).__init__()
        self.zone1 = False
        self.zone2 = False
        return


@registerComponent
class HierarchyModifier2(object):
    group = DEMO_CATEGORY
    editorTitle = b'Hierarchy Modifier 2'
    domain = CGF.Domain.Client
    top = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Top Object', value=CGF.GameObject)
    bottom = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Bottom Object', value=CGF.GameObject)
    box = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Box Object', value=CGF.GameObject)
    cameraTransform = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Camera Transform', value=CGF.TransformComponent)
    areaTrigger = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Area Trigger', value=Triggers.AreaTriggerComponent)


class TestHierarchyModifierSystem(CGF.System):
    ModifierCreated = CGF.CreateReaction(CGF.ReactRw(HierarchyModifier))
    ModifierActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(HierarchyModifier))
    Modifier2Activated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(HierarchyModifier2))
    Modifier2Iterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(HierarchyModifier2))
    TransformAccess = CGF.AccessReaction(CGF.Rw(CGF.TransformComponent))
    AreaTriggerAccess = CGF.AccessReaction(CGF.Rw(Triggers.AreaTriggerComponent))
    HierarchyAccess = CGF.AccessReaction(CGF.Rw(CGF.HierarchyComponent))
    ModifierAccess = CGF.AccessReaction(CGF.Rw(HierarchyModifier))
    Modifier2Access = CGF.AccessReaction(CGF.Rw(HierarchyModifier2))
    Reactions = CGF.Reactions(ModifierCreated, ModifierActivated, Modifier2Activated, Modifier2Iterate, TransformAccess, AreaTriggerAccess, HierarchyAccess, ModifierAccess, Modifier2Access)

    def update(self):
        for hierarchyModifier in self.reaction(self.ModifierCreated):
            hierarchyModifier.root = None
            hierarchyModifier.go1 = None
            hierarchyModifier.go2 = None
            hierarchyModifier.go3 = None

        triggerAccess = self.reaction(self.AreaTriggerAccess)
        for go, hierarchyModifier in self.reaction(self.ModifierActivated):
            self._onHierarchyModifierAdded(hierarchyModifier, go, triggerAccess)

        for go, hierarchyModifier2 in self.reaction(self.Modifier2Activated):
            self._onHierarchyModifierAdded2(hierarchyModifier2, go, triggerAccess)

        self._tick()
        return

    def _onHierarchyModifierAdded(self, hierarchyModifier, go, triggerAccess):
        self._setupRoot(hierarchyModifier, go)
        if hierarchyModifier.areaTrigger1:
            areaTrigger1 = triggerAccess.find(hierarchyModifier.areaTrigger1)
            areaTrigger1.addEnterReaction((lambda who, where: self._switchConnectFirstTrigger(go, where)))
        if hierarchyModifier.areaTrigger2:
            areaTrigger2 = triggerAccess.find(hierarchyModifier.areaTrigger2)
            areaTrigger2.addEnterReaction((lambda who, where: self._switchConnectSecondTrigger(go, where)))
        return

    def _onHierarchyModifierAdded2(self, hierarchyModifier2, go, triggerAccess):
        if hierarchyModifier2.areaTrigger:
            areaTrigger = triggerAccess.find(hierarchyModifier2.areaTrigger)
            areaTrigger.addEnterReaction((lambda who, where: self._unwrapFigure(go, where)))
            areaTrigger.addExitReaction((lambda who, where: self._wrapFigure(go, where)))
        return

    def _tick(self):
        player = BigWorld.player()
        if player is None or isPlayerAccount():
            return
        if hasattr(player, b'getVehicleAttached'):
            vehicle = player.getVehicleAttached()
            if vehicle is None:
                return
            transformAccess = self.reaction(self.TransformAccess)
            for hmodifier in self.reaction(self.Modifier2Iterate):
                transfComp = transformAccess.find(hmodifier.cameraTransform)
                direction = vehicle.position - transfComp.worldTransform.translation
                matrix = transfComp.transform
                transfComp.transform = math_utils.createRTMatrix((
                 direction.yaw, direction.pitch, 0.0), matrix.translation)

        return

    def _setupRoot(self, hierarchyModifier, root):
        hierarchyModifier.root = root
        hierarchy = self.hierarchy
        hierarchyModifier.go1 = hierarchy.findFirstNodeByName(root, hierarchyModifier.gameObject1)
        hierarchyModifier.go2 = hierarchy.findFirstNodeByName(root, hierarchyModifier.gameObject2)
        hierarchyModifier.go3 = hierarchy.findFirstNodeByName(root, hierarchyModifier.gameObject3)
        return

    def _unwrapFigure(self, hierarchyModifier2Go, where):
        _logger.debug(b'HierarchyModifier2. Trigger entered')
        modifier2Access = self.reaction(self.Modifier2Access)
        hierarchyModifier2 = modifier2Access.find(hierarchyModifier2Go)
        hierarchyAccess = self.reaction(self.HierarchyAccess)
        hierarchy = self.hierarchy
        gom = self.gom
        topGoName = gom.gameObject(hierarchyModifier2.top).name
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'Head', topGoName)
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'Back', gom.gameObject(hierarchyModifier2.bottom).name)
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'Camera', topGoName)
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'LH', b'TL')
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'RH', b'TR')
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'LL', b'BL')
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'RL', b'BR')
        return

    def _wrapFigure(self, hierarchyModifier2Go, where):
        _logger.debug(b'HierarchyModifier2. Trigger exited')
        modifier2Access = self.reaction(self.Modifier2Access)
        hierarchyModifier2 = modifier2Access.find(hierarchyModifier2Go)
        hierarchyAccess = self.reaction(self.HierarchyAccess)
        hierarchy = self.hierarchy
        boxGoName = self.gom.gameObject(hierarchyModifier2.box).name
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'Head', boxGoName)
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'Back', boxGoName)
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'Camera', b'Bot')
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'LH', boxGoName)
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'RH', boxGoName)
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'LL', boxGoName)
        self._changeHierarchy(hierarchy, hierarchyAccess, where, b'RL', boxGoName)
        return

    def _changeHierarchy(self, hierarchy, hierarchyAccess, go, childName, newParentName):
        parent = hierarchy.findFirstNodeByName(go, newParentName)
        child = hierarchy.findFirstNodeByName(go, childName)
        if parent.valid and child.valid:
            hierarchyComp = hierarchyAccess.find(child)
            hierarchyComp.parent = self.gom.gameObjectUuid(parent)
        return

    def _switchConnectFirstTrigger(self, modifierGo, _):
        _logger.debug(b'HierarchyModifier. Trigger 1 entered')
        modifierAccess = self.reaction(self.ModifierAccess)
        modifier = modifierAccess.find(modifierGo)
        if not modifier.zone1:
            self.__connect(modifier.go1, modifier.go2)
            modifier.zone1 = True
        else:
            self.__connectToRoot(modifier, modifier.go2)
            modifier.zone1 = False
        return

    def _switchConnectSecondTrigger(self, modifierGo, _):
        _logger.debug(b'HierarchyModifier. Trigger 2 entered')
        modifierAccess = self.reaction(self.ModifierAccess)
        modifier = modifierAccess.find(modifierGo)
        if not modifier.zone2:
            self.__connect(modifier.go2, modifier.go3)
            modifier.zone2 = True
        else:
            self.__connectToRoot(modifier, modifier.go3)
            modifier.zone2 = False
        return

    def __connect(self, rootObject, sourceObj):
        self._updateTransform(sourceObj, rootObject)
        hierarchyAccess = self.reaction(self.HierarchyAccess)
        hierarchyComp = hierarchyAccess.find(sourceObj)
        hierarchyComp.parent = self.gom.gameObjectUuid(rootObject)
        return

    def __connectToRoot(self, modifier, sourceObj):
        self._updateTransform(sourceObj, modifier.root)
        q = CGF.CommandQueue(self.gom)
        q.removeComponent(sourceObj, CGF.HierarchyComponent)
        q.createComponent(sourceObj, CGF.HierarchyComponent, modifier.root)
        return

    def _updateTransform(self, go, newParent):
        transformAccess = self.reaction(self.TransformAccess)
        objectTransform = transformAccess.find(go)
        newLocal = objectTransform.worldTransform
        parentTransform = transformAccess.find(newParent)
        parentInv = parentTransform.worldTransform
        parentInv.invert()
        newLocal.postMultiply(parentInv)
        objectTransform.transform = newLocal
        return


@registerComponent
class TestModelSwapper(object):
    group = DEMO_CATEGORY
    editorTitle = b'Test Model Swapper'
    domain = CGF.Domain.Client
    model1 = ComponentProperty(type=CGF.PropertyType.String, value=b'', editorName=b'model1', annotations={b'path': b'*.model'})
    model2 = ComponentProperty(type=CGF.PropertyType.String, value=b'', editorName=b'model2', annotations={b'path': b'*.model'})


class ModelSwapperSystem(CGF.System):
    SwapperCreated = CGF.CreateReaction(CGF.ReactRw(TestModelSwapper))
    SwapperIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.GameObject, CGF.Rw(TestModelSwapper))
    Reactions = CGF.Reactions(SwapperCreated, SwapperIterate)

    def __init__(self):
        super(ModelSwapperSystem, self).__init__()
        self.__swapTime = 0
        return

    def update(self):
        for swapper in self.reaction(self.SwapperCreated):
            swapper.currentModel = swapper.model1

        q = CGF.CommandQueue(self.gom)
        self.__swapTime += self.clock.updateDelta
        if self.__swapTime > 5.0:
            self.__swapTime = 0
            for g, s in self.reaction(self.SwapperIterate):
                model = s.currentModel
                if model == s.model1:
                    s.currentModel = s.model2
                else:
                    s.currentModel = s.model1
                q.removeComponent(g, GenericComponents.DynamicModelComponent)
                q.createComponent(g, GenericComponents.DynamicModelComponent, model)

        return
