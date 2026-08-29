from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView
from gui.impl.gen.view_models.views.lobby.platoon.members_window_model import PrebattleTypes
from gui.impl.lobby.platoon.view.subview.platoon_chat_subview import ChatSubview
from helpers import i18n

class VersusAIMembersView(SquadMembersView):
    _prebattleType = PrebattleTypes.EVENT

    def __init__(self, prbType):
        super(VersusAIMembersView, self).__init__(prbType)
        self.viewModel.setShouldShowFindPlayersButton(False)
        return

    def _addSubviews(self):
        self._addSubviewToLayout(ChatSubview())
        return

    def _onFindPlayers(self):
        return

    def _getTitle(self):
        title = (b'').join((
         i18n.makeString(backport.text(R.strings.platoon.squad())),
         i18n.makeString(backport.text(R.strings.versusAI_platoon.members.header.versusAI()))))
        return title
