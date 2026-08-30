from skeletons.gui.game_control import IGameController

class IEventController(IGameController):

    def isEnabled(self):
        raise NotImplementedError
        return

    def getEventStartTime(self):
        raise NotImplementedError
        return

    def getEventFinishTime(self):
        raise NotImplementedError
        return
