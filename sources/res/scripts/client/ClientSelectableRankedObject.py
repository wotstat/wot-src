from __future__ import absolute_import
from ClientSelectableObject import ClientSelectableObject
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController

class ClientSelectableRankedObject(ClientSelectableObject):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def onEnterWorld(self, prereqs):
        super(ClientSelectableRankedObject, self).onEnterWorld(prereqs)
        self.__rankedController.onGameModeStatusUpdated += self.__onGameModeStatusUpdate
        self.__onGameModeStatusUpdate()
        return

    def onLeaveWorld(self):
        self.__rankedController.onGameModeStatusUpdated -= self.__onGameModeStatusUpdate
        super(ClientSelectableRankedObject, self).onLeaveWorld()
        return

    def onMouseClick(self):
        super(ClientSelectableRankedObject, self).onMouseClick()
        self.__rankedController.doActionOnEntryPointClick()
        return

    def __onGameModeStatusUpdate(self, *_):
        isEnabled = self.__rankedController.isEnabled()
        hasCurSeason = self.__rankedController.getCurrentSeason() is not None
        hasPrevSeason = self.__rankedController.getPreviousSeason() is not None
        if isEnabled and not hasCurSeason and not hasPrevSeason:
            self.setEnable(False)
        else:
            self.setEnable(True)
        return
