from new_year.skeletons.new_year import INyWindowHelper

class NyWindowHelper(INyWindowHelper):
    __slots__ = (b'__windowLocks',)

    def __init__(self):
        self.__windowLocks = set()
        return

    def isLocked(self, windowTag):
        return windowTag in self.__windowLocks

    def lock(self, windowTag):
        self.__windowLocks.add(windowTag)
        return

    def unlock(self, windowTag):
        self.__windowLocks.remove(windowTag)
        return
