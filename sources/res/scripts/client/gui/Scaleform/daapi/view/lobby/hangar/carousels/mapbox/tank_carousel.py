from constants import Configs
from gui.Scaleform.daapi.view.lobby.hangar.carousels import BattlePassTankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.mapbox.carousel_data_provider import MapboxCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.mapbox.carousel_filter import MapboxCarouselFilter
from helpers import dependency, server_settings
from skeletons.gui.lobby_context import ILobbyContext

class MapboxTankCarousel(BattlePassTankCarousel):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        super(MapboxTankCarousel, self).__init__()
        self._carouselDPCls = MapboxCarouselDataProvider
        self._carouselFilterCls = MapboxCarouselFilter
        return

    def _populate(self):
        super(MapboxTankCarousel, self)._populate()
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        return

    def _dispose(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        super(MapboxTankCarousel, self)._dispose()
        return

    @server_settings.serverSettingsChangeListener(Configs.MAPBOX_CONFIG.value)
    def __onServerSettingChanged(self, *_):
        self.updateVehicles()
        return
