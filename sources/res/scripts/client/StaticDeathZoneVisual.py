from __future__ import absolute_import, division
import enum, BigWorld
from Math import Vector3, Vector4
from Event import Event
from helpers import dependency
from gui.shared import g_eventBus
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import GameEvent
from gui.doc_loaders import GuiColorsLoader
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.account_helpers.settings_core import ISettingsCore
from account_helpers.settings_core import settings_constants
from script_component.DynamicScriptComponent import DynamicScriptComponent

class _DrawType(enum.IntEnum):
    NORMAL = 0
    STRIPES = 1


class StaticDeathZoneVisual(DynamicScriptComponent):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)
    onShowDeathZone = Event()
    onHideDeathZone = Event()

    def __init__(self):
        super(StaticDeathZoneVisual, self).__init__()
        self._borders = _BordersHelper()
        self._borders.init(self.entity.position, self.deathzone_size)
        self._borderDrawType = _DrawType.NORMAL
        return

    def onDestroy(self):
        self.hide()
        g_eventBus.removeListener(GameEvent.ARENA_BORDER_TYPE_CHANGED, self._onArenaBorderTypeChanged, scope=EVENT_BUS_SCOPE.BATTLE)
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        self.entity.onActiveChanged -= self._onEntityActiveChanged
        return

    def show(self):
        if self.drawBorder:
            self._drawBorders()
        StaticDeathZoneVisual.onShowDeathZone(self.entity.zoneId, self)
        return

    def hide(self):
        if self.drawBorder:
            self._hideBorders()
        StaticDeathZoneVisual.onHideDeathZone(self.entity.zoneId)
        return

    def getClosestPoint(self, point, _):
        closestPoint = self._borders.getClosestPoint(point)
        return (closestPoint, (point - closestPoint).length)

    def getCorners(self):
        return self._borders.rect

    def getDimensions(self):
        return self.deathzone_size

    def _onAvatarReady(self):
        super(StaticDeathZoneVisual, self)._onAvatarReady()
        g_eventBus.addListener(GameEvent.ARENA_BORDER_TYPE_CHANGED, self._onArenaBorderTypeChanged, scope=EVENT_BUS_SCOPE.BATTLE)
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        self.entity.onActiveChanged += self._onEntityActiveChanged
        arenaBorderCtrl = self.sessionProvider.shared.arenaBorder
        if arenaBorderCtrl:
            self._updateBorderDrawType(arenaBorderCtrl.getDrawType())
        if self.entity.isActive:
            self.show()
        return

    def _onEntityActiveChanged(self, isActive):
        if isActive:
            self.show()
        else:
            self.hide()
        return

    def _removeBorders(self):
        spaceID = self._spaceID
        if spaceID:
            BigWorld.ArenaBorderHelper.removeBorder(spaceID, self.zoneIndex)
        return

    def _drawBorders(self):
        spaceID = self._spaceID
        if spaceID:
            BigWorld.ArenaBorderHelper.setBorderBounds(spaceID, self.zoneIndex, self.entity.position, self._borders.bounds)
            color = self.__getCurrentColor(self.settingsCore.getSetting(settings_constants.GRAPHICS.COLOR_BLIND))
            BigWorld.ArenaBorderHelper.setBorderColor(spaceID, self.zoneIndex, color)
            BigWorld.ArenaBorderHelper.setBorderVisible(spaceID, self.zoneIndex, True)
        return

    def _hideBorders(self):
        spaceID = self._spaceID
        if spaceID:
            BigWorld.ArenaBorderHelper.setBorderVisible(spaceID, self.zoneIndex, False)
        return

    def _updateBorderDrawType(self, arenaDrawType):
        self._borderDrawType = _DrawType.STRIPES if arenaDrawType == _DrawType.NORMAL else _DrawType.NORMAL
        spaceID = self._spaceID
        if spaceID:
            BigWorld.ArenaBorderHelper.setBordersDrawType(spaceID, self.zoneIndex, self._borderDrawType)
        return

    def _onArenaBorderTypeChanged(self, event):
        self._updateBorderDrawType(event.ctx[b'drawType'])
        return

    @property
    def _spaceID(self):
        player = BigWorld.player()
        if player and player.spaceID:
            return player.spaceID
        else:
            return

    def __onSettingsChanged(self, diff):
        if settings_constants.GRAPHICS.COLOR_BLIND in diff:
            color = self.__getCurrentColor(diff[settings_constants.GRAPHICS.COLOR_BLIND])
            spaceID = self._spaceID
            if spaceID:
                BigWorld.ArenaBorderHelper.setBorderColor(spaceID, self.zoneIndex, color)
        return

    def __getCurrentColor(self, colorBlind):
        colors = GuiColorsLoader.load()
        scheme = colors.getSubScheme(b'areaBorder', b'color_blind' if colorBlind else b'default')
        color = scheme[b'rgba'] / 255
        return color


class _BordersHelper(object):

    def __init__(self):
        self._bounds = Vector4(0, 0, 0, 0)
        self._min = Vector3(0, 0, 0)
        self._max = Vector3(0, 0, 0)
        return

    def init(self, center, size):
        self._bounds = Vector4(-size.x / 2, -size.z / 2, size.x / 2, size.z / 2)
        self._min = Vector3(center.x + self._bounds[0], center.y, center.z + self._bounds[3])
        self._max = Vector3(center.x + self._bounds[2], center.y, center.z + self._bounds[1])
        return

    def getClosestPoint(self, point):
        x = min(max(point[0], self._min.x), self._max.x)
        z = min(max(point[2], self._max.z), self._min.z)
        if x != point.x or z != point.z:
            return Vector3(x, point.y, z)
        return self._max

    @property
    def rect(self):
        return (self._min, self._max)

    @property
    def bounds(self):
        return self._bounds
