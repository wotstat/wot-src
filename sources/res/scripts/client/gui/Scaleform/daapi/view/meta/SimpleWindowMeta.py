from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SimpleWindowMeta(AbstractWindowView):

    def onBtnClick(self, action):
        self._printOverrideError(b'onBtnClick')
        return

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)
        return

    def as_setTextS(self, header, descrition):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(header, descrition)
        return

    def as_setImageS(self, imgPath, imgBottomMargin):
        if self._isDAAPIInited():
            return self.flashObject.as_setImage(imgPath, imgBottomMargin)
        return

    def as_setButtonsS(self, buttonsList, align, btnWidth):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtons(buttonsList, align, btnWidth)
        return
