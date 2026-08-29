from __future__ import absolute_import
from builtins import object
import typing
if typing.TYPE_CHECKING:
    from Math import Vector3, Vector2
    import CGF

class AreaTriggerComponent(object):
    id = None
    objectsInProximity = None
    valid = None

    def addEnterReaction(self, reaction):
        return

    def addExitReaction(self, reaction):
        return

    def addFilter(self, filter, dynamic=False):
        return

    def destroy(self, *args):
        return

    def removeEnterReaction(self, id):
        return

    def removeExitReaction(self, id):
        return


class AreaTriggerTarget(object):
    id = None
    valid = None

    def destroy(self, *args):
        return


class CylinderAreaComponent(object):
    height = None
    id = None
    radius = None
    valid = None

    def __init__(self, height, radius):
        return

    def destroy(self, *args):
        return


class PrismAreaComponent(object):
    height = None
    id = None
    points = None
    valid = None

    def __init__(self, points, height, minHeight, maxHeight):
        return

    def destroy(self, *args):
        return


class SquareAreaComponent(object):
    id = None
    maxBounds = None
    minBounds = None
    valid = None

    def __init__(self, minBounds, maxBounds):
        return

    def destroy(self, *args):
        return


class TimeTriggerComponent(object):
    counter = None
    id = None
    valid = None

    def __init__(self, deltaTime=0.0, repeatCount=1):
        return

    def addFireReaction(self, reaction):
        return

    def destroy(self, *args):
        return

    def removeFireReaction(self, index):
        return

    def reset(self, delta, count=1):
        return
