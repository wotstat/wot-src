from collections import namedtuple
from items.components import legacy_stuff
from soft_exception import SoftException
from wrapped_reflection_framework import reflectedNamedTuple
from wrapped_reflection_framework import ReflectionMetaclass
RecoilEffect = reflectedNamedTuple(b'RecoilEffect', (b'lodDist', b'amplitude', b'backoffTime', b'returnTime'))
SpinEffect = namedtuple(b'SpinEffect', (b'activationSound', b'deactivationSound'))
DEFAULT_TEMPERATURE_SEGMENT_SIZE = 5

class GunShot(legacy_stuff.LegacyStuff):
    __slots__ = (b'shell', b'defaultPortion', b'piercingPower', b'speed', b'gravity', b'maxDistance', b'maxHeight', b'acceleration', b'ignoreDispersion')
    __metaclass__ = ReflectionMetaclass

    def __init__(self, shell, defaultPortion, piercingPower, speed, gravity, maxDistance, maxHeight, acceleration, ignoreDispersion):
        super(GunShot, self).__init__()
        self.shell = shell
        self.defaultPortion = defaultPortion
        self.piercingPower = piercingPower
        self.speed = speed
        self.gravity = gravity
        self.maxDistance = maxDistance
        self.maxHeight = maxHeight
        self.acceleration = acceleration
        self.ignoreDispersion = ignoreDispersion
        return

    def __repr__(self):
        res = b'{}(' + (b', ').join(aName + b'=' + str(getattr(self, aName)) for aName in self.__slots__) + b')'
        return res.format(self.__class__.__name__)

    def copy(self):
        raise SoftException(b'Operation "GunShot.copy" is not allowed')
        return


class TemperatureGunParams(object):
    TemperatureGunState = namedtuple(b'TemperatureGunState', [
     1, 2, 3, 4, 5, 6, 
     7, 8])
    __slots__ = (b'states', b'temperatureThresholds', b'temperatureSegmentSize')

    def __init__(self, states, temperatureThresholds, temperatureSegmentSize=DEFAULT_TEMPERATURE_SEGMENT_SIZE):
        self.states = states
        self.temperatureThresholds = temperatureThresholds
        self.temperatureSegmentSize = temperatureSegmentSize
        return

    def __repr__(self):
        return (b'TemperatureGunParams(states = {}, temperatureThresholds = {}, temperatureSegmentSize = {}))').format(self.states, self.temperatureThresholds, self.temperatureSegmentSize)
