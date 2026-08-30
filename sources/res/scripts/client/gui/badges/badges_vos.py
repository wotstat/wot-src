from gui.impl import backport
from gui.impl.gen.resources import R
from gui.shared.formatters import text_styles, icons
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.settings import ICONS_SIZES
_UNIQUE_SUFFIX_BADGE_TOOLTIPS = {b'ranked_2020_leader_suffix': (TOOLTIPS_CONSTANTS.BADGES_SUFFIX_RANKED_ITEM)}

def getSuffixBadgeTooltip(badge):
    if badge.isSuffixLayout():
        return _UNIQUE_SUFFIX_BADGE_TOOLTIPS.get(badge.getName(), TOOLTIPS_CONSTANTS.BADGES_SUFFIX_ITEM)
    return b''


def makeBadgeVO(badge):
    return {b'id': (badge.badgeID), 
       b'title': (text_styles.stats(badge.getUserName())), 
       b'description': (text_styles.main(badge.getUserDescription())), 
       b'enabled': (badge.isAchieved), 
       b'selected': (badge.isSelected), 
       b'highlightIcon': (badge.getHighlightIcon()), 
       b'isFirstLook': (badge.isNew()), 
       b'visual': (badge.getBadgeVO(ICONS_SIZES.X80))}


def makeSuffixBadgeVO(badge):
    stripImg = R.images.gui.maps.icons.library.badges.strips.c_68x28.dyn((b'strip_{}').format(badge.badgeID))
    labelDyn = R.strings.badge.suffix.dyn((b'badge_{}').format(badge.badgeID))
    labelText = text_styles.main(backport.text(labelDyn())) if labelDyn else b''
    activeLabelText = text_styles.stats(backport.text(labelDyn())) if labelDyn else b''
    return {b'id': (badge.badgeID), 
       b'label': (text_styles.concatStylesToSingleLine(labelText, icons.starYellow(0)) if badge.isTemporary else labelText), 
       b'activeLabel': (text_styles.concatStylesToSingleLine(activeLabelText, icons.starYellow(0)) if badge.isTemporary else activeLabelText), 
       b'tooltip': (getSuffixBadgeTooltip(badge)), 
       b'stripImg': (backport.image(stripImg()) if stripImg else b''), 
       b'img': (badge.getSuffixSmallIcon()), 
       b'hasFootnoteMark': (badge.isTemporary)}
