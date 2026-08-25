from __future__ import absolute_import
import ResMgr
from chat_commands_consts import MarkerType
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import BaseMinimapMarkerComponent, World2DActionMarkerComponent, ComponentBitMask, World2DLocationMarkerComponent
from gui.impl.backport import getIntegralFormat

class PveAttackDirectionComponent(BaseMinimapMarkerComponent):

    @classmethod
    def configReader(cls, section):
        config = super(PveAttackDirectionComponent, cls).configReader(section)
        config.update({b'bitmapName': (section.readString(b'bitmapName', b'')), 
           b'isFlipped': (section.readBool(b'isFlipped', False))})
        return config

    def _setupMarker(self, gui, **kwargs):
        super(PveAttackDirectionComponent, self)._setupMarker(gui, **kwargs)
        gui.invoke(self._componentID, b'setArrow', self._config[b'bitmapName'], self._config[b'isFlipped'])
        isReconnect = kwargs.get(b'isReconnect', False)
        if not isReconnect:
            gui.invoke(self._componentID, b'animate')
        return


class PveAttackDirectionMinimapComponent(PveAttackDirectionComponent):

    @property
    def maskType(self):
        return ComponentBitMask.MINIMAP_MARKER


class PveAttackDirectionFullscreenMapComponent(PveAttackDirectionComponent):

    @property
    def maskType(self):
        return ComponentBitMask.FULLSCREEN_MAP_MARKER


class PveFlagMinimapComponent(BaseMinimapMarkerComponent):

    def _setupMarker(self, gui, **kwargs):
        isReconnect = kwargs.get(b'isReconnect', False)
        if not isReconnect:
            gui.invoke(self._componentID, b'animate')
        return

    @property
    def maskType(self):
        return ComponentBitMask.MINIMAP_MARKER


class PveFlagFullscreenMapComponent(BaseMinimapMarkerComponent):

    def _setupMarker(self, gui, **kwargs):
        isReconnect = kwargs.get(b'isReconnect', False)
        if not isReconnect:
            gui.invoke(self._componentID, b'animate')
        return

    @property
    def maskType(self):
        return ComponentBitMask.FULLSCREEN_MAP_MARKER


class PveTargetFlagMinimapComponent(BaseMinimapMarkerComponent):

    @property
    def maskType(self):
        return ComponentBitMask.MINIMAP_MARKER


class PveTargetFlagFullscreenMapComponent(BaseMinimapMarkerComponent):

    @property
    def maskType(self):
        return ComponentBitMask.FULLSCREEN_MAP_MARKER


class PveFlagLocationMarkerComponent(World2DLocationMarkerComponent):

    def _setupMarker(self, gui, **kwargs):
        super(PveFlagLocationMarkerComponent, self)._setupMarker(gui, **kwargs)
        gui.invokeMarker(self.componentID, b'stopAnimation')
        return

    @property
    def bcMarkerType(self):
        return MarkerType.NON_INTERACTIVE


class PveFlagVehicleMarkerComponent(World2DActionMarkerComponent):

    def __init__(self, *args, **kwargs):
        super(PveFlagVehicleMarkerComponent, self).__init__(*args, **kwargs)
        self._vehicleMarkerGUI = None
        return

    @classmethod
    def configReader(cls, section):
        config = super(PveFlagVehicleMarkerComponent, cls).configReader(section)
        config.update({b'symbolIndex': (section.readInt(b'symbolIndex', 0)), 
           b'symbolOffset': (section.readInt(b'symbolOffset', 0))})
        return config

    def attachGUI(self, guiProvider, **kwargs):
        self._vehicleMarkerGUI = guiProvider.getVehicleMarkerPlugin()
        return super(PveFlagVehicleMarkerComponent, self).attachGUI(guiProvider, **kwargs)

    def update(self, distance, *args, **kwargs):
        super(PveFlagVehicleMarkerComponent, self).update(distance, *args, **kwargs)
        self._updateDistance(distance)
        return

    def clear(self):
        super(PveFlagVehicleMarkerComponent, self).clear()
        self._vehicleMarkerGUI = None
        return

    def _setupMarker(self, gui, **kwargs):
        super(PveFlagVehicleMarkerComponent, self)._setupMarker(gui, **kwargs)
        self._insertSymbol()
        return

    def _deleteMarker(self):
        self._removeSymbol()
        super(PveFlagVehicleMarkerComponent, self)._deleteMarker()
        return

    def _getVehicleMarker(self):
        if self._vehicleMarkerGUI:
            return self._vehicleMarkerGUI.getVehicleMarker(self._targetID)
        else:
            return

    def _insertSymbol(self):
        vehicleMarker = self._getVehicleMarker()
        if vehicleMarker:
            self._vehicleMarkerGUI.invokeMarker(vehicleMarker.getMarkerID(), b'insertSymbol', self._config[b'symbol'], self._config[b'symbolIndex'], self._config[b'symbolOffset'])
            self._vehicleMarkerGUI.invokeMarker(vehicleMarker.getMarkerID(), b'callInsertedSymbolMethod', self._config[b'symbol'], b'setMeters', self._METERS_STRING)
        return

    def _removeSymbol(self):
        vehicleMarker = self._getVehicleMarker()
        if vehicleMarker:
            self._vehicleMarkerGUI.invokeMarker(vehicleMarker.getMarkerID(), b'removeSymbol', self._config[b'symbol'])
        return

    def _updateDistance(self, distance):
        vehicleMarker = self._getVehicleMarker()
        if vehicleMarker:
            self._vehicleMarkerGUI.invokeMarker(vehicleMarker.getMarkerID(), b'callInsertedSymbolMethod', self._config[b'symbol'], b'setDistance', getIntegralFormat(distance))
        return


class PveAnimatedFlagMarkerComponent(World2DLocationMarkerComponent):

    @property
    def bcMarkerType(self):
        return MarkerType.NON_INTERACTIVE
