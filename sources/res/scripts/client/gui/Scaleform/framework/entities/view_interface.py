class ViewInterface(object):

    @property
    def uiImpl(self):
        raise NotImplementedError
        return

    @property
    def layer(self):
        raise NotImplementedError
        return

    @property
    def viewScope(self):
        raise NotImplementedError
        return

    @property
    def key(self):
        raise NotImplementedError
        return

    @property
    def alias(self):
        raise NotImplementedError
        return

    @property
    def uniqueName(self):
        raise NotImplementedError
        return

    @property
    def settings(self):
        raise NotImplementedError
        return

    @property
    def soundManager(self):
        raise NotImplementedError
        return

    def isViewModal(self):
        raise NotImplementedError
        return

    def getAlias(self):
        raise NotImplementedError
        return

    def setAlias(self, alias):
        raise NotImplementedError
        return

    def getSubContainersSettings(self):
        raise NotImplementedError
        return

    def getUniqueName(self):
        raise NotImplementedError
        return

    def setUniqueName(self, name):
        raise NotImplementedError
        return

    def getCurrentScope(self):
        raise NotImplementedError
        return

    def setCurrentScope(self, scope):
        raise NotImplementedError
        return
