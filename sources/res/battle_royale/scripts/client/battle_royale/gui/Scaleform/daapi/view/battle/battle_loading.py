from gui.Scaleform.daapi.view.meta.BattleRoyaleLoadingMeta import BattleRoyaleLoadingMeta
from gui.impl import backport
from gui.impl.gen.resources import R
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController

class BattleLoading(BattleRoyaleLoadingMeta):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    def _populate(self):
        super(BattleLoading, self)._populate()
        arenaDP = self.sessionProvider.getArenaDP()
        self.as_setHeaderDataS({b'battleType': (arenaDP.getPersonalDescription().getFrameLabel()), 
           b'battleTypeIconPathBig': (self._getBattleTypeIconPath(b'c_136x136')), 
           b'battleTypeIconPathSmall': (self._getBattleTypeIconPath(b'c_64x64')), 
           b'title': (backport.text(R.strings.battle_royale.fullStats.title())), 
           b'subTitle': (backport.text(R.strings.battle_royale.fullStats.subTitle())), 
           b'description': (backport.text(R.strings.battle_royale.fullStats.description()))})
        return

    def _formatTipTitle(self, tipTitleText):
        return tipTitleText

    def _formatTipBody(self, tipBody):
        return tipBody

    def _getBattleTypeIconPath(self, sizeFolder=b'c_136x136'):
        arenaDP = self.sessionProvider.getArenaDP()
        if self.__battleRoyaleController.isStPatrick():
            resRoot = R.images.battle_royale.gui.maps.st_patrick.icons.battleTypes
        else:
            resRoot = R.images.gui.maps.icons.battleTypes
        iconRes = resRoot.dyn(sizeFolder).dyn(arenaDP.getPersonalDescription().getFrameLabel())
        if iconRes.exists():
            return backport.image(iconRes())
        return b''

    def _makeVisualTipVO(self, arenaDP, tip=None):
        vo = {b'tipIcon': (self.gui.resourceManager.getImagePath(tip.icon) if tip is not None else None)}
        return vo
