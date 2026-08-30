import BigWorld
from shared_utils.avatar_helpers import VehicleTelemetry

def getAvatarDatabaseID():
    dbID = 0
    player = BigWorld.player()
    arena = getattr(player, b'arena', None)
    if arena is not None:
        vehID = getattr(player, b'playerVehicleID', None)
        if vehID is not None and vehID in arena.vehicles:
            dbID = arena.vehicles[vehID][b'accountDBID']
    return dbID


def getAvatarSessionID():
    player = BigWorld.player()
    avatarSessionID = getattr(player, b'sessionID', b'')
    return avatarSessionID
