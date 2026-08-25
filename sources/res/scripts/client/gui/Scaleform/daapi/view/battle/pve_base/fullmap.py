from __future__ import absolute_import, division
import GUI
from gui.Scaleform.daapi.view.battle.classic.minimap import GlobalSettingsPlugin
from gui.Scaleform.daapi.view.battle.pve_base.minimap import PveMinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import PersonalEntriesPlugin
from gui.Scaleform.genConsts.LAYER_NAMES import LAYER_NAMES
from gui.battle_control import minimap_utils
_FLASH_NAME = b'pveFullMap'
_MINIMAP_COMPONENT_PATH = (b'_level0.root.{}.main.{}.entriesContainer').format(LAYER_NAMES.VIEWS, _FLASH_NAME)
_MINIMAP_SIZE = (352, 352)

class PveFullMapGlobalSettingsPlugin(GlobalSettingsPlugin):

    def _toogleVisible(self):
        return


class PveFullMapPersonalEntriesPlugin(PersonalEntriesPlugin):
    __slots__ = ()

    def __init__(self, parentObj):
        super(PveFullMapPersonalEntriesPlugin, self).__init__(parentObj)
        bottomLeft, upperRight = self._parentObj.getBoundingBox()
        width = upperRight[0] - bottomLeft[0]
        self.setDefaultViewRangeCircleSize(width * minimap_utils.MINIMAP_SIZE[0] / _MINIMAP_SIZE[0])
        return


class PveFullMapComponent(PveMinimapComponent):

    def setMinimapCenterEntry(self, entityID):
        return

    def setVisibleRect(self, bl, tr):
        return

    def setZoom(self, zoom):
        return

    def _setupPlugins(self, arenaVisitor):
        setup = super(PveFullMapComponent, self)._setupPlugins(arenaVisitor)
        setup[b'settings'] = PveFullMapGlobalSettingsPlugin
        setup[b'personal'] = PveFullMapPersonalEntriesPlugin
        return setup

    def _getFlashName(self):
        return _FLASH_NAME

    def _createFlashComponent(self):
        return GUI.WGPveMinimapGUIComponentAS3(self.app.movie, _MINIMAP_COMPONENT_PATH)

    def _getMinimapSize(self):
        return _MINIMAP_SIZE
