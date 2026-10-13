from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty

class RespawnPolicyVehicleLinkComponentDescr(object):
    category = b'Respawns'
    editorTitle = b'RespawnPolicyVehicleLinkComponent'
    domain = CGF.Domain.All
    vehicleId = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'vehicleId', value=0)
