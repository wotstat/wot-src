from __future__ import absolute_import
from skeletons.gui.game_control import IGameController
import typing
if typing.TYPE_CHECKING:
    from Event import Event
    from halloween_common.halloween_constants import QUEUE_TYPE
    from halloween.gui.halloween_gui_constants import DifficultyLevel
    from halloween.gui.game_control.difficulty_level_controller import _Level

class IDifficultyLevelController(IGameController):
    onChangeDifficultyLevelStatus = None
    onChangeDifficultyLevel = None

    def selectLevel(self, level):
        raise NotImplementedError
        return

    def getSelectedLevel(self):
        raise NotImplementedError
        return

    def getCurrentQueueType(self):
        raise NotImplementedError
        return

    def getLevelsInfo(self):
        raise NotImplementedError
        return

    @staticmethod
    def getLastSelectedLevel():
        raise NotImplementedError
        return
