from __future__ import absolute_import
import BigWorld, CGF
from cgf_script.registration import ComponentProperty, registerComponent
from GenericComponents import DynamicModelComponent
from cgf_components.hover_component import IsHoveredComponent, SelectionComponent

@registerComponent
class IsHighlighted(object):
    editorTitle = b'Is Highlighted'
    domain = CGF.Domain.ClientEditor


@registerComponent
class HighlightComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = b'Highlight'
    group = b'Common'
    color = ComponentProperty(type=CGF.PropertyType.Vector4, editorName=b'Color', value=(0, 0, 0, 1), annotations={b'colorPicker': {b'255Range': False, b'useAlpha': True}})
    groupName = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Group name')
    drawerMode = ComponentProperty(type=CGF.PropertyType.Int, value=0, editorName=b'drawerMode')
    colorIndex = ComponentProperty(type=CGF.PropertyType.Int, value=4, editorName=b'colorIndex')
    overridenHighlightModel = ComponentProperty(type=CGF.PropertyType.Link, value=CGF.GameObject, editorName=b'overridenHighlightModel')

    def __init__(self):
        super(HighlightComponent, self).__init__()
        self.callbackID = None
        return


class HighlightSystem(CGF.System):
    HoverActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRo(IsHoveredComponent), CGF.ReactRo(SelectionComponent))
    HoverDeactivated = CGF.DeactivateReaction(CGF.GameObject, CGF.ReactRo(IsHoveredComponent), CGF.ReactRo(SelectionComponent))
    DynamicModelHighlightActivated = CGF.ActivateReaction(CGF.ReactRo(IsHighlighted), CGF.ReactRo(HighlightComponent), CGF.ReactRo(DynamicModelComponent))
    DynamicModelHighlightDeactivated = CGF.DeactivateReaction(CGF.ReactRo(IsHighlighted), CGF.ReactRo(HighlightComponent), CGF.ReactRo(DynamicModelComponent))
    HighlightComponentDeactivated = CGF.DeactivateReaction(CGF.ReactRo(HighlightComponent), CGF.ReactRo(DynamicModelComponent))
    HighlightModelIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Ro(HighlightComponent), CGF.Ro(DynamicModelComponent))
    DynamicModelAccess = CGF.AccessReaction(CGF.Ro(DynamicModelComponent))
    Reactions = CGF.Reactions(HoverActivated, HoverDeactivated, DynamicModelHighlightActivated, DynamicModelHighlightDeactivated, HighlightComponentDeactivated, HighlightModelIterate, DynamicModelAccess)

    def update(self):
        q = CGF.CommandQueue(self.gom)
        dynamicModelAccess = self.reaction(self.DynamicModelAccess)
        highlightModelIterate = self.reaction(self.HighlightModelIterate)
        for gameObject, _, selection in self.reaction(self.HoverDeactivated):
            self.onHoverRemoved(selection, gameObject, q)

        for _, highlightComponent, dynamicModelComponent in self.reaction(self.DynamicModelHighlightDeactivated):
            self.onDynamicModelHighlightRemoved(highlightComponent, dynamicModelComponent, dynamicModelAccess, highlightModelIterate)

        for highlightComponent, dynamicModelComponent in self.reaction(self.HighlightComponentDeactivated):
            self.onHighlightComponentRemoved(highlightComponent, dynamicModelComponent, dynamicModelAccess)

        for gameObject, _, selection in self.reaction(self.HoverActivated):
            self.onHoverAdded(selection, gameObject, q)

        for _, highlightComponent, dynamicModelComponent in self.reaction(self.DynamicModelHighlightActivated):
            self.onDynamicModelHighlightAdded(highlightComponent, dynamicModelComponent, dynamicModelAccess, highlightModelIterate)

        return

    def onHoverAdded(self, selection, gameObject, queue):
        if selection.highlight:
            queue.createComponent(gameObject, IsHighlighted)
        return

    def onHoverRemoved(self, selection, gameObject, queue):
        if selection.highlight:
            queue.removeComponent(gameObject, IsHighlighted)
        return

    def onDynamicModelHighlightAdded(self, highlightComponent, dynamicModelComponent, dynamicModelAccess, highlightModelIterate):
        BigWorld.wgSetEdgeDetectEdgeColor(highlightComponent.colorIndex - 1, highlightComponent.color)
        self.__edgeDetectDynamicModel(True, highlightComponent, dynamicModelComponent, dynamicModelAccess)
        self.__enableGroupDraw(True, highlightComponent.groupName, highlightModelIterate, dynamicModelAccess)
        return

    def onDynamicModelHighlightRemoved(self, highlightComponent, dynamicModelComponent, dynamicModelAccess, highlightModelIterate):
        self.__edgeDetectDynamicModel(False, highlightComponent, dynamicModelComponent, dynamicModelAccess)
        self.__enableGroupDraw(False, highlightComponent.groupName, highlightModelIterate, dynamicModelAccess)
        return

    def onHighlightComponentRemoved(self, highlightComponent, dynamicModelComponent, dynamicModelAccess):
        self.__edgeDetectDynamicModel(False, highlightComponent, dynamicModelComponent, dynamicModelAccess)
        return

    def __edgeDetectDynamicModel(self, enable, highlightComponent, dynamicModelComponent, dynamicModelAccess):
        dynamicModel = dynamicModelComponent
        highlightObj = self.gom.gameObject(highlightComponent.overridenHighlightModel)
        if highlightObj.valid:
            overridenHighlightModel = dynamicModelAccess.find(highlightObj)
            if overridenHighlightModel:
                dynamicModel = overridenHighlightModel
        if enable:
            BigWorld.wgAddEdgeDetectDynamicModel(dynamicModel, highlightComponent.colorIndex, highlightComponent.drawerMode)
        else:
            BigWorld.wgDelEdgeDetectDynamicModel(dynamicModel)
        return

    def __enableGroupDraw(self, enable, groupName, highlightModelIterate, dynamicModelAccess):
        for highlightComponent, dynamicModelComponent in highlightModelIterate:
            if highlightComponent.groupName and highlightComponent.groupName == groupName:
                self.__edgeDetectDynamicModel(enable, highlightComponent, dynamicModelComponent, dynamicModelAccess)

        return
