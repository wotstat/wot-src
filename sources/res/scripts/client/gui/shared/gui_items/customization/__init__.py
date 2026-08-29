from collections import namedtuple
from items.components.c11n_constants import ProjectionDecalDirectionTags
from shared_utils import first

def directionByTag(tags):
    directionTags = (tag for tag in tags if tag.startswith(ProjectionDecalDirectionTags.PREFIX))
    return first(directionTags, ProjectionDecalDirectionTags.ANY)


def isNeedToMirrorProjectionDecal(item, slot):
    if not item.canBeMirroredHorizontally:
        return False
    itemDirection = directionByTag(item.tags)
    slotDirection = directionByTag(slot.tags)
    if itemDirection == ProjectionDecalDirectionTags.ANY or slotDirection == ProjectionDecalDirectionTags.ANY:
        return False
    return itemDirection != slotDirection


CustomizationTooltipContext = namedtuple(b'CustomizationTooltipContext', (b'itemCD', b'vehicleIntCD', b'showInventoryBlock', b'level', b'showOnlyProgressBlock', b'showStatusBlock'))
CustomizationTooltipContext.__new__.__defaults__ = (
 -1, -1, False, -1, False, True)
C11nStyleProgressData = namedtuple(b'C11nStyleProgressData', (b'styleID', b'branch', b'level'))
C11nStyleProgressData.__new__.__defaults__ = (-1, -1, -1)
