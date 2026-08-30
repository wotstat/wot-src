from gui.shared.gui_items.processors.referral_program import CollectRPPgbPointsProcessor
from helpers import dependency
from skeletons.gui.game_control import IReferralProgramController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from web.web_client_api import w2c, w2capi, W2CSchema, Field
from web.common import formatReferralProgramInfo

class _CloseReferralProgramViewSchema(W2CSchema):
    pass


class _OpenContentPage(W2CSchema):
    url = Field(required=True, type=basestring)


@w2capi(name=b'referral_program', key=b'action')
class ReferralProgramWebApi(W2CSchema):
    __referralCtrl = dependency.descriptor(IReferralProgramController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    @w2c(_CloseReferralProgramViewSchema, b'close_referral_program_view')
    def closeReferralProgramView(self, cmd):
        if self.__referralCtrl:
            self.__referralCtrl.hideWindow()
        return

    @w2c(W2CSchema, name=b'get_rp_pgb_info')
    def getRPPgbInfo(self, _):
        return formatReferralProgramInfo()

    @w2c(W2CSchema, name=b'collect_rp_pgb_points')
    def collectRPPgbPoints(self, _):
        success, error = False, b''
        processor = CollectRPPgbPointsProcessor()
        response = yield processor.request()
        if response:
            success, error = response.success, response.userMsg
        else:
            error = b'Undefined server error'
        yield {b'success': success, 
           b'error': error}
        return
