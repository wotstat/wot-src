from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent
from GenericComponents import StateSwitcherComponent
_DEFAULT_HEALTH = 300

class DEATH_REASON(object):
    UNKNOWN = 0
    DESTROYED = 1


class DeathComponentDescriptor(object):
    category = b'Common'
    editorTitle = b'Death Component'


class HealthComponentDescriptor(object):
    category = b'Common'
    editorTitle = b'Health Component'
    maxHealth = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'MaxHealth', value=_DEFAULT_HEALTH)
    health = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'CurrentHealth', value=_DEFAULT_HEALTH)


@registerComponent
class RemoveOnDeathComponent(object):
    category = b'Death'
    editorTitle = b'Remove On Death Component'
    domain = CGF.Domain.All
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Delay', value=0.0)


@registerComponent
class SpawnOnDeathComponent(object):
    category = b'Death'
    editorTitle = b'Spawn On Death Component'
    domain = CGF.Domain.All
    prefabPath = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Spawn Prefab', annotations={b'path': b'*.prefab'})
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGF.PropertyType.Bool, editorName=b'Attach to GO', value=True)


@registerComponent
class VehicleHealthObserverComponent(object):
    category = b'Common'
    editorTitle = b'Vehicle Health Observer Component'
    domain = CGF.Domain.All
    state = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'State', value=StateSwitcherComponent.NORMAL_STATE, annotations={b'comboBox': {b'None': (str(StateSwitcherComponent.NONE_STATE)), 
                     b'Normal': (str(StateSwitcherComponent.NORMAL_STATE)), 
                     b'Damaged': (str(StateSwitcherComponent.DAMAGED_STATE)), 
                     b'Critical': (str(StateSwitcherComponent.CRITICAL_STATE))}})
