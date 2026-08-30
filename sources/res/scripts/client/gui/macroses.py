from __future__ import absolute_import
import base64
from future.moves.urllib.parse import quote_plus
import BigWorld, constants
from adisp import adisp_async, adisp_process
from helpers import getClientLanguage, dependency
from helpers.http.url_formatters import addParamsToUrlQuery
from skeletons.gui.login_manager import ILoginManager
from skeletons.gui.web import IWebController
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.game_control import IMarathonEventsController

def getLanguageCode(args=None):
    code = getClientLanguage()
    return code.replace(b'_', b'-')


@dependency.replace_none_kwargs(connectionMgr=IConnectionManager)
def getAreaID(args=None, connectionMgr=None):
    if connectionMgr is not None:
        areaID = connectionMgr.areaID
    else:
        areaID = None
    if areaID:
        result = str(areaID)
    else:
        result = b'errorArea'
    return result


@dependency.replace_none_kwargs(connectionMgr=IConnectionManager)
def getEncodedLogin(args=None, connectionMgr=None):
    if connectionMgr is not None:
        login = connectionMgr.loginName
    else:
        login = None
    if login:
        result = login
    else:
        result = b'errorLogin'
    return base64.b64encode(result)


@dependency.replace_none_kwargs(connectionMgr=IConnectionManager)
def getQuotedLogin(args=None, connectionMgr=None):
    if connectionMgr is not None:
        login = connectionMgr.lastLoginName
    else:
        login = None
    if login:
        result = quote_plus(login)
    else:
        result = b''
    return result


@dependency.replace_none_kwargs(connectionMgr=IConnectionManager)
def getDatabaseID(args=None, connectionMgr=None):
    if connectionMgr is not None:
        dbID = connectionMgr.databaseID
    else:
        dbID = None
    if dbID:
        result = str(dbID)
    else:
        result = b'errorID'
    return result


@dependency.replace_none_kwargs(connectionMgr=IConnectionManager)
def getPeripheryID(args=None, connectionMgr=None):
    if connectionMgr is not None:
        return str(connectionMgr.peripheryID)
    else:
        return str(constants.STANDALONE_CLUSTER_ID)


def getUnitServerID(args=None):
    try:
        unitID = str(BigWorld.player().unitMgr.id)
    except AttributeError:
        unitID = b''

    return unitID


def getAuthRealm(args=None):
    return constants.AUTH_REALM


def getCurrentRealm(args=None):
    return constants.CURRENT_REALM


@dependency.replace_none_kwargs(marathonCtrl=IMarathonEventsController)
def getMarathonPackage(args=None, marathonCtrl=None):
    from gui.marathon.marathon_constants import MarathonState
    postfix = b''
    result = b''
    marathon = marathonCtrl.getPrimaryMarathon()
    if marathon is not None:
        currentStep, _ = marathon.getMarathonProgress()
        packageTemplate = marathon.packageTemplate
        state = marathon.getState()
        if state == MarathonState.FINISHED:
            postfix = marathon.finishedPostfix
        result = packageTemplate.format(currentStep, postfix)
    return result


@dependency.replace_none_kwargs(marathonCtrl=IMarathonEventsController)
def getMarathonStylePackage(args=None, marathonCtrl=None):
    from gui.marathon.marathon_constants import MarathonState
    postfix = b''
    result = b''
    marathon = marathonCtrl.getPrimaryMarathon()
    if marathon is not None:
        packageTemplate = marathon.packageStyleTemplate
        state = marathon.getState()
        if state == MarathonState.FINISHED:
            postfix = marathon.finishedPostfix
        result = packageTemplate.format(postfix)
    return result


@dependency.replace_none_kwargs(loginManager=ILoginManager)
def isSteamClient(args=None, loginManager=None):
    return str(int(loginManager.isWgcSteam))


def getClanDBID(args=None):
    clansCtrl = dependency.instance(IWebController)
    return str(clansCtrl.getClanDbID())


def getSyncMacroses():
    return {b'LANGUAGE_CODE': getLanguageCode, 
       b'AREA_ID': getAreaID, 
       b'ENCODED_LOGIN': getEncodedLogin, 
       b'QUOTED_LOGIN': getQuotedLogin, 
       b'DB_ID': getDatabaseID, 
       b'PERIPHERY_ID': getPeripheryID, 
       b'AUTH_REALM': getAuthRealm, 
       b'UNIT_SERVER_ID': getUnitServerID, 
       b'CLAN_DBID': getClanDBID, 
       b'CURRENT_REALM': getCurrentRealm, 
       b'PACKAGE_ID': getMarathonPackage, 
       b'STYLE_PACKAGE_ID': getMarathonStylePackage, 
       b'IS_STEAM': isSteamClient}


@adisp_async
def getWgniToken(proxy, args, params, callback):

    def _cbWrapper(response):
        if response and response.isValid():
            callback(str(response.getToken()))
        else:
            callback(b'')
        return

    from gui.shared.utils.requesters import getTokenRequester
    tokenRqs = getTokenRequester(constants.TOKEN_TYPE.WGNI)
    if not tokenRqs.isInProcess():
        tokenRqs.request(timeout=10.0)(_cbWrapper)
    else:
        _cbWrapper(response=None)
    return


@adisp_async
@adisp_process
def getTargetURL(proxy, args, params, callback):
    result = args or b''
    if result:
        url = yield proxy.parse(result, params)
        result = quote_plus(url)
    callback(result)
    return


@adisp_async
@adisp_process
def getUrlParams(proxy, args, params, callback):
    result = args or b''
    params = params or {}
    if result:
        url = yield proxy.parse(result, params)
        result = addParamsToUrlQuery(url, params)
    callback(result)
    return


def getAsyncMacroses():
    return {b'WGNI_TOKEN': getWgniToken, 
       b'TARGET_URL': getTargetURL, 
       b'PARAMS': getUrlParams}
