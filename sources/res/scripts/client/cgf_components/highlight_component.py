import BigWorld, CGF
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from GenericComponents import DynamicModelComponent
from hover_component import IsHoveredComponent

@registerComponent
class IsHighlighted(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor


@registerComponent
class HighlightComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = b'Highlight'
    category = b'Common'
    color = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName=b'Color', value=(0, 0, 0, 1), annotations={b'colorPicker': {b'255Range': False, b'useAlpha': True}})
    groupName = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Group name')

    def __init__(self):
        super(HighlightComponent, self).__init__()
        self.isActive = True
        return


class HighlightManager(CGF.ComponentManager):

    @onAddedQuery(IsHoveredComponent, CGF.GameObject)
    def onHoverAdded(self, _, gameObject):
        gameObject.createComponent(IsHighlighted)
        return

    @onRemovedQuery(IsHoveredComponent, CGF.GameObject)
    def onHoverRemoved(self, _, gameObject):
        gameObject.removeComponentByType(IsHighlighted)
        return

    @onAddedQuery(IsHighlighted, HighlightComponent, DynamicModelComponent)
    def onDynamicModelHighlightAdded(self, _, highlightComponent, dynamicModelComponent):
        if highlightComponent.isActive:
            BigWorld.setEdgeDetectEdgeColor(3, highlightComponent.color)
            BigWorld.addEdgeDetectDynamicModel(dynamicModelComponent)
            self.__enableGroupDraw(True, highlightComponent.groupName)
        return

    @onRemovedQuery(IsHighlighted, HighlightComponent, DynamicModelComponent)
    def onDynamicModelHighlightRemoved(self, _, highlightComponent, dynamicModelComponent):
        BigWorld.delEdgeDetectDynamicModel(dynamicModelComponent)
        self.__enableGroupDraw(False, highlightComponent.groupName)
        return

    @onRemovedQuery(HighlightComponent, DynamicModelComponent)
    def onHighlightComponentRemoved(self, _, dynamicModelComponent):
        BigWorld.delEdgeDetectDynamicModel(dynamicModelComponent)
        return

    def __enableGroupDraw(self, enable, groupName):
        highlightQuery = CGF.Query(self.spaceID, (HighlightComponent, DynamicModelComponent))
        for highlightComponent, dynamicModelComponent in highlightQuery:
            if highlightComponent.groupName and highlightComponent.groupName == groupName:
                if enable and highlightComponent.isActive:
                    BigWorld.addEdgeDetectDynamicModel(dynamicModelComponent)
                else:
                    BigWorld.delEdgeDetectDynamicModel(dynamicModelComponent)

        return
