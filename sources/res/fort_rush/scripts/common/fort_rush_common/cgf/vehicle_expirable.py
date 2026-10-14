from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty

class VehicleExpirableComponentDescriptor(object):
    category = b'Expirable'
    editorTitle = b'Vehicle Expirable Component'
    domain = CGF.Domain.All
    duration = ComponentProperty(CGF.PropertyType.Float, editorName=b'Duration', value=0.0)
