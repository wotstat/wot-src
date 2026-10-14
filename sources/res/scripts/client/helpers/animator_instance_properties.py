from __future__ import absolute_import
from collections import namedtuple
AnimatorInstanceProperties = namedtuple(b'AnimatorInstanceProperties', (b'delay', b'speed', b'loopCount', b'loop'))
AnimatorInstanceProperties.__new__.__defaults__ = (0.0, 1.0, -1, True)
