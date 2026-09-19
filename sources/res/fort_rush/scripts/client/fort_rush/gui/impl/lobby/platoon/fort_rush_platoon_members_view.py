from __future__ import absolute_import
from enum import Enum
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView
from helpers import i18n

class _PrebattleTypes(Enum):
    FORT_RUSH = b'fort_rush'


class FortRushPlatoonMembersView(SquadMembersView):
    _prebattleType = _PrebattleTypes.FORT_RUSH

    def _onLoading(self):
        super(FortRushPlatoonMembersView, self)._onLoading()
        self.viewModel.setShouldShowFindPlayersButton(False)
        return

    def _onFindPlayers(self):
        return

    def _getTitle(self):
        title = (b'').join((
         i18n.makeString(backport.text(R.strings.platoon.squad())),
         i18n.makeString(backport.text(R.strings.platoon.members.header.fort_rush()))))
        return title

    def _getWindowInfoTooltipHeaderAndBody(self):
        tooltipHeader = backport.text(R.strings.platoon.fort_rush.members.header.tooltip.header())
        tooltipBody = backport.text(R.strings.platoon.fort_rush.members.header.tooltip.body())
        return (tooltipHeader, tooltipBody)
