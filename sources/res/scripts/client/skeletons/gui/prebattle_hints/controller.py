from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from hints_common.prebattle.schemas import BaseHintModel

class IPrebattleHintsController(object):

    def fini(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isEnabledForCurrentBattleSession(self):
        raise NotImplementedError
        return

    def addControlStrategy(self, arenaBonusType, strategy):
        raise NotImplementedError
        return

    def removeControlStrategy(self, arenaBonusType):
        raise NotImplementedError
        return

    def onShowHintsWindowSuccess(self, hint):
        raise NotImplementedError
        return


class IPrebattleHintsControlStrategy(object):

    def hasHintToShow(self, arenaBonusType):
        raise NotImplementedError
        return

    def getHintToShow(self, arenaBonusType):
        raise NotImplementedError
        return

    def onShowHintsWindowSuccess(self, hint):
        raise NotImplementedError
        return
