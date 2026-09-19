from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty

class IndividualRespawnTimerComponentDescr(object):
    category = b'Respawns'
    editorTitle = b'IndividualRespawnTimerComponent'
    domain = CGF.Domain.All
    respawnDelay = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'respawnDelay', value=1)
    timeOfDeath = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'timeOfDeath', value=0.0)
