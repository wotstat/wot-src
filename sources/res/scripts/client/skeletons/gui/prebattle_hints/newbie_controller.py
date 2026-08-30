from __future__ import absolute_import
from skeletons.gui.prebattle_hints.controller import IPrebattleHintsControlStrategy

class INewbiePrebattleHintsController(IPrebattleHintsControlStrategy):

    def fini(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def onConfirmationWindowShown(self):
        raise NotImplementedError
        return
