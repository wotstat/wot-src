from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Tuple, Optional
    from Event import Event
    from halloween_common.configs.halloween_bestiary import BestiaryModel, EnemyModel
    from halloween.gui.game_control.halloween_bestiary_controller import EnemyData

class IHalloweenBestiaryController(IGameController):
    onSettingsUpdate = None

    def _getConfig(self):
        raise NotImplementedError
        return

    def getEnemyByIntCD(self, intCD):
        raise NotImplementedError
        return

    def getEnemyByToken(self, token):
        raise NotImplementedError
        return

    def getTokenIdxByEnemy(self, enemy):
        raise NotImplementedError
        return

    @property
    def enemies(self):
        raise NotImplementedError
        return

    def hasEnemy(self, token):
        raise NotImplementedError
        return

    def getFirstNewEnemy(self):
        raise NotImplementedError
        return

    @property
    def hasUnlockedEnemies(self):
        raise NotImplementedError
        return

    @property
    def isBestiaryPostponed(self):
        raise NotImplementedError
        return

    @isBestiaryPostponed.setter
    def isBestiaryPostponed(self, value):
        raise NotImplementedError
        return
