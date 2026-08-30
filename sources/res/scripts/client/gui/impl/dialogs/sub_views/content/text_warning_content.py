from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.dialogs.dialog_template_utils import toString
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.dialogs.sub_views.text_with_warning_view_model import TextWithWarningViewModel
from gui.impl.pub import ViewImpl

class TextWithWarning(ViewImpl):
    __slots__ = ()

    def __init__(self, mainText, warningText=None):
        settings = ViewSettings(R.views.dialogs.sub_views.content.TextWithWarning())
        settings.model = TextWithWarningViewModel()
        settings.kwargs = {b'mainText': mainText, 
           b'warningText': warningText}
        super(TextWithWarning, self).__init__(settings)
        return

    def _onLoading(self, mainText, warningText, *args, **kwargs):
        super(TextWithWarning, self)._onLoading(*args, **kwargs)
        viewModel = self.getViewModel()
        viewModel.setMainText(toString(mainText))
        if warningText:
            viewModel.setWarningText(toString(warningText))
        return

    def updateText(self, text):
        self.getViewModel().setText(toString(text))
        return
