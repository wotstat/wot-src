from debug_utils import LOG_DEBUG
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.game_control import IEpicBattleController

class AvatarFrontlineComponent(DynamicScriptComponent):
    __battleController = dependency.descriptor(IEpicBattleController)

    def onDestroy(self):
        super(AvatarFrontlineComponent, self).onDestroy()
        self.__battleController.reset()
        return

    def set_sectors(self, _):
        self.__battleController.setOwnSectors(self.sectors)
        LOG_DEBUG(b'[EPIC_QUEST] New sectors', self.sectors)
        return

    def set_questName(self, _):
        LOG_DEBUG(b'[EPIC_QUEST] New quest', self.questName)
        self.__battleController.setQuest(self.questName)
        return

    def set_sectorProgression(self, _):
        self.__battleController.setSectorProgression(self.sectorProgression)
        LOG_DEBUG(b'[EPIC_QUEST] New sectorProgression', self.sectorProgression)
        return

    def updateQuestProgress(self, questName, progressesInfo):
        LOG_DEBUG(b'[EPIC_QUEST] Progress:', self.questName, questName, progressesInfo)
        self.__battleController.updateQuestProgress(questName, progressesInfo)
        return

    def notifySupplyActivated(self, supplyTypeID):
        LOG_DEBUG(b'[EPIC_PROGRESSION] Supply activated:', supplyTypeID)
        self.__battleController.onSupplyActivated(supplyTypeID)
        return

    def notifyAirshipCome(self, isAlly):
        LOG_DEBUG(b'[EPIC_PROGRESSION] Airship Come')
        self.__battleController.onAirshipCome(isAlly)
        return

    def setCurrentSector(self, sectorID):
        self.__battleController.setCurrentSector(sectorID)
        return

    def _onAvatarReady(self):
        if self.questName:
            self.__battleController.setQuest(self.questName)
        if self.sectors:
            self.__battleController.setOwnSectors(self.sectors)
        if self.sectorProgression:
            self.__battleController.setSectorProgression(self.sectorProgression)
        return
