from gui.Scaleform.daapi.view.lobby.hangar.carousels import BattlePassTankCarousel

class DebutBoxesTankCarousel(BattlePassTankCarousel):

    def _getFilters(self):
        return super(DebutBoxesTankCarousel, self)._getFilters() + (b'debut_boxes',)

    def getCustomParams(self):
        data = super(DebutBoxesTankCarousel, self).getCustomParams()
        data.update({b'debut_boxes': True})
        return data
