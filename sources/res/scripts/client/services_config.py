from __future__ import absolute_import
import logging
__all__ = (b'getClientServicesConfig',)
_logger = logging.getLogger(__name__)

def getClientServicesConfig(manager):
    import account_helpers, connection_mgr, MapActivities, dyn_objects_cache, gui, gameplay, helpers, uilogging, festivity
    from vehicle_systems.appearance_cache import AppearanceCache
    from skeletons.connection_mgr import IConnectionManager
    from skeletons.map_activities import IMapActivities
    from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache
    from skeletons.vehicle_appearance_cache import IAppearanceCache
    from system_events import g_systemEvents
    manager.addInstance(IConnectionManager, connection_mgr.ConnectionManager(), finalizer=b'fini')
    manager.addInstance(IMapActivities, MapActivities.MapActivities(), finalizer=b'destroy')
    manager.addInstance(IBattleDynamicObjectsCache, dyn_objects_cache.BattleDynamicObjectsCache(), finalizer=b'destroy')
    manager.addInstance(IAppearanceCache, AppearanceCache(), finalizer=b'clear')
    manager.addConfig(account_helpers.getAccountHelpersConfig)
    manager.addConfig(gameplay.getGameplayConfig)
    manager.addConfig(festivity.getFestivityConfig)
    g_systemEvents.onFestivityConfigReady(manager)
    manager.addConfig(gui.getGuiServicesConfig)
    manager.addConfig(uilogging.getUILoggingConfig)
    manager.addConfig(helpers.getHelperServicesConfig)
    from gui import GUI_SETTINGS
    if GUI_SETTINGS.isGuiEnabled():
        try:
            import tutorial
        except ImportError:
            _logger.exception(b'Module tutorial not found')
            from helpers import tutorial

    else:
        from helpers import tutorial
    manager.addConfig(tutorial.getTutorialConfig)
    return
