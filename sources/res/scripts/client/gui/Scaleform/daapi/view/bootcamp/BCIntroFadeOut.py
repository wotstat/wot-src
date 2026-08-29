from gui.Scaleform.daapi.view.meta.BCIntroFadeOutMeta import BCIntroFadeOutMeta
from bootcamp.BootCampEvents import g_bootcampEvents

class BCIntroFadeOut(BCIntroFadeOutMeta):

    def __init__(self, settings):
        super(BCIntroFadeOut, self).__init__()
        self.__duration = settings[b'duration']
        return

    def finished(self):
        self.destroy()
        return

    def _populate(self):
        super(BCIntroFadeOut, self)._populate()
        g_bootcampEvents.onArenaStarted()
        self.__start()
        return

    def __start(self):
        self.as_startFadeoutS(self.__duration)
        return

    def __onFinish(self, destroyView):
        g_bootcampEvents.onIntroVideoStop()
        if destroyView:
            self.destroy()
        return
