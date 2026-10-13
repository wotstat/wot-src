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
                if decodePrice.currency is None or decodePrice.amount > controller.getArtefactKeyQuantity():
                    return makeError(b'server_error')
            else:
                skipPrice = artefact.skipPrice
                if skipPrice.currency is None or skipPrice.amount > controller.getArtefactKeyQuantity():
                    return makeError(b'server_error')
            return makeSuccess()


class CheckTwitchCon(SyncValidator):

    def __init__(self, controller, commanderIDs, isEnabled=True):
        super(CheckTwitchCon, self).__init__(isEnabled)
        self.controller = controller
        self.commanderIDs = commanderIDs
        return

    def _validate(self):
        controller = self.controller
        if not controller.isEnabled():
            return makeError(b'server_error')
        usesCerts = 0
        for commanderID, count in self.commanderIDs:
            usesCerts += count
            if count <= 0:
                return makeError(b'server_error')
            if controller.getRemainLimits(commanderID) - count < 0:
                return makeError(b'server_error')

        if usesCerts > controller.getCertificateCount():
            return makeError(b'server_error')
        return makeSuccess()
