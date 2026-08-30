from gui.Scaleform.daapi.view.lobby.hangar.carousels import BattlePassTankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.stronghold.carousel_data_provider import StrongholdCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.stronghold.carousel_filter import StrongholdCarouselFilter
from helpers import dependency
from skeletons.gui.game_control import IDebutBoxesController

class StrongholdTankCarousel(BattlePassTankCarousel):
    __debutBoxesController = dependency.descriptor(IDebutBoxesController)

    def __init__(self):
        super(StrongholdTankCarousel, self).__init__()
        self._carouselDPCls = StrongholdCarouselDataProvider
        self._carouselFilterCls = StrongholdCarouselFilter
        return

    def getCustomParams(self):
        data = super(StrongholdTankCarousel, self).getCustomParams()
        if self.__debutBoxesController.isEnabled():
            data.update({b'debut_boxes': True})
        return data
