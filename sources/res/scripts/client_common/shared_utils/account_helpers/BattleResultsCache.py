from __future__ import absolute_import
import os, zlib
from functools import partial
from future.moves import pickle
from future.utils import viewitems
import BigWorld, AccountCommands, constants
from battle_results_shared import VehicleInteractionDetails
from battle_results import unpackClientBattleResults
from debug_utils import LOG_CURRENT_EXCEPTION
from external_strings_utils import unicode_from_utf8
from py2to3.compat import base64compat
BATTLE_RESULTS_VERSION = 1
CACHE_DIR = os.path.join(os.path.dirname(unicode_from_utf8((constants.IS_BOT or BigWorld.wg_getPreferencesFilePath)() if 1 else b'.')[1]), b'battle_results')

class BattleResultsCache(object):

    def __init__(self):
        self.__account = None
        self.__ignore = True
        self.__waiting = False
        clean()
        return

    def onAccountBecomePlayer(self):
        self.__ignore = False
        self.__waiting = False
        return

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True
        return

    def setAccount(self, account):
        self.__account = account
        return

    def get(self, arenaUniqueID, callback):
        errorCode, results = self.__checkErrorsAndGetFromCache(arenaUniqueID, self.__account.name)
        if errorCode is not None:
            if callback is not None:
                callback(errorCode, results)
            return
        self.__waiting = True
        proxy = partial(self.__onGetResponse, callback, None)
        self.__account._doCmdInt3(AccountCommands.CMD_REQ_BATTLE_RESULTS, arenaUniqueID, 0, 0, proxy)
        return

    def getOther(self, arenaUniqueID, resultsSubUrl, callback):
        errorCode, results = self.__checkErrorsAndGetFromCache(arenaUniqueID, resultsSubUrl)
        if errorCode is not None:
            if callback is not None:
                callback(errorCode, results)
            return
        raise NotImplementedError
        return

    def __checkErrorsAndGetFromCache(self, arenaUniqueID, uniqueFolderName):
        if self.__ignore:
            return (AccountCommands.RES_NON_PLAYER, None)
        else:
            if self.__waiting:
                return (AccountCommands.RES_COOLDOWN, None)
            battleResults = load(uniqueFolderName, arenaUniqueID)
            if battleResults is not None:
                return (AccountCommands.RES_CACHE, convertToFullForm(battleResults))
            return (None, None)

    def __onGetResponse(self, callback, resultsSubUrl, requestID, resultID, errorStr, ext=None):
        if resultID != AccountCommands.RES_STREAM:
            self.__waiting = False
            if callback is not None:
                callback(resultID, None)
            return
        self.__account._subscribeForStream(requestID, partial(self.__onStreamComplete, callback, resultsSubUrl))
        return

    def __onStreamComplete(self, callback, resultsSubUrl, isSuccess, data):
        self.__waiting = False
        try:
            isSelfResults = resultsSubUrl is None
            battleResults = pickle.loads(zlib.decompress(data))
            folderName = self.__account.name if isSelfResults else resultsSubUrl
            save(folderName, battleResults)
            if callback is not None:
                callback(AccountCommands.RES_STREAM, convertToFullForm(battleResults))
            if isSelfResults:
                self.__account.base.doCmdInt3(AccountCommands.REQUEST_ID_NO_RESPONSE, AccountCommands.CMD_BATTLE_RESULTS_RECEIVED, battleResults[0], 0, 0)
        except Exception:
            LOG_CURRENT_EXCEPTION()
            if callback is not None:
                callback(AccountCommands.RES_FAILURE, None)

        return


def save(accountName, battleResults):
    fileHandler = None
    try:
        arenaUniqueID = battleResults[0]
        folderName = getFolderName(accountName, arenaUniqueID)
        if not os.path.isdir(folderName):
            os.makedirs(folderName)
        fileName = os.path.join(folderName, b'%s.dat' % arenaUniqueID)
        fileHandler = open(fileName, b'wb')
        pickle.dump((BATTLE_RESULTS_VERSION, battleResults), fileHandler, -1)
    except Exception:
        LOG_CURRENT_EXCEPTION()

    if fileHandler is not None:
        fileHandler.close()
    return


def load(uniqueFolderName, arenaUniqueID):
    fileHandler = None
    try:
        fileName = os.path.join(getFolderName(uniqueFolderName, arenaUniqueID), b'%s.dat' % arenaUniqueID)
        if not os.path.isfile(fileName):
            return
        fileHandler = open(fileName, b'rb')
        version, battleResults = pickle.load(fileHandler)
    except Exception:
        LOG_CURRENT_EXCEPTION()

    if fileHandler is not None:
        fileHandler.close()
    if version == BATTLE_RESULTS_VERSION:
        return battleResults
    else:
        return


def getFolderName(uniqueFolderName, arenaUniqueID):
    battleStartDay = (arenaUniqueID & 4294967295L) // 86400
    return os.path.join(CACHE_DIR, base64compat.b32encode(b'%s;%s' % (uniqueFolderName, battleStartDay)))


def clean():
    try:
        for root, dirs, files in os.walk(CACHE_DIR, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))

            for name in dirs:
                os.rmdir(os.path.join(root, name))

    except Exception:
        LOG_CURRENT_EXCEPTION()

    return


def convertToFullForm(compactForm):
    arenaUniqueID, avatarResults, vehicleResults, otherResults = compactForm
    vehicleResults = pickle.loads(zlib.decompress(vehicleResults))
    avatarResults = pickle.loads(zlib.decompress(avatarResults))
    personal = {}
    fullForm = {b'arenaUniqueID': arenaUniqueID, 
       b'personal': personal, 
       b'common': {}, b'players': {}, b'vehicles': {}, b'avatars': {}}
    personal[b'avatar'] = unpackClientBattleResults(avatarResults)
    for vehTypeCompDescr, ownResults in viewitems(vehicleResults):
        vehPersonal = personal[vehTypeCompDescr] = unpackClientBattleResults(ownResults)
        if vehPersonal is None:
            continue
        vehPersonal[b'details'] = VehicleInteractionDetails.fromPacked(vehPersonal[b'details']).toDict()

    commonAsList, playersAsList, vehiclesAsList, avatarsAsList = pickle.loads(zlib.decompress(otherResults))
    fullForm[b'common'] = unpackClientBattleResults(commonAsList)
    for accountDBID, playerAsList in viewitems(playersAsList):
        fullForm[b'players'][accountDBID] = unpackClientBattleResults(playerAsList)

    for accountDBID, avatarAsList in viewitems(avatarsAsList):
        fullForm[b'avatars'][accountDBID] = unpackClientBattleResults(avatarAsList)

    for vehicleID, vehiclesInfo in viewitems(vehiclesAsList):
        fullForm[b'vehicles'][vehicleID] = []
        for vehTypeCompDescr, vehicleInfo in viewitems(vehiclesInfo):
            fullForm[b'vehicles'][vehicleID].append(unpackClientBattleResults(vehicleInfo))

    return fullForm
