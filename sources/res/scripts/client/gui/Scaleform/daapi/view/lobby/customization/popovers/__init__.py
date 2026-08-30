from __future__ import absolute_import
from collections import namedtuple
from gui.Scaleform.daapi.view.lobby.customization.shared import TYPES_ORDER
ItemsGroupVO = namedtuple(b'ItemsGroupVO', (b'userName', b'titleLabel', b'isTitle'))

class C11nPopoverItemData(object):
    __slots__ = (b'item', b'season', b'slotsIds', b'isBase', b'isRemovable', b'isRemoved', b'isFromInventory')

    def __init__(self, item, season=None, isBase=False, isRemovable=False, isRemoved=False, isFromInventory=False):
        self.item = item
        self.season = season
        self.slotsIds = []
        self.isBase = isBase
        self.isRemovable = isRemovable
        self.isRemoved = isRemoved
        self.isFromInventory = isFromInventory
        return


def orderKey(itemData):
    item = itemData.item
    typeOrder = TYPES_ORDER.index(item.itemTypeID)
    return (
     not itemData.isBase, itemData.isRemovable, typeOrder, item.intCD, not itemData.isFromInventory)
