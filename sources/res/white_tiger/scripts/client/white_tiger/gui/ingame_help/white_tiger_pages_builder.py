from cgf_components import wt_helpers
from gui.impl import backport
from gui.impl.gen import R
from gui.ingame_help.detailed_help_pages import DetailedHelpPagesBuilder, HelpPagePriority, addPage
from white_tiger_common.wt_constants import ARENA_GUI_TYPE

class WhiteTigerHelpPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isWhiteTiger',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.DEFAULT

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        header = backport.text(R.strings.white_tiger.detailsHelp.mainTitle())
        vehType = b'hunter'
        if ctx[b'isBoss']:
            vehType = b'boss'
        for pageNum in xrange(1, 4):
            pageName = b'page' + str(pageNum)
            addPage(datailedList=pages, headerTitle=header, title=backport.text(R.strings.white_tiger.detailsHelp.dyn(vehType).dyn(pageName).title()), descr=backport.text(R.strings.white_tiger.detailsHelp.dyn(vehType).dyn(pageName).description()), vKeys=[], buttons=[], image=backport.image(R.images.white_tiger.gui.maps.icons.battleHelp.dyn(vehType)()))

        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        isWhiteTiger = arenaVisitor.getArenaGuiType() == ARENA_GUI_TYPE.WHITE_TIGER
        ctx[b'isWhiteTiger'] = isWhiteTiger
        if isWhiteTiger:
            ctx[b'isBoss'] = wt_helpers.isBoss()
        return
