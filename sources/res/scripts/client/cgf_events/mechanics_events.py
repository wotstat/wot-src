from __future__ import absolute_import
import CGF, Vehicular

def postSightPointerSectorEvent(spaceID, entityID, slotName, targetWidth, targetDistance, targetOpacity, duration):
    CGF.postEvent(spaceID, Vehicular.VariablesChangedEvent(entityID=entityID, slotName=slotName, varValueMap={b'sectorVision/length': targetDistance, 
       b'sectorVision/width': targetWidth, 
       b'sectorVision/opacity': targetOpacity, 
       b'sectorVision/duration': duration}))
    return
