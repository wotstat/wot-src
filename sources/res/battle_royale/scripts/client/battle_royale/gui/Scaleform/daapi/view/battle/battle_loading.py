from gui.Scaleform.daapi.view.meta.BattleRoyaleLoadingMeta import BattleRoyaleLoadingMeta
from gui.impl.gen.resources import R
from gui.impl import backport

class BattleLoading(BattleRoyaleLoadingMeta):

    def _populate(self):
        super(BattleLoading, self)._populate()
        arenaDP = self.sessionProvider.getArenaDP()
        self.as_setHeaderDataS({b'battleType': (arenaDP.getPersonalDescription().getFrameLabel()), 
           b'title': (backport.text(R.strings.battle_royale.fullStats.title())), 
           b'subTitle': (backport.text(R.strings.battle_royale.fullStats.subTitle())), 
           b'description': (backport.text(R.strings.battle_royale.fullStats.description()))})
        return

    def _formatTipTitle(self, tipTitleText):
        return tipTitleText

    def _formatTipBody(self, tipBody):
        return tipBody

    def _makeVisualTipVO(self, arenaDP, tip=None):
        vo = {b'tipIcon': (self.gui.resourceManager.getImagePath(tip.icon) if tip is not None else None)}
        return vo
