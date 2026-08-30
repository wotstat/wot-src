import typing
from gui.battle_results.pbs_helpers.common import isPersonalBattleResult
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable import _ReusableInfo
    from gui.battle_results.reusable.shared import VehicleSummarizeInfo
    from gui.battle_results.stats_ctrl import BattleResults

def isNotPersonalBattleResult(summarizeInfo, battleResults):
    return not isPersonalBattleResult(summarizeInfo, battleResults)


def hasStunEfficiency(summarizeInfo, _):
    return summarizeInfo.stunNum > 0


def hasArtilleryStrike(summarizeInfo, _):
    return summarizeInfo.artilleryFortEquipDamageDealt > 0


def getStatsParamValue(summarizeInfo, fields, _):
    return (getattr(summarizeInfo, field) for field in fields)


def getMileageValue(summarizeInfo, fields, _):
    return (getattr(summarizeInfo, field) / 1000.0 for field in fields)


def getPlayerContextMenuArgs(reusable, databaseID, vehicleCD):
    playerInfo = reusable.players.getPlayerInfo(databaseID)
    return {b'dbID': databaseID, 
       b'userName': (playerInfo.realName), 
       b'clanAbbrev': (playerInfo.clanAbbrev), 
       b'isAlly': (playerInfo.team == reusable.getPersonalTeam()), 
       b'vehicleCD': vehicleCD, 
       b'wasInBattle': True, 
       b'clientArenaIdx': (reusable.arenaUniqueID), 
       b'arenaType': (reusable.common.arenaGuiType)}
