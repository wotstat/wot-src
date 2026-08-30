from __future__ import absolute_import
from typing import TYPE_CHECKING, Tuple
from items.components import legacy_stuff
from py2to3.patched_future import with_metaclass
from soft_exception import SoftException
from wrapped_reflection_framework import reflectedNamedTuple
from wrapped_reflection_framework import ReflectionMetaclass
if TYPE_CHECKING:
    from items.vehicle_items import Shell
RecoilEffect = reflectedNamedTuple(b'RecoilEffect', (b'lodDist', b'amplitude', b'backoffTime', b'returnTime'))

class GunShot(with_metaclass(ReflectionMetaclass, legacy_stuff.LegacyStuff)):
    __slots__ = (b'shell', b'defaultPortion', b'piercingPower', b'speed', b'gravity', b'nominalMaxDistance', b'maxDistance', b'maxHeight')

    def __init__(self, shell, defaultPortion, piercingPower, speed, gravity, maxDistance, maxHeight):
        super(GunShot, self).__init__()
        self.shell = shell
        self.defaultPortion = defaultPortion
        self.piercingPower = piercingPower
        self.speed = speed
        self.gravity = gravity
        self.nominalMaxDistance = maxDistance
        self.maxDistance = maxDistance
        self.maxHeight = maxHeight
        return

    def __repr__(self):
        return (b'GunShot(shell = {}, ppower = {}, speed = {}, gravity = {}, nominalMaxDistance - {}, maxDistance = {}, maxHeight = {}))').format(self.shell, self.piercingPower, self.speed, self.gravity, self.nominalMaxDistance, self.maxDistance, self.maxHeight)

    def copy(self):
        raise SoftException(b'Operation "GunShot.copy" is not allowed')
        return
