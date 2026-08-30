from __future__ import absolute_import
from comp7_core.gui.ingame_help.detailed_help_pages import Comp7CorePagesBuilder
from comp7_common.comp7_constants import ARENA_GUI_TYPE
from comp7.gui.ingame_help import HelpPagePriority
from gui.impl.gen import R

class Comp7PagesBuilder(Comp7CorePagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isComp7',)
    _PAGE_NAMES = (b'seasonModifiers', b'poi', b'roleSkills', b'nightMaps', b'rules')
    _MODE_RES_ROOT_TEXTS = R.strings.ingame_help.detailsHelp.comp7
    _MODE_RES_ROOT_IMAGES = R.images.comp7.gui.maps.icons.battleHelp

    @classmethod
    def priority(cls):
        return HelpPagePriority.COMP7

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isComp7'] = arenaVisitor.getArenaGuiType() in ARENA_GUI_TYPE.COMP7_RANGE
        return
