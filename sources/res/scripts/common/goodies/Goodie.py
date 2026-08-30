import time
from goodie_constants import GOODIE_STATE

class Goodie(object):
    __slots__ = [
     b'uid', b'state', b'expiration', b'counter']

    def __init__(self, uid, state=GOODIE_STATE.INACTIVE, expiration=0, counter=0):
        self.uid = uid
        self.state = state
        self.expiration = expiration
        self.counter = counter
        return

    def isActive(self):
        return self.state == GOODIE_STATE.ACTIVE

    def isExpired(self):
        if self.expiration and self.expiration < time.time():
            return True
        else:
            return False

        return

    def toPdata(self):
        return (
         self.state, self.expiration, self.counter)
