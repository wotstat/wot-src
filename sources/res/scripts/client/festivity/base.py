from collections import namedtuple
import logging
from pprint import pformat
import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
_logger = logging.getLogger(__name__)

def _defaultLogger(*args):
    msg = pformat(args)
    _logger.debug(b'[SERVER CMD RESPONSE]:%s', msg)
    return


def _getProxy(callback):
    if callback is not None:
        return (lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr, ext))
    else:
        return


FestivityQuestsHangarFlag = namedtuple(b'FestivityQuestsHangarFlag', b'icon, iconDisabled, flagBackground')

class BaseFestivityRequester(AbstractSyncDataRequester):
    dataKey = None

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().festivities.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    def _preprocessValidData(self, data):
        festivityData = data.get(self.dataKey, {})
        return dict(festivityData)


class BaseFestivityProcessor(object):

    def __init__(self):
        super(BaseFestivityProcessor, self).__init__()
        self.__commandProxy = None
        return

    def setCommandProxy(self, account):
        self.__commandProxy = account
        return

    def _perform(self, command, callback=None, *args):
        if self.__commandProxy is not None:
            cmdArgs = list(args) + [_getProxy(callback)]
            self.__commandProxy.perform(command, *cmdArgs)
        else:
            _logger.info(b'Festivity command can not be invoked due to proxy is not defined: cmd = %d', command)
        return
