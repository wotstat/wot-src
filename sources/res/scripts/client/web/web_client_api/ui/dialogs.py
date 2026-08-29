import adisp, th_async
from gui.impl.pub.dialog_window import DialogButtons
from gui.shared.event_dispatcher import showPreformattedDialog
from shared_utils import first
from web.web_client_api import WebCommandException, w2c, W2CSchema, Field

def _dialogButtonsValidator(buttonsList, _=None):
    for button in buttonsList:
        if first(button.keys()) not in DialogButtons.ALL:
            raise WebCommandException((b'unsupported button label "{}"').format(first(button.keys())))

    return True


class _DialogSchema(W2CSchema):
    preset = Field(required=True, type=basestring)
    title = Field(required=False, type=basestring, default=b'')
    message = Field(required=False, type=basestring, default=b'')
    buttons = Field(required=True, type=list, validator=_dialogButtonsValidator)
    focusedButton = Field(required=False, type=basestring, default=None)
    btnDownSounds = Field(required=False, type=dict, default=None)


class DialogsWebApiMixin(object):

    @w2c(_DialogSchema, b'confirm_dialog_overlay')
    def showDialog(self, cmd):

        @adisp.adisp_async
        @th_async.th_async
        def proxy(callback):
            res = yield th_async.th_await(showPreformattedDialog(cmd.preset, cmd.title, cmd.message, cmd.buttons, cmd.focusedButton, cmd.btnDownSounds))
            callback(res)
            return

        result = yield proxy()
        yield {b'buttonID': result}
        return
