from constants import IS_DEVELOPMENT
from gui.Scaleform.daapi.view.battle.classic.minimap import GlobalSettingsPlugin, ClassicTeleportPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.component import MinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap.entries import VehicleEntry
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import ArenaVehiclesPlugin
from helpers import i18n
_MINIMAP_DIMENSIONS = 10
_ANIMATION_SPG = b'enemySPG'
_ANIMATION_ENEMY = b'firstEnemy'

class StoryModeVehicleEntry(VehicleEntry):
    __slots__ = ()

    def getSpottedAnimation(self, pool):
        if self._isEnemy and self._isActive and self._isInAoI:
            if self.getActualSpottedCount() == 1:
                if self._classTag == b'SPG':
                    return _ANIMATION_SPG
                return _ANIMATION_ENEMY
        return b''


class StoryModeArenaVehiclesPlugin(ArenaVehiclesPlugin):
    __slots__ = ()

    def __init__(self, parent):
        super(StoryModeArenaVehiclesPlugin, self).__init__(parent=parent, clazz=StoryModeVehicleEntry)
        return

    def _getDisplayedName(self, vInfo):
        playerName = vInfo.player.name
        if playerName.startswith(b'#'):
            return i18n.makeString(playerName)
        return super(StoryModeArenaVehiclesPlugin, self)._getDisplayedName(vInfo)


class StoryModeMinimapComponent(MinimapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(StoryModeMinimapComponent, self)._setupPlugins(arenaVisitor)
        setup[b'settings'] = GlobalSettingsPlugin
        setup[b'vehicles'] = StoryModeArenaVehiclesPlugin
        if IS_DEVELOPMENT:
            setup[b'teleport'] = ClassicTeleportPlugin
        return setup

    def hasMinimapGrid(self):
        return True

    def getMinimapDimensions(self):
        return _MINIMAP_DIMENSIONS

    def getBoundingBox(self):
        arenaVisitor = self.sessionProvider.arenaVisitor
        bl, tr = arenaVisitor.type.getBoundingBox()
        topRightX, topRightY = tr
        bottomLeftX, bottomLeftY = bl
        vSide = topRightX - bottomLeftX
        hSide = topRightY - bottomLeftY
        if vSide > hSide:
            bl = (
             bottomLeftX, bottomLeftX)
            tr = (topRightX, topRightX)
        else:
            bl = (
             bottomLeftY, bottomLeftY)
            tr = (topRightY, topRightY)
        return (bl, tr)
