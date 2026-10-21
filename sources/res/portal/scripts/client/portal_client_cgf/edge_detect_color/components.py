import CGF, Math
from cgf_script.component_meta_class import registerComponent, CGFMetaTypes, ComponentProperty
_DEFAULT_FILL_COLOR = Math.Vector4(0.561, 0.816, 0.863, 1)
_DEFAULT_SOLID_OVERLAY = Math.Vector4(0.561, 0.816, 0.863, 0.5)
_DEFAULT_SOLID_DESTRUCTIBLE = Math.Vector4(0.35, 0.55, 0.58, 0.5)
_DEFAULT_PATTERN_OVERLAY = Math.Vector4(0.22, 0.35, 0.38, 0.25)
_DEFAULT_PATTERN_OVERLAY_FOREGROUND = Math.Vector4(0.561, 0.816, 0.863, 1)
_DEFAULT_PATTERN_DESTRUCTIBLE = Math.Vector4(0.22, 0.35, 0.38, 0.25)
_DEFAULT_PATTERN_DESTRUCTIBLE_FOREGROUND = Math.Vector4(0.561, 0.816, 0.863, 1)
_COLOR_PICKER = {b'colorPicker': {b'255Range': False, b'useAlpha': True}}

@registerComponent
class EdgeDetectFillColorComponent(object):
    category = b'Portal'
    editorTitle = b'Edge Detect Fill Color'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    fillColor = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName=b'Fill Color', value=_DEFAULT_FILL_COLOR, annotations=_COLOR_PICKER)
    solidOverlay = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName=b'Teammate Solid Overlay', value=_DEFAULT_SOLID_OVERLAY, annotations=_COLOR_PICKER)
    solidDestructible = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName=b'Teammate Solid Destructible', value=_DEFAULT_SOLID_DESTRUCTIBLE, annotations=_COLOR_PICKER)
    patternOverlayForeground = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName=b'Teammate Pattern Overlay Foreground', value=_DEFAULT_PATTERN_OVERLAY_FOREGROUND, annotations=_COLOR_PICKER)
    patternOverlay = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName=b'Teammate Pattern Overlay', value=_DEFAULT_PATTERN_OVERLAY, annotations=_COLOR_PICKER)
    patternDestructibleForeground = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName=b'Teammate Pattern Destructible Foreground', value=_DEFAULT_PATTERN_DESTRUCTIBLE_FOREGROUND, annotations=_COLOR_PICKER)
    patternDestructible = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName=b'Teammate Pattern Destructible', value=_DEFAULT_PATTERN_DESTRUCTIBLE, annotations=_COLOR_PICKER)
