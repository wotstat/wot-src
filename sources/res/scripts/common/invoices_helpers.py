from constants import DOSSIER_TYPE
from dossiers2.custom.clan_layout import CLAN_DOSSIER_LIST_BLOCKS
from dossiers2.custom.account_layout import ACCOUNT_DOSSIER_STATIC_BLOCKS, ACCOUNT_DOSSIER_BINARY_SET_BLOCKS, ACCOUNT_DOSSIER_BLOCKS, ACCOUNT_DOSSIER_DICT_BLOCKS, ACCOUNT_DOSSIER_LIST_BLOCKS

def checkAccountDossierOperation(dossierType, blockName, recordName, opType):
    if dossierType not in (DOSSIER_TYPE.ACCOUNT,):
        return (False, b'Invalid dossier type')
    if not opType:
        return (False, b'Dossier operation param required')
    if blockName in ACCOUNT_DOSSIER_STATIC_BLOCKS or blockName in ACCOUNT_DOSSIER_BINARY_SET_BLOCKS:
        blockBuilder = ACCOUNT_DOSSIER_BLOCKS[blockName]
        if not (recordName in blockBuilder.recordsLayout or recordName.startswith(b'tankExpert') or recordName.startswith(b'mechanicEngineer') or recordName.startswith(b'collectorVehicle')):
            return (False, b'Invalid dossier record')
        if opType not in (b'add', b'set'):
            return (False, b'Invalid dossier operation')
    elif blockName in ACCOUNT_DOSSIER_DICT_BLOCKS:
        if opType not in (b'set', b'append'):
            return (False, b'Invalid dossier operation')
    elif blockName in ACCOUNT_DOSSIER_LIST_BLOCKS:
        if opType not in (b'append',):
            return (False, b'Invalid dossier operation')
    else:
        return (
         False, b'Dossier block invoice change not supported')
    return (True, b'')


def checkClanDossierOperation(dossierType, blockName, recordName, opType):
    if dossierType not in (DOSSIER_TYPE.CLAN,):
        return (False, b'Invalid dossier type')
    if not opType:
        return (False, b'Dossier operation param required')
    if blockName in CLAN_DOSSIER_LIST_BLOCKS:
        if opType not in (b'append',):
            return (False, b'Invalid dossier operation')
    else:
        return (
         False, b'Dossier block invoice change not supported')
    return (True, b'')


def getLogDefaultsDossierOperation(finOpType, itemTypeIdx, partnerID=0, actionSetID=0):
    return {b'opType': finOpType, 
       b'itemTypeIdx': itemTypeIdx, 
       b'partnerID': partnerID, 
       b'actionSetID': actionSetID, 
       b'valueTypeID': 0, 
       b'secValueTypeID': 0, 
       b'valueAmount': 0, 
       b'itemNumber': 0, 
       b'secValueAmount': 0, 
       b'vehTypeCompDescr': 0, 
       b'typeCompDescr': 0}
