from __future__ import absolute_import
from gui.filters.ranked_carousel_filter import RankedCarouselFilter
from gui.Scaleform.daapi.view.lobby.hangar.carousels.ranked.carousel_data_provider import RankedCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.tank_carousel import BattlePassTankCarousel

class RankedTankCarousel(BattlePassTankCarousel):

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
