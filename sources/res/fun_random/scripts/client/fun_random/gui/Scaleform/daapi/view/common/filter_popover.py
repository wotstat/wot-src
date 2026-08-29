from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from constants import ARENA_BONUS_TYPE
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin
from gui.Scaleform.daapi.view.common.filter_popover import FILTER_SECTION, BattlePassCarouselFilterPopover
from gui.impl import backport
from gui.shared.utils.functions import makeTooltip
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

def fillFunRandomFilterVO(vo, selected, enabled):
    vo.update({b'value': (backport.image(FunAssetPacksMixin.getModeIconsResRoot().library.carousel_filter())), 
       b'tooltip': (makeTooltip(header=backport.text(FunAssetPacksMixin.getModeLocalsResRoot().tooltip.filter.header()), body=backport.text(FunAssetPacksMixin.getModeLocalsResRoot().tooltip.filter.body()))), 
       b'selected': selected, 
       b'enabled': enabled})
    return vo


class FunRandomCarouselFilterPopover(BattlePassCarouselFilterPopover):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    @classmethod
    def _generateMapping(cls, hasRented, hasEvent, hasRoles, **kwargs):
        mapping = super(FunRandomCarouselFilterPopover, cls)._generateMapping(hasRented, hasEvent, hasRoles, **kwargs)
        filterSpecialsList = mapping[FILTER_SECTION.SPECIALS]
        filterSpecialsList.append(b'funRandom')
        if b'clanRented' in filterSpecialsList:
            filterSpecialsList.remove(b'clanRented')
        config = cls.__lobbyContext.getServerSettings().getCrystalRewardConfig()
        if not config.isCrystalEarnPossible(ARENA_BONUS_TYPE.FUN_RANDOM):
            filterSpecialsList.remove(b'crystals')
        if not BONUS_CAPS.checkAny(ARENA_BONUS_TYPE.FUN_RANDOM, BONUS_CAPS.DAILY_MULTIPLIED_XP):
            filterSpecialsList.remove(b'bonus')
        return mapping

    def _packSpecial(self, entry, ctx, selected, tooltipRes, enabled):
        if entry != b'funRandom':
            return super(FunRandomCarouselFilterPopover, self)._packSpecial(entry, ctx, selected, tooltipRes, enabled)
        return fillFunRandomFilterVO({}, selected, enabled)
