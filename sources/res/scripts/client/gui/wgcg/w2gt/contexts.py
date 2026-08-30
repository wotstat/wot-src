from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class W2gtCtx(CommonWebRequestCtx):

    def __init__(self, clientVersion, eTag, geometryName, gameplayType, vehRole, vehLevel, team, waitingID=b''):
        self.__eTag = eTag
        vehicleRole = self.normalizeVehicleRole(vehRole)
        self.__params = {b'client_version': clientVersion, 
           b'map_name': geometryName, 
           b'gameplay_type': gameplayType, 
           b'vehicle_role': vehicleRole, 
           b'level': vehLevel, 
           b'team': team}
        super(W2gtCtx, self).__init__(waitingID=waitingID)
        return

    @staticmethod
    def normalizeVehicleRole(vehRole):
        if vehRole.startswith(b'role_'):
            return vehRole.split(b'_', 1)[-1]
        return vehRole

    def getRequestType(self):
        return WebRequestDataType.W2GT_DATA

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getParams(self):
        return self.__params

    def getHeaders(self):
        if self.__eTag:
            return {b'If-None-Match': (self.__eTag)}
        return {}
