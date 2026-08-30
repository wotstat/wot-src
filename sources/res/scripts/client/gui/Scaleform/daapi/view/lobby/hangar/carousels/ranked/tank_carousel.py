from gui.Scaleform.daapi.view.lobby.hangar.carousels.ranked.carousel_data_provider import RankedCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.ranked.carousel_filter import RankedCarouselFilter
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.tank_carousel import BattlePassTankCarousel
from helpers import dependency
from skeletons.gui.game_control import IDebutBoxesController

class RankedTankCarousel(BattlePassTankCarousel):
    __debutBoxesController = dependency.descriptor(IDebutBoxesController)

    def __init__(self):
        super(RankedTankCarousel, self).__init__()
        self._carouselDPCls = RankedCarouselDataProvider
        self._carouselFilterCls = RankedCarouselFilter
        return

    def _getInitialFilterVO(self, contexts):
        filtersVO = super(RankedTankCarousel, self)._getInitialFilterVO(contexts)
        filtersVO[b'isRanked'] = True
        return filtersVO

    def _getFilters(self):
        return super(RankedTankCarousel, self)._getFilters() + (b'ranked',)

    def getCustomParams(self):
        data = super(RankedTankCarousel, self).getCustomParams()
        if self.__debutBoxesController.isEnabled():
            data.update({b'debut_boxes': True})
        return data
