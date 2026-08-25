from __future__ import absolute_import
import logging
from typing import TYPE_CHECKING
import AccountCommands
from Event import Event
from constants import CommendationsState
from script_component.DynamicScriptComponent import DynamicScriptComponent
if TYPE_CHECKING:
    from typing import Dict, List
    from commendations_common.CommendationHelpers import CommendationStateType, CommendationsSource
_logger = logging.getLogger(__name__)

class AvatarCommendations(DynamicScriptComponent):

    def __init__(self):
        super(AvatarCommendations, self).__init__()
        _logger.debug(b'CommendationsController initialised!')
        self._messageStateMap = {}
        self.onStateUpdate = Event()
        return

    def onDestroy(self):
        super(AvatarCommendations, self).onDestroy()
        self.onStateUpdate.clear()
        return

    def set_commendationsState(self, oldState):
        self.updateMessageStateMap()
        return

    def setNested_commendationsState(self, path, oldState):
        self.updateMessageStateMap()
        return

    def updateMessageStateMap(self):
        self._messageStateMap = {state[b'vehID']: CommendationsState(state[b'messageState']) for state in self.commendationsState}
        self.onStateUpdate()
        return

    def getMessageStateForVehID(self, vehID):
        return self._messageStateMap.get(vehID, CommendationsState.UNSENT)

    def sendCommendation(self, recipientID, source):
        self.cell.sendCommendation(recipientID, source)
        return

    def clearMessageState(self, callback=None):
        if callback is None:

            def __defaultLogger(resultID, errorCode):
                _logger.debug(b'Action performed: "activateGoodie" resultID=%s, errorCode=%s', resultID, errorCode)
                return

            callback = __defaultLogger
        self.entity._doCmdNoArgs(AccountCommands.CMD_CLEAR_COMMENDATIONS_MESSAGE_STATE, (lambda requestID, resultID, errorCode, ext=None: callback(resultID, errorCode)))
        return
