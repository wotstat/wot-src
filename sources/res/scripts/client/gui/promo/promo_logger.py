import logging
from functools import partial
import BigWorld
from adisp import adisp_process
from gui.macroses import getLanguageCode
from gui.clientgw.promo_screens.contexts import PromoSendActionLogCtx
from helpers import dependency, isPlayerAccount, time_utils
from ids_generators import Int32IDGenerator
from shared_utils import CONST_CONTAINER
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared.promo import IPromoLogger
from skeletons.gui.web import IWebController
_logger = logging.getLogger(__name__)

class PromoLogActions(CONST_CONTAINER):
    RECEIVED_NOTIFY_CENTER = b'ReceivedNotifyCenter'
    GET_MOST_IMPORTANT = b'GetMostImportant'
    OPEN_FROM_TEASER = b'OpenFromTeaser'
    CLOSED_BY_USER = b'ClosedByUser'
    KILLED_BY_SYSTEM = b'KilledBySystem'
    OPEN_FROM_MENU = b'OpenFromMenu'
    OPEN_IN_OLD = b'OpenInOld'


class PromoLogSubjectType(CONST_CONTAINER):
    TEASER = b'Teaser'
    PROMO_SCREEN = b'Promoscreen'
    INDEX = b'Index'
    PROMO_SCREEN_OR_INDEX = b'PromoscreenOrIndex'


class PromoLogSourceType(CONST_CONTAINER):
    NOTIFY_CENTER = b'NotifyCenter'
    FIRST_LOGIN = b'Firstlogin'
    AFTER_BATTLE = b'10stBattle'
    PRMP = b'PRMP'
    SSE = b'SSE'


def _getPlayerDatabaseID():
    if isPlayerAccount():
        return BigWorld.player().databaseID
    return


class PromoLogger(IPromoLogger):
    __PARAMS_MAP = {b'action': {b'set': (PromoLogActions.ALL())}, b'type': {b'set': (PromoLogSubjectType.ALL()), b'default': (PromoLogSubjectType.TEASER)}, b'teaserid': {}, b'slug': {}, b'spaid': {b'default': _getPlayerDatabaseID}, b'time': {b'default': (time_utils.getCurrentTimestamp)}, b'success': {}, b'lang': {b'default': getLanguageCode}, b'source': {b'set': (PromoLogSourceType.ALL())}, b'url': {}}
    __TEASER_PARAMS_MAP = {b'promoID': b'teaserid', b'url': b'url', b'slug': b'slug'}
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __webController = dependency.descriptor(IWebController)
    __ANSWER_WAITING_TIME = 30
    __IDGenerator = Int32IDGenerator()

    def __init__(self):
        self.__requestIDs = {}
        return

    @adisp_process
    def logAction(self, **kwargs):
        if self.__isEnabled():
            ctx = PromoSendActionLogCtx(self.__packData(kwargs))
            yield self.__webController.sendRequest(ctx=ctx)
        return

    def logTeaserAction(self, teaserData, **kwargs):
        dataToSend = kwargs.copy()
        if teaserData:
            for sourceName, targetName in self.__TEASER_PARAMS_MAP.iteritems():
                dataToSend[targetName] = teaserData.get(sourceName)

        self.logAction(**dataToSend)
        return

    def getLoggingFuture(self, teaserData=None, **kwargs):
        if not self.__isEnabled():
            return None
        else:
            requestID = self.__IDGenerator.next()
            callbackID = BigWorld.callback(self.__ANSWER_WAITING_TIME, partial(self.__sendDelayed, teaserData, requestID, **kwargs))
            self.__requestIDs[requestID] = callbackID
            return partial(self.__sendDelayed, teaserData, requestID, callbackID, **kwargs)

    def fini(self):
        for requestID, callbackID in self.__requestIDs.items():
            BigWorld.cancelCallback(callbackID)
            del self.__requestIDs[requestID]

        return

    def __isEnabled(self):
        return self.__lobbyContext.getServerSettings().isPromoLoggingEnabled()

    def __sendDelayed(self, teaserData, requestID, callbackID=None, **kwargs):
        if requestID in self.__requestIDs:
            del self.__requestIDs[requestID]
            if callbackID is not None:
                BigWorld.cancelCallback(callbackID)
            success = kwargs.pop(b'success', None)
            if teaserData is not None:
                self.logTeaserAction(teaserData, success=success, **kwargs)
            else:
                self.logAction(success=success, **kwargs)
        return

    def __packData(self, data):
        result = {}
        for paramName, settings in self.__PARAMS_MAP.iteritems():
            if paramName in data:
                value = data[paramName]
                possibleValues = settings.get(b'set')
                if possibleValues and value not in possibleValues:
                    _logger.error(b'Wrong value for enumerable %s', paramName)
                    continue
                result[paramName] = value
            elif b'default' in settings:
                default = settings[b'default']
                result[paramName] = default() if callable(default) else default

        return result
