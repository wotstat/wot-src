from __future__ import absolute_import
import typing
from helpers_common import reprSlots

class ShotParams(object):
    __slots__ = (b'sourceID', b'gunIndexDelayed', b'shellKindIdx', b'predictShooting')

    def __init__(self, sourceID, gunIndexDelayed, shellKindIdx, predictShooting):
        self.sourceID = sourceID
        self.gunIndexDelayed = gunIndexDelayed
        self.shellKindIdx = shellKindIdx
        self.predictShooting = predictShooting
        return

    __repr__ = reprSlots
