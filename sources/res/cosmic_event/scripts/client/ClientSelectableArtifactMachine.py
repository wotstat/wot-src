from ClientSelectableObject import ClientSelectableObject
from skeletons.gui.game_control import ICosmicEventBattleController
from helpers import dependency

class ClientSelectableArtifactMachine(ClientSelectableObject):
    __cosmicController = dependency.descriptor(ICosmicEventBattleController)

    def onEnterWorld(self, prereqs):
        super(ClientSelectableArtifactMachine, self).onEnterWorld(prereqs)
        self.__cosmicController.onPrimeTimeStatusUpdated += self.__onGameModeStatusUpdate
        self.__onGameModeStatusUpdate()
        self.setEnable(True)
        return

    def onLeaveWorld(self):
        self.__cosmicController.onPrimeTimeStatusUpdated -= self.__onGameModeStatusUpdate
        super(ClientSelectableArtifactMachine, self).onLeaveWorld()
        return

    def onMouseClick(self):
        super(ClientSelectableArtifactMachine, self).onMouseClick()
        self.__cosmicController.switchPrb()
        return

    def __onGameModeStatusUpdate(self, *_):
        self.setEnable(self.__cosmicController.isAvailable())
        return
