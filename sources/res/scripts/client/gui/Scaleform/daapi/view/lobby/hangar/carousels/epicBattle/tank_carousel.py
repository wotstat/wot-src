from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.tank_carousel import BattlePassTankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.epicBattle.carousel_data_provider import EpicBattleCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.epicBattle.carousel_filter import EpicBattleCarouselFilter
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

class EpicBattleTankCarousel(BattlePassTankCarousel):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)
    _DISABLED_FILTERS = [
     b'bonus']

    def __init__(self):
        super(EpicBattleTankCarousel, self).__init__()
        self._carouselDPCls = EpicBattleCarouselDataProvider
        self._carouselFilterCls = EpicBattleCarouselFilter
        return

    def _populate(self):
        super(EpicBattleTankCarousel, self)._populate()
        self.as_useExtendedCarouselS(self.__epicController.isUnlockVehiclesInBattleEnabled())
        indexToScroll = self._carouselDP.getIndexToScroll()
        if indexToScroll >= 0:
            self.as_scrollToSlotS(indexToScroll)
        return

    def _getInitialFilterVO(self, contexts):
        filtersVO = super(EpicBattleTankCarousel, self)._getInitialFilterVO(contexts)
        filtersVO[b'isFrontline'] = True
        for entry in filtersVO.get(b'hotFilters', []):
            if entry[b'id'] in self._DISABLED_FILTERS:
                entry[b'enabled'] = False
                entry[b'selected'] = False

        return filtersVO
