from __future__ import absolute_import
from typing import TYPE_CHECKING
import resource_helper
from constants import ITEM_DEFS_PATH
from gui.shared.gui_items.badge import BadgeLayouts, BadgeTypes
from realm import CURRENT_REALM
from soft_exception import SoftException
if TYPE_CHECKING:
    from typing import Optional, Dict
_BADGES_XML_PATH = ITEM_DEFS_PATH + b'badges.xml'

def _readBadges():
    result = {}
    ctx, section = resource_helper.getRoot(_BADGES_XML_PATH)
    for ctx_, subSection in resource_helper.getIterator(ctx, section[b'badges']):
        item = resource_helper.readItem(ctx_, subSection, name=b'badge')
        if not item.name:
            raise SoftException(b'No name for badge is provided', item.name)
        if b'id' not in item.value:
            raise SoftException(b'No ID for badge is provided', item.value)
        value = dict(item.value)
        realms = value.pop(b'realm', None)
        if realms is not None:
            if CURRENT_REALM in realms.get(b'exclude', []) or b'include' in realms and CURRENT_REALM not in realms.get(b'include', []):
                continue
        if b'weight' not in value:
            value[b'weight'] = -1.0
        if b'type' not in value:
            value[b'type'] = 0
        if value[b'type'] == BadgeTypes.COLLAPSIBLE and b'group' not in value:
            raise SoftException(b'Invalid badge. No group for the COLLAPSIBLE badge', value)
        if b'layout' not in value:
            value[b'layout'] = BadgeLayouts.PREFIX
        else:
            layout = value[b'layout']
            if layout not in BadgeLayouts.ALL():
                raise SoftException((b'Invalid badge layout type "{}" is provided').format(layout))
        value[b'name'] = item.name
        result[value[b'id']] = value

    resource_helper.purgeResource(_BADGES_XML_PATH)
    return result


def getSelectedByLayout(badgesIDs):
    prefixBadge = 0
    suffixBadge = 0
    availableBadges = getAvailableBadges()
    for bID in badgesIDs:
        badgeDescr = availableBadges.get(bID, None)
        if badgeDescr:
            layout = badgeDescr.get(b'layout', BadgeLayouts.PREFIX)
            if layout == BadgeLayouts.PREFIX:
                prefixBadge = bID
            else:
                suffixBadge = bID

    return (
     prefixBadge, suffixBadge)


def getAvailableBadges():
    global _badges
    if _badges is None:
        _badges = _readBadges()
    return _badges


def reloadAvailableBadges():
    global _badges
    if _badges:
        _badges = _readBadges()
    return


_badges = None
