__revision__ = b'$Id$'
__all__ = [b'new', b'_UserFriendlyRNG', b'OSRNG', b'Fortuna']
import OSRNG, Fortuna
from Crypto.Random import _UserFriendlyRNG

def new(*args, **kwargs):
    return _UserFriendlyRNG.new(*args, **kwargs)


def atfork():
    _UserFriendlyRNG.reinit()
    return


def get_random_bytes(n):
    return _UserFriendlyRNG.get_random_bytes(n)
