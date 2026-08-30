class IStorage(object):

    def close(self):
        raise NotImplementedError
        return

    def add(self, name, data, callback):
        raise NotImplementedError
        return

    def remove(self, name):
        raise NotImplementedError
        return

    def isStored(self, name):
        raise NotImplementedError
        return

    def getAll(self):
        raise NotImplementedError
        return
