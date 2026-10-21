import typing
from events_core_client.skeletons.event_controller import IEventController
from skeletons.gui.game_control import ISeasonProvider
if typing.TYPE_CHECKING:
    from typing import Optional
    from Event import Event

class IPortalEventController(IEventController, ISeasonProvider):
    onPrimeTimeStatusUpdated = None
    onPortalBattleConfigChanged = None
    onVehicleUpgradesMasksChanged = None
    onVehicleExperienceChanged = None
    onComplexityLevelChanged = None
    onMaxAvailableComplexityLevelChanged = None
    onPortalSquadStateChanged = None

    def isAvailable(self):
        raise NotImplementedError
        return

    def isFrozen(self):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return

    @property
    def battleLevel(self):
        raise NotImplementedError
        return

    @battleLevel.setter
    def battleLevel(self, battleLevel):
        raise NotImplementedError
        return

    @property
    def maxComplexityLevel(self):
        raise NotImplementedError
        return

    def setMaxAvailableComplexityLevel(self, maxAvailableComplexityLevel):
        raise NotImplementedError
        return

    def onSquadBattleLevelChanged(self, battleLevel):
        raise NotImplementedError
        return

    def selectRandomBattle(self):
        raise NotImplementedError
        return

    def selectPortal(self):
        raise NotImplementedError
        return

    def getQuestRewards(self, questID):
        raise NotImplementedError
        return

    def getCurrentStampsCount(self):
        raise NotImplementedError
        return

    def getCurrentLevel(self):
        raise NotImplementedError
        return

    def getDeserializedUpgradeTreeLevel(self, vehicle, level):
        raise NotImplementedError
        return

    def getUpgradeLevel(self, vehicle):
        raise NotImplementedError
        return

    def getCurrentVehicleLevel(self, vehicle):
        raise NotImplementedError
        return

    def getMaxUnlockedLevel(self, vehicle):
        raise NotImplementedError
        return

    def canUpgradeVehicle(self, vehicle):
        raise NotImplementedError
        return

    def getVehicleUpgradeTree(self, vehicle):
        raise NotImplementedError
        return

    def getVehicleUpgradeNodes(self, vehicle):
        raise NotImplementedError
        return

    def getVehicleExperience(self, vehicle):
        raise NotImplementedError
        return

    def getComplexityLevelStatus(self, level):
        raise NotImplementedError
        return

    def isComplexityLevelLocked(self, level):
        raise NotImplementedError
        return

    def getComplexityRecommendedVehicleLvl(self, level):
        raise NotImplementedError
        return

    def getVehicleAbilities(self, vehicle, includeLocked=False):
        raise NotImplementedError
        return

    def getVehicleModifiers(self, vehicle):
        raise NotImplementedError
        return

    def getStampsNeededForStage(self, level):
        raise NotImplementedError
        return

    def getSeasonStartEndDate(self):
        raise NotImplementedError
        return

    def getBadges(self):
        raise NotImplementedError
        return

    def getMedals(self):
        raise NotImplementedError
        return

    def getAbilityDuration(self, abilityName):
        raise NotImplementedError
        return

    def getAbilityCooldown(self, abilityName):
        raise NotImplementedError
        return

    def getTotalLevelsCount(self):
        raise NotImplementedError
        return

    def getProgression(self):
        return NotImplementedError

    def onLobbyInited(self, event):
        return

    def onPrbEnter(self):
        return

    def onPrbLeave(self):
        return

    def getOrderedPortalVehicles(self):
        raise NotImplementedError
        return

    def setCurrentSelectedVehicle(self, vehicleID):
        raise NotImplementedError
        return

    def selectNextPortalVehicle(self):
        raise NotImplementedError
        return

    def selectPrevPortalVehicle(self):
        raise NotImplementedError
        return

    def getPortalVehicleByInvID(self, invID):
        raise NotImplementedError
        return

    def getCurrentSelectedVehicle(self):
        raise NotImplementedError
        return

    def getFinishedLevelsCount(self):
        raise NotImplementedError
        return

    def getCurrentStampsAtLevel(self, level):
        raise NotImplementedError
        return

    def upgradeCurrentVehicle(self, upgradeNodeNumber):
        raise NotImplementedError
        return

    def resetCurrentVehicleUpgrades(self):
        raise NotImplementedError
        return

    def showOutroVideo(self):
        raise NotImplementedError
        return

    def showIntroVideo(self):
        raise NotImplementedError
        return
