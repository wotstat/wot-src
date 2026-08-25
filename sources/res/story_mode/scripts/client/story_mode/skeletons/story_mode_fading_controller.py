from skeletons.gui.game_control import IGameController

class IStoryModeFadingController(IGameController):

    def show(self, layerID):
        raise NotImplementedError
        return

    def hide(self, layerID):
        raise NotImplementedError
        return
