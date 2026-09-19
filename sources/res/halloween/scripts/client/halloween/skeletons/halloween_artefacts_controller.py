from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle
    from halloween.gui.game_control.halloween_artefacts_controller import Artefact

class IHalloweenArtefactsController(IGameController):
    onArtefactStatusUpdated = None
    onArtefactKeyUpdated = None
    onArtefactSettingsUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def selectedArtefactID(self):
        raise NotImplementedError
        return

    @selectedArtefactID.setter
    def selectedArtefactID(self, artefactID):
        raise NotImplementedError
        return

    @property
    def needSelectNextSlide(self):
        raise NotImplementedError
        return

    @needSelectNextSlide.setter
    def needSelectNextSlide(self, value):
        raise NotImplementedError
        return

    def artefactsSorted(self):
        raise NotImplementedError
        return

    def regularArtefacts(self):
        raise NotImplementedError
        return

    def getFinalArtefact(self):
        raise NotImplementedError
        return

    def getArtefact(self, artefactID):
        raise NotImplementedError
        return

    def isArtefactOpened(self, artefactID):
        raise NotImplementedError
        return

    def isArtefactReceived(self, artefactID):
        raise NotImplementedError
        return

    def getArtefactKeyQuantity(self):
        raise NotImplementedError
        return

    def getCurrentArtefactProgress(self):
        raise NotImplementedError
        return

    def getAvailableArtefactProgress(self):
        raise NotImplementedError
        return

    def getMaxArtefactsProgress(self):
        raise NotImplementedError
        return

    def getArtefactsCount(self):
        raise NotImplementedError
        return

    def getRareAttachmentsFromArtefact(self, artefactID):
        raise NotImplementedError
        return

    def isArtefactHasTwitchConCertificate(self, artefactID):
        raise NotImplementedError
        return

    def isExistUnreceivedTwitchConCertificate(self):
        raise NotImplementedError
        return

    def getArtefactIDForAccessToVehicle(self, vehTypeCD):
        raise NotImplementedError
        return

    def getLackOfKeysForArtefact(self, artefactID):
        raise NotImplementedError
        return

    def getLackOfKeysForArtefacts(self):
        raise NotImplementedError
        return

    def getQuest(self, questID):
        raise NotImplementedError
        return

    def openArtefact(self, artefactID, isSkipQuest):
        raise NotImplementedError
        return

    def getMainGiftVehicle(self):
        raise NotImplementedError
        return

    def getMainGiftStyle(self):
        raise NotImplementedError
        return

    def getOpenedArtefactToken(self, artefactID):
        raise NotImplementedError
        return

    def geArtefactIDFromOpenToken(self, token):
        raise NotImplementedError
        return

    def isFinalArtefact(self, artefect):
        raise NotImplementedError
        return

    def getIndex(self, artefactID):
        raise NotImplementedError
        return

    def isProgressCompleted(self):
        raise NotImplementedError
        return

    def resetSelectedArtefactID(self):
        raise NotImplementedError
        return

    def getArtefactIDByIndex(self, index):
        raise NotImplementedError
        return
