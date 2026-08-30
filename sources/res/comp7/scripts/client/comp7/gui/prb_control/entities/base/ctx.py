from gui.prb_control.entities.base.ctx import PrbAction
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getSquadSize', b'squadSize'))
class Comp7PrbAction(PrbAction):

    def __init__(self, actionName, squadSize, mmData=0, accountsToInvite=None):
        super(Comp7PrbAction, self).__init__(actionName, mmData, accountsToInvite)
        self.__squadSize = squadSize
        return

    def getSquadSize(self):
        return self.__squadSize
