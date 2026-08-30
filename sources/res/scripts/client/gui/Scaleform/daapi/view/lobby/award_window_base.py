from gui.Scaleform.daapi.view.meta.AwardWindowsBaseMeta import AwardWindowsBaseMeta
from gui.server_events.awards import AwardAbstract

class AwardWindowBase(AwardWindowsBaseMeta):

    def __init__(self, ctx):
        super(AwardWindowBase, self).__init__()
        if b'award' not in ctx:
            raise UserWarning(b'Key "award" is not found in context', ctx)
        if not isinstance(ctx[b'award'], AwardAbstract):
            raise UserWarning(b'Value of "award" should be instance of AwardAbstract', ctx)
        self._award = ctx[b'award']
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _populate(self):
        super(AwardWindowBase, self)._populate()
        data = {b'windowTitle': (self._award.getWindowTitle()), 
           b'backImage': (self._award.getBackgroundImage()), 
           b'header': (self._award.getHeader()), 
           b'description': (self._award.getDescription())}
        data.update(self._getTypeSpecificFields())
        self.as_setDataS(data)
        self.__playSound()
        return

    def _getTypeSpecificFields(self):
        return {}

    def _dispose(self):
        if self._award is not None:
            self._award.clear()
            self._award = None
        super(AwardWindowBase, self)._dispose()
        return

    def __playSound(self):
        sound = self._award.getSound()
        if sound is not None:
            self.soundManager.playInstantSound(sound)
        return
