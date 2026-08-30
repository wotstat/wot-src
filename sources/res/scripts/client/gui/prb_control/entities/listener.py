from gui.prb_control.entities.base.legacy.listener import ILegacyListener
from gui.prb_control.entities.base.listener import IPrbListener
from gui.prb_control.entities.base.pre_queue.listener import IPreQueueListener
from gui.prb_control.entities.base.unit.listener import IUnitListener, IStrongholdListener

class IGlobalListener(ILegacyListener, IUnitListener, IPreQueueListener, IStrongholdListener, IPrbListener):

    def onPrbEntitySwitching(self):
        return

    def onPrbEntitySwitched(self):
        return

    def startGlobalListening(self):
        if self.prbDispatcher:
            self.prbDispatcher.addListener(self)
        return

    def stopGlobalListening(self):
        if self.prbDispatcher:
            self.prbDispatcher.removeListener(self)
        return
