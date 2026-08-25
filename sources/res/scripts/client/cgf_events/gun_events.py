from __future__ import absolute_import
import typing, CGF, Vehicular

def postVehicularSingleShotEvent(spaceID, entityID, slotName, gunID):
    CGF.postEvent(spaceID, Vehicular.SingleShotEvent(entityID=entityID, slotName=slotName, gunID=gunID))
    return


def postVehicularMultiShotEvent(spaceID, entityID, slotName, gunIDs):
    CGF.postEvent(spaceID, Vehicular.MultiShotEvent(entityID=entityID, slotName=slotName, gunIDs=gunIDs))
    return


def postVehicularContinuousBurstEvent(spaceID, entityID, slotName, active):
    CGF.postEvent(spaceID, Vehicular.ContinuousBurstEvent(entityID=entityID, slotName=slotName, active=active))
    return


def postVehicularFireRateChangedEvent(spaceID, entityID, slotName, shotsPerSec):
    CGF.postEvent(spaceID, Vehicular.FireRateChangedEvent(entityID=entityID, slotName=slotName, shotsPerSec=shotsPerSec))
    return


def postVehicularVariablesChangedEvent(spaceID, entityID, slotName, varValueMap):
    CGF.postEvent(spaceID, Vehicular.VariablesChangedEvent(entityID=entityID, slotName=slotName, varValueMap=varValueMap))
    return
