import typing
from frameworks.wulf import ViewModel, Array
from gui.impl.gen.resources import R
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets
from gui.impl.pub.dialog_window import DialogWindow, DialogFlags

class PureDialogWindow(DialogWindow):

    def __init__(self, content=None, bottomContent=None, parent=None, balanceContent=None, enableBlur=True, preset=DialogPresets.DEFAULT, flags=DialogFlags.TOP_FULLSCREEN_WINDOW):
        super(PureDialogWindow, self).__init__(bottomContent=bottomContent, parent=parent, balanceContent=balanceContent, enableBlur=enableBlur, content=content, flags=flags)
        self._setPreset(preset)
        return

    def setTitle(self, title=R.invalid(), args=None, fmtArgs=None, namedFmtArgs=True):
        model = self.viewModel
        if title != R.invalid():
            model.setTitle(title)
        if fmtArgs:
            self._addArgsOfModel(model.getTitleFmtArgs(), fmtArgs)
            model.setIsTitleFmtArgsNamed(namedFmtArgs)
        elif args:
            self._addArgsOfString(model.getTitleArgs(), args)
        return

    def setFormattedTitle(self, formattedTitle=b''):
        if formattedTitle != b'':
            self.viewModel.setFormattedTitle(formattedTitle)
        return

    def setIcon(self, icon):
        self.viewModel.setIcon(icon)
        return

    def addButton(self, name, label, isFocused=False, invalidateAll=False, soundDown=None, rawLabel=b''):
        self._addButton(name, label, isFocused, invalidateAll, soundDown=soundDown, rawLabel=rawLabel)
        return

    def setBackground(self, backImg):
        self.viewModel.setBackgroundImage(backImg)
        return

    def _getResultData(self):
        if self.bottomContentViewModel is not None:
            return self.bottomContentViewModel.getIsSelected()
        else:
            return super(PureDialogWindow, self)._getResultData()

    @staticmethod
    def _addArgsOfModel(arrModel, args):
        for arg in args:
            arrModel.addViewModel(arg)

        arrModel.invalidate()
        return

    @staticmethod
    def _addArgsOfString(arrModel, args):
        for arg in args:
            arrModel.addString(arg)

        arrModel.invalidate()
        return
