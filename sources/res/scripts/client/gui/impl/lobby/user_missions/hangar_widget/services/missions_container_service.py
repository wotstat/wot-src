from __future__ import absolute_import
import logging
from future.utils import viewvalues, viewitems
from typing import TYPE_CHECKING
from gui.impl.lobby.user_missions.hangar_widget.services import IMissionsContainerService
from gui.shared import g_eventBus, events
from gui.shared.system_factory import collectUserMissionPlugins
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
import Event
if TYPE_CHECKING:
    from typing import Any, Dict, Optional
    from gui.impl.lobby.user_missions.hangar_widget.plugins import IUserMissionPlugin
_logger = logging.getLogger(__name__)

class MissionsContainerService(IMissionsContainerService):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(MissionsContainerService, self).__init__()
        self.onShowPlugin = Event.Event()
        self.onHidePlugin = Event.Event()
        self._plugins = {}
        self._visiblePlugins = set()
        self._selectedSlides = {}
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADING, self._collectPlugins)
        return

    def isPluginVisible(self, viewAlias):
        return viewAlias in self._visiblePlugins

    def showPlugin(self, viewAlias):
        plugin = self._plugins.get(viewAlias)
        if plugin is not None:
            self._visiblePlugins.add(viewAlias)
            _logger.debug(b'Plugin %s was added to visible plugins %s', viewAlias, self._visiblePlugins)
            self.onShowPlugin(plugin)
        else:
            _logger.error(b'Failed to show plugin. Alias %s not in plugins %s', viewAlias, self._plugins)
        return

    def hidePlugin(self, viewAlias):
        if viewAlias in self._visiblePlugins:
            self._visiblePlugins.remove(viewAlias)
            _logger.debug(b'Plugin with alias %s was hidden', viewAlias)
            self.onHidePlugin(viewAlias)
        return

    def getVisiblePlugins(self):
        return {alias: self._plugins[alias] for alias in self._visiblePlugins if self._plugins.get(alias) is not None}

    def getSelectedSlide(self, sliderId):
        return self._selectedSlides.get(sliderId)

    def onSlideChanged(self, selectedSlide):
        sliderId = selectedSlide.get(b'sliderId')
        slideId = selectedSlide.get(b'slideId')
        if sliderId and slideId:
            self._selectedSlides[sliderId] = slideId
        return

    def finalize(self):
        g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADING, self._collectPlugins)
        for plugin in viewvalues(self._plugins):
            plugin.stopListening()

        self._plugins.clear()
        self._visiblePlugins.clear()
        self._selectedSlides.clear()
        self.onShowPlugin.clear()
        self.onHidePlugin.clear()
        return

    def _updateVisiblePlugins(self):
        for alias, plugin in viewitems(self._plugins):
            if plugin.isPluginEnabled():
                self._visiblePlugins.add(alias)

        return

    def _collectPlugins(self, _):
        for plugin in collectUserMissionPlugins():
            self._plugins[plugin.getViewAlias()] = plugin
            plugin.startListening()

        self._updateVisiblePlugins()
        return
