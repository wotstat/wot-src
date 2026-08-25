from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from last_stand.gui.game_control.ls_artefacts_controller import Artefact

class ILSArtefactsController(IGameController):
    onArtefactStatusUpdated = None
    onProgressPointsUpdated = None
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

    def resetSelectedArtefactID(self):
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

    def getKingRewardArtefact(self):
        raise NotImplementedError
        return

    def getRareAttachmentsFromArtefact(self, artefactID):
        raise NotImplementedError
        return

    def getArtefact(self, artefactID):
        raise NotImplementedError
        return

    def isArtefactOpened(self, artefactID):
        raise NotImplementedError
        return

    def remainNotOpened(self, artefactID):
        raise NotImplementedError
        return

    def isArtefactReceived(self, artefactID):
        raise NotImplementedError
        return

    def getProgressPointsQuantity(self):
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

    def getLackOfPointsForArtefact(self, artefactID):
        raise NotImplementedError
        return

    def getLackOfPointsForArtefacts(self):
        raise NotImplementedError
        return

    def getArtefactProgressPointsCost(self, artefactID):
        raise NotImplementedError
        return

    def openArtefact(self, artefactID, isSkipQuest):
        raise NotImplementedError
        return

    def isArtefactHasLootBoxGift(self, artefactID):
        raise NotImplementedError
        return

    def isAnyArtefactsHasLootBoxGift(self):
        raise NotImplementedError
        return

    def getMainGift(self):
        raise NotImplementedError
        return

    def geArtefactIDFromOpenToken(self, token):
        raise NotImplementedError
        return

    def isFinalArtefact(self, artefect):
        raise NotImplementedError
        return

    def isKingRewardArtefact(self, artefect):
        raise NotImplementedError
        return

    def getIndex(self, artefactID):
        raise NotImplementedError
        return

    def isProgressCompleted(self):
        raise NotImplementedError
        return

    def getArtefactIDByIndex(self, index):
        raise NotImplementedError
        return

    def getLastUnopenedArtefactId(self):
        raise NotImplementedError
        return
