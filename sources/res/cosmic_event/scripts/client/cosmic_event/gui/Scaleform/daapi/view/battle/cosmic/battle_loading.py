from gui.Scaleform.daapi.view.meta.CosmicBattleLoadingMeta import CosmicBattleLoadingMeta
from gui.impl import backport
from gui.impl.gen import R

class CosmicBattleLoading(CosmicBattleLoadingMeta):

    def _populate(self):
        super(CosmicBattleLoading, self)._populate()
        self.as_setTipTitleS(backport.text(R.strings.cosmicEvent.battle.loadingScreen.title()))
        self.as_setTipsS([
         backport.text(R.strings.cosmicEvent.battle.loadingScreen.tip1()),
         backport.text(R.strings.cosmicEvent.battle.loadingScreen.tip2()),
         backport.text(R.strings.cosmicEvent.battle.loadingScreen.tip3())])
        return

    def invalidateArenaInfo(self):
        return

    def _setTipsInfo(self):
        return

    def _addArenaTypeData(self):
        return
