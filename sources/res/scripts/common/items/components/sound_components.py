from __future__ import absolute_import
from collections import namedtuple
from py2to3.patched_future import with_metaclass
from wrapped_reflection_framework import ReflectionMetaclass, reflectedNamedTuple
__all__ = (b'SoundPair', b'StatedSounds', b'HullAimingSound', b'SoundSiegeModeStateChange', b'WWTripleSoundConfig')
SoundPair = reflectedNamedTuple(b'SoundPair', (b'PC', b'NPC'))
StatedSounds = reflectedNamedTuple(b'StatedSounds', (b'state', b'underLimitSounds', b'overLimitSounds'))
HullAimingSound = reflectedNamedTuple(b'HullAimingSound', (b'lodDist', b'angleLimitValue', b'sounds'))
SoundSiegeModeStateChange = namedtuple(b'SoundSiegeModeStateChange', [
 18, 
 19, 
 20, 
 21, 
 22, 
 23, 
 24])

class WWTripleSoundConfig(with_metaclass(ReflectionMetaclass, object)):
    __slots__ = (b'__eventNames',)

    def __init__(self, wwsound, wwsoundPC, wwsoundNPC):
        super(WWTripleSoundConfig, self).__init__()
        self._configure(wwsound, wwsoundPC, wwsoundNPC)
        return

    def _configure(self, wwsound, wwsoundPC, wwsoundNPC):
        if wwsoundPC:
            if wwsoundNPC:
                self.__eventNames = (
                 wwsoundPC, wwsoundNPC)
            else:
                self.__eventNames = (
                 wwsoundPC, wwsound)
        elif wwsoundNPC:
            self.__eventNames = (
             wwsound, wwsoundNPC)
        else:
            self.__eventNames = (
             wwsound, wwsound)
        return

    def isEmpty(self):
        return not self.__eventNames[0] and not self.__eventNames[1]

    def getEvents(self):
        return self.__eventNames
