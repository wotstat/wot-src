from __future__ import absolute_import
from soft_exception import SoftException
LOBBY_REQUIRED_LIBRARIES = [
 3, 
 4, 
 5, 
 6, 
 7, 
 8, 
 9]
BATTLE_REQUIRED_LIBRARIES = [
 3, 
 5, 
 10, 
 11, 
 7, 
 12, 
 13]
ADDITIONAL_BATTLE_REQUIRED_LIBRARIES = {}

def addLobbyRequiredLibraries(swfList, personality):
    intersection = set(LOBBY_REQUIRED_LIBRARIES).intersection(set(swfList))
    if intersection:
        raise SoftException((b'LOBBY_REQUIRED_LIBRARIES already has swf(s):{swfs}. Personality: {personality}').format(swfs=intersection, personality=personality))
    LOBBY_REQUIRED_LIBRARIES.extend(swfList)
    return


def addBattleRequiredLibraries(swfList, arenaGuiType, personality):
    intersection = set(BATTLE_REQUIRED_LIBRARIES).intersection(set(swfList))
    if intersection:
        raise SoftException((b'BATTLE_REQUIRED_LIBRARIES already has swf(s):{swfs}. Personality: {personality}').format(swfs=intersection, personality=personality))
    if arenaGuiType in ADDITIONAL_BATTLE_REQUIRED_LIBRARIES:
        raise SoftException((b'ADDITIONAL_BATTLE_REQUIRED_LIBRARIES already has arena gui type:{t}. Personality: {personality}').format(t=arenaGuiType, personality=personality))
    ADDITIONAL_BATTLE_REQUIRED_LIBRARIES.update({arenaGuiType: swfList})
    return
