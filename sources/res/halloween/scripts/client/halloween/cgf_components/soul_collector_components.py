from __future__ import absolute_import
import CGF, GenericComponents
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class SoulCollectorProgressComponent(object):
    category = b'Halloween'
    editorTitle = b'Soul Collector Progress Component'
    progressSectors = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'Progress Sectors', value=0)
    sectorOffsetY = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Progress Sector Y Offset', value=0.0)
    progressSequence = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Progress Sequence', value=b'')


@registerComponent
class SoulCollectorComponent(object):
    category = b'Halloween'
    editorTitle = b'SoulCollectorComponent'
    loadProgressGO = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Progress GO', value=CGF.GameObject)
    energyGlowAnimator = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Energy Glow Animator', value=GenericComponents.AnimatorComponent)
    auraAnimator = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Aura Animator', value=GenericComponents.AnimatorComponent)
    drainerAnimator = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Drainer Animator', value=GenericComponents.AnimatorComponent)
