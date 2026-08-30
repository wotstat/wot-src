from helpers import dependency
from skeletons.gui.game_control import IReferralProgramController
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _CloseReferralProgramViewSchema(W2CSchema):
    pass


class _OpenContentPage(W2CSchema):
    url = Field(required=True, type=basestring)


@w2capi(name=b'referral_program', key=b'action')
class ReferralProgramWebApi(W2CSchema):
    __referralCtrl = dependency.descriptor(IReferralProgramController)

    @w2c(_CloseReferralProgramViewSchema, b'close_referral_program_view')
    def closeReferralProgramView(self, cmd):
        if self.__referralCtrl:
            self.__referralCtrl.hideWindow()
        return
