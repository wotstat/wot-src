from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from account_helpers.pet_system import PetSystem
    from gui.pet_system.requester import PetRequesterRequester
    from gui.pet_system.pet_animation_helper import PetPrefabProxy, StoragePrefabProxy
    from pet_system_common.EventConfig import EventConfig
    from pet_system_common.GeneralConfig import GeneralConfig
    from pet_system_common.PetConfig import PetConfig
    from pet_system_common.BonusConfig import BonusConfig
    from pet_system_common.PetPromoConfig import PetPromoConfig
    from pet_system_common.PetSynergyConfig import PetSynergyConfig
    from typing import List, Set, Optional
    from Event import Event
    EventID = str
    PetID = int
    NameID = int
    BonusID = int
    PlaceName = str
    StaticTrigger = int
    Synergy = int
    StateBehavior = int

class IPetSystemController(IGameController):
    onUpdateActivePet = None
    onUpdatePrefab = None
    onUpdateEventData = None
    onUpdateUnlockedPetsIDs = None
    onUpdateAppliedBonus = None
    onUpdateSynergy = None
    onUpdateCanInteractInHangar = None

    @property
    def petProxy(self):
        raise NotImplementedError
        return

    @property
    def storageProxy(self):
        raise NotImplementedError
        return

    @property
    def isInStorage(self):
        raise NotImplementedError
        return

    @property
    def isInEventFulscreen(self):
        raise NotImplementedError
        return

    @property
    def petInHangar(self):
        raise NotImplementedError
        return

    @property
    def canInteractInHangar(self):
        raise NotImplementedError
        return

    @property
    def commandSender(self):
        raise NotImplementedError
        return

    @property
    def requester(self):
        raise NotImplementedError
        return

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    def getActiveEvent(self):
        raise NotImplementedError
        return

    def isFirstClickEnable(self):
        raise NotImplementedError
        return

    def getPetsConfig(self):
        raise NotImplementedError
        return

    def getBonusConfig(self):
        raise NotImplementedError
        return

    def getGeneralConfig(self):
        raise NotImplementedError
        return

    def getPetEventConfig(self):
        raise NotImplementedError
        return

    def getPetsPromoConfig(self):
        raise NotImplementedError
        return

    def getPetSynergyConfig(self):
        raise NotImplementedError
        return

    def onStorageEntered(self):
        return

    def onStorageExited(self):
        return

    def addPetDev(self, petID):
        raise NotImplementedError
        return

    def buyPet(self, petID):
        raise NotImplementedError
        return

    def changePet(self, petID):
        raise NotImplementedError
        return

    def selectActivePet(self, petID):
        raise NotImplementedError
        return

    def selectPetStateBehavior(self, stateBehavior):
        raise NotImplementedError
        return

    def selectPetName(self, petID, nameID):
        raise NotImplementedError
        return

    def showEventView(self, isFullScreen=False):
        raise NotImplementedError
        return

    def sendFirstClick(self):
        raise NotImplementedError
        return

    def getActivePet(self):
        raise NotImplementedError
        return

    def getUnlockedPets(self):
        raise NotImplementedError
        return

    def getAvailableNames(self):
        raise NotImplementedError
        return

    def getAvailableBonuses(self):
        raise NotImplementedError
        return

    def getPetIDInHangar(self):
        raise NotImplementedError
        return

    def isPetInHangarPromoting(self):
        raise NotImplementedError
        return

    def getStateBehavior(self):
        raise NotImplementedError
        return

    def addSynergyDev(self, synergyPoints, petID=None):
        raise NotImplementedError
        return

    def haveActivePromotion(self):
        raise NotImplementedError
        return

    def getUnlockedAndPromoPets(self):
        raise NotImplementedError
        return

    def checkBonusCapsForPetBonus(self):
        raise NotImplementedError
        return
