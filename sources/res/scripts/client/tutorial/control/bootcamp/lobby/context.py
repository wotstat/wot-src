from tutorial.control import context
from helpers import dependency
from skeletons.gui.game_control import IBootcampController

class BootcampLobbyStartReqs(context.StartReqs):

    def isEnabled(self):
        return self.bootcampController.isInBootcamp()

    def prepare(self, ctx):
        return

    def process(self, descriptor, ctx):
        return True


class BootcampBonusesRequester(context.BonusesRequester):
    bootcampController = dependency.descriptor(IBootcampController)

    def __init__(self):
        lessonNum = self.bootcampController.getLessonNum()
        wonBattlesMask = (1 << lessonNum) - 1
        super(BootcampBonusesRequester, self).__init__(completed=wonBattlesMask)
        return

    def setCompleted(self, _):
        return

    def request(self, _=None):
        return
