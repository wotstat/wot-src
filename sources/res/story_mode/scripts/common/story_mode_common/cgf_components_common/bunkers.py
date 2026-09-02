from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty
from constants import ATTACK_REASON

class BunkerLogicComponentDescriptor(object):
    category = b'Bunker'
    editorTitle = b'Bunker Logic'
    domain = CGF.Domain.All
    destructibleEntityId = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'Destructible Entity ID', value=0)
    transitionChild = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Transition', value=CGF.GameObject)
    destroyedChild = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Destroyed', value=CGF.GameObject)
    markerDistance = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'Marker max distance', value=300)
    resistAttackReasons = ComponentProperty(type=CGF.PropertyType.StringList, editorName=b'Resist Attack Reasons', value=(
     ATTACK_REASON.RAM,
     ATTACK_REASON.BATTLESHIP,
     ATTACK_REASON.DESTROYER))
