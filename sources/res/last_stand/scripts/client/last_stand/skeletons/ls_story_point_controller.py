from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class ILSStoryPointController(IGameController):
    FIRST_STORY_POINT_INDEX = None
    onStoryPointStatusUpdated = None

    @property
    def selectedStoryPointID(self):
        raise NotImplementedError
        return

    @selectedStoryPointID.setter
    def selectedStoryPointID(self, artefactID):
        raise NotImplementedError
        return

    @property
    def storyPoints(self):
        raise NotImplementedError
        return

    def getIndex(self, storyPointID):
        raise NotImplementedError
        return

    def getStoryPointIDByIndex(self, index):
        raise NotImplementedError
        return

    def getStoryPointsCount(self):
        raise NotImplementedError
        return

    def isStoryPointReceived(self, storyPointID):
        raise NotImplementedError
        return
