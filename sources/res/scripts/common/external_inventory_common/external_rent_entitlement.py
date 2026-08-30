from __future__ import absolute_import
from items import vehicles
EXTERNAL_RENT_ENTITLEMENT_PREFIX = b'ext_rent'

def isExternalRentEntitlement(entitlementCode):
    return entitlementCode.startswith(EXTERNAL_RENT_ENTITLEMENT_PREFIX)


def parseEntitlement(entitlementCode):
    if not isExternalRentEntitlement(entitlementCode):
        return (False, None, b'Wrong prefix')
    else:
        tokens = entitlementCode.split(b':')
        if len(tokens) < 3:
            return (False, None, b'Wrong amount of tokens')
        vehName = tokens[1] + b':' + tokens[2]
        if not vehicles.g_list.isVehicleExisting(vehName):
            return (False, None, b'Unknown vehicle')
        nationID, innationID = vehicles.g_list.getIDsByName(vehName)
        vehTypeCompDescr = vehicles.makeIntCompactDescrByID(b'vehicle', nationID, innationID)
        partnerCode = None
        if len(tokens) >= 4:
            partnerCode = tokens[3]
        data = {b'vehTypeCompDescr': vehTypeCompDescr, 
           b'partnerCode': partnerCode}
        return (
         True, data, b'')
