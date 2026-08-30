from warnings import warnpy3k
warnpy3k(b'the mutex module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
from collections import deque

class mutex:

    def __init__(self):
        self.locked = False
        self.queue = deque()
        return

    def test(self):
        return self.locked

    def testandset(self):
        if not self.locked:
            self.locked = True
            return True
        else:
            return False

        return

    def lock(self, function, argument):
        if self.testandset():
            function(argument)
        else:
            self.queue.append((function, argument))
        return

    def unlock(self):
        if self.queue:
            function, argument = self.queue.popleft()
            function(argument)
        else:
            self.locked = False
        return
