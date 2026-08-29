from soft_exception import SoftException
LOBBY_REQUIRED_LIBRARIES = [
 2, 
 3, 
 4, 
 5, 
 6, 
 7, 
 8]
BATTLE_REQUIRED_LIBRARIES = [
 2, 
 4, 
 9, 
 10, 
 6, 
 11, 
 12]
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
