from __future__ import absolute_import
import CGF
from cgf_script.registration import registerComponent, ComponentProperty

@registerComponent
class ProBoostEffectsConfigComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = b'Pro Boost Effects Config'
    category = b'Hangar'
    vseVisible = False
    activationPrefab = ComponentProperty(type=CGF.PropertyType.String, value=b'', editorName=b'Activation prefab', annotations={b'path': b'*.prefab'})
    deactivationPrefab = ComponentProperty(type=CGF.PropertyType.String, value=b'', editorName=b'Deactivation prefab', annotations={b'path': b'*.prefab'})
