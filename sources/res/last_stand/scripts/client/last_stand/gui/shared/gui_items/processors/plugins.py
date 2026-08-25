from __future__ import absolute_import
from gui.shared.gui_items.processors.plugins import SyncValidator, makeError, makeSuccess

class CheckArtefact(SyncValidator):

    def __init__(self, controller, artefactID, isSkipQuest, isEnabled=True):
        super(CheckArtefact, self).__init__(isEnabled)
        self.controller = controller
        self.artefactID = artefactID
        self.isSkipQuest = isSkipQuest
        return

    def _validate(self):
        controller = self.controller
        if not controller.isEnabled():
            return makeError(b'server_error')
        else:
            artefact = controller.getArtefact(self.artefactID)
            if not self.isSkipQuest:
                if not controller.isArtefactReceived(self.artefactID):
                    return makeError(b'server_error')
                decodePrice = artefact.decodePrice
                if decodePrice.currency is None or decodePrice.amount > controller.getProgressPointsQuantity():
                    return makeError(b'server_error')
            else:
                skipPrice = artefact.skipPrice
                if skipPrice.currency is None or skipPrice.amount > controller.getProgressPointsQuantity():
                    return makeError(b'server_error')
            return makeSuccess()
