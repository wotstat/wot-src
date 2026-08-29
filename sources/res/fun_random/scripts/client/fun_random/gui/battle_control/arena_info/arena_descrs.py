import BattleReplay
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode
from gui.battle_control.arena_info.arena_descrs import ArenaWithLabelDescription
from gui.impl import backport

class FunRandomArenaDescription(ArenaWithLabelDescription, FunAssetPacksMixin, FunSubModesWatcher):

    def isInvitationEnabled(self):
        replayCtrl = BattleReplay.g_replayCtrl
        return not replayCtrl.isPlaying

    def getBattleTypeIconPath(self, sizeFolder=b'c_136x136'):
        iconRes = self.getModeIconsResRoot().battle_type.dyn(sizeFolder).dyn(self.getFrameLabel())
        if iconRes.exists():
            return backport.image(iconRes())
        return b''

    def getDescriptionString(self, isInBattle=True):
        return self.__getDescriptionString() or self.getModeUserName()

    @hasBattleSubMode(defReturn=b'')
    def __getDescriptionString(self):
        subModeName = backport.text(self.getBattleSubMode(self._visitor).getLocalsResRoot().userName())
        return self.getModeDetailedUserName(subModeName=subModeName)
