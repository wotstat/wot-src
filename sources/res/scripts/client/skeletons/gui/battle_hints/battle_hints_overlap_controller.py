from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.battle_hints.queues import BattleHint

class IBattleHintsOverlapController(object):

    def fini(self):
        raise NotImplementedError
        return

    def hintShown(self, battleHInt):
        raise NotImplementedError
        return

    def hintHidden(self):
        raise NotImplementedError
        return
