def subtitleDecorator(function):

    def onCall(self, *args, **kwargs):
        if getattr(self.__class__, b'content', False) and self.content and self.content[b'voiceovers']:
            data = self.content[b'voiceovers'].pop(0)
            if data[b'voiceover']:
                self.soundManager.playSound(data[b'voiceover'])
            if data[b'subtitle']:
                if getattr(self.__class__, b'tutorial', False) and self.tutorial is not None:
                    from tutorial.data.effects import HasTargetEffect, EFFECT_TYPE
                    effects = [
                     HasTargetEffect(data[b'subtitle'], EFFECT_TYPE.SHOW_WINDOW, None)]
                    self.tutorial.storeEffectsInQueue(effects, benefit=True, isGlobal=True)
                    funcEffect = self.tutorial.getFirstElementOfTop()
                    funcEffect.triggerEffect()
                else:
                    from gui.shared.event_dispatcher import showSubtitleWindow
                    showSubtitleWindow(messageVO={b'voiceovers': [data]})
        return function(self, *args, **kwargs)

    return onCall
