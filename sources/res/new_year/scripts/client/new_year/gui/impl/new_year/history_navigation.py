class NavigationHistory(object):

    def __init__(self):
        self.__chain = []
        self.__states = {}
        self.__goingBack = False
        return

    def addToHistory(self, alias, state):
        self.__chain.append(alias)
        self.__states[alias] = state
        return

    def getLast(self, pop=False):
        if self.__chain:
            if pop:
                return self.__chain.pop()
            return self.__chain[-1]
        else:
            return

    def pop(self):
        if self.__chain:
            self.__chain.pop()
        return

    def getState(self, viewAlias):
        return self.__states.get(viewAlias)

    def setGoingBack(self, value):
        self.__goingBack = value
        return

    def getGoingBack(self):
        return self.__goingBack

    def invalidateViewState(self, viewAlias):
        if viewAlias not in self.__chain and viewAlias in self.__states:
            del self.__states[viewAlias]
        return

    def remove(self, viewAlias):
        if viewAlias in self.__chain:
            self.__chain.remove(viewAlias)
            del self.__states[viewAlias]
        return

    def clear(self):
        self.__chain = []
        self.__states = {}
        return

    @property
    def isEmpty(self):
        return len(self.__chain) == 0
