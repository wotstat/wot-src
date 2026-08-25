from __future__ import absolute_import
import CGF, SoundGroups
from cgf_script.registration import ComponentProperty, registerComponent
from cgf_components.hover_component import IsHoveredComponent, HoverGroupTrackerComponent

@registerComponent
class HoverableComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = b'Hoverable'
    group = b'Common'
    groupTracker = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Group tracker', value=HoverGroupTrackerComponent)


@registerComponent
class HoverSoundComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = b'Hover group sound'
    group = b'Common'
    hoverAddingSound = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Hover adding sound', value=b'')
    hoverRemovingSound = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Hover removing sound', value=b'')


class HoverGroupSystem(CGF.System):
    HoverableActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(HoverableComponent), CGF.ReactHas(IsHoveredComponent))
    HoverableDeactivated = CGF.DeactivateReaction(CGF.GameObject, CGF.ReactRw(HoverableComponent), CGF.ReactHas(IsHoveredComponent))
    HoverSoundActivated = CGF.ActivateReaction(CGF.ReactRo(HoverSoundComponent), CGF.ReactHas(IsHoveredComponent))
    HoverSoundDeactivated = CGF.DeactivateReaction(CGF.ReactRo(HoverSoundComponent), CGF.ReactHas(IsHoveredComponent))
    HoverGroupTrackerAccess = CGF.AccessReaction(CGF.Ro(HoverGroupTrackerComponent))
    Reactions = CGF.Reactions(HoverableActivated, HoverableDeactivated, HoverSoundActivated, HoverSoundDeactivated, HoverGroupTrackerAccess)

    def update(self):
        hoverGroupTrackerAccess = self.reaction(self.HoverGroupTrackerAccess)
        for gameObject, hoverableComponent in self.reaction(self.HoverableDeactivated):
            self.onHoverRemoved(hoverableComponent, gameObject, hoverGroupTrackerAccess)

        for hoverSound in self.reaction(self.HoverSoundDeactivated):
            self.onHoverSoundRemoved(hoverSound)

        for gameObject, hoverableComponent in self.reaction(self.HoverableActivated):
            self.onHoverAdded(hoverableComponent, gameObject, hoverGroupTrackerAccess)

        for hoverSound in self.reaction(self.HoverSoundActivated):
            self.onHoverSoundAdded(hoverSound)

        return

    def onHoverAdded(self, hoverableComponent, gameObject, hoverGroupTrackerAccess):
        groupTracker = hoverGroupTrackerAccess.find(hoverableComponent.groupTracker)
        if groupTracker:
            groupTracker.addHoveredGO(gameObject)
        return

    def onHoverRemoved(self, hoverableComponent, gameObject, hoverGroupTrackerAccess):
        groupTracker = hoverGroupTrackerAccess.find(hoverableComponent.groupTracker)
        if groupTracker:
            groupTracker.removeHoveredGO(gameObject)
        return

    def onHoverSoundAdded(self, hoverSound):
        if hoverSound.hoverAddingSound:
            SoundGroups.g_instance.playSound2D(hoverSound.hoverAddingSound)
        return

    def onHoverSoundRemoved(self, hoverSound):
        if hoverSound.hoverRemovingSound:
            SoundGroups.g_instance.playSound2D(hoverSound.hoverRemovingSound)
        return
