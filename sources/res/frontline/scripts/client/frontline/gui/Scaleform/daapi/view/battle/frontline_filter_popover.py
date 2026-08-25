from frontline.gui.Scaleform.daapi.view.meta.FrontlineCarouselFilterPopoverMeta import FrontlineCarouselFilterPopoverMeta
from gui.filters.carousel_filter import FILTER_KEYS
from gui.Scaleform.daapi.view.common.common_constants import FILTER_POPOVER_SECTION
from helpers import dependency
from skeletons.gui.game_control import IVehiclePlaylistsController

class FrontlineBattleTankCarouselFilterPopover(FrontlineCarouselFilterPopoverMeta):
    _BASE_SPECIALS_LIST = [
     FILTER_KEYS.FAVORITE, FILTER_KEYS.PREMIUM]
    __vehiclePlaylistsCtrl = dependency.descriptor(IVehiclePlaylistsController)

    def _getInitialVO(self, filters, xpRateMultiplier):
        dataVO = super(FrontlineBattleTankCarouselFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        dataVO[b'specialSectionVisible'] = True
        dataVO[b'searchSectionVisible'] = True
        dataVO[b'progressionsSectionVisible'] = False
        vehicleLevels = self._carousel.getCustomParams().get(b'vehicleLevelsFilter', list())
        if self._carousel is not None and not len(vehicleLevels) > 1:
            dataVO[b'tankTierSectionVisible'] = False
        return dataVO

    def _generateMapping(self, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        mapping = super(FrontlineBattleTankCarouselFilterPopover, self)._generateMapping(hasRented, hasEvent, hasRoles, hasCustomization, **kwargs)
        vehicleLevels = kwargs.get(b'vehicleLevelsFilter', list())
        if len(vehicleLevels) > 1:
            mapping[FILTER_POPOVER_SECTION.LEVELS] = [(b'level_{}').format(lvl) for lvl in vehicleLevels]
        else:
            mapping[FILTER_POPOVER_SECTION.LEVELS] = []
        return mapping

    def onPlayListsChange(self, playListId):
        self.__vehiclePlaylistsCtrl.setSelectedID(playListId)
        self._carousel.sortVehicles(None)
        self._update()
        return

    def setTankCarousel(self, carousel):
        super(FrontlineBattleTankCarouselFilterPopover, self).setTankCarousel(carousel)
        self.as_updatePlayListsS(self._carousel.getVehiclePlayList())
        return
