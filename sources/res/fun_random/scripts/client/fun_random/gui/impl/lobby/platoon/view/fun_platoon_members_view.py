from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.platoon.members_window_model import PrebattleTypes
from gui.impl.lobby.platoon.platoon_helpers import getPlatoonBonusState
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView
from gui.impl.lobby.platoon.view.subview.platoon_chat_subview import ChatSubview

class FunRandomMembersView(SquadMembersView, FunAssetPacksMixin, FunSubModesWatcher):
    _prebattleType = PrebattleTypes.FUNRANDOM

    @hasDesiredSubMode(defReturn=b'')
    def _getTitle(self):
        subModeName = backport.text(self.getDesiredSubMode().getLocalsResRoot().userName())
        return backport.text(R.strings.fun_random.platoonView.title(), subModeName=subModeName)

    def _setHeaderBg(self, fileName, model):
        model.header.setBackgroundImage(backport.image(self.getModeIconsResRoot().platoon.dyn(fileName)()))
        return

    def _onFindPlayers(self):
        return

    def _addSubviews(self):
        self._addSubviewToLayout(ChatSubview())
        return

    def _addListeners(self):
        super(FunRandomMembersView, self)._addListeners()
        self.startSubSelectionListening(self.__onSubModeSelected)
        return

    def _removeListeners(self):
        self.stopSubSelectionListening(self.__onSubModeSelected)
        super(FunRandomMembersView, self)._removeListeners()
        return

    def _updateFindPlayersButton(self, *args):
        with self.viewModel.transaction() as model:
            model.setShouldShowFindPlayersButton(value=False)
        return

    def __onSubModeSelected(self, *_):
        self.viewModel.setRawTitle(self._getTitle())
        self._setBonusInformation(getPlatoonBonusState(True))
        return
