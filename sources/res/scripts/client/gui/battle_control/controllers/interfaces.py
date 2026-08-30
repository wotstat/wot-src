class IBattleController(object):
    __slots__ = ()

    def startControl(self, *args):
        raise NotImplementedError
        return

    def stopControl(self):
        raise NotImplementedError
        return

    def getControllerID(self):
        raise NotImplementedError
        return


class IBattleControllersRepository(object):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        raise NotImplementedError
        return

    def destroy(self):
        raise NotImplementedError
        return

    def getController(self, ctrlID):
        raise NotImplementedError
        return

    def addController(self, ctrl):
        raise NotImplementedError
        return
