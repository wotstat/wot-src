class BaseMessagesController(object):

    def __init__(self, model):
        self._model = model
        return

    def cleanUp(self):
        self._model = None
        return
