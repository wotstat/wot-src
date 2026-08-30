from __future__ import absolute_import
from future.utils import viewitems
from debug_utils import LOG_ERROR
from gui.Scaleform.framework.entities.abstract.TextManagerMeta import TextManagerMeta
from gui.Scaleform.genConsts.TEXT_MANAGER_STYLES import TEXT_MANAGER_STYLES as _TMS
from gui.shared.formatters import text_styles

class TextManager(TextManagerMeta):

    def __init__(self):
        super(TextManager, self).__init__()
        self.__styles = text_styles.getRawStyles([v for k, v in viewitems(_TMS.__dict__) if not k.startswith(b'_')])
        return

    def getTextStyle(self, style):
        if style in self.__styles:
            result = self.__styles[style]
        else:
            LOG_ERROR(b'Style is not found', style)
            result = b''
        return result

    def _dispose(self):
        self.__styles.clear()
        super(TextManager, self)._dispose()
        return


class TextIcons(object):
    CHECKMARK_ICON = b'checkmark'
    NUT_ICON = b'nut'
    PERCENT_ICON = b'percent'
    ALERT_ICON = b'alert'
    INFO_ICON = b'info'
    PREMIUM_IGR_SMALL = b'premiumIgrSmall'
    PREMIUM_IGR_BIG = b'premiumIgrBig'
    ORDER_IN_PROGRESS_ICON = b'order_in_progress'
    CLOCK_ICON = b'clock'
    NOT_AVAILABLE = b'notAvailable'
    LEVEL_5 = b'level5'
    LEVEL_10 = b'level10'
    SWORDS = b'swords'
    HUMANS = b'humans'
    CREDITS = b'credits'
    GOLD = b'gold'
    XP = b'xp'
    FREE_XP = b'freeXP'
    ARROW_BUTTON = b'arrowButton'
    NO_SEASON = b'noSeason'
    ICONS = (NUT_ICON, PERCENT_ICON, ALERT_ICON, INFO_ICON, PREMIUM_IGR_SMALL, PREMIUM_IGR_BIG,
     ORDER_IN_PROGRESS_ICON, CLOCK_ICON, CHECKMARK_ICON, NOT_AVAILABLE, LEVEL_5, LEVEL_10, SWORDS,
     HUMANS, CREDITS, GOLD, XP, FREE_XP, ARROW_BUTTON, NO_SEASON)
