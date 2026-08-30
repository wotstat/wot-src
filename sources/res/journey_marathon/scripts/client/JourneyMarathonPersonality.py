from __future__ import absolute_import
import logging
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig
from gui.shared.system_factory import registerBannerEntryPointValidator
from journey_marathon.gui.game_control import registerJMSystemHandlers
from journey_marathon.gui.impl.lobby.gf_notifications import registerJMNotifications
from system_events import g_systemEvents
_info = logging.getLogger(__name__).info

def preInit():
    _info(b'preInit personality: %s', __name__)
    registerJMSystemHandlers()
    registerJMNotifications()
    g_systemEvents.onDependencyConfigReady += _updateServicesConfigAndRegisterBanner
    return


def init():
    g_overrideScaleFormViewsConfig.initExtensionLobbyPackages(__name__, (b'journey_marathon.gui.impl.lobby',))
    return


def start():
    return


def fini():
    _info(b'fini personality: %s', __name__)
    from jm_services_config import updateServicesConfig
    g_systemEvents.onDependencyConfigReady -= updateServicesConfig
    return


def _updateServicesConfigAndRegisterBanner(manager):
    from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
    from jm_services_config import updateServicesConfig
    from journey_marathon.gui.impl.lobby.jm_event_banner import JmEventBanner
    updateServicesConfig(manager)
    banners = EventBannersContainer()
    banners.registerEventBanner(JmEventBanner)
    registerBannerEntryPointValidator(JmEventBanner.NAME, JmEventBanner.isEnabled)
    return
