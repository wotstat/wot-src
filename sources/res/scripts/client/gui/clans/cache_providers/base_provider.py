class IBaseProvider(object):

    def start(self):
        raise NotImplementedError
        return

    def stop(self, withClear=False):
        raise NotImplementedError
        return
