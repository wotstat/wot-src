from gui.Scaleform.Waiting import Waiting
from web.web_client_api import w2c, W2CSchema, Field

class _WaitingToggleControlSchema(W2CSchema):
    enabled = Field(required=True, type=bool)


class _WaitingToggleSchema(W2CSchema):
    show = Field(required=True, type=bool)


class _GlobalWaitingToggleSchema(W2CSchema):
    show = Field(required=True, type=bool)
    messageID = Field(required=False, type=basestring, default=b'browser/w2c_call')


class WaitingWebApiMixin(object):

    @w2c(_WaitingToggleControlSchema, b'waiting_toggle_control')
    def waitingToggleControl(self, cmd, ctx):
        browserView = ctx[b'browser_view']
        browserView.browser.setAllowAutoLoadingScreen(not cmd.enabled)
        return

    @w2c(_WaitingToggleSchema, b'waiting_toggle')
    def waitingToggle(self, cmd, ctx):
        browserView = ctx[b'browser_view']
        browserView.showLoading(cmd.show)
        return

    @w2c(_GlobalWaitingToggleSchema, b'global_waiting_toggle')
    def globalWaitingToggle(self, cmd):
        if cmd.show:
            Waiting.show(cmd.messageID)
        else:
            Waiting.hide(cmd.messageID)
        return
