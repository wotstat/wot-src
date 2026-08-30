class ICongratsCtx(object):

    @property
    def background(self):
        raise NotImplementedError
        return

    @property
    def title(self):
        raise NotImplementedError
        return

    @property
    def description(self):
        raise NotImplementedError
        return

    @property
    def image(self):
        raise NotImplementedError
        return

    @property
    def imageAlt(self):
        raise NotImplementedError
        return

    @property
    def confirmLabel(self):
        raise NotImplementedError
        return

    @property
    def backLabel(self):
        raise NotImplementedError
        return

    def onConfirm(self):
        raise NotImplementedError
        return

    def onBack(self):
        raise NotImplementedError
        return
